from django.core.exceptions import ValidationError


# Валидатор проверки цены на положительное значение
def validate_positive(value):
    if value < 0:
        raise ValidationError('Значение цены должно быть положительным',
                              code='invalid')