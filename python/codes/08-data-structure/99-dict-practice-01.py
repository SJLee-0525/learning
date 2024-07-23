# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    blood_type_dict = {}
    for blood_type in blood_types:
        if blood_type not in blood_type_dict:
            blood_type_dict[blood_type] = 1
        else:
            blood_type_dict[blood_type] = blood_type_dict[blood_type] + 1

    return blood_type_dict

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    blood_type_dict = {}
    for blood_type in blood_types:
        if blood_type_dict.get(blood_type, None) == None:
            blood_type_dict[blood_type] = 1
        else:
            blood_type_dict[blood_type] = blood_type_dict.get(blood_type) + 1
    
    return blood_type_dict

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
