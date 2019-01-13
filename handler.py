from flux import fluxion
import tkinter as tk
from PIL import ImageTk
import MySQLdb
import webbrowser
from validate_email import validate_email
import threading
from queue import Queue


assets_path = "assets/"
conn = None
user = None
interfaces = None
networks = None
admin = False
q = Queue()


def open_facebook():
    webbrowser.open_new(r"http://www.facebook.com")


def open_linkedin():
    webbrowser.open_new(r"http://www.linkedin.com")


def open_twitter():
    webbrowser.open_new(r"http://www.twitter.com")


def has_digit(input_string):
    return any(char.isdigit() for char in input_string)


def has_lower(input_string):
    return any(char.islower() for char in input_string)


def has_upper(input_string):
    return any(char.isupper() for char in input_string)


def set_globals(connection=None, username=None, interface=None, network=None, access=None):
    global conn, user, interfaces, networks, admin

    if connection is not None:
        conn = connection

    if username is not None:
        user = username

    if interface is not None:
        interfaces = interface

    if network is not None:
        networks = network

    if access is not None:
        admin = access


def start_attack(network_listbox):
    selected = network_listbox.curselection()[0]
    q.put(selected)


def scan(interface_listbox, f):
    current_frame = f[0]
    next_frame = f[1]
    window_name = f[2]
    root = f[3]

    selected = interface_listbox.curselection()[0]
    q.put(selected)

    show_frame(current_frame, next_frame, window_name, root)


def run_tool(f):
    global interfaces, networks
    current_frame = f[0]
    next_frame = f[1]
    window_name = f[2]
    root = f[3]
    t = threading.Thread(target=fluxion, args=(q,))
    t.start()
    q.put(interfaces)
    q.put(networks)

    show_frame(current_frame, next_frame, window_name, root)


def signup(error, e, f):
    global conn
    cur = conn.cursor()

    first_name = e[0].get()
    last_name = e[1].get()
    email = e[2].get()
    password = e[3].get()
    confirm_password = e[4].get()

    current_frame = f[0]["frame"]
    next_frame = f[1]["frame"]
    window_name = f[2]
    root = f[3]

    valid = True

    if not first_name.isalpha():
        error.configure(text="Invalid first name, must contain letters only!")
        valid = False
        return

    if not last_name.isalpha():
        error.configure(text="Invalid last name, must contain letters only!")
        valid = False
        return

    if not validate_email(email):
        error.configure(text="Invalid email!")
        valid = False
        return

    if not (has_upper(password) and has_lower(password) and has_digit(password) and 10 <= len(password) <= 25):
        error.configure(text="""Invalid password, must contain:
        1- One upper case letter
        2- One upper case letter
        3- One number""")
        valid = False
        return

    if confirm_password != password:
        error.configure(text="Passwords do not match!")
        valid = False
        return

    if valid:
        error.configure(text="")
        query = "INSERT INTO account (email, password, admin, first_name, last_name) " \
                "VALUES ('{email}', '{password}', {admin}, '{first_name}', '{last_name}')"\
            .format(email=email, password=password, admin=0, first_name=first_name, last_name=last_name)
        cur.execute(query)
        show_frame(current_frame, next_frame, window_name, root)


def select_all(e):
    widget = e.widget
    widget.select_range(0, tk.END)
    widget.icursor(tk.END)


def logout(f):
    global user, admin
    current_frame = f[0]
    next_frame = f[1]
    root_name = f[2]
    root = f[3]

    user = None
    admin = None

    show_frame(current_frame, next_frame, root_name, root)


def login(e, p, f):
    current_frame = f[0]["frame"]
    current_canvas = f[0]["canvas"]
    next_frame = f[1]["frame"]
    root_name = f[2]
    root = f[3]

    authenticate(e, p)

    if user is not None:
        e.delete(0, tk.END)
        p.delete(0, tk.END)
        show_frame(current_frame, next_frame, root_name, root)
    else:
        current_canvas.create_text((230, 490), anchor="n", text='Invalid username or password!', font='times 16 bold',
                                   fill='red')  # INVALID LOGIN LABEL


def authenticate(e, p):
    email = e.get()
    passw = p.get()
    global conn, user, admin

    cur = conn.cursor()

    query = "SELECT email, admin FROM account WHERE email='{}' AND password='{}'".format(email, passw)
    cur.execute(query)
    res = cur.fetchone()
    if res is not None:
        user = res[0]
        if res[1] == 1:
            admin = True


def init_root(title="Cover", size="480x800", resizeable_height=False, resizeable_width=False):
    root = tk.Tk()
    root.title(title)
    root.geometry(size)
    root.resizable(height=resizeable_height, width=resizeable_width)

    root.bind('<Control-a>', select_all)
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
    global conn
    conn = MySQLdb.connect(host=host, user=user, passwd=passw, db=db)


def show_frame(current_frame, frame, title, root):
    root.title(title)
    current_frame.pack_forget()
    frame.pack()
