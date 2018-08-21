from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoicesTable(admin.TabularInline):
    """
    Permet d'afficher et de créer les choix depuis le
    formulaire des questions
    """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """
    Paramétrage de l'affichage des champs dans
    l'interface d'administration Django
    """
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoicesTable]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # ordering = ('-pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
