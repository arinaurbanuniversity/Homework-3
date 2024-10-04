def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    obj_module = getattr(obj, '__module__', 'built-in' if isinstance(obj, (int, float, str, list, dict, set)) else None)

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info


class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value

number_info = introspection_info(42)
print(number_info)

my_obj = MyClass(10)
class_info = introspection_info(my_obj)
print(class_info)