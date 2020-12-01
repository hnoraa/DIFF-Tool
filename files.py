#!/usr/bin/python3
# file routines
import os

def file_exists(f):
    return os.path.exists(f)

def is_file(f):
    return os.path.isfile(f)

def file_empty(f):
    return os.path.getsize(f) == 0

def source_larger(f_source, f_target):
    if os.path.getsize(f_source) > os.path.getsize(f_target):
        return True
    return False

def equal_size(f_source, f_target):
    if os.path.getsize(f_source) == os.path.getsize(f_target):
        return True
    return False