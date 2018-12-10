import re
import argparse

from nltk.tokenize import sent_tokenize

def read_file(filepath):
    with open(filepath, "r") as f:
        return [s.strip() for s in f.readlines()]

def remove_empty(lines):
    return [s for s in lines if s]

def delete_header(lines):
    i = 0
    header_marker = "START OF THIS PROJECT GUTENBERG"
    while header_marker not in lines[i]:
        i += 1

    return lines[i+1:]

def delete_footer(lines):
    i = 0
    footer_marker = "END OF THIS PROJECT GUTENBERG"
    while footer_marker not in lines[i]:
        i += 1

    return lines[:i]

def mush(lines):
    whole_text = " ".join(lines)
    return re.sub("\s+", " ", whole_text)

def tokenize_into_sentences(lines):
    whole_text = mush(lines)
    return sent_tokenize(whole_text)

def replace_single_quotes_with_double(text):
    return text.replace(" '", ' "').replace("' ", '" ').replace('""', '"')

def replace_contractions(lines):
    lines = [line.replace("'t", "t") for line in lines]
    lines = [line.replace("'ve", "ve") for line in lines]
    lines = [line.replace("'ll", "ll") for line in lines]
    lines = [line.replace("'m", "m") for line in lines]
    lines = [line.replace("'s", "s") for line in lines]
    return lines


def main(args):
    input_file = args.input_file
    output_file = args.output_file

    book = open(input_file).read()

    paras = book.split("\n\n")
    paras = [s.replace("\n", " ") for s in paras]
    paras = [s for s in paras if s.strip() != ""]
    paras = delete_header(paras)
    paras = delete_footer(paras)
    paras = paras[args.skip_first:]

    with open(output_file, "w") as of:
        of.write("\n".join(paras))


def parse_args():
    parser = argparse.ArgumentParser(description="Convert novels from Project Gutenberg into a standard format for processing")
    parser.add_argument('-o', '--output-file', required=True, help="Path to the output text file")
    parser.add_argument('-i', '--input-file', required=True, help="Path to the input text file")
    parser.add_argument('-s', '--skip-first', type=int, required=False, default=0, help="Skip first n lines from the output file")
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
