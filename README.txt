catlang v0.0.2: a toy stack-based language
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

You can also pop on very primitive procedures

    >_> 3 3 [ + ] [ - ]

| [ - ] |
| [ + ] |
| 3     |
| 3     |
---------

If statements also work, in form:

    [ true_branch ] [ false_branch ] true_or_false_value if

    >_> 3 3 [ + ] [ - ] true if 

| 6 |
-----

    >_> 3 3 [ + ] [ - ] false if 

| 0 |
-----

That's about it.

Changelog
---------

- v0.0.2: Procedures, if statement

Planned
-------

- Refactor parser
- While loops
- Nested procedures
