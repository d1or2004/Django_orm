from django.contrib import admin
from .models import Book, Author, Bookings, Comment

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Bookings)
admin.site.register(Comment)
