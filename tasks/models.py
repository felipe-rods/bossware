from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


PRIORITY_CHOICES = (
    ('H', 'Alta'),
    ('M', 'Média'),
    ('L', 'Baixa'),
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='tasks'
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)

    def clean(self):
        created = self.created_at or timezone.now().date()
        if self.deadline and self.deadline < created:
            raise ValidationError('O prazo não pode ser anterior à data de criação.')

    def __str__(self):
        return self.title
