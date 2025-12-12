import sys

if __name__ == '__main__':
    position = 50
    counter = 0
    with open(f'../../resources/day1/{sys.argv[1]}', 'r') as h:
        content = h.read()
        lines = content.split('\n')
        inputs = [int(line[1:]) * (-1 if line[0] == 'L' else 1) for line in lines ]
        for i in inputs:
            position += i
            if position % 100 == 0:
                counter += 1
        print(f'Part 1: {counter}')
        counter = 0
        position = 50
        for i in inputs:
            position += i
            if 0 >= position != i:
                counter += 1
            counter += abs(position) // 100
            position = position % 100
        print(f'Part 2: {counter}')