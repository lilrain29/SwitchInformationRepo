from django.contrib import admin
from .models import Switch, Port


class PortInline(admin.TabularInline):
    model = Port
    extra = 0
    fields = (
        "number", "connected_device", "ip_address", "device_name",
        "portType", "status", "vlanNum", "upLink", "addInfo", "cabPlacement"
    )


@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    list_display = (
        "name", "placement", "serialNum", "inventoryNum",
        "macAddr", "ip_address", "ports_count"
    )
    search_fields = ("name", "ip_address", "serialNum", "inventoryNum", "macAddr")
    list_filter = ("placement",)
    inlines = [PortInline]


@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = (
        "switch", "number", "connected_device", "ip_address", "device_name",
        "portType", "status", "vlanNum", "upLink", "addInfo", "cabPlacement"
    )
    list_filter = ("status", "portType", "switch")
    search_fields = ("connected_device", "ip_address", "device_name", "vlanNum")