sum = 0

# file = 'sample_b.txt'
file = 'data_b.txt'

digits = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]

f = open(file, 'r')
for line in f.readlines():
    print("read " + line)
    first = None
    last = None
    for p in range(0, len(line)-1):
        i = None
        c = line[p]
        print("char " + c)
        if c >= '0' and c <= '9':
            i = int(c)
        else:
            for digit in range(0, len(digits)):
                # print(line[p:] + "/" + digits[digit])
                if line[p:].startswith(digits[digit]):
                    i = digit+1
                    # p += len(digits[digit])
        if i is not None:
            if first is None:
                first = i
            last = i
    value = first*10 + last
    print(value)
    sum += value
print(sum)