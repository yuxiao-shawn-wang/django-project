from django.db import models

class Squirrel(models.Model):
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length=20, primary_key=True)
    AM = 'AM'
    PM = 'PM'
    Shift_Choices = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]
    Shift = models.CharField(
        max_length=2,
        choices=Shift_Choices,
    )
    Date = models.DateField("Date")
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Other_Age = '?'
    Missing_Age = ''
    Age_Choices = [
        (Adult,'Adult'),
        (Juvenile,'Juvenile'),
        (Other_Age,'Unknown'),
        (Missing_Age,'Missing'),
    ]
    Age = models.CharField(
        max_length=10,
        choices=Age_Choices,
        default=Other_Age,
    )
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    Other_Color = ''
    Fur_Choices = [
        (Gray,'Gray'),
        (Cinnamon,'Cinnamon'),
        (Black,'Black'),
        (Other_Color,'Missing'),
        ]
    Primary_Fur_Color = models.CharField(
        max_length=10,
        choices=Fur_Choices,
        default=Other_Color,
    )
    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    Other_Location = ''
    Location_Choices = [
        (Ground_Plane,'Ground Plane'),
        (Above_Ground,'Above Ground'),
        (Other_Location,'Missing'),
    ]
    Location = models.CharField(
        max_length=15,
        choices=Location_Choices,
        default=Other_Location,
    )
    Specific_Location = models.TextField(max_length=200)
    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()
    Other_Activities = models.TextField(max_length=200)
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_flags = models.BooleanField()
    Tail_twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()
