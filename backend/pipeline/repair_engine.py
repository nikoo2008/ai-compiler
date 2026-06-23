def repair(error_message):

    if "ui" in error_message:
        return "Regenerate UI"

    if "api" in error_message:
        return "Regenerate API"

    if "db" in error_message:
        return "Regenerate DB"

    if "auth" in error_message:
        return "Regenerate Auth"

    return "Unknown issue"