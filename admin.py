from django.contrib import admin
from .models import Stacks 
from .models import Alert

#admin.site.register(Stacks)
#admin.site.register(Alert)

@admin.register(Stacks)
class StackAdmin(admin.ModelAdmin):
	list_display = ('nameCompany', 'nameSystem', 'versionSystem', 'vendeur', 'typeSystem')


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
	fields = ('nomAlert', 'descriptionAlert', 'sousValeurAlert')