import secrets
import argparse
from string import punctuation
from pathlib import Path

def read_list(wordlist):
    with open(wordlist) as wordfile:
        lines = wordfile.read().splitlines()
    return lines

def generate(wordlist, nwords, cap=1, punct=1):
    lines = read_list(wordlist)

    if cap > nwords:
        raise ValueError("Cannot capitalize more than %d words" % nwords)

    # Get nwords random words
    words = [secrets.choice(lines).rstrip() for j in range(nwords)]
    final = []

    # Capitalize n of those, remove them from the old list and add to new
    for j in range(cap):
        word = secrets.choice(words)
        final.append(word[0].upper() + word[1:])
        words.remove(word)

    # Add remaining words as lowercase
    final = final + words

    # Add punctuation inbetween words
    for j in range(punct):
        # No interpuncts before the first word
        pos = secrets.randbelow(len(final)-1)+1
        final.insert(pos, secrets.choice(punctuation))

    return ''.join(final)

def setup_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--nwords',
                        default=3,
                        type=int,
                        help="No of words")

    parser.add_argument('-p', '--punct',
                        default=1,
                        type=int,
                        help="No of punctuation characters")

    parser.add_argument('-c', '--cap',
                        default=1,
                        type=int,
                        help="No of capitalized Words")

    parser.add_argument('-w', '--wordlist',
                        default=None,
                        help="Path to word list")
    return parser


if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args()

    # No wordlist given: use default wordlist
    if args.wordlist == None:
        args.wordlist = (Path(__file__) /  '../diceware.txt').resolve()

    print(generate(**vars(args)))
