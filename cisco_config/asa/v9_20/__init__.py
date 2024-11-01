from ..common import command


__all__ = (
    "hints",
)


hints = (
    command.access_list.extended.ExtendedAccessList,
    command.access_list.remark.AccessListRemark,
    command.banner.Banner,
    command.ftp.PassiveFtpMode,
    command.hostname.Hostname,
    command.interface.Interface,
    command.mac.ModifyAutomaticMacAddress,
    command.meta.AsaVersion,
    command.names.Names,
    command.object.Object,
    command.object_group.ObjectGroup,
    command.pager.PagerLines,
    command.password.EnablePassword
)
