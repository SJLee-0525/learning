# print(bin(10))
# print(hex(10))
#
# print(int('1011', 2))
# print(int('b', 16))
#
# print(11 ^ 13)
# print(0b1011 ^ 0b1101)
# print(bin(11 ^ 13))
# print(bin(0b1011 ^ 0b1101))

# print(7070 ^ 1004)
# print(6258 ^ 1004)

# print(bin(0b1101 << 2))
# print(bin(0b1101 >> 2))
#
# print(int('1101', 2))
# print(int('110100', 2))
# print(int('11', 2))

# print(1101 & (1 << 2))

# def B_bit_print(i):
#     output = ''
#     for j in range(7, -1, -1):
#         if i & (1 << j):
#             output += '1'
#         else:
#             output += '0'
#     print(output)
#
# for i in range(-5, 6):
#     print(f'{i} = ', end='')
#     B_bit_print(i)

# -5 = 11111011
# -4 = 11111100
# -3 = 11111101
# -2 = 11111110
# -1 = 11111111
# 0 = 00000000
# 1 = 00000001
# 2 = 00000010
# 3 = 00000011
# 4 = 00000100
# 5 = 00000101

# t1 = 10
# t2 = 3.141592
#
# print(f'변수 값은 {t1} 입니다.')
# print(f'변수 값은 {t2:.2f} 입니다.')

print(0.1 + 0.1 + 0.1 == 0.3)