from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password

class Accounts_Table(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    
    # Use EmailField for email addresses
    gmail = models.EmailField(
        max_length=50,
        validators=[MinLengthValidator(5, message="Email must be at least 5 characters long.")]
    )

    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(4, message="Username must be at least 4 characters long.")]
    )
    
    password = models.CharField(
        max_length=128,  # Increase length for hashed passwords
        validators=[MinLengthValidator(8, message="Password must be at least 8 characters long.")]
    )

    security = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3, message="Security question answer must be at least 3 characters long.")]
    )

    def save(self, *args, **kwargs):
        # Hash the password before saving if it's set
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'argon2$', 'bcrypt$', 'crypt$', 'django_bcrypt')):
            self.password = make_password(self.password)
        
        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''}".strip()
