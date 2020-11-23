#takes a string, returns sanitized string
#gets rid of extra whitespace, numbers, and punctuation
def sanitize(text):
    santext = text
    chars = ["[", "]", ".", "<", ">", ":", ";", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "\"", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "}", "{", "?"]
    for char in chars:
        santext = santext.replace(char, "")
    santext = santext.strip()
    return santext