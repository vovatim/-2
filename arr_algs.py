mass = [2, 17, 278, 3, 100, 3365, 1, 905]


def find_min(mass):
    i = 0
    min = mass[0]
    while i < len(mass):
        if mass[i] < min:
            min = i
            min = mass[i]
        i = i + 1
    return min


def sred_mass(mass):
    s = 0
    for z in mass:
        s = s + z
    s = s / len(mass)
    return s


print ("1) Минимум в массиве:", (find_min(mass)))
print ("2) Среднее арифметическое в массиве:", (sred_mass(mass)))



