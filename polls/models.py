from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'

    def __unicode__(self):
        pass
