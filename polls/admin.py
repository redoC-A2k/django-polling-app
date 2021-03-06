from django.contrib import admin
from .models import Choice, Question
# Register your models here.

class ChoiceInline(admin.TabularInline):
    """ChoiceInline admin class"""
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """Question class admin"""
    fieldsets = [
            (None,{'fields':['question_text']}),
            ('Date information',{'fields':['pub_date'],'classes':['collapse']})
            ]
    list_display = ('question_text','pub_date','was_published_recently')
    inlines = [ChoiceInline]
    search_fields = ['question_text']
    list_filter = ['pub_date']

admin.site.register(Question,QuestionAdmin)
