import test_context
from dice.die import Die
from dice.error import NoSuchFaceError

d = Die.d(20)
rs = {}
NROLLS = 100000

try:
  d.set_face(30)
except NoSuchFaceError as ex:
  print('Set incorrect face, error appropriately thrown:\n%s' % ex)

for _ in range(NROLLS):
  v = d.roll()
  if v not in rs:
    rs[v] = 1
  else:
    rs[v] += 1
    
for i in range(1, 21):
  print('%s: %s, %.2f%%' % (i, rs[i], rs[i]/NROLLS*100))
