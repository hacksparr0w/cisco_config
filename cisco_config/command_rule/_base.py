from pydantic import BaseModel


class CommandRule(BaseModel):
    name: str
    parameters: list
    subcommands: list[CommandRule]
