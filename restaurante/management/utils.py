from django.core.exceptions import ValidationError

def validate_cpf(cpf: str):
    factors =  list(range(11, 1, -1))

    v1 = sum(
        [factor * int(digit) for factor, digit in zip(factors[1:], cpf[:9])]
    )

    v2 = sum(
        [factor * int(digit) for factor, digit in zip(factors, cpf[:10])]
    )

    v1 = (v1 * 10) % 11
    if v1 == 10:
        v1 = 0   
    
    v2 = (v2 * 10) % 11

    if f"{v1}{v2}" != cpf[9:11]:
        raise ValidationError(
            f"{cpf} não é um cpf válido"
        )