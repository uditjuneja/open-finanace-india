import re


RE_PAN = re.compile(r"[A-Z]{5}[0-9]{4}[A-Z]{1}")


def is_pan_valid(PAN):
    global RE_PAN
    PAN = PAN.upper()

    if RE_PAN.match(PAN):
        return True
    return False
