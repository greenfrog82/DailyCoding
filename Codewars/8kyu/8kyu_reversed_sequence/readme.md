# [8kyu Reversed sequence](https://www.codewars.com/kata/reversed-sequence)


Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]


## My Solution

```python
def reversed_seq(n):
    return list(range(n, 0, -1))