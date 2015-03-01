# -*- coding: utf-8 -*-

import re
import sys

noun_suffixes = {
    'moska_1': (
        'a u om ov oma ih i ov e ovi ovom ove ovih'.split(), ''),
    'moska_prid': ('i ega emu em im a ih ima e imi'.split(), 'i'),
    'zenska_1': ('a e i o 0 ama ah am ami'.split(), 'a'),
    'zenska_2': ('0 i jo ema eh im em mi'.split(), ''),
    'zenska_prid': ('a e i o ih ima im'.split(), 'a'),
    'srednja_o': ('o a u om i 0 oma ih'.split(), 'o'),
    'srednja_e': ('e a u em i 0 ema ih'.split(), 'e'),
    'spregatve_sed': ('m š 0 va ta mo te jo'.split(), 'ti'),
    'spregatve_pr': ('l la li le'.split(), 'ti')
}

dictionary = []
with open('sbsj.html') as f:
    for line in f.readlines():
        dictionary.append(line.split()[0].strip().lower())

dictionary = set(dictionary)


def get_nominative(word):
    word = word.strip().lower()
    if word in dictionary:
        return word
    elif len(word) > 3:
        for name, declension in noun_suffixes.iteritems():
            suffixes = declension[0]
            suffixes.sort(key=len, reverse=True)
            for suffix in suffixes:
                if word[-len(suffix):] == suffix:
                    base_form = word[:len(word) - len(suffix)] + \
                                declension[1]
                elif suffix == '0':
                    base_form = word + declension[1]
                else:
                    base_form = word
                if base_form in dictionary:
                    return base_form
                elif word in dictionary:
                    return word

if len(sys.argv) == 1:
    test_words = ''
    with open('testtext.txt') as f:
        for line in f.readlines():
            test_words += re.sub(r'["|,|:|!|.|;]+', ' ', line)

    success = 0
    failure = 0
    failures = []
    for word in test_words.split():
        returned = get_nominative(word)
        if type(returned) is str:
            success += 1
        else:
            failure += 1
            failures.append(word)

    print failures

    print 'Successes: {}\nFailures: {}\nTotal: {}'.format(success, failure,
                                                          success + failure)

else:
    for arg in sys.argv[1:]:
        print get_nominative(arg)