# read from flag_in_numbers.txt then convert to ascii


def main():
    flag = []
    with open('flag_in_numbers.txt', 'r') as f:
        for line in f:
            flag.append(chr(int(line.strip())))
    print(''.join(flag))

main()