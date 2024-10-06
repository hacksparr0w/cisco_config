from __future__ import annotations

from io import TextIOBase
from typing import Generator, Iterable, Optional, Union

from pydantic import BaseModel


__all__ = (
    "Comment",
    "Eol",
    "Token",
    "TokenReader",
    "Word",

    "token_reader"
)


class Comment(BaseModel):
    content: str


class Eol(BaseModel):
    pass


class Word(BaseModel):
    value: str


type Token = Union[
    Comment,
    Eol,
    Word
]


class _ControlCharacter:
    COMMENT_START_CHARACTERS = ("!",)


type _ProcessingResult = tuple[Iterable[Token], Optional[_TokenReaderState]]


class _ReadingCommentState(BaseModel):
    buffer: str

    def process(self, character: str) -> _ProcessingResult:
        if not character:
            return (Comment(content=self.buffer),), None
        elif character == "\n":
            return (Comment(content=self.buffer), Eol()), _SeekingState()
        else:
            return (), _ReadingCommentState(buffer=self.buffer + character)


class _ReadingWordState(BaseModel):
    buffer: str

    def process(self, character: str) -> _ProcessingResult:
        if not character:
            return (Word(value=self.buffer),), None
        elif character == "\n":
            return (Word(value=self.buffer), Eol()), _SeekingState()
        elif character.isspace():
            return (Word(value=self.buffer),), _SeekingState()
        else:
            return (), _ReadingWordState(buffer=self.buffer + character)


class _SeekingState(BaseModel):
    def process(self, character: str) -> _ProcessingResult:
        if not character:
            return (), None
        if character in _ControlCharacter.COMMENT_START_CHARACTERS:
            return (), _ReadingCommentState(buffer="")
        if character == "\n":
            return (Eol(),), self
        if character.isspace():
            return (), self
        else:
            return (), _ReadingWordState(buffer=character)


type _TokenReaderState = Union[
    _ReadingCommentState,
    _ReadingWordState,
    _SeekingState
]


type TokenReader = Generator[Token, None, None]


def token_reader(source: TextIOBase) -> TokenReader:
    state: Optional[_TokenReaderState] = _SeekingState()

    while True:
        character = source.read(1)

        assert state is not None

        iterable, state = state.process(character)

        yield from iterable

        if not state:
            return
