from django.db import models


class HomeEducatorSubjects(models.Model):
    firstSubject = models.TextField(db_column='1st Subject')
    secondSubject = models.TextField(db_column='2nd Subject')
    thirdSubject = models.TextField(db_column='3rd Subject')

    class Meta:
        db_table = 'Home Educator Subjects'

class OutsideEducatorSubjects(models.Model):
    firstSubject = models.TextField(db_column='1st Subject')
    secondSubject = models.TextField(db_column='2nd Subject')
    thirdSubject = models.TextField(db_column='3rd Subject')

    class Meta:
        db_table = 'Outside Educator Subjects'


class HomeEducator(models.Model):
    homeTutorName = models.CharField(max_length=30)
    homeTutorEmail = models.EmailField(max_length=50)
    university = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    experience = models.IntegerField()
    homeTutorLocation = models.CharField(max_length=15)
    homeTutorContact = models.CharField(max_length=11)
    homeTutorPassword = models.CharField(max_length=20)
    homeTutorRating = models.FloatField()

    class Meta:
         db_table = 'Home Educator Info'

class OutsideEducator(models.Model):
    outsideTutorName = models.CharField(max_length=30)
    outsideTutorEmail = models.EmailField(max_length=50)
    institute = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    outsideTutorLocation = models.CharField(max_length=15)
    outsideTutorContact = models.CharField(max_length=11)
    outsideTutorPassword = models.CharField(max_length=20)
    outsideTutorRating = models.FloatField()

    class Meta:
         db_table = 'Outside Educator Info'


class TemporaryE(models.Model):
    id = models.IntegerField(primary_key=True)
    tutorName = models.TextField(db_column='Tutor Name')
    tutorPassword = models.CharField(max_length=20,db_column='Password')
    tutorType = models.CharField(max_length=20,db_column='Type',default='')

    class Meta:
        db_table = "Educator Temporary Table"

