

def serialize(value):
    if isinstance(value, types):
        return {k: serialize(v) for k, v in value.__dict__.items()}
    elif isinstance(value, (Model, Collection)):
        return serialize_model(value)
    else:
        return value
    
