import string

CHAR_SET = set(string.ascii_uppercase + string.digits)

# Face Extraction Configurations
FACE_BUFFER = 30
SCALE_FACTOR = 1.16
MIN_NEIGHBORS = 5
MIN_SIZE = (25, 25)
