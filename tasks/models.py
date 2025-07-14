from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


PRIORITY_CHOICES = (
    ('H', 'Alta'),
    ('M', 'Média'),
    ('L', 'Baixa'),
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='tasks'
    )
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)

    def clean(self):
        if self.deadline < self.created_at:
            raise ValidationError('Prazo não pode ser anterior à data de criação.')
