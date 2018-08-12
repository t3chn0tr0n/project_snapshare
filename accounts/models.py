from django.db import models

class Temp_user(models.Model):
    uname = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    token = models.CharField(max_length=100)

    def __str__(self):
            return self.uname

    def varify_token(self, token):
        if self.token == token:
            return True
        else:
            return False

    def migrate(self):
        user = User.objects.create_user(self.uname, password=self.password, email=self.email)
        return redirect('index')