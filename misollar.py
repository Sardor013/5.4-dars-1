
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)




def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first, last))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)




def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    mutated_string = ''.join(string_list)
    return mutated_string




if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)





def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)





if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))