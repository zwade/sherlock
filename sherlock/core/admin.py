from django.contrib import admin
from .models import Hunt, Clue, Submission

# Register your models here.
admin.site.register(Hunt)
admin.site.register(Clue)
admin.site.register(Submission)
