input_line = input()
split_line = input_line.split(' ')
int_A = int(split_line[0])
int_B = int(split_line[1])
int_C = int(split_line[2])
N = 0
N += int_A
N *= int_B
N %= int_C
print(N)