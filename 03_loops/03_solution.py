number = 3
# continue use to skip a particular value and running after this particulae value.
for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)
