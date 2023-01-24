from rest_framework.viewsets import ModelViewSet
from .models import Employee,Role,Node, Role_Node,Document,Folder,File,Role_Folder
from .serializers import RoleModelSerializer,NodeModelSerializer,RoleNodeModelSerializer
from .serializers import DocumentModelSerializer,FolderModelSerializer,FileModelSerializer,RoleFolderModelSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer

class NodeViewSet(ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = RoleNodeModelSerializer

class RoleNodeViewSet(ModelViewSet):
    queryset = Role_Node.objects.all()
    serializer_class = NodeModelSerializer

class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentModelSerializer

class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderModelSerializer

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileModelSerializer


class RoleFolderViewSet(ModelViewSet):
    queryset = Role_Folder.objects.all()
    serializer_class = RoleFolderModelSerializer