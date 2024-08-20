from rest_framework.exceptions import ValidationError

forbidden_words = [
    "ставки",
    "крипта",
    "продам",
    "гараж",
    "знакомства",
    "порно",
    "казино",
]


def validate_forbidden_words(value):
    if value.lower() in forbidden_words:
        raise ValidationError(f'The value "{value}" contains forbidden words.')
