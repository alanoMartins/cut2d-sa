import random
import math

def initial_temperature(size):
    return [random.randrange(size) for p in range(0, size)]

def perturba(temperatures, actual_index, interator):
    next_idx = random.choice(xrange(0, len(temperatures)))
    diff = temperatures[next_idx] - temperatures[actual_index]

    if diff < 0:
        return next_idx
    else:
        p = math.exp(-diff / interator)
        return next_idx if random.random() < p else actual_index  # Permuta ??

def sa_alt():
    temperatures = initial_temperature(L)
    initial_index = random.choice(xrange(0, len(temperatures)))  # Ele deu uma dica de como escolher o primeiro
    indice_local = initial_index
    indice_melhor = initial_index
    interator = 1
    alpha = 0.8
    LIMIT = 1000
    LIMIT_REPEAT = 50
    counter_breaker = 0

    while interator < LIMIT:

        indice_local_aux = perturba(temperatures, indice_local, interator)

        if indice_local == indice_local_aux:
            counter_breaker += 1
        else:
            indice_local = indice_local_aux
            counter_breaker = 0

        if counter_breaker > LIMIT_REPEAT:
            break

        if temperatures[indice_local] < temperatures[indice_melhor]:
            indice_melhor = indice_local
        interator = + 1

    print "Minimum temp found: %d at index: %d" % (temperatures[indice_melhor], indice_melhor)
