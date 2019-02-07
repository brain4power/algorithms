STR = 'papa'


def count_subs(input_string):
    hashs = set()
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            hashs.add(hash(input_string[i:j]))
    return len(hashs) - 1


print(count_subs(STR))


def count_subs_2(input_string):
    hashs = [hash(input_string[i:j]) for i in range(len(input_string)) for j in range(i + 1, len(input_string) + 1)]
    return len(set(hashs)) - 1


print(count_subs_2(STR))
