# -*- coding: utf-8 -*-
import sys
import re

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
with open('dictionary.txt') as f:
    for line in f.readlines():
        dictionary.append(line.split()[0].strip().lower())
dictionary = set(dictionary)

checked = []

def get_nominative(word):
    word = re.sub(r'["|,|:|!|?|.|;|\'|(|)|\\|/]+', ' ', word)
    word = word.strip().lower()
    if word in checked:
        return True
    checked.append(word)
    if len(word) > 2:
        out = test_regular_cases(word)
        if not out:
            out = test_special_cases(word)
        if out:
            return out 
    return False, word

def test_regular_cases(word):
    if word in dictionary:
        return word
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
            elif word[len(word)-len(declension[1])-1] in ['t', 'j'] and \
                    word[:len(word)-len(declension[1])-1] in dictionary:
                return word[:len(word)-len(declension[1])-1]
            elif word[len(word)-len(declension[1])-2:
                    len(word)-len(declension[1])-1] == 'ov' and \
                    word[:len(word)-len(declension[1])-2] in dictionary:
                return word[:len(word)-len(declension[1])-2]
             
    return False

def test_special_cases(word):
    if 'tr' in word:
        word = re.sub(r'tr','ter', word)
    elif 'pr' in word:
        word = re.sub(r'pr','per', word)
    elif 'vk' in word:
        word = re.sub(r'vk','vek', word)
    elif 'lc' in word:
        word = re.sub(r'lc','lec', word)
    elif 'tm' in word:
        word = re.sub(r'tm','tem', word)
    elif 'zm' in word:
        word = re.sub(r'zm','zem', word)
    return test_regular_cases(word)

if __name__ == '__main__':
    success = 0
    fail = 0
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            out = get_nominative(arg)
            if type(out) is str:
                print out
                success += 1
            elif type(out) is tuple:
                print 'Not found: ', out[1]
                fail += 1

    else:
        with open('i.txt') as f:
            for line in f.readlines():
                for word in line.split():
                    out = get_nominative(word)
                if type(out) is str:
                    print out
                    success += 1
                elif type(out) is tuple:
                    print 'Not found: ', out[1]
                    fail += 1

    print '200: ', success
    print '404: ', fail
    total = success + fail
    pc = success *100 / total
    print 'Total: ', total, ' == ', pc, '%'
