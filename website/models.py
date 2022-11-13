from django.db import models


class Appointment(models.Model):
    """This class is for an appointment with the doctor"""
    department = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    phone =  models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    """This class is for website newsletter"""
    email = models.EmailField()

    def __str__(self):
        return self.email


class Quote(models.Model):
    """This class is for Quote"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    website = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Contact(models.Model):
    """This class is for users to contact the admin"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
