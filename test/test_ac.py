
import test_context
from creatures.stats.armor_class import ArmorClass
from creatures.stats.modifier import Modifier

ac = ArmorClass()
ac.add_perma_mod(Modifier(2, 'Proficiency'))
ac.add_perma_mod(Modifier(2, 'Rogue'))
ac.add_temp_mod(Modifier(-2, 'Stunned'))
tm = Modifier(-4, 'Is a sheep')
ac.add_temp_mod(tm)
print(ac.get_description())

print('\n\n')

tm.remove_from_parent()
print(ac.get_description())
