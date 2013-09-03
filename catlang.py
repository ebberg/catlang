#!/usr/bin/env python

from __future__ import print_function
from inspect import getargspec

print("NANANANANANANANA CATLANG")

stack = []

toylang = {
        'pop': lambda:print(pop()),
        'peek': lambda:print(peek()),
        'stack': lambda:print(stack),
        '+': lambda a, b: int(a)+int(b),
        '-': lambda a, b: int(a)-int(b),
        '*': lambda a, b: int(a)*int(b),
        '/': lambda a, b: int(a)/int(b),
}
lang = toylang

def lookup(word):
    try:
        return lang[word]
    except KeyError:
        return None

def push(word):
    stack.append(word)

def peek():
    return stack[-1]

def pop():
    global stack
    word = peek()
    stack = stack[0:-1]
    return word

def execute(word):
    args = []
    function = lookup(word)
    for i in range(0, len(getargspec(function).args)):
        args.append(pop())
    reply = apply(function, tuple(args))
    if reply:
        push(reply)

def parse_line(line):
    return line.split(' ')

def interpret_words(words):
    for w in words:
        if lookup(w):
            execute(w)
        else:
            push(w)

while True:
    try:
        interpret_words(parse_line(raw_input('>_> ')))
        execute('stack')
    except KeyboardInterrupt:
        break

print("\ngoodbye cat says SIGTERM")

