import sys


nouns = {}
with open('nouns.txt') as f:
    for line in f:
        k, v = line.split(':')
        nouns[k] = v


def find_word(word):
    f.write('{}:{}'.format(word, nouns[word]))
    return nouns[word]


with open('nouns_clean.txt', 'a') as f:
    for arg in sys.argv:
        find_word(arg)

if len(sys.argv) < 2:
    print('Enter at least one word to find')
    sys.exit(0)