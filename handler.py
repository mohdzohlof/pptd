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
webpages = None
admin = False
interface_label_scan = None
network_label_scan = None
found = False

q = None


def scanning(label, root):
    global interface_label_scan
    interface_label_scan = label

    # Get the current message
    current_status = label["text"]

    # If the message is "Scanning...", start over with "Working"
    if current_status.endswith("..."):
        current_status = "Scanning for interfaces"

    # If not, then just add a "." on the end
    else:
        current_status += "."

    # Update the message
    label["text"] = current_status

    # After 1 second, update the status
    root.after(1000, lambda: scanning(label, root))


def handshake_waiting(label_handshake, root):
    # Get the current message
    current_status = label_handshake["text"]

    # If the message is "Working...", start over with "Working"
    if current_status.endswith("..."):
        current_status = "Waiting for handshake"

    # If not, then just add a "." on the end
    else:
        current_status += "."

    # Update the message
    label_handshake["text"] = current_status

    # After 1 second, update the status
    root.after(1000, lambda: handshake_waiting(label_handshake, root))


def attack_in_progress(label_handshake, root):
    # Get the current message
    current_status = label_handshake["text"]

    # If the message is "Working...", start over with "Working"
    if current_status.endswith("..."):
        current_status = "Attack in progress"

    # If not, then just add a "." on the end
    else:
        current_status += "."

    # Update the message
    label_handshake["text"] = current_status

    # After 1 second, update the status
    root.after(1000, lambda: attack_in_progress(label_handshake, root))


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


def set_globals(connection=None, username=None, interface=None, network=None, access=None, webpage=None):
    global conn, user, interfaces, networks, admin, webpages

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

    if webpage is not None:
        webpages = webpage


def __exit(navigation):
    current_page = navigation[0]
    next_page = navigation[1]
    window_name = navigation[2]
    root = navigation[3]

    q.put("exit")

    show_frame(current_page, next_page, window_name, root)


def rescan(current_frame):

    c = current_frame.winfo_children()[0]
    network_confirm_button = c.winfo_children()[3]
    network_rescan_button = c.winfo_children()[4]

    q.put("rescan")
    q.put(network_confirm_button)
    q.put(network_rescan_button)


def stop_handshake(current_frame):
    c = current_frame.winfo_children()[0]
    network_listbox = c.winfo_children()[0]
    network_confirm_button = c.winfo_children()[3]
    network_rescan_button = c.winfo_children()[4]
    network_stop_handshake_button = c.winfo_children()[5]

    network_listbox.delete(0, "end")
    network_confirm_button.configure(state="normal")
    network_rescan_button.configure(state="normal")
    network_stop_handshake_button.configure(state="disabled")

    q.put("ammah na3eemah, na3ameeen!!")
    q.put(network_confirm_button)
    q.put(network_rescan_button)


def wait_handshake(navigation):
    current_frame = navigation[0]
    next_frame = navigation[1]
    window_name = navigation[2]
    root = navigation[3]

    if found:
        show_frame(current_frame, next_frame, window_name, root)
    else:
        root.after(1, lambda: wait_handshake(navigation))


def get_webpages(network_listbox, network_error_label, navigation):

    if len(network_listbox.curselection()) > 0:
        current_frame = navigation[0]
        c = current_frame.winfo_children()[0]
        network_confirm_button = c.winfo_children()[3]
        network_rescan_button = c.winfo_children()[4]
        network_stop_handshake_button = c.winfo_children()[5]

        network_confirm_button.configure(state="disabled")
        network_rescan_button.configure(state="disabled")
        network_stop_handshake_button.configure(state="normal")
        selected = networks.curselection()[0]
        q.put(selected)
        wait_handshake(navigation)
    else:
        network_error_label.configure(text="Please select an interface!")


def start_attack():
    selected = webpages.curselection()[0]
    q.put(selected)


def scan(interface_listbox, interface_error_label, f):
    current_frame = f[0]
    next_frame = f[1]
    window_name = f[2]
    root = f[3]

    if len(interface_listbox.curselection()) > 0:
        c = next_frame.winfo_children()[0]
        network_confirm_button = c.winfo_children()[3]
        network_rescan_button = c.winfo_children()[4]
        selected = interface_listbox.curselection()[0]
        q.put(selected)
        q.put(network_confirm_button)
        q.put(network_rescan_button)

        show_frame(current_frame, next_frame, window_name, root)
    else:
        interface_error_label.configure(text="Please select an interface!")


def run_tool(f):
    global interfaces, networks, q
    q = Queue()
    current_frame = f[0]
    next_frame = f[1]
    window_name = f[2]
    root = f[3]
    t = threading.Thread(target=fluxion, args=(q,))
    t.start()
    q.put(interfaces)
    q.put(networks)
    q.put(webpages)

    c = next_frame.winfo_children()[0]
    button = c.winfo_children()[3]
    q.put(button)
    q.put(interface_label_scan)

    show_frame(current_frame, next_frame, window_name, root)


def signup(error, entries, navigation):
    global conn
    cur = conn.cursor()
    first_name = entries[0].get()
    last_name = entries[1].get()
    email = entries[2].get()
    password = entries[3].get()
    confirm_password = entries[4].get()

    current_frame = navigation[0]["frame"]
    next_frame = navigation[1]["frame"]
    window_name = navigation[2]
    root = navigation[3]

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
        error.configure(text="Password must contain upper case letter, lower case letter and a number")
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
        conn.commit()
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


def login(email_entry, password_entry, navigation):
    current_frame = navigation[0]["frame"]
    current_canvas = navigation[0]["canvas"]
    next_frame = navigation[1]["frame"]
    root_name = navigation[2]
    root = navigation[3]

    authenticate(email_entry, password_entry)

    if user is not None:
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        show_frame(current_frame, next_frame, root_name, root)
    else:
        current_canvas.create_text((238, 435), anchor="center", text='Invalid email or password!', font='times 16 bold',
                                   fill='red')  # INVALID LOGIN LABEL


def authenticate(email_entry, password_entry):
    email = email_entry.get()
    passw = password_entry.get()
    global conn, user, admin

    cur = conn.cursor()

    query = "SELECT email, admin FROM account WHERE email='{}' AND password='{}'".format(email, passw)
    cur.execute(query)
    res = cur.fetchone()
    if res is not None:
        user = res[0]
        if res[1] != 0:
            admin = True


def init_root(title="Cover", size="476x730", resizeable_height=False, resizeable_width=False):
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
    if title == "Interfaces":
        c = frame.winfo_children()[0]
        interface_scanning_label = c.winfo_children()[1]
        interface_error_label = c.winfo_children()[2]
        interface_confirm_button = c.winfo_children()[3]
        interface_scanning_label.place(x=163, y=570)
        interface_error_label.configure(text="")
        interface_confirm_button.configure(state="disabled")
    elif title == "Networks":
        c = frame.winfo_children()[0]
        network_handshake_label = c.winfo_children()[1]
        network_error_label = c.winfo_children()[2]
        network_confirm_button = c.winfo_children()[3]
        network_rescan_button = c.winfo_children()[4]
        network_stop_handshake_button = c.winfo_children()[5]

        network_handshake_label.place_forget()
        network_error_label.configure(text="")
        network_confirm_button.configure(state="disabled")
        network_rescan_button.configure(state="disabled")
        network_stop_handshake_button.configure(state="disabled")
