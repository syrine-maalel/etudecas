from django.contrib import admin
from .models import Participant, Reservation


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 1  


class ParticipantAdmin(admin.ModelAdmin):
    
    list_display = ('cin', 'username', 'email', 'participant_category', 'created_at')
    
    
    search_fields = ('cin', 'username', 'email')
    
    
    list_filter = ('participant_category', 'created_at')
    
   
    list_per_page = 20  
    
    # 5. Define ordering (display participants by latest sign-up date)
    ordering = ('-created_at',)
    
    # 6. Group fields into sections for better organization
    fieldsets = (
        ('Personal Information', {
            'fields': ('cin', 'username', 'email', 'participant_category', 'first_name', 'last_name')
        }),
        ('Permissions and Status', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'created_at', 'update_at')
        }),
    )
    
    # 7. Read-only fields (non-modifiable)
    readonly_fields = ('last_login', 'created_at', 'update_at')
    
    # 8. Inline display of related reservations
    inlines = [ReservationInline]

# Custom admin class for Reservation
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('participant', 'conference', 'reservation_date', 'confirmed')  # Include 'confirmed'
    search_fields = ('participant__username', 'conference__title')  # Search by participant or conference
    list_filter = ('confirmed', 'reservation_date')  # Filter by confirmation status and reservation date
    actions = ['mark_confirmed', 'mark_unconfirmed']  # Add actions for bulk confirmation status changes
    
    # 9. Add actions to mark reservations as confirmed or unconfirmed
    def mark_confirmed(self, request, queryset):
        queryset.update(confirmed=True)
    mark_confirmed.short_description = "Mark selected reservations as confirmed"

    def mark_unconfirmed(self, request, queryset):
        queryset.update(confirmed=False)
    mark_unconfirmed.short_description = "Mark selected reservations as unconfirmed"

# Register the customized admin classes
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Reservation, ReservationAdmin)
