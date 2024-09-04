input_line = input()
split_line = list(map(int, input_line.split(' ')))
print(split_line[0] - split_line[1] + split_line[2])