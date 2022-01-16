class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, new_width):
    self.width = new_width
    return

  def set_height(self, new_height):
    self.height = new_height
    return

  def get_area(self, width, height):
    return width * height

  def get_perimeter(self, width, height):
    return 2 * height + 2 * width
  
  def get_diagonal(self, width, height):
    return (width**2 + height**2)/2
  
  def get_picture(self):
    '''prints the shape as a bunch of *'''
    picture = ""
    line = "*" * self.width + "\n"
    picture += line * self.height
    print(picture)

  def get_amount_inside(self, shape):
    '''Calculates times the given shape could fit inside this objects shape'''
    pass


class Square(Rectangle):
  pass
