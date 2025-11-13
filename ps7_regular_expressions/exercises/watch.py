import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        pattern="youtube"
        new_pattern="youtu.be"
        s = re.sub(pattern, new_pattern, s)
        matches = re.search(r"(https?://)(?:www\.)(youtu.be).com/embed(/\w+)", s, re.IGNORECASE)
        return (matches.group(1)+matches.group(2)+matches.group(3))
    except:
        sys.exit("None")


if __name__ == "__main__":
    main()