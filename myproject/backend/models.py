from django.db import models
from django.contrib.auth.models import User


class Core(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    level = models.IntegerField(default=0)

    def click(self):
        self.coins += self.click_power

        if self.coins >= self.check_level_price():
            self.level += 1

            return True
        return False

    def check_level_price(self):
        return (self.level ** 2 + 1) * 100 * (self.level + 1)


class Boost(models.Model):
    core = models.ForeignKey(Core, null=False, on_delete=models.CASCADE)
    lvl = models.IntegerField(default=1)
    price = models.IntegerField(default=10)
    power = models.IntegerField(default=1)
