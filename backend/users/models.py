from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'first_name', 'last_name']
    ROLE_USER = 'user'
    ROLE_ADMIN = 'admin'
    USERS_ROLE = (
        (ROLE_USER, 'Пользователь'),
        (ROLE_ADMIN, 'Админ'),
    )
    role = models.CharField(
        choices=USERS_ROLE,
        max_length=10,
        verbose_name='Роль пользователя',
        default=ROLE_USER
    )
    username = models.CharField('username', max_length=150, unique=True)
    password = models.TextField('password', max_length=150)
    email = models.EmailField('e-mail', max_length=254, unique=True)
    first_name = models.TextField('first_name', max_length=150)
    last_name = models.TextField('last_name', max_length=150)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Подписчик на автора рецепта'
    )
    author = models.ForeignKey(
        CustomUser, null=True,
        on_delete=models.CASCADE,
        related_name='followed',
        verbose_name='Автор',
        help_text='Автор рецепта'
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['author', 'user'],
            name='unique_object'
        )]
