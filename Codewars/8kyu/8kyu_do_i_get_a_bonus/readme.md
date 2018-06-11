# [8kyu Do I get a bonus?](https://www.codewars.com/kata/do-i-get-a-bonus/train/python)

It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?

Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "£" (= "\u00A3", JS and Java) or "$" (C#, C++, Ruby, Clojure, Elixir, PHP and Python).

## My Solution

```python
def bonus_time(salary, bonus):
    return '$%d' % (salary * 10 if bonus else salary)
```

## Ohter Solutions

```python
def bonus_time(salary, bonus):
    return '${}'.format(salary * (10 if bonus else 1))
```