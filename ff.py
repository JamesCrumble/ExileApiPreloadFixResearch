# import pymem
# import struct

# process = pymem.Pymem('PathOfExile.exe')

# start_address_of_server_data = 1583346734432

# buffer = ''


# # data = bytearray()
# # print(data)
# data = bytearray(process.read_bytes(
#     start_address_of_server_data, 1024
# ))
# for byte_ in data:
#     try:
#         buffer += chr(byte_)
#     except:
#         ...

# print(buffer)


import socket

print(socket.gethostbyaddr('169.51.22.40'))
