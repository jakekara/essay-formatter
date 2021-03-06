from argparse import ArgumentParser
import os
import html2markdown
from markdownify import markdownify

subcommand_name = "html2markdown"


def register(parser: ArgumentParser):
    parser.add_argument("-i", "--infile", help="input HTML file", required=True)
    parser.add_argument("-o", "--outfile", help="output JSON file", required=True)
    parser.add_argument(
        "-b",
        "--beast-mode",
        action="store_true",
        help="more aggressive removal of HTML",
    )


def main(args):

    print()
    print("Converting HTML to Markdown")
    print("===========================")
    print()

    try:
        html = open(args.infile, encoding="utf-8").read()
    except Exception as e:
        raise Exception(f"Could not open file '{args.infile}': {e}")

    try:
        if args.beast_mode:
            md = markdownify(html)
            print(" \U0001f9e8 Using beast mode!")
        else:
            md = html2markdown.convert(html)
        print(" \u2705 Converted HTML to Markdown")
    except Exception as e:
        raise Exception(f"Could not convert file to Markdown: {e}")

    try:
        bytes_written = open(args.outfile, "w", encoding="utf-8").write(md)
        print(f" \U0001f4be Saved file '{args.outfile}'")
    except Exception as e:
        raise Exception(f"Could not write output to '{args.outfile}': {e}")

    print(f" \u2728 Done! \u2728")
    print()
