class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __str__(self):
      square = f"Rectangle(width={self.width}, height={self.height})"
      return square
  
  def set_width(self, new_width):
    self.width = new_width
    return

  def set_height(self, new_height):
    self.height = new_height
    return

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.height + 2 * self.width
  
  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5
  
  def get_picture(self):
    '''prints the shape as a bunch of *'''
    picture = ""
    if self.width > 50 or self.height > 50:
      picture += "Too big for picture"
    else:
      line = "*" * self.width + "\n"
      picture += line * self.height
    return picture

  def get_amount_inside(self, shape):
    '''Calculates times the given shape could fit inside this objects shape'''
    no_in_width = int(self.width/shape.width)
    no_in_height = int(self.height/shape.height)
    return no_in_height * no_in_width


class Square(Rectangle):
  
  def __init__(self, sides):
    self.height = sides
    self.width = sides
  
  def __str__(self):
    square = f"Square(side={self.width})"
    return square

  def set_side(self, new_sides):
    self.width = new_sides
    self.height = new_sides
    return
