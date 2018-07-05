# 배열에서 중복되는 원소 찾기 

1부터 1씩 증가하는 정렬되지 않은 원소 n개를 갖는 배열이 있다고 가정하자.  

예를들어 배열 원소가 5개라고 할 때, 다음과 같다. 

```python
[1, 2, 3, 4, 5] # 중복된 원소가 없는 경우
[1, 3, 2, 3, 4] # 중복된 원소가 있는 경우 (여기서 중복된 원소는 3)
```

이떄 배열에 중복되는 원소는 반드시 단 **한쌍**이다. 

함수를 하나 만드는데 이 함수는 인자로 앞서 설명한 조건의 배열을 인자로 받아 중복 된 원소가 발견되면 중복 된 원소의 값을 그렇지 않으면 -1을 반환하는 함수를 작성하시오. 

단, 인자로 전달 받은 inputs을 정렬하거나 변경하면 안된다. 즉, inputs는 immutable이라고 가정한다.
