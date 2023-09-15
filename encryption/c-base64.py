import sys
import base64


def encode(raw=""):
    '''A simple script to correctly generate single line
    base64 encoded string in utf-8 encoding'''
    base64string = base64.b64encode(raw.encode("utf-8")).decode("utf-8")

    print(base64string)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3", sys.argv[0], "some-text-to-encode")
    else:
        raw = sys.argv[1]
        encode(raw=raw)
