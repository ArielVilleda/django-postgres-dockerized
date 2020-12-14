from django.db import models
# from django.utils.translation import gettext_lazy as _


# class User(models.Model):
#     class UserStatus(models.TextChoices):
#         IN_PAYMENT_VALIDATION = ('in_payment_validation',
#                                  _('VALIDATING PAYMENT'))
#         HAS_LATE_PAYMENT = ('has_late_payment', _('DEBTOR LATE PAYMENT'))
#         BANNED = ('banned', _('BANNED'))
#         NORMAL = ('normal', _('CORRECT STATUS'))
#     name = models.CharField(max_length=127, null=False, blank=False)
#     last_name = models.CharField(max_length=127, null=True)
#     second_last_name = models.CharField(max_length=127, null=True)
#     password = models.CharField(max_length=255, null=True)
#     phone = models.CharField(max_length=63, null=True)
#     email = models.EmailField(max_length=255, null=False, unique=True)
#     email_verified_at = models.DateTimeField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=31, choices=UserStatus.choices,
#                               null=False, blank=False,
#                               default=UserStatus.IN_PAYMENT_VALIDATION)

#     def __str__(self):
#         return self.name


# class TaxData(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              related_name='tax_data')
#     social_reason = models.CharField(max_length=255, null=False, blank=False)
#     address = models.CharField(max_length=255, null=False, blank=False)
#     phone = models.CharField(max_length=63, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.social_reason


# class UserPaymentMethod(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              related_name='payment_method')
#     name = models.CharField(max_length=127, null=True)
#     card_last_numbers = models.CharField(max_length=63, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class StoreCategory(models.Model):
#     name = models.CharField(max_length=127, null=False, blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Store(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              related_name='store')
#     category = models.ForeignKey(StoreCategory, null=True,
#                                  on_delete=models.SET_NULL,
#                                  related_name='stores')
#     name = models.CharField(max_length=255, null=False, blank=False,
#                             unique=True)
#     logo = models.CharField(max_length=255, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Domain(models.Model):
#     class DomainStatus(models.TextChoices):
#         AVAILABLE = ('available', _('AVAILABLE'))
#         SUSPENDED = ('suspended', _('SUSPENDED'))
#         IN_USE = ('in_use', _('IN_USE'))
#     url = models.CharField(max_length=255, null=False, blank=False,
#                            unique=True)
#     name = models.CharField(max_length=255, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=31, choices=DomainStatus.choices,
#                               null=False, blank=False,
#                               default=DomainStatus.AVAILABLE)

#     def __str__(self):
#         return self.url


# class PaymentPlans(models.Model):
#     name = models.CharField(max_length=255, null=False, blank=False,
#                             unique=True)
#     base_price = models.FloatField(null=False)
#     time_span = models.SmallIntegerField(null=False, default=30)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class StoreTemplate(models.Model):
#     class StoreTemplateStatus(models.TextChoices):
#         AVAILABLE = ('available', _('AVAILABLE'))
#         SUSPENDED = ('suspended', _('SUSPENDED'))
#     name = models.CharField(max_length=255, null=False, blank=False,
#                             unique=True)
#     url = models.CharField(max_length=255, null=False, blank=False,
#                            unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=31,
#                               choices=StoreTemplateStatus.choices,
#                               null=False, blank=False,
#                               default=StoreTemplateStatus.AVAILABLE)

#     def __str__(self):
#         return self.url


# class Application(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              related_name='application')
#     payment_plan = models.ForeignKey(PaymentPlans, null=True,
#                                      on_delete=models.SET_NULL,
#                                      related_name='applications')
#     domain = models.ForeignKey(Domain, null=True, on_delete=models.SET_NULL,
#                                related_name='application')
#     store_template = models.ForeignKey(StoreTemplate, null=True,
#                                        on_delete=models.SET_NULL,
#                                        related_name='applications')
#     cost = models.FloatField(null=False)
#     payment_date = models.DateTimeField(null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.cost)


# class Payment(models.Model):
#     application = models.ForeignKey(Application, on_delete=models.CASCADE,
#                                     related_name='payments')
#     income = models.FloatField(null=False)
#     # unique=True for reference parameter?
#     reference = models.CharField(max_length=255, null=False, blank=False)
#     status = models.CharField(max_length=255, null=False, blank=False)
#     application_date = models.DateTimeField(null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.reference


# class Admin(models.Model):
#     name = models.CharField(max_length=127, null=False, blank=False)
#     email = models.EmailField(max_length=255, null=False, unique=True)
#     password = models.CharField(max_length=255, null=True)
#     email_verified_at = models.DateTimeField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class AwsInstance(models.Model):
#     application = models.ForeignKey(Application, on_delete=models.CASCADE,
#                                     related_name='aws_instance')
#     admin = models.ForeignKey(Admin, null=True, on_delete=models.SET_NULL,
#                               related_name='aws_instance')
#     ip = models.CharField(max_length=255, null=False, blank=False)
#     aws_login_data = models.CharField(max_length=255, null=False, blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.ip


# class Lead(models.Model):
#     store_category = models.ForeignKey(StoreCategory, null=True,
#                                        on_delete=models.SET_NULL,
#                                        related_name='leds')
#     store_template = models.ForeignKey(StoreTemplate, null=True,
#                                        on_delete=models.SET_NULL,
#                                        related_name='leds')
#     email = models.EmailField(max_length=255, null=False, unique=True)
#     domain = models.CharField(max_length=255, null=True)
#     current_application_step = models.CharField(max_length=63, null=False,
#                                                 blank=False, default='1')
#     additional_data = models.CharField(max_length=255, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.current_application_step
