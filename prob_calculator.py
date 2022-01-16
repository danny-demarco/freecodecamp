from random import randrange

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  ''''''
  pass

class Hat:

  def __init__(self, **kwargs):
    dict = self.__dict__.update((k,v) for k, v in kwargs.items())
    self.contents = []
    for k,v in dict:
      for v in k, v:
        self.contents.append(k)
    
  def draw(self, balls):
    removed = []
    if balls >= len(self.contents):
      return self.contents
    else:
      for ball in balls:
        position = randrange(len(self.contents))
        removed.append(self.contents[position])
        self.contents.pop(position)
      return removed