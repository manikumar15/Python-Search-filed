from django.db import models

class News(models.Model):
    Email = models.EmailField()

    def __str__(self):
        return self.Email

class Python(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    message=models.TextField(max_length=100)
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Api(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    message=models.TextField(max_length=100)
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Html(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    message=models.TextField(max_length=100)
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Search(models.Model):
    course = models.CharField(max_length=40,null=True)
    faculty = models.CharField(max_length=40,null=True)
    timings =  models.CharField(max_length=40,null=True)
    duration = models.CharField(max_length=40,null=True)
    location = models.CharField(max_length=40,null=True)


    def __str__(self):
        return self.course