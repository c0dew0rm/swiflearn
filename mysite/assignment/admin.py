from django.contrib import admin
from .models import UserProfile, Class, Question, ClassTaken
# Register your models here.


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'age', 'city', 'grade', 'board', ]
    list_display = ['user', 'age', 'city', 'grade', 'board']


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['classTitle', 'instructorName']})
    ]
    # fields = ['classTitle', 'instructorName', ]
    list_display = ['classTitle', 'instructorName', ]
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['className', 'question', ]
    readonly_fields = ['id',]
    list_display = ['id', 'className', 'question', ]


@admin.register(ClassTaken)
class ClassTakenAdmin(admin.ModelAdmin):
    readonly_fields = ['id',]
    fields = ['user', 'classTaken']
    list_display = ['id', 'user', 'classTaken']
