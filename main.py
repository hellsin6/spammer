import sys
from G_Python.g_python.gextension import Extension
from G_Python.g_python.htools import RoomUsers

extension_info = {
    "title": "Room scanner",
    "description": "no se",
    "version": "1.0",
    "author": "Hellsin6 + Dieegox77"
}

ext = Extension(extension_info, sys.argv)
ext.start()

room_users = RoomUsers(ext)
room_users.on_new_users(lambda users: print(list(map(str, users))))