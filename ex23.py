import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # str.strip() - returns string copy with leading/trailing chars removed
    next_lang = line.strip()
    # str.encode() - return encoded version of the string as a bytes object. Default encoding is 'utf-8'.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # bytes.decode() - return string decoded from the given bytes. Default encoding is 'utf-8'.
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)