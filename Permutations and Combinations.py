N = int(input("How many items would you like to find the permutations/combinations of?"))

ordinal = lambda number: "%d%s" % (number, "tsnrhtdd"[(number / 10 % 10 != 1) * (number % 10 < 4) * number % 10::4])

items = [input("Enter the " + ordinal(item) + " item:") for item in range(1, N + 1)]

find_combinations = lambda things: [[y for j, y in enumerate(set(things)) if (k >> j) & 1] for k in
                                    range(2 ** len(set(things)))]

print(find_combinations(items))
