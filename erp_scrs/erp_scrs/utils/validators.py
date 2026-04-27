def validate_non_empty(value, field_name):
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value


def validate_int(value, field_name):
    try:
        return int(value)
    except:
        raise ValueError(f"{field_name} must be a number")


def validate_positive(value, field_name):
    if value <= 0:
        raise ValueError(f"{field_name} must be positive")
    return value