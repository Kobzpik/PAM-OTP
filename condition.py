import random
import time

##############
import sys
# adding directory system path
sys.path.insert(0, '/home/kobz/pam/pam_condition')

import colors
from utils.print_utils import print_section

 

def otp_2fa():
    """
    Authenticates the user by asking him the time.

    :return (bool): True if users answer was correct, otherwise - False.
    """
    
    print_section(text="Hello There! Can you tell me what the time is? Answer quickly! The clock is ticking!",
    header_text="WTF is the Time??", header_color=colors.YELLOW)

    #answer=1
    print("testing.........")
    answer = raw_input("Enter the number")
        #answer = input(colors.YELLOW + "\nAnswer (hh:mm format): " + colors.ENDC)
        #current_time = time.localtime()
    correct_answer = 1

        # if current_time.tm_min < 10:
        #     correct_answer = str(current_time.tm_hour) + ":0" + str(current_time.tm_min)
        # else:
        #     correct_answer = str(current_time.tm_hour) + ":" + str(current_time.tm_min)

    return answer == correct_answer



sys.exit()