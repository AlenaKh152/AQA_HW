import os
os.system('cls')


def check_sequence(sequence):
    if sequence == sorted(sequence) and len(sequence) == len(set(sequence)):
        return True
    else:
        for i in sequence:
            if i >= sequence[sequence.index(i) + 1]:
                del sequence[sequence.index(i) + 1]
                break
        return bool(sequence == sorted(sequence) and len(sequence) == len(set(sequence)))


print(check_sequence([1, 2, 3]))  # == True
print(check_sequence([1, 2, 1, 2]))  # == False
print(check_sequence([1, 3, 2, 1]))  # == False
print(check_sequence([1, 2, 3, 4, 5, 3, 5, 6]))  # == False
print(check_sequence([40, 50, 60, 10, 20, 30]))  # == False
