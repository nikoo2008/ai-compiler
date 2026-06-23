def build_ir(intent):

    ir = {
        "app_type": intent["app_type"],
        "entities": {},
        "flows": [],
        "roles": {}
    }

    for entity in intent["entities"]:
        ir["entities"][entity] = []

    for role in intent["roles"]:
        ir["roles"][role] = []

    return ir