#!/usr/bin/env python3

import math
import meta_heuristic as sa


def gen_solution():
    []


def cmp_solution(s0, s1):
    []


def initial_solution():
    []





def f(s):
    s


s0 = gen_solution()

M = 5000
P = 1000
L = 10000
a = 0.8


# print setup


def sa():
    s = s0
    t = sa.initial_temperature()
    j = 1
    nsucc = 0

    while True:
        i = 1
        while True:
            si = sa.perturba(s)
            diff_s = f(si) - f(s)

            if diff_s <= 0 or math.exp(-diff_s / t) > math.random(0, 1):
                s = si
                nsucc = nsucc + 1
            i = i + 1

            if nsucc >= L or i >= P:  # equilibrium
                break

        t = a * t
        j = j + 1

        if nsucc == 0 or j >= M:  # stop condition
            break

            # print best solution



sa.sa_alt()
