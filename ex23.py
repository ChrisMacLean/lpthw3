# how come no from before import, is sys just so standard like it knows where it is?
# Or is it a higher folder that contains argv and we were super specific before
import sys
script, input_encoding, error = sys.argv

# define everything first really only do stuff in the last two lines
# this function has 3 variables
def main(language_file, encoding, errors):
    line = language_file.readline()

# if language_file.readline() returns anything then do the indented part else it skips
# practically its saying for every line in the languages.txt file execute because everyline has values
    if line:
        # print_line is not a variable here so that's why I have to redefine it as variable later
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# this uses "line" from above def I think
# what is strip()? removes all whitespaces and new line stuff
# encode(encoding)? turns this into the raw bytes
# decode()? turns this into the utf-8 string
# both have two parameters (encoding, errors)
# in this case encoding is hardcoded to UTF-8 by our argv values
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

# I think this basically shows raw string and encoding attempt results
    print(raw_bytes, "<===>", cooked_string)

# here we hardcode in UTF-8
languages = open("languages.txt", encoding="utf-8")

# so its always doing the print thing?
# we are calling the function main so its going to make an if-loop
main(languages, input_encoding, error)
