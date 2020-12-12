from collections import defaultdict
n = input().strip()
l = len(n)
i = 0
count_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
final_count = defaultdict(int)


while i < l:
    c = n[i]
    j = i+1
    while j < l and n[j] == c:
        j += 1
    consec_count = j - i
    if i != 0:
        print('and', end=' ')
    if consec_count >= 1:
        i = j - 1
    i += 1
    if consec_count != 1:
        print('{} {}\'s'.format(count_words[consec_count-1], c), end=' ')
    else:
        print('{} {}'.format(count_words[consec_count-1], c), end=' ')
    final_count[int(c)] += consec_count
print()
for i, (num, cnt) in enumerate(final_count.items()):
    if i != 0:
        print('and', end=' ')
    if cnt != 1:
        print('{} {}\'s'.format(count_words[cnt-1], num), end=' ')
    else:
        print('{} {}'.format(count_words[cnt-1], num), end=' ')
