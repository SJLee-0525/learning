# 모듈 사용하기 (import)
# import my_math

# print(my_math.add(1, 2))

# 모듈 사용하기 (from)
# from my_math import add

# print(add(1, 2))

# 패키지 사용하기
from my_package.math import my_math

print(my_math.add(3, 4)) # 7

from my_package.statistics import tools

print(tools.mod(1, 2)) # 1

import math

help(math)