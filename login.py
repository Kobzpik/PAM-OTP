import site

site.main()

import sys 
# adding directory system path
sys.path.insert(0, '/home/kobz/pam/pam_condition')

import random
import pathlib

from condition import  otp_2fa
from utils.utils import is_user_allowed
import colors
from utils.print_utils import print_header, print_section


games_list = [otp_2fa]




def get_user(pamh):
    """
    Returns the username that interacts with the PAM module
    :param (PamHandle) pamh: PamHandle object
    :return (str): username
    """

    try:
        user = pamh.get_user(None)
        return user
    except pamh.exception as e:
        return e.pam_result


def pam_sm_authenticate(pamh, flags, argv):
    """
    Handles the authentication of the user. Part of the auth management group.

    :param (PamHandle) pamh: PamHandle object
    :param (list) flags: list of flags passed to this script
    :param (list) argv: list of arguments passed to pam_python.so module.
    :return (int): PAM return code
    """
    user = get_user(pamh)

    if not is_user_allowed(user):
        return pamh.PAM_USER_UNKNOWN

    game = random.choice(games_list)

    if game():
        print_header("AUTHENTICATED!")
        return pamh.PAM_SUCCESS
    else:
        print_header("UNAUTHENTICATED!", header_color=colors.RED)

    return pamh.PAM_AUTH_ERR


def pam_sm_open_session(pamh, flags, argv):
    """
    Handles the opening of the user session. Part of the session management group.

    :param (PamHandle) pamh: PamHandle object
    :param (list) flags: list of flags passed to this script
    :param (list) argv: list of arguments passed to pam_python.so module.
    :return (int): PAM return code
    """
    user = get_user(pamh)

    if not is_user_allowed(user):
        return pamh.PAM_USER_UNKNOWN

    home_dir = pathlib.Path("/home/" + user)

    if not home_dir.exists():
        print_section(text="Hmmm... someone here doesnt have a home directory...\n"
                           "Don't worry, I am on it!\n",
        header_text="Pam Message!", header_color=colors.PURPLE)

        home_dir.mkdir()

    return pamh.PAM_SUCCESS


def pam_sm_close_session(pamh, flags, argv):
    """
    Handles the closing of the user session. Part of the session management group.

    :param (PamHandle) pamh: PamHandle object
    :param (list) flags: list of flags passed to this script
    :param (list) argv: list of arguments passed to pam_python.so module.
    :return (int): PAM return code
    """
    return pamh.PAM_SUCCESS


def pam_sm_setcred(pamh, flags, argv):
    """
    Handles the credentials change of the user. Part of the passwd management group.

    :param (PamHandle) pamh: PamHandle object
    :param (list) flags: list of flags passed to this script
    :param (list) argv: list of arguments passed to pam_python.so module.
    :return (int): PAM return code
    """
    return pamh.PAM_SUCCESS


def pam_sm_acct_mgmt(pamh, flags, argv):
    """
    Handles the validation of the user. Part of the account management group.
    NOTE: I when researching the module I didn't managed to make this function to be called.

    :param (PamHandle) pamh: PamHandle object
    :param (list) flags: list of flags passed to this script
    :param (list) argv: list of arguments passed to pam_python.so module.
    :return (int): PAM return code
    """
    return pamh.PAM_SUCCESS


def pam_sm_chauthtok(pamh, flags, argv):
    return pamh.PAM_SUCCESS
