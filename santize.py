#takes a string, returns sanitized string
#gets rid of extra whitespace, numbers, and punctuation
def sanitize(line):
    sanline= line.strip("[]<>:;1234567890,.!\"!@#$%^&*()}{")
    sanline = sanline.strip()
    return sanline

def sanfile(file):
    santext = file.read.strip("[]<>:;1234567890,.!\"!@#$%^&*()}{")
    santext = santext.strip()
    file.seek(0)
    return sanfile