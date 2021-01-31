import math

class DieEquation(object):
  def __init__(self, ndice, nsides, mod):
    self.ndice = ndice
    self.nsides = nsides
    self.mod = mod
    
  def _calc(self):
    return math.floor(self.ndice * (self.nsides + 1) / 2 + self.mod)
    
  def __repr__(self):
    return '%s (%sd%s %s %s)' % (self._calc(), self.ndice, self.nsides, '+' if self.mod >= 0 else '-', abs(self.mod))
