from django.contrib import admin
from .models import Question


class QuestionsAdmin(admin.ModelAdmin):
        model = Question
        list_display=('category','ask','correct_answer')
        readonly_fields = ('registered','modified')
        

admin.site.register(Question, QuestionsAdmin)