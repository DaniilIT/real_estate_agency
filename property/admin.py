from django.contrib import admin

from .models import Flat, Complaint, Owner


# class PropertyOwnerFlats(models.Model):
#     owner = models.ForeignKey(PropertyOwner, models.DO_NOTHING)
#     flat = models.ForeignKey(PropertyFlat, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'property_owner_flats'
#         unique_together = (('owner', 'flat'),)


class OwnerFlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ('town', 'address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('likes',)
    inlines = [
        OwnerFlatInline,
    ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

