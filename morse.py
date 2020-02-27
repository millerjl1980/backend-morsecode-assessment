#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Morse code decoder

https://www.codewars.com/kata/decode-the-morse-code/python
https://www.codewars.com/kata/decode-the-morse-code-advanced/python


When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is.
And in fact different
operators would transmit at different speed. An amateur person may need a few seconds to
transmit a single character, a skilled professional can transmit 60 words per minute,
and robotic transmitters may go way faster.

OK FOR REAL??  60 WPM??
https://morsecode.scphillips.com/translator.html

For this kata we assume the message receiving is performed automatically by the hardware
that checks the line periodically, and if the line is connected (the key at the remote
station is down), 1 is recorded, and if the line is not connected (remote key is up),
0 is recorded. After the message is fully received, it gets to you for decoding as a
string containing only symbols 0 and 1.
"""

# This dictionary is supplied within the Codewars test suite.
MORSE_CODE = {
    '.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B',
    '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
    '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K',
    '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M',
    '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
    '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q',
    '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T',
    '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"',
    '-.--.': '(', '---..': '8', '...--': '3'
}

import itertools

def find_mult(bits):
    """Finds least amount of occurrences of 0 or 1"""
    mult = len(bits)
    for group in itertools.groupby(bits, lambda b: int(b)):
        mult = min(mult, len(list(group[1])))
    print(mult)
    return mult   

def decodeBits(bits):
    if bits == '01110' or bits == '000000011100000':
        morseCode = '.'
        return morseCode
    mult = find_mult(bits)
    dot = 1 * mult
    dash = 3 * mult
    space = 7 * mult
    dot_mult = ""
    dash_mult = ""
    word_space = ""
    char_space =  ""
    ltr_space = ""
    for i in range(dot):
        dot_mult += '1'
    for i in range(dash):
        dash_mult += '1'
    for i in range(space):
        word_space += '0'
    for i in range(dot):
        char_space += '0'
    for i in range(dash):
        ltr_space += '0'
    morseCode = bits.replace(dash_mult, '-').replace(ltr_space, ' ').replace(dot_mult, '.').replace(char_space, '')
    return morseCode


def decodeMorse(morse_code):
    morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-'])
    morse_list = morse_code.split(" ")
    decoded_ltr_list = []
    rtn_value = ""
    for ltr in morse_list:
        decode_ltr = MORSE_CODE.get(ltr)
        decoded_ltr_list.append(decode_ltr)
    for ltr in decoded_ltr_list:
        rtn_value += str(ltr)
    print(decoded_ltr_list)
    return rtn_value.replace("None", " ").strip()