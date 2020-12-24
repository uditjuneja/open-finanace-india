import re

RE_CREDIT_CARD = {
    "Amex Card": re.compile(r"^3[47][0-9]{13}$"),
    "BCGlobal": re.compile(r"^(6541|6556)[0-9]{12}$"),
    "Carte Blanche Card": re.compile(r"^389[0-9]{11}$"),
    "Diners Club Card": re.compile(r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$"),
    "Discover Card": re.compile(
        r"^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$"
    ),
    "Insta Payment Card": re.compile(r"^63[7-9][0-9]{13}$"),
    "JCB Card": re.compile(r"^(?:2131|1800|35\d{3})\d{11}$"),
    "KoreanLocalCard": re.compile(r"^9[0-9]{15}$"),
    "Laser Card": re.compile(r"^(6304|6706|6709|6771)[0-9]{12,15}$"),
    "Maestro Card": re.compile(r"^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$"),
    "Mastercard": re.compile(
        r"^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$"
    ),
    "Solo Card": re.compile(
        r"^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$"
    ),
    "Switch Card": re.compile(
        r"^(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}$"
    ),
    "Union Pay Card": re.compile(r"^(62[0-9]{14,17})$"),
    "Visa Card": re.compile(r"^4[0-9]{12}(?:[0-9]{3})?$"),
    "Visa Master Card": re.compile(r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$"),
}


def is_cc_valid(CC_NO: str):
    global RE_CREDIT_CARD

    for provider in RE_CREDIT_CARD:
        reg_compile = RE_CREDIT_CARD[provider]
        if reg_compile.match(CC_NO):
            return provider

    return False
