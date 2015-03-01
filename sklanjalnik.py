suffixes_plain = '0 a u 0 u om a ov oma a ih oma i ov om e ih i 0 i i 0 i jo ' \
                 'i i ema i eh ema i i em i eh mi'.split()

suffixes_minus_one = 'i ega emu ega em im a ih ima a ih ima i ih im e ih imi ' \
                     'a e i o i o i 0 ama i ah ama e 0 am e ah ami a e i o i ' \
                     'o i ih ima i ih ima e ih im e ih imi e a u e u em i 0 ' \
                     'ema 0 ih ema a 0 em a ih i o a u o u om i 0 oma i ih ' \
                     'oma a 0 om a ih i o ega emu o em im'.split()

words = {}


with open('nouns.txt', 'w') as f:
    def do_magic(word):
        word = word.strip()
        if len(word) < 3 or \
                        word[len(word)-2:] == 'ti' or \
                        word[len(word)-3:] == 'ski' or \
                        word[len(word)-3:] == 'ska' or \
                        word[len(word)-3:] == 'sko':
            return
        print(word)
        for suffix in suffixes_plain:
            if suffix == '0':
                suffix = ''
            out = word + suffix
            words[out] = word
            f.write('{}:{}\n'.format(word, out))

        for suffix in suffixes_minus_one:
            if suffix == '0':
                suffix = ''
            out = word[:len(word) - 1] + suffix
            words[out] = word
            f.write('{}:{}\n'.format(out, word))

    with open('sbsj.html') as f2:
        for line in f2:
            do_magic(line)