# [8kyu Fake Binary](https://www.codewars.com/kata/fake-binary/train/python)

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

## My Solution

```python
def fake_bin(x):
    return ''.join('0' if 5 > int(ch) else '1' for ch in x)
```

## Other Solutions

```python
def fake_bin(x):
    return ''.join('0' if '5' > ch else '1' for ch in x)
```