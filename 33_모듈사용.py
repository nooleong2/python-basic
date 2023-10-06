# 두개의 차이 앞에 모듈네임을 붙일것인지 안붙일것인지 차이 그 외에 동일

import calculator_module as c # 별칭 사용 (왜? 호출 할때 너무 길어서)
print("import")
c.add(10, 20)
c.substract(10, 5)
c.multiple(9, 9)
c.division(10, 2)

from calculator_module import * # 별칭 까지 안쓰고 싶을 때 단 메소드 이름이 많이 겹칠거같다 안쓰는것이 좋을 듯
print("from import")
add(10, 20)
substract(10, 5)
multiple(9, 9)
division(10, 2)



