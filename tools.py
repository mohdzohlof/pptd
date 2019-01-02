from tkinter import Tk
from PIL import ImageTk
import MySQLdb

assets_path = "assets/"


def init_root():
    root = Tk()
    root.title("Cover page")
    root.geometry("480x800")  # window
    root.resizable(0, 0)
    return root


def init_images(path, files):
    images = []
    for file in files:
        images.append(ImageTk.PhotoImage(file="{path}{file}".format(path=path, file=file)))
    return images


def init_db(db, host="localhost", user="root", passw=""):
    db = MySQLdb.connect(host=host,
                         user=user,
                         passwd=passw,
                         db=db)

    cur = db.cursor()

    return db, cur
