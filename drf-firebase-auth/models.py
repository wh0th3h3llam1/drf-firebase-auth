from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class AbstractFirebaseUser(AbstractBaseUser, PermissionsMixin):
    """
    An Abstract class from which `User` model should inherit to 
    integrate with Firebase Authentication
    """
    uid = models.CharField(
        verbose_name=_("UID"),
        unique=True,
        default=uuid4,
        max_length=48
    )
    display_name = models.CharField(
        verbose_name=_("Display Name"),
        max_length=64,
        blank=True,
        null=True,
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"),
        unique=True,
        error_messages={
            "unique": "A user with this phone number already exists",
        },
    )
    email = models.EmailField(
        verbose_name=_("Email Address"),
        unique=True,
        blank=True,
        null=True,
        error_messages={"unique": "A user with this email already exists"},
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff Status"),
        default=False,
        help_text="Designate whether the user can log into this admin site.",
    )
    is_superuser = models.BooleanField(
        verbose_name=_("Superuser Status"),
        default=False,
        help_text=_("Designates that this user has all permissions without "
            "explicitly assigning them."),
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text="Designates whether this use should be treated as active. "
        "Unselect this instead of deleting accounts (soft delete)",
    )
    date_joined = models.DateTimeField(verbose_name=_("date joined"), default=timezone.now)
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "uid"
    REQUIRED_FIELDS = ["phone_number"]

    class Meta:
        abstract = True

    def get_username(self):
        return f"{self.identifier}"

    def clean(self):
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def identifier(self):
        return self.display_name or self.phone_number or self.email or self.uid


class FirebaseUser(AbstractFirebaseUser):
    class Meta(AbstractFirebaseUser.Meta):
        swappable = "AUTH_USER_MODEL"
