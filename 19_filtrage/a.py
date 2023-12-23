#!/bin/env python3
import re
sum = 0

# file = 'sample_a.txt'
file = 'data_a.txt'

code = []
parts = []

def parseCode(line):
    global code
    (name, spec) = re.match("(.*)\{(.*)\}", line).groups()
    code.append( f"def f_{name}(part):" )
    for cond in spec.split(','):
        print("# cond = ", cond)
        if ':' in cond:
            (field, oper, value, dest) = re.match("([xmas])([<>])(\d+):(.+)", cond).groups()
            code.append( f"  if part['{field}'] {oper} {value}:" )
            indent = '  '
        else:
            dest = cond
            indent = ''
        if dest == 'R':
            code.append( f"{indent}  print('R')" )
            code.append( f"{indent}  return 0" )
        elif dest == 'A':
            code.append( f"{indent}  print('A')" )
            code.append( f"{indent}  return part['sum']" )
        else:
            code.append( f"{indent}  print('{dest}')" )
            code.append( f"{indent}  return f_{dest}(part)" )
    code.append( "" )

def parsePart(line):
    specs = {}
    sum = 0
    for s in line[1:-1].split(','):
        (k, v) = s.split('=')
        sum += int(v)
        specs[k] = int(v)
    specs['sum'] = sum
    parts.append(specs)

section=1

for i, line in enumerate(open(file)):
    line = line.strip('\n')
    print("# read " + line)
    if section == 1 and line == "":
        section = 2
        continue
    if section == 1:
        parseCode(line)
    else:
        parsePart(line)

print("# CODE :")
print('\n'.join(code))
print("# PARTS :")
print("sum = 0")
for p in parts:
    print(f"print({p})")
    print(f"sum += f_in({p})")
print("print(sum)")

