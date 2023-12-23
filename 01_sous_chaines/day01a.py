sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

# url = 'https://adventofcode.com/2023/day/1/input'
# f = requests.get(url) # open('sample.txt', 'r')
# for data in f:
f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    first = None
    last = None
    for c in line:
        # print("char " + c)
        if c >= '0' and c <= '9':
            i = int(c)
            if first is None:
                first = i
            last = i
    value = first*10 + last
    print(value)
    sum += value
print(sum)