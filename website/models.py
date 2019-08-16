from django.db import models

# Create your models here.

choices = (
    ('Web', 'Web'),
    ('Android App', 'Android App'),
    ('IOS App', 'IOS App'),
)

state_choices = (
    ('FCT', 'FCT'),
    ('Abia', 'Abia'),
    ('Adamawa', 'Adamawa'),
    ('Akwa Ibom', 'Akwa Ibom'),
    ('Anambra', 'Anambra'),
    ('Bauchi', 'Bauchi'),
    ('Bayelsa', 'Bayelsa'),
    ('Benue', 'Benue'),
    ('Borno', 'Borno'),
    ('Cross River', 'Cross River'),
    ('Delta', 'Delta'),
    ('Ebonyi', 'Ebonyi'),
    ('Edo', 'Edo'),
    ('Ekiti', 'Ekiti'),
    ('Enugu', 'Enugu'),
    ('Gombe', 'Gombe'),
    ('Imo', 'Imo'),
    ('Jigawa', 'Jigawa'),
    ('Kaduna', 'Kaduna'),
    ('Kano', 'Kano'),
    ('Katsina', 'Katsina'),
    ('Kebbi', 'Kebbi'),
    ('Kogi', 'Kogi'),
    ('Kwara', 'Kwara'),
    ('Lagos', 'Lagos'),
    ('Nassarawa', 'Nassarawa'),
    ('Niger', 'Niger'),
    ('Ogun', 'Ogun'),
    ('Ondo', 'Ondo'),
    ('Osun', 'Osun'),
    ('Oyo', 'Oyo'),
    ('Plateau', 'Plateau'),
    ('Rivers', 'Rivers'),
    ('Sokoto', 'Sokoto'),
    ('Taraba', 'Taraba'),
    ('Yobe', 'Yobe'),
    ('Zamfara', 'Zamfara'),
    

)

class Support(models.Model):
    full_name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 11)
    email = models.EmailField()
    problem = models.CharField(choices = choices, max_length = 20)
    complaint = models.TextField()

    def __str__(self):
        return self.full_name


class Contact_us(models.Model):
    full_name = models.CharField(max_length = 200)
    email = models.EmailField()
    subject = models.CharField(max_length = 500)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.full_name

class Get_started(models.Model):
    organization = models.CharField(max_length = 200)
    email = models.EmailField()
    phone = models.CharField(max_length = 11)
    location = models.CharField(choices = state_choices, max_length = 30)
    entry = models.TextField()

    class Meta:
        verbose_name = 'Get Started'
        verbose_name_plural = 'Get Started'

    def __str__(self):
        return self.organization

