from flux import fluxion
import tkinter as tk
from PIL import ImageTk
import webbrowser
from validate_email import validate_email
import threading
from queue import Queue
import db
import hashlib


assets_path = "assets/"
user = None
interfaces = None
networks = None
webpages = None
interface_label_scan = None
network_label_scan = None
found = False

q = None


def md5(password):
    string = password.encode('utf-8')
    algorithm = hashlib.md5()
    algorithm.update(string)
    hash_string = algorithm.hexdigest()
    return hash_string


def view_users(settings_users_listbox):
    settings_users_listbox.delete(0, "end")
    org_id = db.get_org_id(user)
    employees = db.get_users_by_org(org_id)
    for employee in [employee for employee in employees if employee != user]:
        settings_users_listbox.insert("end", employee)


def remove_user(settings_users_error_label, settings_users_listbox, navigation):
    settings_users_error_label.configure(fg="red")
    if len(settings_users_listbox.curselection()) < 1:
        settings_users_error_label.configure(text="Please select a user!")
        return
    else:
        selection = settings_users_listbox.curselection()
        for idx in selection:
            user_email = settings_users_listbox.get(idx)
            db.remove_user_org(user_email)
            show_frame(navigation[0], navigation[1], navigation[2], navigation[3])
            settings_users_error_label.configure(fg="green")
            settings_users_error_label.configure(text="Updated successfully!")


def change_org_password(settings_admin_error_label, entries, navigation):
    settings_admin_error_label.configure(fg="red")
    password = db.get_password(user)

    current_password = md5(entries[0].get())
    new_org_pass = entries[1].get()
    confirm_new_org_pass = entries[2].get()

    if current_password != password:
        settings_admin_error_label.configure(text="Invalid password!")
        return

    if new_org_pass != confirm_new_org_pass:
        settings_admin_error_label.configure(text="Passwords do not match!")
        return

    if not password_is_valid(new_org_pass):
        settings_admin_error_label.configure(text="Password must contain upper case letter, lower case letter and a number")
        return

    org_id = db.get_org_id(user)

    db.update_org_password(org_id, md5(new_org_pass))
    show_frame(navigation[0], navigation[1], navigation[2], navigation[3])
    settings_admin_error_label.configure(fg="green")
    settings_admin_error_label.configure(text="Updated successfully!")


def update_info(settings_error_label, entries, navigation):
    updated = False
    current_password = md5(entries[0].get())
    new_password = entries[1].get()
    confirm_new_password = entries[2].get()
    org_name = entries[3].get()
    org_pass = entries[4].get()

    password = db.get_password(user)

    if current_password != password:
        settings_error_label.configure(text="Invalid password!")
        return

    if len(new_password) > 0 or len(confirm_new_password) > 0:
        if new_password != confirm_new_password:
            settings_error_label.configure(text="Passwords do not match!")
            return
        elif not password_is_valid(new_password):
            settings_error_label.configure(text="Password must contain upper case letter, lower case letter and a number")
            return
        else:
            db.update_password(user, md5(new_password))
            updated = True
    else:
        settings_error_label.configure(text="")

    if len(org_name) > 0 or len(org_pass) > 0:
        org_info = db.get_org_by_name(org_name)
        if org_name != org_info[1]:
            settings_error_label.configure(text="Organization does not exist!")
        elif org_pass != org_info[2]:
            settings_error_label.configure(text="Invalid organization password")
        else:
            updated = True
            db.update_organization(user, org_info[0])
    else:
        settings_error_label.configure(text="")

    if updated:
        show_frame(navigation[0], navigation[1], navigation[2], navigation[3])
        settings_error_label.configure(text="updated successfully")


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


def set_globals(username=None, interface=None, network=None, access=None, webpage=None):
    global user, interfaces, networks, admin, webpages

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


def change_network(navigation):
    current_frame = navigation[0]
    next_frame = navigation[1]
    window_name = navigation[2]
    root = navigation[3]

    q.put("back")

    c = next_frame.winfo_children()[0]
    network_listbox = c.winfo_children()[0]
    network_confirm_button = c.winfo_children()[3]
    network_rescan_button = c.winfo_children()[4]

    network_listbox.delete(0, "end")
    q.put(network_confirm_button)
    q.put(network_rescan_button)

    show_frame(current_frame, next_frame, window_name, root)


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
    global found
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


def start_attack(webpages_error_label, webpages_attack_label, webpages_listbox, webpages_confirm_button, webpages_back_button):
    if len(webpages_listbox.curselection()) > 0:
        webpages_error_label.place_forget()
        webpages_attack_label.place(x=180, y=540)
        selected = webpages.curselection()[0]
        q.put(selected)
        webpages_confirm_button.configure(state="disabled")
        webpages_back_button.configure(state="normal")
    else:
        webpages_error_label.place(x=238, y=540, anchor="center")


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
    cur = db.conn.cursor()
    first_name = entries[0].get()
    last_name = entries[1].get()
    email = (entries[2].get()).upper()
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

    if not password_is_valid(password):
        error.configure(text="Password must contain upper case letter, lower case letter and a number")
        valid = False
        return

    if confirm_password != password:
        error.configure(text="Passwords do not match!")
        valid = False
        return

    if valid:
        error.configure(text="")

        db.create_user(email, md5(password), first_name, last_name)

        show_frame(current_frame, next_frame, window_name, root)


