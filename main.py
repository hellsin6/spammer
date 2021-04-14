import sys
from G_Python.g_python.gextension import Extension
from G_Python.g_python.htools import RoomUsers
from G_Python.g_python.hparsers import HEntityType
from G_Python.g_python.hpacket import HPacket

extension_info = {
    "title": "Agregador de amigos",
    "description": "Roberto Carlos",
    "version": "1.0",
    "author": "Hellsin6 + Dieegox77"
}

ext = Extension(extension_info, sys.argv)
ext.start()

def spammer(users):
	for user in users:
		if user.entity_type == HEntityType.HABBO:
			ext.send_to_server(HPacket("RequestFriend", user.name))
			print("Added %s" % user.name)

room_users = RoomUsers(ext)
room_users.on_new_users(spammer)