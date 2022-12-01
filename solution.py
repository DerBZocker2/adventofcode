from bisect import insort
from functools import reduce

file = open('./input.txt')

def iterate(acc: tuple[int, list[int]], line: str):
  elf_sum, leaderboard = acc

  if line == '\n':
    insort(leaderboard, elf_sum)
    return (0, leaderboard)
  
  return (elf_sum + int(line), leaderboard)

_, leaderboard = reduce(iterate, file.readlines(), (0, []))

print(f"Max = {leaderboard[-1]}")
print(f"Top 3 = {sum(leaderboard[-3:])}")
