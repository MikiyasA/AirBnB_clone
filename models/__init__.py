#!/usr/bin/python3
"""
The module to create a unique FileStorage instance for your application
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
