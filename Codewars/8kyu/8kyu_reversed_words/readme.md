# [8kyu Reversed words](https://www.codewars.com/kata/reversed-words)

Complete the solution so that it reverses all of the words within the string passed in.

Example:

```python
reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
```


## My Solution

```python
def reverseWords(str):
    # return ' '.join(reversed(str.split(' ')))
```

## Other Solutions

```python
def reverseWords(str):
    return ' '.join(str.split(' ')[::-1])
```

```python
def reverseWords(str):
    return ' '.join(reversed(str.split()))
```
