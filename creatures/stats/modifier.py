
class Modifier (object):
  def __init__(self, val, source):
    self.value = val
    self.source = source
    self.parent = None
    
  def remove_from_parent(self):
    self.parent.remove(self)
