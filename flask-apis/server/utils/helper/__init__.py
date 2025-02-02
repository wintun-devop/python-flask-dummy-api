import uuid

def to_dict(obj)->dict: 
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

def to_lower_case_string(input_string:str)->str:
    return input_string.lower()

def uuid_string()->str:
    return uuid.uuid4()