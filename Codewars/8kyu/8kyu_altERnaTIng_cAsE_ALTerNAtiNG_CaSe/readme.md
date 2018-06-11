# [altERnaTIng cAsE <=> ALTerNAtiNG CaSe](https://www.codewars.com/kata/alternating-case-%3C-equals-%3E-alternating-case)

altERnaTIng cAsE <=> ALTerNAtiNG CaSe
Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

```python
"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
"1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
"String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
```

As usual, your function/method should be pure, i.e. it should not mutate the original string.

## My Solution

```python
def to_alternating_case(string):
    # return ''.join(ch if not ch.isalpha() else ch.upper() if ch.islower() else ch.lower() for ch in string)
    # return string.swapcase()
    return ''.join(ch.upper() if ch.islower() else ch.lower() for ch in string)
```

## Other Solutions

```python
def to_alternating_case(string):
    return string.swapcase()
```

```python
to_alternating_case = string.swapcase()
```

```python
 def to_alternating_case(string):
    return ''.join(ch.upper() if ch.islower() else ch.lower() for ch in string)
```