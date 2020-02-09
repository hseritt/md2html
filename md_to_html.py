#!/usr/bin/env python

import sys
import markdown

""" Supposedly all the supported extensions for the markdown module.
    Remove as needed.
"""
EXTENSIONS = [
    'extra', 'abbr', 'attr_list', 'def_list', 'fenced_code',
    'footnotes', 'tables', 'admonition',
    'codehilite', 'legacy_attrs', 'legacy_em', 'meta',
    'nl2br', 'sane_lists', 'smarty', 'toc', 'wikilinks',
]


def show_usage():
    """ Shows the user how to use this script and all the possible combinations
    of arguments.
    """
    print("""
    md_to_html.py - Markdown to HTML Python script

    Usage:

    Takes markdown file as input and outputs to an html file.

    Examples:

    md_to_html.py [input file] [output file]
    md_to_html.py test.md test.html > outputs markdown text from test.md
        and outputs to test.html.
    md_to_html.py test.md > outputs markdown text from test.md
        and outputs to test.md.html
    md_to_html.py > takes input from user and outputs to out.html
    """)
    sys.exit(0)


if len(sys.argv) > 1 and '--help' in sys.argv == '--help':
    show_usage()


try:
    INFILE = sys.argv[1]
except IndexError:
    in_str = input(
        "No input file given. Enter text string instead"
        " and I'll convert this to html: "
    )
    INFILE = None

try:
    OUTFILE = sys.argv[2]
except IndexError:
    if INFILE:
        OUTFILE = f'{INFILE}.html'

try:
    OUTFILE
except NameError:
    OUTFILE = 'out.html'


class MdToHtmlConverter:

    in_str = ''

    def __init__(self, infile: str=None, outfile: str=None):
        self.infile = infile
        self.outfile = outfile

    def set_infile(self, infile: str):
        self.infile = infile

    def set_in_str(self, in_str: str):
        self.in_str = in_str

    def set_outfile(self, outfile: str):
        self.outfile = outfile

    def run(self):
        if self.infile:
            with open(self.infile, 'r') as fi:
                with open(self.outfile, 'w') as fo:
                    fo.write(
                        markdown.markdown(
                            fi.read(), extensions=EXTENSIONS
                        )
                    )
        else:
            with open(self.outfile, 'w') as fo:
                fo.write(
                    markdown.markdown(self.in_str, extensions=EXTENSIONS)
                )


if __name__ == '__main__':
    converter = MdToHtmlConverter()
    if INFILE:
        converter.set_infile(INFILE)
    else:
        converter.set_in_str(in_str)
    converter.set_outfile(OUTFILE)
    converter.run()
