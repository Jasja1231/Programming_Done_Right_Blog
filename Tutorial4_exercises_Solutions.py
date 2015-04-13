__author__ = "mikaeilorfanian"

import string

def exercise10(text):
    text_length = len(text)
    sub_string = ''
    counter = 0
    
    for index in range(len(text)):
        if text[index] == 'b':
            if index + 2 < text_length:
                sub_string = text[index] + text[index + 1] + text[index + 2]
                if sub_string == 'bob':
                    counter += 1
    
    return counter

def exercise11(text):
    alphabet = string.ascii_lowercase
    L = [ord(letter) for letter in text]
    sub_L = [0]
    all_subs = []

    for index in range(len(L)):
        if L[index] == sub_L[-1] + 1:
            sub_L.append(L[index])
        else:
            all_subs.append(sub_L)
            sub_L = [0, L[index]]
        if index == len(L) - 1:
            all_subs.append(sub_L)

    ans = []
    for l in all_subs:
        if len(l) > len(ans):
            ans = l

    ans = ans[1:]
    ans = [chr(elem) for elem in ans]

    return ans