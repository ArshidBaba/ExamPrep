from django.db import models
from django.db.models import manager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Questions(models.Model):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']
         
    q_id = models.IntegerField(default=0,  verbose_name="Question No.")
    question = models.CharField(max_length=255, verbose_name="Question")
    # title = models.CharField(default="Question", max_length=255, verbose_name=_("Title"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    correct_option = models.IntegerField(verbose_name="Answer")
    subject = models.CharField(max_length=255, verbose_name="Subject")
    exam_name = models.CharField(max_length=255, verbose_name="Exam")
    exam_year = models.IntegerField(verbose_name="Year")
    date = models.DateTimeField(auto_now=True, verbose_name="Date Created")

    def __str__(self):
        return self.title   

class Answers(models.Model):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']
         
    question = models.ForeignKey(Questions, related_name='answer', on_delete=models.DO_NOTHING)
    title = models.CharField(null=True, max_length=255, verbose_name=_("Title"))
    answer_text = models.CharField(max_length=255, verbose_name="Answer")
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.title
