from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Director(models.Model):
    director_id = models.AutoField(primary_key=True)
    director_first_name = models.CharField(max_length=45, unique=True)
    director_last_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s %s' % (self.director_first_name, self.director_last_name)

    def get_absolute_url(self):
        return reverse('director_detail',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('director_update',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['director_last_name', 'director_first_name']
        constraints = [
            UniqueConstraint(fields=['director_last_name', 'director_first_name'], name='unique_director')
        ]


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    actor_first_name = models.CharField(max_length=45, unique=True)
    actor_last_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s %s' % (self.actor_first_name, self.actor_last_name)

    def get_absolute_url(self):
        return reverse('actor_detail',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('actor_update',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['actor_last_name', 'actor_first_name']
        constraints = [
            UniqueConstraint(fields=['actor_last_name', 'actor_first_name'], name='unique_actor')
        ]


class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % (self.platform_name)

    def get_absolute_url(self):
        return reverse('platform_detail',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('platform_update',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['platform_name']
        constraints = [
            UniqueConstraint(fields=['platform_name'], name='unique_platform')
        ]


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % (self.genre_name)

    def get_absolute_url(self):
        return reverse('genre_detail',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('genre_update',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['genre_name']
        constraints = [
            UniqueConstraint(fields=['genre_name'], name='unique_genre')
        ]


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_year = models.IntegerField(unique=True)
    movie_name = models.CharField(max_length=45, unique=True)
    genre = models.ForeignKey(Genre, related_name="movies", on_delete=models.PROTECT)
    director = models.ForeignKey(Director, related_name="movies", on_delete=models.PROTECT)

    def __str__(self):
        result = '%s [%s] (%s)' % (self.movie_name, self.genre, self.movie_year)
        return result

    def get_absolute_url(self):
        return reverse('movie_detail',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('movie_update',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['movie_name', 'genre', 'movie_year']
        constraints = [
            UniqueConstraint(fields=['movie_year', 'movie_name', 'genre'], name='unique_movie')
        ]


class Casting(models.Model):
    casting_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, related_name="castings", on_delete=models.PROTECT)
    actor = models.ForeignKey(Actor, related_name="castings", on_delete=models.PROTECT)

    def __str__(self):
        result = '%s / %s' % (self.movie, self.actor)
        return result

    def get_absolute_url(self):
        return reverse('casting_detail',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('casting_update',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['movie', 'actor']
        constraints = [
            UniqueConstraint(fields=['movie', 'actor'], name='unique_casting')
        ]


class Watching(models.Model):
    watching_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, related_name="watchings", on_delete=models.PROTECT)
    platform = models.ForeignKey(Platform, related_name="watchings", on_delete=models.PROTECT)

    def __str__(self):
        result = '%s / %s' % (self.movie, self.platform)
        return result

    def get_absolute_url(self):
        return reverse('watching_detail',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('watching_update',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['movie', 'platform']
        constraints = [
            UniqueConstraint(fields=['movie', 'platform'], name='unique_watching')
        ]