from typing import Literal

from ...command import Command


__all__ = (
    "FtpModePassiveCommand",
    "FtpModePassiveRemoveCommand"
)


class FtpModePassiveCommand(Command):
    key: tuple[Literal["ftp"], Literal["mode"], Literal["passive"]] = (
        "ftp",
        "mode",
        "passive"
    )


class FtpModePassiveRemoveCommand(Command):
    key: tuple[
        Literal["no"],
        Literal["ftp"],
        Literal["mode"],
        Literal["passive"]
    ] = ("no", "ftp", "mode", "passive")
