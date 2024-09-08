from django.contrib import admin
from .models import Question,Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice

class QuestionAdmn(admin.ModelAdmin):
    fieldsets=[
            (None,{"fields":["qt"]}),
            (None,{"fields":["pd"],
                   'classes':['collapse']})
               ]
    inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmn)