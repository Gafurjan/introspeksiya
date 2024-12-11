import os
from pprint import pprint
import sys

def  introspection_info(sobj):
    dict = {}
    dict['type'] = type(sobj)
    dict['attributes'] = dir(sobj)
    # dict['method'] = [method for method in dir(sobj) if callable(getattr(sobj, method)) and not method.startswith("__")]
    dict['method'] = [method for method in dir(sobj) if callable(getattr(sobj, method))]
    dict['module_name'] = os.path.basename(sys.modules['__main__'].__file__)

    return dict

number_info = introspection_info(42)
print(number_info)

