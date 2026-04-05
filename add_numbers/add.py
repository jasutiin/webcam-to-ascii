import ctypes

add_cpp = ctypes.CDLL("add_numbers/add.dll")

add_cpp.add.argtypes = [ctypes.c_int, ctypes.c_int]
add_cpp.add.restype = ctypes.c_int # return type

def add(a, b):
    return add_cpp.add(a, b)