from consts import ALLOWED_GROUPS
import grp


def is_user_allowed(username, allowed_groups=ALLOWED_GROUPS):
    """
    Checks if the user inside the allowed groups.

    :param (str) username: username.
    :param (set(str)) allowed_groups: list of the allowed group names.
    :return: returns True if the user inside the allowed groups.
    """
    return len([g.gr_name for g in grp.getgrall() if username in g.gr_mem and g.gr_name in allowed_groups]) > 0
