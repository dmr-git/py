#!/usr/bin/env python3

# excercise 3.3 from ThinkPython .pdf book


def draw_col_sep(col_width):
    print("+ " + "- " * col_width, end="")


def draw_hl(cols, col_width):
    for x in range(cols):
        draw_col_sep(col_width)
    print("+")


def draw_box_sep(col_width):
    print("| " + " " * (col_width * 2), end="")


def draw_box(cols, col_width):
    for x in range(cols):
        draw_box_sep(col_width)
    print("|")


def draw_grid(cols, rows, size):
    for x in range(rows):
        draw_hl(cols, size)
        for y in range(size):
            draw_box(cols, size)
    draw_hl(cols, size)


draw_grid(2, 2, 4)
print()
draw_grid(4, 4, 4)
