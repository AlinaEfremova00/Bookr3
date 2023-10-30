from django.contrib import admin
from revieWs.models import (Publisher, Contributor, Book, BookContributor, Review)
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)