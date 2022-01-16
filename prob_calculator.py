import copy 
# import random
from random import randrange

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)
    
  def draw(self, balls):
    removed = []
    if balls >= len(self.contents):
      return self.contents
    else:
      for ball in range(balls):
        position = randrange(len(self.contents))
        removed.append(self.contents[position])
        self.contents.pop(position)
      return removed
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  '''Repeats the same experiment a specified number of times to calculate the probability of drawing at least a certain number of specified objects'''
  successful_experiment = 0
  for experiment in range(num_experiments):
    '''Use of deepcopy ensures each experiment conducted is exactly the same'''
    expected = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)

    for color in balls_drawn:
      if color in expected:
        expected[color] -= 1
    
    if all(color <= 0 for color in expected.values()):
      successful_experiment += 1

  return successful_experiment / num_experiments