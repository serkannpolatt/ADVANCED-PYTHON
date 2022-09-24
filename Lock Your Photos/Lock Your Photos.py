from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('key.key' , 'wb' ) as f:
    f.write(key)
fernet = Fernet(key)
with open('#photo.jpg#' , ' rb') as f:
    Photo =f.read()
lock= fernet.encrypt(Photo)
with open('#photo.jpg#' , 'wb') as lock_Photo:
    lock_Photo.write(lock)
print("Your Photo is Locked")


#unlock 

with open('key.key', ' rb') as f:
    key = f.read()
fernet = Fernet(key)
with open('#photo.jpg#' , 'rb') as f:
    Photo = f.read()
lock = fernet.decrypt(Photo)
with open('test.txt' , 'wb') as Unlock_Photo:
    Unlock= Photo.write(lock)
print("Your Photo is UnLocked")