from django.contrib import admin
from myapp.models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, { 'fields': ['question']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'date', 'was_published_recently')
    list_filter = ['date']
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
