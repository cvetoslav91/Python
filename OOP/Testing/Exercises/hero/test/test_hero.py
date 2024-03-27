from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Batman', 10, 100, 50)
        self.enemy = Hero('Spiderman', 5, 100, 10)

    def test_init(self):
        self.assertEqual('Batman', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_against_yourself(self):
        self.enemy.username = 'Batman'
        with self.assertRaises(Exception) as exception:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(exception.exception))

    def test_health_less_than_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as exception:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(exception.exception))

    def test_enemy_health_less_than_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as exception:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Spiderman. He needs to rest", str(exception.exception))

    def test_hero_health_if_draw(self):
        self.enemy.level = 100
        self.hero.battle(self.enemy)

        self.assertEqual(-900, self.hero.health)

    def test_enemy_health_if_draw(self):
        self.hero.battle(self.enemy)
        self.assertEqual(-400, self.enemy.health)

    def test_if_func_returns_text(self):
        self.assertEqual("You win", self.hero.battle(self.enemy))

    def test_if_func_returns_draw_message(self):
        self.enemy.level = 100
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_if_func_returns_lose_message(self):
        self.hero.level = 0
        self.enemy.level = 100
        self.assertEqual("You lose", self.hero.battle(self.enemy))

    def test_if_hero_wins(self):
        self.hero.battle(self.enemy)

        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(55, self.hero.damage)

    def test_if_enemy_wins(self):
        self.hero.level = 0
        self.enemy.level = 100
        self.hero.battle(self.enemy)

        self.assertEqual(101, self.enemy.level)
        self.assertEqual(105, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test_str(self):
        self.assertEqual("Hero Batman: 10 lvl\n"
                         "Health: 100\n"
                         "Damage: 50\n", str(self.hero))



if __name__ == '__main__':
    main()
