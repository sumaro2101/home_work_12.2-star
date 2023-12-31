
def get_val(collection, key, default="git"):
    if not collection or key not in [item for item in collection.keys()]:
        return default
    
    return collection[key]
