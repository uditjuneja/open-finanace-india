import re


RE_AADHAR = re.compile(r"^[2-9]{1}[0-9]{11}")


def is_aadhar_valid(AADHAR):
    global RE_AADHAR
    AADHAR = AADHAR.upper()

    if RE_AADHAR.match(AADHAR):
        return False
    return True
