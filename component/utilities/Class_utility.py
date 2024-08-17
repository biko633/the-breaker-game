import gc
def get_all_instances(of_class):
    _instances = []
    for obj in gc.get_objects():
        if isinstance(obj, of_class):  
            _instances.append(obj)
    return _instances