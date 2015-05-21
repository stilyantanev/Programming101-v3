from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField()
    cover = models.ImageField(blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.rating)


class Projection(models.Model):
    movie = models.ForeignKey(Movie)
    movie_format = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        text = "{} - {} - {} - {}"
        text = text.format(self.movie, self.movie_format, self.date, self.time)

        return text


class Reservation(models.Model):
    projection = models.ForeignKey(Projection)
    username = models.CharField(max_length=100)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()

    def __str__(self):
        text = "{} - {} - {} - {}"
        text = text.format(self.projection, self.username, self.row, self.col)

        return text
