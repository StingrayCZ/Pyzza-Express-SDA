from django.contrib.auth.models import User
from django.db import models


class Meal(models.Model):
    FOOD_TYPE = (
        ("hlavné jedlo", "hlavné jedlo"),
        ("špecialita", "špecialita"),
        ("burger", "burger"),
        ("príloha", "príloha"),
        ("cestoviny", "cestoviny"),
        ("šalát", "šalát"),
        ("pizza", "pizza"),
        ("polievka", "polievka"),
        ("dezert", "dezert"),
        ("nápoj", "nápoj"),
    )

    food_name = models.CharField(max_length=200)
    food_description = models.CharField(max_length=2000, blank=True)
    food_price = models.FloatField()
    food_image = models.ImageField(default="default.png", upload_to="images/")
    food_types = models.CharField(choices=FOOD_TYPE, max_length=20, default="špecialita")
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name

    class Meta:
        app_label = 'menu_app'

