def rps(p1, p2):
    cases = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
    return 'Draw!' if p1 == p2 else 'Player 1 won!' if cases.get(p1) == p2 else 'Player 2 won!'

print(rps('rock', 'scissors') == "Player 1 won!")
print(rps('scissors', 'paper') == "Player 1 won!")
print(rps('paper', 'rock') == "Player 1 won!")

print(rps('scissors', 'rock') == "Player 2 won!")
print(rps('paper', 'scissors') == "Player 2 won!")
print(rps('rock', 'paper') == "Player 2 won!")

print(rps('rock', 'rock') == 'Draw!')
print(rps('scissors', 'scissors') == 'Draw!')
print(rps('paper', 'paper') == 'Draw!')
