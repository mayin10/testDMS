from django.db import models
from django.contrib.auth.models import User
from db.base_model import BaseModel

# Create your models here.

class Role(BaseModel):
    role_name = models.CharField(max_length=100)
    def __str__(self):
        return self.role_name

class Employee(models.Model):
    company_choices = (
        (1, '01_company'),
        (2, '02_company'),
    )
    pos_choices = (
        (1, '01_intern'),
        (2, '02_extern'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    company = models.SmallIntegerField(default=1, choices=company_choices, verbose_name='Company')
    pos = models.SmallIntegerField(default=1, choices=pos_choices, verbose_name='Position')
    role= models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Node(BaseModel):
    node_name = models.CharField(max_length=100)
    p_id = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    def parent(self):
        return Node.objects.get(pk=self.p_id)

    def path(self):
        return self.parent+"/"+self.node_name
    def __str__(self):
        return self.node_name



class Role_Node(BaseModel):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    def role_name(self):
        return self.employee.rolename
    def node_name(self):
        return self.node.node_name
    def __str__(self):
        return self.role.rolename + ' --  ' + self.node.node_name


class Document(BaseModel):
    status_choices = (
        (1, 'in plan'),
        (2, 'in processing'),
        (3, 'Approved'),
    )
    location = models.CharField(max_length=100)
    documentID = models.CharField(max_length=100, unique=True)
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='status')
    version = models.IntegerField(default=0)
    note = models.TextField(help_text="note", verbose_name="note")

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = verbose_name
        ordering = ("documentID",)

    def __str__(self):
        return self.documentID

class Folder(BaseModel):
    right_choices = (
        (1, 'read'),
        (2, 'read + update'),
        (3, 'read + update + create'),
        (4, 'read + update + create + delete'),

    )
    folder_name = models.CharField(max_length=100)
    p_id = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    right = models.SmallIntegerField(default=1, choices=right_choices, verbose_name='right')
    def __str__(self):
        return self.folder_name

class Role_Folder(BaseModel):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    def role_name(self):
        return self.role.rolename
    def folder_name(self):
        return self.folder.node_name
    def __str__(self):
        return self.role.rolename + ' --  ' + self.folder.folder_name


class File(BaseModel):
    type_choices = (
        (1, 'doc'),
        (2, 'excel'),
        (3, 'pdf'),
        (4, 'image'),
        (5, 'dwg'),
    )
    file_name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    version = models.IntegerField(default=0)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    type = models.SmallIntegerField(default=1, choices=type_choices, verbose_name='type')
    note = models.TextField(help_text="note", verbose_name="note")
    def __str__(self):
        return self.file_name
