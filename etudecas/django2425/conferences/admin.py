from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Conference
from users.models import *
from django.db.models import Count
# Register your models here.
class ReservationInline(admin.StackedInline):
    model=Reservation
    extra=1
    readonly_fields=('reservation_date',)
    can_delete=True
class ConferenceDateFilter(admin.SimpleListFilter): #j c
     title='date conf filter '
     parameter_name='conference_date'

     def lookups(self,request,model_admin):
          return(
               ('past','past conf'),
               ('today','today conf'),
               ('upcoming','upcoming conf'),
          )
     
     def queryset(self, request, queryset) :
          
          if self.value()=='past':
               return queryset.filter(start_date__lt=timezone.now().date()) 
          if self.value()=='today':     
               return queryset.filter(start_date=timezone.now().date())
          if self.value()=='upcoming':     
               return queryset.filter(start_date__gt=timezone.now().date())
          return queryset


class ParticipantFilter(admin.SimpleListFilter):
      #question j b
      title="participant filter"
      parameter_name="paticipants"
      def lookups(self,request,model_admin) :
           return (
               ('0',('no participants')),
               ('more',('more participants'))
           )
      #reste j b
      def queryset(self, request, queryset) :
          
          if self.value()=='0':
               return queryset.annotate(participant_count=Count('reservations')).filter(participant_count=0) #annotate 5ater relation many to many

          if self.value()=='more':     
               return queryset.annotate(participant_count=Count('reservations')).filter(participant_count__gt=0)
          return queryset

     

class ConferenceAdmin(admin.ModelAdmin):
    list_display=('title','location','start_date','end_date','price')
    search_fields=('title',)
    list_per_page=2
    ordering=('start_date','title')    
    fieldsets =(
        ('Descriptions',{
            'fields':('title','description','capacity','category','location','price')
        }),
        ('Horraires',{
            'fields':('start_date','end_date','created_at','update_at')
        }),
        ('Documents',{
            'fields':('program',)
        })
    )
    readonly_fields=('created_at','update_at')
    inlines=[ReservationInline]
    autocomplete_fields=('category',)
    list_filter=('title',ParticipantFilter,ConferenceDateFilter) #qeust j 
admin.site.register(Conference,ConferenceAdmin)



