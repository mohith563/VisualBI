from collections import Counter

ages = [int(i) for i in input().split(',')]
count = Counter(ages)
print('Age Group      Total No. of people')
for i in range(1, 101, 10):
    print('{} - {}      '.format(i, i+9).ljust(15, ' '), end='')
    c = 0
    for j in range(i, i+10):
        c += count[j]
    print(c)
