import json
import random

# 은행 목록
banks = [
    "신한은행", "국민은행", "우리은행", "하나은행", "NH농협은행",
    "카카오뱅크", "토스뱅크", "기업은행", "부산은행", "대구은행",
    "광주은행", "전북은행", "제주은행", "씨티은행", "스탠다드차타드은행"
]

# 상품 목록
products = [
    "정기예금", "특판정기예금", "우대정기예금", "청년정기예금", 
    "서민정기예금", "일반적금", "정기적금", "특판적금", 
    "자동차금융상품", "주택청약종합저축", "외화예금", "유니온 정기예금"
]

# 설명 목록
descriptions = [
    "안정적인 금리를 제공하는 정기예금입니다.",
    "높은 금리와 안전성을 자랑하는 상품입니다.",
    "특별한 조건을 만족할 경우 우대금리를 제공합니다.",
    "장기 가입 시 금리 우대를 제공합니다.",
    "신규 가입 고객을 위한 특별 이벤트가 있습니다.",
    "자동이체로 간편하게 관리할 수 있는 상품입니다."
]

# 더미 데이터 생성
deposit_products = []
deposit_options = []

for i in range(1, 501):
    fin_prdt_cd = f"DP{i:03}"
    kor_co_nm = random.choice(banks)
    fin_prdt_nm = f"{kor_co_nm} {random.choice(products)}"
    etc_note = random.choice(descriptions)
    join_deny = random.choice([1, 2, 3])
    join_member = "누구나 가입 가능" if join_deny == 1 else "서민층 전용"
    join_way = random.choice(["온라인", "방문", "온라인 및 방문"])
    spcl_cnd = "우대금리 조건 만족 시" if join_deny == 1 else "가입 6개월 이상 유지 시"

    deposit_products.append({
        "fin_prdt_cd": fin_prdt_cd,
        "kor_co_nm": kor_co_nm,
        "fin_prdt_nm": fin_prdt_nm,
        "etc_note": etc_note,
        "join_deny": join_deny,
        "join_member": join_member,
        "join_way": join_way,
        "spcl_cnd": spcl_cnd
    })

    intr_rate = round(random.uniform(2.0, 3.5), 2)
    intr_rate2 = round(random.uniform(2.5, 4.0), 2)
    save_trm = random.choice([6, 12, 24, 36, 48, 60])

    deposit_options.append({
        "product": fin_prdt_cd,
        "fin_prdt_cd": fin_prdt_cd,
        "intr_rate_type_nm": random.choice(["고정금리", "변동금리"]),
        "intr_rate": intr_rate,
        "intr_rate2": intr_rate2,
        "save_trm": save_trm
    })

# JSON 파일로 저장
with open('deposit_products.json', 'w', encoding='utf-8') as f:
    json.dump(deposit_products, f, ensure_ascii=False, indent=4)

with open('deposit_options.json', 'w', encoding='utf-8') as f:
    json.dump(deposit_options, f, ensure_ascii=False, indent=4)

print("더미 데이터 파일이 생성되었습니다.")
