#!/usr/bin/python3
"""
Directoy package for organization of code and import modules
"""


from .engine.file_storage import FileStorage

# Create FileStorage instance
storage = FileStorage()

# Loads the previous save of instance
storage.reload()
