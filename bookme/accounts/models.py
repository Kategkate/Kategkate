from django.contrib.auth.models import AbstractUser, Group

# here there is an option to add customized fields for the user


class User(AbstractUser):
    def save(self, *args, **kwargs):
        created = self.id is None
        super(User, self).save(*args, **kwargs)
        if created:
            group = Group.objects.get(name='common users')
            self.groups.add(group)
            self.save()




