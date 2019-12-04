from django.db import models


class Lesson(models.Model):
    class Meta:
        db_table = "lesson"

    title = models.CharField(max_length=255)
    length = models.IntegerField()
    shown = models.BooleanField(default=True)
