from django.contrib import admin

from .models import Article, Scope, AssignedTags


class AssignedTagsInline(admin.TabularInline):
    model = AssignedTags
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (AssignedTagsInline, )


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = (AssignedTagsInline, )
