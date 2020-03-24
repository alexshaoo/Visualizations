N = int(input("How many items would you like to find the permutations/combinations of?"))


def ordinal(number):
    if 10 <= number <= 19:
        return "%d%s" % (number, "th")
    elif number % 10 == 1:
        return "%d%s" % (number, "st")
    elif number % 10 == 2:
        return "%d%s" % (number, "nd")
    elif number % 10 == 3:
        return "%d%s" % (number, "rd")
    return "%d%s" % (number, "th")
    
    # return "%i%s" % (number, "tsnrhtdd"[(number / 10 % 10 != 1) * (number % 10 < 4) * number % 10::4])


# Gets input of different items
items = [input("Enter the " + ordinal(item) + " item:") for item in range(1, N + 1)]

"""
# Gets whether the user wants permutations or combinations
# TODO: Rename this variable to something that doesn't sound finicky
perm_or_comb = input("Enter 'P' if you want permutations, and 'C' if you want combinations.")

# Gets whether the user wants repetitions or not
repetition = input("Enter 'Y' if you want repetitions, and 'N' if you don't want any.")
"""


def find_combinations_without_repeats(things):
    combinations = []
    
    # Change things to a set because we don't worry about order or repeats
    things = set(things)
    
    # The number of different permutations of a set is 2 to the power of however many distinct items are in the set
    for i in range(2 ** len(things)):
        
        # Current combination
        combination = []
        
        for j, k in enumerate(things):
            if (i >> j) & 1:
                combination.append(k)
        
        # Only want lists that contain elements
        if combination:
            combinations.append(combination)
    
    return sorted(combinations, key=len)


def find_combinations_with_repeats(things):
    combinations = []
    
    # The number of different permutations of a set is 2 to the power of however many distinct items are in the set
    for i in range(2 ** len(things)):
        
        # Current combination
        combination = []
        for j, k in enumerate(things):
            if (i >> j) & 1:
                combination.append(k)
        
        # Only want lists that contain elements
        if combination:
            combinations.append(combination)
            combination = []
    
    return combinations


def find_permutations(things):
    if len(things) <= 1:
        return things
    
    else:
        for index, item in enumerate(things):
            return things[:index + 1] + find_permutations(things[0: 1]) + things[index + 1:]


def find_permutations_without_repeats(things):
    permutations = []
    
    combinations = find_combinations_without_repeats(things)
    
    for combination in combinations:
        permutations.append(find_permutations(things, combination[0], combination[-1]))
    
    return permutations


def find_permutations_with_repeats(things):
    permutations = []
    
    combinations = find_combinations_with_repeats(things)
    
    for combination in combinations:
        permutations.append(find_permutations(things, combination[0], combination[-1]))
    
    return permutations


print(find_permutations_without_repeats(items))
