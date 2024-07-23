# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기


# 1. [] 표기법을 사용한 방법
# def dict_invert(input_dict):
#     new_dict = {}
#     for key, value in input_dict.items():
#         if value not in new_dict:
#             new_dict[value] = [key]
#         else:
#             new_dict[value].extend([key])
        
#     return new_dict


# # 2. get 메서드를 사용한 방법
# def dict_invert(input_dict):
#     new_dict = {}
#     for key, value in input_dict.items():
#         if new_dict.get(value, None) == None:
#             new_dict[value] = [key]
#         else:
#             new_dict[value].extend([key])
        
#     return new_dict


# # 3. setdefault 메서드를 사용한 방법
def dict_invert(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        if value not in new_dict:
            new_dict.setdefault(value, [key])
        else:
            temp_value = new_dict.setdefault(value)
            temp_value.append(key)
            new_dict.setdefault(value, temp_value)

    return new_dict


print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
print(
    dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
)  # {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}
