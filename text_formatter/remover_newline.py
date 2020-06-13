#!/usr/bin/env python3
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("raw_text_file", help="Text file to be cleaned up.")
parser.add_argument("-o", "--output", help="Name of formatted text file. If not specified, the original file will be overwritten.")
parser.add_argument("-d", "--dir", help="Directory of the files")
args = parser.parse_args()


def remove_extra_newlines(raw):
    clean = re.sub(r'\n\s*\n', '\n\n', raw)
    return clean


def main():
    """
    read raw text file, remove new lines, and save a new file (or replace the old one)
    :return:
    """
    if args.dir is None:
        fp = args.raw_text_file
    else:
        fp = os.path.join(args.dir, args.raw_text_file)

    if args.output is None:
        output_file = fp
    else:
        output_file = os.path.join(args.dir, args.output)

    with open(fp, "r") as f:
        raw_text = f.read()
    text = remove_extra_newlines(raw_text)
    with open(output_file, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
