def draw_cards(*args, **kwargs):
    monsters = []
    spells = []
    for name, type_of_card in args:
        if type_of_card == 'monster':
            monsters.append(name)
        else:
            spells.append(name)

    for name, type_of_card in kwargs.items():
        if type_of_card == 'monster':
            monsters.append(name)
        else:
            spells.append(name)

    if monsters:
        result = "Monster cards:\n"
        result += '\n'.join(['  ***' + m for m in sorted(monsters, reverse=True)])

    if spells:
        if not monsters:
            result = "Spell cards:\n"
        else:
            result += "\nSpell cards:\n"
        result += '\n'.join(['  $$$' + m for m in sorted(spells)])

    return result

print(draw_cards(("cyber dragon", "monster"), freeze="spell"))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell",
                 destroy="spell", ))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell", ))


import unittest


class TestDrawCardsFunction(unittest.TestCase):

    def test_case_zero_one(self):
        result = draw_cards(
            ('cyber dragon', 'monster'),
            freeze='spell',
        )

        self.assertEqual(
            result.strip(),
            """Monster cards:
  ***cyber dragon
Spell cards:
  $$$freeze""")


if __name__ == '__main__':
    unittest.main()
