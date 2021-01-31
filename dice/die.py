
from dice.error import NoSuchFaceError
import random


class Die (object):
  def __init__(self, faces):
    self._faces = faces
    self._cur_face_idx = 0
    
  def roll(self):
    self._cur_face_idx = random.randint(0, len(self._faces) - 1)
    return self.cur_face
    
  def set_face(self, face_val):
    if face_val in self._faces:
      self._cur_face_idx = self._faces.index(face_val)
    else:
      raise NoSuchFaceError('The given face value [%s] doesn\'t exist on this die.' % face_val)
  
  @property  
  def num_sides(self):
    return len(self._faces)
  
  @property  
  def cur_face(self):
    return self._faces[self._cur_face_idx]
   
  @staticmethod 
  def d(num_faces):
    return Die(range(1, num_faces+1))
