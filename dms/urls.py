from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(prefix="role-api", viewset=views.RoleViewSet)
router.register(prefix="node-api", viewset=views.NodeViewSet)
router.register(prefix="role-node-api", viewset=views.RoleNodeViewSet)
router.register(prefix="document-api", viewset=views.DocumentViewSet)
router.register(prefix="folder-api", viewset=views.FolderViewSet)
router.register(prefix="file-api", viewset=views.FileViewSet)
router.register(prefix="role-foler-api", viewset=views.RoleFolderViewSet)

urlpatterns = [
    path("", include(router.urls))
]