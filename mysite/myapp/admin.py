from django.contrib import admin
from myapp.models import Gate, GateFunction, GateType, GateMaterial, GateMaterials#, FenceGate, BuildingGate

class GateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'installation_date', 'width_m']
    search_fields = [
        'name',
        'width_m',
        'height_m',
        # 'installation_date',
        # 'is_date_estimated',
        # 'gate_open_maximum_degrees',
        # 'gate_open_minimum_degrees'
    ]
    list_filter = [
        'name',
        # 'width_m',
        # 'height_m',
        # 'installation_date',
        # 'is_date_estimated',
        # 'gate_open_maximum_degrees',
        # 'gate_open_minimum_degrees'
    ]
    autocomplete_fields = [
        'gate_type_uuid',
        'gate_function_uuid'
    ]

    def gate_name(self, obj):
        return obj.name

class GateFunctionAdmin(admin.ModelAdmin):
    list_display = ['id', 'primary_function', 'last_update', 'last_update_by']
    search_fields = [
        'primary_function',
        'last_update',
        'last_update_by'
    ]
    list_filter = [
        'primary_function'
    ]

    def gate_function(self, obj):
        return obj.primary_function

class GateTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'primary_type', 'last_update', 'last_update_by']
    search_fields = [
        'primary_type',
        'last_update',
        'last_update_by'
    ]
    list_filter = [
        'primary_type'
    ]

    def gate_type(self, obj):
        return obj.primary_type

class GateMaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'material', 'last_update', 'last_update_by']
    search_fields = [
        'material',
        'last_update',
        'last_update_by'
    ]
    list_filter = [
        'material'
    ]

    def gate_material(self, obj):
        return obj.material

class GateMaterialsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_update', 'last_update_by']
    search_fields = [
        'name',
        'last_update',
        'last_update_by'
    ]
    list_filter = [
        'name',
    ]

    def gate_materials(self, obj):
        return obj.material


admin.site.register(Gate, GateAdmin)
admin.site.register(GateFunction, GateFunctionAdmin)
admin.site.register(GateType, GateTypeAdmin)
admin.site.register(GateMaterial, GateMaterialAdmin)
admin.site.register(GateMaterials, GateMaterialsAdmin)
# Register your models here.
