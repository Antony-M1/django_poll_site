from django.contrib import admin
from .models import (
    Question,
    Choice,
    Department,
    Employee,
    Project
)

admin.site.site_header = "Polls Administration"
admin.site.site_title = "Your Admin Title"
admin.site.index_title = "Welcome to Your Admin Panel"

admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']


admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


admin.site.register(Employee, EmployeeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name',]


admin.site.register(Project, ProjectAdmin)
