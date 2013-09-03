#!/usr/bin/env python

from __future__ import print_function

print("NANANANANANANANA CATLANG")

stack = []
toylang = {
        'push': lambda:not_implemented,
        'pop': lambda:not_implemented,
        'peek': lambda:not_implemented,
        'execute': lambda:not_implemented,
        'stack': lambda:not_implemented,
        '+': lambda:not_implemented,
        '-': lambda:not_implemented,
        '*': lambda:not_implemented,
        '/': lambda:not_implemented,
}
lang = toylang

def lookup(word):
    pass

def push(word):
    pass

def pop(word):
    pass

def peek(word):
    pass

def execute():
    pass

def parse_line(line):
    return line.split(' ')

def execute_words(words):
    print(words)

while True:
    try:
        execute_words(parse_line(raw_input('>_> ')))
    except KeyboardInterrupt:
        break

print("\ngoodbye cat says SIGTERM")
