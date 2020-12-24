import re


RE_GSTIN = re.compile(r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}")


def is_gstin_valid(GSTIN):
    global RE_GSTIN
    GSTIN = GSTIN.upper()

    if RE_GSTIN.match(GSTIN):
        return True
    return False
