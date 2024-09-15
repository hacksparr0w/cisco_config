from typing import Iterable, Self


__all__ = (
    "Replayable",
)


class Replayable[T]:
    def __init__(self, stream: Iterable[T]) -> None:
        self._stream = stream

        self._is_recording = False
        self._replay_buffer = []
        self._replay_index = None

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> T:
        if self._replay_index is not None:
            value = self._replay_buffer[self._replay_index]
            self._replay_index += 1

            if self._replay_index >= len(self._replay_buffer):
                self._replay_index = None

                if not self._is_recording:
                    self._replay_buffer.clear()

            return value
        
        value = next(self._stream)

        if self._is_recording:
            self._replay_buffer.append(value)

        return value

    def has_recorded(self, index: int) -> bool:
        return index < len(self._replay_buffer)

    def replay(self, index: int) -> None:
        if index < 0:
            raise ValueError("Replay index must be a positive integer")

        if index >= len(self._replay_buffer):
            raise ValueError("Replay index out of bounds")

        self._replay_index = index

    def start_recording(self) -> int:
        self._is_recording = True

        return len(self._replay_buffer)

    def stop_recording(self) -> None:
        self._is_recording = False
