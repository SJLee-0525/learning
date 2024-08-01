def strlen(a):
    count = 0
    for elem in a:
        if elem == '\0':
            return count
        count += 1

a = ['a', 'b', 'c', '\0']
print(strlen(a))

def my_strcmp(string_1, string_2):
    if string_1 == string_2:
        return 0
    else:
        