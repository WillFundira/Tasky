from django.db import models
from django.contrib.auth.models import User

# Create your models here
# database structure

class Task(models.Model):
    # one to many relationshi
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    created =  models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    
    # when returning muliplt queries, order by the stated value
    class Meta:
        ordering = ['complete']

