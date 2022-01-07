RULES = {
  ('scissors', 'paper'): 'Scissors cut Paper',
  ('paper', 'rock'): 'Paper covers Rock',
  ('rock', 'scissors'): 'Rock breaks Scissors',
  ('rock', 'lizard'): 'Rock crushes Lizard',
  ('lizard', 'spock'): 'Lizard poisons Spock',
  ('spock', 'scissors'): 'Spock melts Scissors',
  ('lizard', 'scissors'): 'Scissors decapitate Lizard',
  ('lizard', 'paper'): 'Lizard eats Paper',
  ('spock', 'paper'): 'Paper disproves Spock',
  ('spock', 'rock'): 'Spock vaporizes Rock',
  
}

hand1 = input("Hand 1: ").lower()
hand2 = input("Hand 2: ").lower()
winner = RULES.get((hand1, hand2), RULES.get((hand2, hand1), 'Tie'))
print(winner) 
