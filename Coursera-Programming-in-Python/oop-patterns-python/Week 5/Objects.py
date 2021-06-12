from abc import ABC, abstractmethod
import pygame
import random
import Service


def create_sprite(img, sprite_size):
    icon = pygame.image.load(img).convert_alpha()
    icon = pygame.transform.scale(icon, (sprite_size, sprite_size))
    sprite = pygame.Surface((sprite_size, sprite_size), pygame.HWSURFACE)
    sprite.blit(icon, (0, 0))
    return sprite

class AbstractObject(ABC):
    @abstractmethod
    def __init__(self):
        self.sprite = []

    @abstractmethod
    def draw(self, display):
        pass
    
class Interactive(ABC):

    @abstractmethod
    def interact(self, engine, hero):
        pass


class Ally(AbstractObject, Interactive):

    def __init__(self, icon, action, position):
        self.sprite = icon
        self.action = action
        self.position = position

    def interact(self, engine, hero):
        self.action(engine, hero)

    def draw(self, display):
        display.draw_objects(self.sprite, self.position)

class Creature(AbstractObject):

    def __init__(self, icon, stats, position):
        self.sprite = icon
        self.stats = stats
        self.position = position
        self.calc_max_HP()
        self.hp = self.max_hp

    def calc_max_HP(self):
        self.max_hp = 5 + self.stats["endurance"] * 2

    def draw(self, display):
        display.draw_object(self.sprite, self.position)


class Enemy(Creature, Interactive):

    def __init__(self, icon, stats, exp, position):
        super().__init__(icon, stats, position)
        self.exp = exp
        self.calc_max_HP()
        self.hp = self.max_hp
        self.action = Service.add_gold

    def interact(self, engine, hero):
        hit = random.randint(0, 1)
        if hit == 1:
            hero.hp -= self.stats["strength"]
        if hero.hp <= 0:
            engine.notify("You'r DEAD")
            engine.game_process = False
        else:
            hero.exp += self.exp
            for i in hero.level_up():
                engine.notify(i)
            self.action(engine, hero)


class Hero(Creature):

    def __init__(self, stats, icon):
        pos = [1, 1]
        self.level = 1
        self.exp = 0
        self.gold = 0
        super().__init__(icon, stats, pos)

    def level_up(self):
        while self.exp >= 100 * (2 ** (self.level - 1)):
            yield "level up!"
            self.level += 1
            self.stats["strength"] += 2
            self.stats["endurance"] += 2
            self.calc_max_HP()
            self.hp = self.max_hp


class Effect(Hero):

    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        self.apply_effect()

    @property
    def position(self):
        return self.base.position

    @position.setter
    def position(self, value):
        self.base.position = value

    @property
    def level(self):
        return self.base.level

    @level.setter
    def level(self, value):
        self.base.level = value

    @property
    def gold(self):
        return self.base.gold

    @gold.setter
    def gold(self, value):
        self.base.gold = value

    @property
    def hp(self):
        return self.base.hp

    @hp.setter
    def hp(self, value):
        self.base.hp = value

    @property
    def max_hp(self):
        return self.base.max_hp

    @max_hp.setter
    def max_hp(self, value):
        self.base.max_hp = value

    @property
    def exp(self):
        return self.base.exp

    @exp.setter
    def exp(self, value):
        self.base.exp = value

    @property
    def sprite(self):
        return self.base.sprite

    @sprite.setter
    def sprite(self, value):
        self.base.sprite = value

    @abstractmethod
    def apply_effect(self):
        self.calc_max_HP()
        if self.max_hp < self.hp:
            self.hp = self.max_hp


# FIXME
# add classes
class Berserk(Effect):

    def apply_effect(self):
        self.stats["strength"] += 5
        super().apply_effect()


class Blessing(Effect):

    def apply_effect(self):
        self.stats["strength"] += 1
        self.stats["intelligence"] += 1
        self.stats["luck"] += 2
        super().apply_effect()


class Weakness(Effect):

    def apply_effect(self):
        self.stats["strength"] -= 2
        self.stats["endurance"] -= 2
        super().apply_effect()

class Curse(Effect):
    def apply_effect(self):
        self.stats["strength"] -= 2
        self.stats["luck"] -= 2
        super().apply_effect()