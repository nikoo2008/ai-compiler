required_keys = [
    "ui",
    "api",
    "db",
    "auth"
]


def validate_config(config):

    for key in required_keys:

        if key not in config:
            return False, f"{key} missing"

    return True, "valid"