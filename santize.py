#takes a string, returns sanitized string
#gets rid of extra whitespace, numbers, and punctuation
def sanitize(line):
    sanline= line.strip("[]<>:;1234567890,.!\"!@#$%^&*()}{")
    sanline = sanline.strip()
    return sanline