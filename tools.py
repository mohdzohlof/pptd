import tkinter as tk
from PIL import ImageTk
import MySQLdb


assets_path = "assets/"


def init_root(title="Cover", size="480x780", resizeable_height=False, resizeable_width=False):
    root = tk.Tk()
    root.title(title)
    root.geometry(size)
    root.resizable(height=resizeable_height, width=resizeable_width)
    return root


def init_pages(frames):
    pages = {}
    for frameName, frame in frames.items():
        pages[frameName] = {}
        pages[frameName]["frame"] = frame
        if frameName == "cover":
            pages[frameName]["canvas"] = init_canvas(frame, bg="#243746")
        else:
            pages[frameName]["canvas"] = init_canvas(frame)
    return pages


def init_frame(parent, width=480, height=800):
    return tk.Frame(parent, width=width, height=height)


def init_frames(frameList, parent, width=480, height=800):
    frames = {}
    for frame in frameList:
        frames[frame] = init_frame(parent, width, height)
    return frames


def init_canvas(parent, width=480, height=800, bg=None):
    canvas = tk.Canvas(parent, width=width, height=height)
    if bg is not None:
        canvas.configure(bg=bg)
    return canvas


def init_images(files):
    images = {}
    for file in files:
        name = file.split(".")[0]
        images[name] = init_image(file)
    return images


def init_image(file):
    file = "{}" + file
    return ImageTk.PhotoImage(file=construct_file(file))


def construct_file(x):
    return x.format(assets_path)


def init_db(db, host="localhost", user="root", passw=""):
    db = MySQLdb.connect(host=host,
                         user=user,
                         passwd=passw,
                         db=db)

    cur = db.cursor()

    return db, cur


def show_frame(current_frame, frame, title, root):
    root.title(title)
    current_frame.pack_forget()
    frame.pack()
