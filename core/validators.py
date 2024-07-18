from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_cpf(value):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, value))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        raise ValidationError(_('CPF deve ter 11 dígitos.'))

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        raise ValidationError(_('CPF inválido.'))

    # Calcula o primeiro dígito verificador
    sum = 0
    for i in range(9):
        sum += int(cpf[i]) * (10 - i)
    remainder = 11 - (sum % 11)
    if remainder == 10 or remainder == 11:
        remainder = 0
    if remainder != int(cpf[9]):
        raise ValidationError(_('CPF inválido.'))

    # Calcula o segundo dígito verificador
    sum = 0
    for i in range(10):
        sum += int(cpf[i]) * (11 - i)
    remainder = 11 - (sum % 11)
    if remainder == 10 or remainder == 11:
        remainder = 0
    if remainder != int(cpf[10]):
        raise ValidationError(_('CPF inválido.'))

    return cpf