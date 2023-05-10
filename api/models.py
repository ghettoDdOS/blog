from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.managers import AuthorManager


class Author(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(_("Телефон"), max_length=15)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = AuthorManager()

    class Meta:
        verbose_name = _("Автор")
        verbose_name_plural = _("Авторы")


class Blog(models.Model):
    author = models.ForeignKey(
        Author,
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("Заголовок"), max_length=50)
    content = models.TextField(_("Содержание"))
    created_at = models.DateTimeField(
        "Дата создания",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Блог")
        verbose_name_plural = _("Блоги")


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog,
        verbose_name="Блог",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        Author,
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )
    content = models.TextField(_("Содержание"))
    created_at = models.DateTimeField(
        "Дата создания",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")
