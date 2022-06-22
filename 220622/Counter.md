# Counter in Collections

## 데이터의 개수를 셀 때 유용한 클래스
```
from collections import Counter
```
## Counter("리스트")의 리턴 값은 "값,횟수" 의 Dictionary형태이다

```
print(Counter("HELLO WORLD"))
print(len(Counter("HELLO WORLD")))

>>
Counter({'L': 3, 'O': 2, 'H': 1, 'E': 1, ' ': 1, 'W': 1, 'R': 1, 'D': 1})
8
```





