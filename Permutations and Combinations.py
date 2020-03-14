from itertools import chain, combinations

items = []

N = int(input("How many items would you like to find the permutations/combinations of?"))

ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])

for i in range(1, N + 1):
    items.append(input("Enter the " + ordinal(i) + " item:"))

perms = combs = []

all_subsets = list(chain.from_iterable(combinations(items, r) for r in range(1, len(items) + 1)))

# This one works better wuu
f = lambda x: [[y for j, y in enumerate(set(x)) if (k >> j) & 1] for k in range(2 ** len(set(x)))]

for item in f(items):
    print(str(item))
