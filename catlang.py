#!/usr/bin/env python

from __future__ import print_function
from inspect import getargspec

print("NANANANANANANANA CATLANG")

# Stores the state of the execution.
stack = []

def cat_if(true_or_false, f_branch, t_branch):
    if true_or_false == "true":
        execute(t_branch)
    elif true_or_false == "false":
        execute(f_branch)
    else:
        raise Exception

toylang = {
        'pop': lambda:print(pop()),
        'peek': lambda:print(peek()),
        'stack': lambda:print(stack),
        '+': lambda a, b: int(a)+int(b),
        '-': lambda a, b: int(a)-int(b),
        '*': lambda a, b: int(a)*int(b),
        '/': lambda a, b: int(a)/int(b),
        'if': cat_if,
}

def dup(a):
    push(a)
    push(a)

def swap(a, b):
    push(b)
    push(a)

def over(a, b):
    push(a)
    push(b)
    push(a)

def rot(a, b, c):
    push(b)
    push(c)
    push(a)

forthlike = {
        'dup': dup,
        'drop': lambda:print(pop()),
        'swap': swap,
        'over': over,
        'rot': rot,
}

# lang is composed of nested scopes of names.
lang = [toylang, forthlike]

def lookup(word):
    for scope in reversed(lang):
        try:
            return scope[word]
        except KeyError:
            pass
    return None

def push(word):
    stack.append(word)

def peek():
    return stack[-1]

def pop():
    return stack.pop()

def execute(word):
    if type(word) == list:
        for w in word:
            execute(w)
    else:
        args = []
        function = lookup(word)
        for i in range(0, len(getargspec(function).args)):
            args.append(pop())
        reply = apply(function, tuple(args))
        if reply != None:
            push(reply)

def parse_line(line):
    tokens = line.split(' ')
    is_proc = False
    words = []
    for t in tokens:
        if is_proc == False and t != '[':
            words.append(t)
        elif is_proc == False and t == '[':
            is_proc = True
            proc = []
        elif is_proc == True and t != ']':
            proc.append(t)
        elif is_proc == True and t == ']':
            is_proc = False
            words.append(proc)
        else:
            pass
    return words

def interpret_words(words):
    for w in words:
        if type(w) == list:
            push(w)
        elif lookup(w):
            execute(w)
        else:
            push(w)

while True:
    try:
        x = parse_line(raw_input('>_> '))
        print(x)
        interpret_words(x)
        execute('stack')
    except EOFError:
        print("\ngoodbye cat says SIGQUIT")
        break
    except KeyboardInterrupt:
        print("\ngoodbye cat says SIGINT")
        break


