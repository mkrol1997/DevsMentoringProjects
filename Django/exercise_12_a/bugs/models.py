from django.db import models


class ProjectModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class UserModel(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}'


class BugModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)

    def json(self):
        return {
            'id': self.pk,
            'description': self.description,
            'username': self.user.username,
            'project': self.project.name,
        }
