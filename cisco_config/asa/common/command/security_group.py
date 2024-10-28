from ....command import Command, Key
from .. import dsl


__all__ = (
    "SecurityGroup",
    "RemoveSecurityGroup"
)


class SecurityGroup(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp2301402396
    """

    key: Key["security-group"]
    target: dsl.security_group.SecurityGroupTarget


class RemoveSecurityGroup(Command):
    """
    See: https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S/sa-shov-commands.html#wp2301402396
    """

    key: Key["no", "security-group"]
    target: dsl.security_group.SecurityGroupTarget
