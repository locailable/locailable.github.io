from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from users.models import Profile
# Create your models here.


class Business(models.Model):
    owner = models.ForeignKey(
        'BusinessOwner', related_name='businesses', null=True, blank=True, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=250)
    address = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    availability = models.ForeignKey('Availability', related_name='businesses', on_delete=models.SET_NULL, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.business_name

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'business_name']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()


class BusinessOwner(models.Model):
    owner_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    business = models.ForeignKey(Business, related_name='owners', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name


class Availability(models.Model):
    availability_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    business = models.ForeignKey(Business, related_name='availabilities', on_delete=models.CASCADE)
    available_tables = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business.business_name} Available Tables: {self.available_tables}"
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='reviews')
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'business']]

    def __str__(self):
        return self.value


