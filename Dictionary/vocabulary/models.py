from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.soz}"

class Notogri(models.Model):
    t_soz = models.ForeignKey(Togri, on_delete=models.CASCADE)
    n_soz = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.n_soz}"

