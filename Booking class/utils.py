def validate_id(value, name):
    try:
        id_value = int(value)
        if id_value <= 0:
            raise ValueError(f"{name} must be positive")
    except ValueError as e:
        print(f"Error: Invalide {name}: {e}")
        return None