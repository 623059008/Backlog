from django.contrib import admin

# Register your models here.
from thing.models import Thing
from thing.models import User

# TEMPLATE_DIRS = (
#     '/thing/templates',
# )
admin.site.register(Thing)
admin.site.register(User)
