from django.db import models

# Create your models here.

class StudentParent(models.Model):
    parentName = models.TextField(db_column='Parent Name')
    parentEmail = models.EmailField(max_length=50, db_column='Email')
    parentLocation = models.TextField(db_column='Location')
    parentContact = models.CharField(max_length=11, db_column='Contact')
    parentPassword = models.CharField(max_length=20,db_column='Password')

    class Meta:
        db_table = "Student's Parent Info"

class TemporarySP(models.Model):
    id = models.IntegerField(primary_key=True)
    parentName = models.TextField(db_column='Parent Name')
    parentPassword = models.CharField(max_length=20,db_column='Password')

    class Meta:
        db_table = "Student's Parent Temporary Table"