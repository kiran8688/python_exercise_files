fileinp = input('> Enter the fil_name: ')
open_file = open(fileinp)
counter = dict()
# read_file = open_file.read()
for line in open_file:
    line = line.rstrip()
    split_lines = line.split()
    for word in split_lines:
        counter [word] = counter.get(word, 0) + 1
        # print(word, counter[word])
largest = -1
commmon_word = None
for k, v in counter.items():
    if v > largest:
        largest = v
        commmon_word = k
print(commmon_word, largest)
# print("line: ", split_lines)
# print("counter", counter)