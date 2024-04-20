from django.db import models
from apps.users.models import Account

STATUS = (
    (0, "Low"),
    (1, "Medium"),
    (2, "High"),
)


class Todo(models.Model):
    title = models.CharField(max_length=223)
    status = models.IntegerField(choices=STATUS, default=0)
    notes = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name="user_todoes")

    def __str__(self) -> str:
        return self.title

