from django.db import models
from studentParent.models import StudentParent
# Create your models here.


class ExamDetails(models.Model):
    examName = models.TextField(db_column='Exam Name')
    examID = models.IntegerField(primary_key=True, db_column='Exam Id')
    examDate = models.DateField(db_column='Exam Date')
    studentMarks = models.FloatField(max_length=6, db_column='Student Marks')
    parentID = models.ForeignKey(StudentParent, db_column='Parent Id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Exam Info'