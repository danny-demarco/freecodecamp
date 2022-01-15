class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    return width

  def set_height(self, height):
    return height

  def get_area(self, width, height):
    return width * height

  def get_perimeter(self, width, height):
    return 2 * height + 2 * width
  
  def get_diagonal(self, width, height):
    return (width**2 + height**2)/2
  
  def get_picture(self, width, height):
    pass


class Square(Rectangle):
  pass
