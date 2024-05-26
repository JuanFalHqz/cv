from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Ability(models.Model):
    ability = models.CharField(max_length=100)

    def __str__(self):
        return self.ability


class User(AbstractUser):
    photo = models.ImageField(upload_to='photos/avatars/',blank=True)
    professional_title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    # Enlaces a perfiles de redes sociales
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    abilities = models.ManyToManyField(Ability, blank=True)

    def __str__(self):
        return self.username


class Mobil(models.Model):
    personalData = models.ForeignKey(User, on_delete=models.CASCADE)
    mobil = models.CharField(max_length=20)

    def __str__(self):
        return self.mobil


class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    location_kind = models.CharField(max_length=100,
                                     choices=(
                                         ('Presencial', 'Presencial'),
                                         ('Híbrido"', 'Híbrido'),
                                         ('Remoto', 'Remoto'),
                                     ))
    employ_kind = models.CharField(max_length=100,
                                   choices=(
                                       ('Contrato temporal', 'Contrato temporal'),
                                       ('Jornada completa', 'Jornada completa'),
                                       ('Jornada parcial', 'Jornada parcial'),
                                       ('Autónomo', 'Autónomo'),
                                   ))
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_currently_work = models.BooleanField(default=False)
    position_title = models.CharField(max_length=100)
    responsibilities = models.TextField()
    achievements = models.TextField()

    def __str__(self):
        return self.company


class UserWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    abilities = models.ManyToManyField(Ability)

    class Meta:
        unique_together = (('user', 'work'),)


class Education(models.Model):
    personal_data = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_currently_education = models.BooleanField(default=False)
    degree = models.CharField(max_length=100)
    honors = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.institution


class Project(models.Model):
    personal_data = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    results = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    personal_data = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(
        choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=100)

    def __str__(self):
        return self.name


class Certification(models.Model):
    personal_data = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reference(models.Model):
    personal_data = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobil = models.ManyToManyField(Mobil)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ProjectsPhoto(models.Model):
    personal_data = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/projects/%Y/%m/%d/')
