from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat

# Create your models here.
from data_show.validators import validate_telephone


def club_directory_path(instance, filename):
    return f'{instance.name}/{filename}'


class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=club_directory_path)
    description = models.TextField()
    structure = models.TextField(blank=True)
    source = models.URLField()
    club_head = models.OneToOneField(
        to='Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='leader',
    )
    manager = models.ForeignKey(
        to='Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='manager',
    )
    create_date = models.DateTimeField(auto_now_add=True)

    def date_ymd(self):
        return self.create_date.strftime('%d of %B, %Y')
    date_ymd.short_description = 'Create date'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_date']


class File(models.Model):
    club = models.ForeignKey(
        to='Club',
        on_delete=models.SET_NULL,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        default='Unknown file',
    )
    file = models.FileField(
        upload_to=club_directory_path,
        unique=True,
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    STATUS_CHOICES = (
        ('L', 'Leader'),
        ('M', 'Manager'),
    )
    portrait = models.ImageField(upload_to='contacts/', blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
    )
    email = models.EmailField(blank=True)
    telephone = models.CharField(
        max_length=17,
        validators=[validate_telephone],
        blank=True,
    )

    def get_contacts(self):
        return Contact.objects.filter(student=self)

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    full_name.admin_order_field = Concat(
        'last_name',
        Value(' '),
        'first_name'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        ordering = [
            'last_name',
            'first_name',
        ]


class Contact(models.Model):
    SOCIAL_SITE_CHOICES = (
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('vk', 'Vkontakte'),
        ('snapchat', 'Snapchat'),
        ('twitter', 'Twitter'),
    )
    student = models.ForeignKey(
        to='Student',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=10,
        choices=SOCIAL_SITE_CHOICES,
    )
    url = models.URLField()

    def __str__(self):
        return self.name
