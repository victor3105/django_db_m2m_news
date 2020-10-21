from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope, AssignedTags


class AssignedTagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                main_count += 1
            if main_count > 1:
                raise ValidationError('Только один раздел может быть основным')
        return super().clean()


class AssignedTagsInline(admin.TabularInline):
    model = AssignedTags
    formset = AssignedTagsInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (AssignedTagsInline, )


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
