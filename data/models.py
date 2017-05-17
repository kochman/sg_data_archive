from django.db import models


class Body(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'bodies'


class Meeting(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()
    session = models.ForeignKey('Session', related_name='meetings')

    def __str__(self):
        return f'{self.session} meeting ({self.date})'


class Membership(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    person = models.ForeignKey('Person', related_name='memberships')
    session = models.ForeignKey('Session', related_name='memberships')
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


class Motion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    number = models.IntegerField()
    descriptor = models.CharField(max_length=200)
    text = models.TextField()
    votes_for = models.IntegerField(null=True)
    votes_against = models.IntegerField(null=True)
    abstentions = models.IntegerField(null=True)
    meeting = models.ForeignKey(Meeting)
    moved_by = models.ForeignKey('Person', related_name='moved_motions', null=True)
    seconded_by = models.ForeignKey('Person', related_name='seconded_motions', null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.descriptor


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    preferred_name = models.CharField(max_length=60, blank=True)
    sessions = models.ManyToManyField('Session', through=Membership)
    profile = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='people_photos')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'people'


class Session(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    body = models.ForeignKey(Body)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

