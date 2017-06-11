#!/usr/bin/env python3

import math
from random import randint, uniform


def f(s):
    x = s[0]
    y = s[1]
    return (x*x+y-11)*(x*x+y-11)+(x+y*y-7)*(x+y*y-7)


def cmp_solution(s0, s1):
    return f(s0) - f(s1)


def perturba(s):
    r = uniform(-6, 6)
    if randint(0, 1) == 0:
        return (r, s[1])
    else:
        return (s[0], r)


def initial_temperature(s):
    k = 0
    i = 0
    acc_diff_s = 0.0
    while True:
        s0 = s
        s = perturba(s)
        diff_s = f(s0) - f(s)
        if diff_s > 0:
            acc_diff_s = acc_diff_s + diff_s
            k = k + 1
        i = i + 1

        if i > 100:
            break

    return 4.48 * (acc_diff_s/k)


def initial_solution():
    return (0, 0)


M = 500000
P = 1000
L = 10000
a = 0.8

# print setup


s0 = initial_solution()
s = s0
t = initial_temperature(s0)
print("Initial temperature: %f" % t)

j = 1
nsucc = 0
while True:
    i = 1
    while True:
        si = perturba(s)
        diff_s = f(si) - f(s)

        if diff_s <= 0 or math.exp(-diff_s/t) > uniform(0, 1):
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
print("final temperature = %f" % t)
print("f(%f, %f) = %f" % (s[0], s[1], f(s)))
