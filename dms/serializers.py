from rest_framework import serializers
from .models import Employee,Role,Node, Role_Node,Document,Folder,File,Role_Folder

class RoleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class NodeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"

class RoleNodeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_Node
        fields = "__all__"

class DocumentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class FolderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =  File
        fields = "__all__"

class RoleFolderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_Folder
        fields = "__all__"