def password_is_valid(password):
    return has_upper(password) and has_lower(password) and has_digit(password) and 10 <= len(password) <= 25


def select_all(e):
    widget = e.widget
    widget.select_range(0, tk.END)
    widget.icursor(tk.END)


def logout(f):
    global user
    current_frame = f[0]
    next_frame = f[1]
    root_name = f[2]
    root = f[3]

    user = None

    show_frame(current_frame, next_frame, root_name, root)


def login(login_error_label, email_entry, password_entry, navigation):
    authenticate(email_entry, password_entry)

    if user is not None:
        show_frame(navigation[0], navigation[1], navigation[2], navigation[3])
    else:
        login_error_label.configure(text="Invalid email or password!")


def authenticate(email_entry, password_entry):
    global user

    email = (email_entry.get()).upper()
    passw = md5(password_entry.get())

    res = db.get_user(email, passw)
    if res is not None:
        user = res


def init_root(title="Cover", size="476x730", resizeable_height=False, resizeable_width=False):
    db.init_db("pptd")
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


def show_frame(current_frame, frame, title, root):
    root.title(title)
    current_frame.pack_forget()
    frame.pack()

    if title == "Sign up":
        c = frame.winfo_children()[0]
        signup_first_name_entry = c.winfo_children()[1]
        signup_last_name_entry = c.winfo_children()[2]
        signup_email_entry = c.winfo_children()[3]
        signup_pass_entry = c.winfo_children()[4]
        signup_confirm_pass_entry = c.winfo_children()[5]
        signup_error_label = c.winfo_children()[6]

        signup_first_name_entry.focus()

        signup_first_name_entry.delete(0, "end")
        signup_last_name_entry.delete(0, "end")
        signup_email_entry.delete(0, "end")
        signup_pass_entry.delete(0, "end")
        signup_confirm_pass_entry.delete(0, "end")
        signup_error_label.configure(text="")
    elif title == "Login":
        c = frame.winfo_children()[0]
        login_email_entry = c.winfo_children()[0]
        login_pass_entry = c.winfo_children()[1]
        login_error_label = c.winfo_children()[2]

        login_error_label.configure(text="")
        login_email_entry.focus()
        login_email_entry.delete(0, "end")
        login_pass_entry.delete(0, "end")
    elif title == "Interfaces":
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
    elif title == "Web Pages":
        c = frame.winfo_children()[0]
        webpages_attack_label = c.winfo_children()[1]
        webpages_error_label = c.winfo_children()[2]
        webpages_confirm_button = c.winfo_children()[3]
        webpages_exit_button = c.winfo_children()[4]

        webpages_attack_label.place_forget()
        webpages_error_label.place_forget()
        webpages_confirm_button.configure(state="normal")
        webpages_exit_button.configure(state="disabled")
    elif title == "Settings":
        admin = db.is_admin(user)
        org_id = db.get_org_id(user)

        c = frame.winfo_children()[0]
        settings_pass_entry = c.winfo_children()[1]
        settings_pass_labelframe = c.winfo_children()[2]
        settings_org_labelframe = c.winfo_children()[3]
        settings_error_label = c.winfo_children()[4]
        settings_admin_button = c.winfo_children()[6]

        settings_new_pass_entry = settings_pass_labelframe.winfo_children()[1]
        settings_confirm_pass_entry = settings_pass_labelframe.winfo_children()[3]

        settings_org_name_label = settings_org_labelframe.winfo_children()[0]
        settings_org_name_entry = settings_org_labelframe.winfo_children()[1]
        settings_org_pass_label = settings_org_labelframe.winfo_children()[2]
        settings_org_pass_entry = settings_org_labelframe.winfo_children()[3]

        settings_pass_entry.focus()
        settings_pass_entry.delete(0, "end")
        settings_new_pass_entry.delete(0, "end")
        settings_confirm_pass_entry.delete(0, "end")
        settings_org_name_entry.delete(0, "end")
        settings_org_pass_entry.delete(0, "end")

        settings_error_label.configure(text="")

        if org_id is not None or admin:
            settings_org_name_label.configure(state="disabled")
            settings_org_name_entry.configure(state="disabled")
            settings_org_pass_label.configure(state="disabled")
            settings_org_pass_entry.configure(state="disabled")
        else:
            settings_org_name_label.configure(state="normal")
            settings_org_name_entry.configure(state="normal")
            settings_org_pass_label.configure(state="normal")
            settings_org_pass_entry.configure(state="normal")

        if admin:
            settings_admin_button.place(x=238, y=650, anchor="center")
        else:
            settings_admin_button.place_forget()
    elif title == "Admin Settings":
        c = frame.winfo_children()[0]
        settings_admin_pass_entry = c.winfo_children()[2]
        settings_admin_org_labelframe = c.winfo_children()[3]
        settings_admin_error_label = c.winfo_children()[4]

        settings_admin_org_pass = settings_admin_org_labelframe.winfo_children()[1]
        settings_admin_org_confirm_pass = settings_admin_org_labelframe.winfo_children()[3]

        settings_admin_error_label.configure(text="")
        settings_admin_error_label.configure(fg="red")

        settings_admin_pass_entry.focus()
        settings_admin_pass_entry.delete(0, "end")
        settings_admin_org_pass.delete(0, "end")
        settings_admin_org_confirm_pass.delete(0, "end")
    elif title == "Users":
        c = frame.winfo_children()[0]
        users_listbox = c.winfo_children()[1]
        view_users(users_listbox)
