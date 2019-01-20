import hashlib


def md5encrytion(password):

    string = password.encode('utf-8')
    algorithim = hashlib.md5()
    algorithim.update(string)
    encrypted = algorithim.hexdigest()
    return encrypted


def valtest(password):
   if md5encrytion(password) == md5encrytion("barakotii"):
       print("Same")
   else:
       print("Error")


valtest("barakotii")