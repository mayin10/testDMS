from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Employee,Role,Node, Role_Node,Document,Folder,File,Role_Folder

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    fields = ['role_name']
    list_display = ('role_name', 'create_time','create_by')
    search_fields = fields
    list_filter = fields

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    fields = ['node_name','p_id','level']
    list_display = ('node_name','parent','level', 'create_time','create_by')

@admin.register(Role_Node)
class RoleNodeAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'node_name' ,'create_time', 'create_by')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("location", "documentID", "status", "version","note")
    search_fields = list_display
    list_filter = list_display

@admin.register(Folder)
class Folder(admin.ModelAdmin):
    list_display = ("folder_name", "p_id", "level", "right")
    search_fields = ("folder_name", "p_id", "level")
    list_filter = ("folder_name", "p_id", "level")

@admin.register(Role_Folder)
class RoleNodeAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'folder_name' ,'create_time', 'create_by')


@admin.register(File)
class File(admin.ModelAdmin):
    list_display = ("file_name", "version", "note")
    search_fields = list_display
    list_filter = list_display

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
