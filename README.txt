catlang v0.0.1: a toy stack-based language
==========================================

Hi! This is Catlang! It is a stack-based programming language!

About
-----

This programming environment consists of a single stack.

|   |
|   |
|   |
|   |
-----

Onto the stack, one can push words.

    >_> 3 2 foo Ms. trainwreck ALSO weeee

| weeee      |
| ALSO       |
| trainwreck |
| Ms.        |
| foo        |
| 2          |
| 3          |
--------------

Some words execute functions.

    >_> pop

| ALSO       |
| trainwreck |
| Ms.        |
| foo        |
| 2          |
| 3          |
--------------

Catlang depends on what words get associated to functions, and at what time.

Usage
-----

Right now, you can fire it up with

`python catlang.py`

Then you can do some basic math.

    >_> 4 4 +
    >_> 3 -
    >_> 6 2 + /

That's about it.

Planned
-------

- v0.0.2: functions can push multiple words onto the stack
- v0.0.3: procedures
