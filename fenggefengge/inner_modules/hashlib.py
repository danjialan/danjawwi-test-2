import hashlib
md5_value = hashlib.md5()
md5_value.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5_value.hexdigest())