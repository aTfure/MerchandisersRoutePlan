from django.contrib import admin
from .models import RoutePlan, Location


# RoutePlan Model
def activate_route_plans(modeladmin, request, queryset):
    queryset.update(is_active=True)
activate_route_plans.short_description = "Mark selected route plans as active"

@admin.register(RoutePlan)
class RoutePlanAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'user', 'date', 'is_active', 'created_at')
    actions = [activate_route_plans]


# Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('route_plan', 'latitude', 'longitude', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('route_plan__route_name',)
    ordering = ('-timestamp',)


admin.site.site_header = "Merchandisers Route Planner Admin"
admin.site.site_title = "Route Planner Admin Portal"
admin.site.index_title = "Welcome to the Route Planner Admin"
