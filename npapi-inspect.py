#!/usr/bin/env python3

import ctypes
import enum
import os
import sys

_, plugin = sys.argv
dll = ctypes.CDLL(os.path.abspath(plugin))

dll.NP_GetPluginVersion.argtypes = []
dll.NP_GetPluginVersion.restype = ctypes.c_char_p

print(dll.NP_GetPluginVersion().decode())

dll.NP_GetMIMEDescription.argtypes = []
dll.NP_GetMIMEDescription.restype = ctypes.c_char_p

print(dll.NP_GetMIMEDescription().decode())

dll.NP_GetValue.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
dll.NP_GetValue.restype = ctypes.c_int16

output = ctypes.c_char_p()

assert not dll.NP_GetValue(None, 1, ctypes.byref(output))
print(output.value.decode())
assert not dll.NP_GetValue(None, 2, ctypes.byref(output))
print(output.value.decode())
