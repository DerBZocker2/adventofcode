# Part 1

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def selection_score(x): return ord(x) - 64
# Calculate the score for your selection


def result_score(opp, you):
  # Calculate the score for the result
  if (opp == you):
    return 3
  match opp:
    case 'A':
      return 6 if you == 'B' else 0
    case 'B':
      return 6 if you == 'C' else 0
    case 'C':
      return 6 if you == 'A' else 0


# Parse turns
turns = [[line[0], chr(ord(line[2]) - 23)]
         for line in open(f"{dir_path}/input.txt", "r")]

# Calculate score per turn
scores = [selection_score(turn[1]) + result_score(turn[0], turn[1])
          for turn in turns]

# Get total
print(sum(scores))


# Part 2


def selection(opp, goal):
  # Determine what you should select to win, lose or draw
  def win(x): return 'B' if x == 'A' else 'C' if x == 'B' else 'A'
  def lose(x): return 'C' if x == 'A' else 'A' if x == 'B' else 'B'

  return lose(opp) if goal == 'A' else opp if goal == 'B' else win(opp)


# Calculate score per turn using new selection
scores = [
    selection_score(selection(turn[0], turn[1])) +
    result_score(turn[0], selection(turn[0], turn[1]))
    for turn in turns]

# Get total
print(sum(scores))
