from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Article_By_Tag_Relation


class RelationInlineFormset(BaseInlineFormSet):
    def clean(self):
        num = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                num += 1

        if num > 1:
                raise ValidationError('ОШИБКА. Больше одного основного раздела. ')
        if num == 0:
            raise ValidationError('ОШИБКА. Не указан основной раздел.')

        return super().clean()


class ScopeRelationInline(admin.TabularInline):
    model = Article_By_Tag_Relation
    formset = RelationInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeRelationInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass