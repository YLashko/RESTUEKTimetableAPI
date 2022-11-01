from django.db import models


class Timetable(models.Model):
    group_id = models.CharField(null=True, max_length=6)
    group_name = models.CharField(null=True, max_length=50)
    updated = models.DateTimeField()


class TableRow(models.Model):
    date = models.DateField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    subject_name = models.CharField(null=True, max_length=200)
    type = models.CharField(null=True, max_length=50)
    professor_name = models.CharField(null=True, max_length=200)
    professor_page_link = models.CharField(null=True, max_length=200)
    rescheduled_info = models.CharField(null=True, max_length=200)
    timetable = models.ForeignKey(Timetable, related_name="row", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.timetable.group_name} {self.date.strftime('%Y-%m-%d')}:\
         {self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')}"

    def dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "start_time": self.start_time.strftime("%H:%M"),
            "end_time": self.end_time.strftime("%H:%M"),
            "subject_name": self.subject_name,
            "type": self.type,
            "rescheduled_info": self.rescheduled_info,
            "professor_name": self.professor_name,
            "professor_page_link": self.professor_page_link
        }
