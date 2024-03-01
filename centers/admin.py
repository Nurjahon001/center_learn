from django.contrib import admin

from centers.models import Center, CenterAuthor, Author, CenterReview


# Register your models here.
class CenterModelAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name','description','courses']
    list_filter = ['create_at']


admin.site.register(CenterAuthor)
admin.site.register(Center,CenterModelAdmin)
admin.site.register(Author)
admin.site.register(CenterReview)