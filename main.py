import handler as h
import tkinter as tk


#test
h.init_db("pptd")
root = h.init_root()
defaultbg = root.cget("bg")

framesList = ["cover", "login", "signup", "home", "tutorials", "manual", "settings", "interfaces", "networks",
              "webpages", "admin_settings", "view_users"]

imagesList = ["coverLogo.png", "emailIcon.png", "facebook.png", "homeIcon.png", "leftArrow.png", "linkedin.png",
              "loginLogo.png", "logoutIcon.png", "manualIcon.png", "passwordIcon.png", "confirmPasswordIcon.png",
              "rightArrow.png", "settingsIcon.png", "signupIcon.png", "toolIcon.png", "tutorialIcon.png", "twitter.png",
              "firstNameIcon.png", "lastNameIcon.png", "tutorialsTestResized.png", "back.png", "waiting.gif"]


images = h.init_images(imagesList)
frames = h.init_frames(framesList, root)
pages = h.init_pages(frames)


for name, page in pages.items():
    frame = page["frame"]
    canvas = page["canvas"]

    if name == "cover":
        button1 = tk.Button(frame, width=480, height=800, bg="#243746", image=images["coverLogo"],
                            command=lambda: h.show_frame(pages["cover"]["frame"], pages["login"]["frame"],
                                                         "Login", root))

        button1.config(activebackground="#243746")
        button1.pack()
        canvas.pack()
        frame.pack()

    elif name == "signup":

        button_back = tk.Button(canvas, image=images["back"], borderwidth=0,
                                command=lambda: h.show_frame(pages["signup"]["frame"], pages["login"]["frame"],
                                                             "Login", root))

        button_back.config(activebackground=defaultbg)
        canvas.create_window(50, 50, window=button_back, height=90, width=90)

        signup_label_error = tk.Label(canvas, font='times 12', fg='red')
        signup_label_error.place(x=238, y=640, anchor="center")
        canvas.create_image(240, 100, image=images["signupIcon"], anchor="center")
        canvas.create_image(85, 230, image=images["firstNameIcon"], anchor="center")
        canvas.create_image(85, 320, image=images["lastNameIcon"], anchor="center")
        canvas.create_image(85, 410, image=images["emailIcon"], anchor="center")
        canvas.create_image(85, 500, image=images["passwordIcon"], anchor="center")
        canvas.create_image(85, 590, image=images["confirmPasswordIcon"], anchor="center")

        canvas.create_text((125, 205), anchor="w", text='First Name', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((125, 295), anchor="w", text='Last Name', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((125, 385), anchor="w", text='Email', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((125, 475), anchor="w", text='Password', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((125, 565), anchor="w", text='Confirm Password', font='times 14 bold', fill='#4D4D4D')

        firstNameEntry = tk.Entry(canvas)
        canvas.create_window(125, 232, window=firstNameEntry, height=30, width=300, anchor="w")

        lastNameEntry = tk.Entry(canvas)
        canvas.create_window(125, 322, window=lastNameEntry, height=30, width=300, anchor="w")

        emailEntry = tk.Entry(canvas)
        canvas.create_window(125, 412, window=emailEntry, height=30, width=300, anchor="w")

        passwordEntry = tk.Entry(canvas, show="*")
        canvas.create_window(125, 502, window=passwordEntry, height=30, width=300, anchor="w")

        confirmPasswordEntry = tk.Entry(canvas, show="*")
        canvas.create_window(125, 592, window=confirmPasswordEntry, height=30, width=300, anchor="w")

        button_signup = tk.Button(canvas,
                                  text="Sign up", font='times 12 bold', bg="#243746", fg='#00acd8',
                                  command=lambda: h.signup(
                                      signup_label_error,
                                      (firstNameEntry, lastNameEntry, emailEntry, passwordEntry, confirmPasswordEntry),
                                      (pages["signup"], pages["login"], "Login", root)))
        button_signup.configure(width=10, height=2)
        canvas.create_window(238, 690, window=button_signup, anchor="center")

        canvas.pack()

    elif name == "login":
        canvas.create_image(240, 120, image=images["loginLogo"], anchor="center")  # Logo Image

        canvas.create_text((90, 280), anchor="w", text='Email:', font='times 12 bold',
                           fill='#243746')  # EMAIL LABEL
        canvas.create_text((90, 365), anchor="w", text='Password:', font='times 12 bold',
                           fill='#243746')  # PASSWORD LABEL

        entry_email = tk.Entry(canvas)  # Email box
        entry_email.focus_set()
        canvas.create_window(90, 315, anchor="w", window=entry_email, height=30, width=300)

        entry_password = tk.Entry(canvas, show="*")  # Password box
        canvas.create_window(90, 390, anchor="w", window=entry_password, height=30, width=300)
        entry_password.bind('<Return>', lambda x: button_login.invoke())
        entry_email.bind('<Return>', lambda x: entry_password.focus_set())

        button_login = tk.Button(canvas, text="LOGIN", font='times 12 bold', fg="#243746",
                                 command=lambda: h.login(entry_email, entry_password,
                                                         (pages["login"], pages["home"], "Home", root)))
        button_login.configure(width=10, height=2)
        canvas.create_window(240, 500, window=button_login)

        button_login_signup = tk.Button(canvas, text='Sign up', borderwidth=0, font='times 12 underline',
                                        fg='#00ACD8', command=lambda: h.show_frame(pages["login"]["frame"],
                                                                                pages["signup"]["frame"],
                                                                                "Sign up", root))
        button_login_signup.configure(width=10, height=2, activebackground=defaultbg)
        canvas.create_window(240, 570, window=button_login_signup)

        button_fb = tk.Button(canvas, image=images["facebook"], borderwidth=0,
                              command=h.open_facebook)  # Tool button
        button_fb.config(activebackground=defaultbg)
        canvas.create_window(92.5, 650, window=button_fb)  # Facebook button position

        button_linkedIn = tk.Button(canvas, image=images["linkedin"], borderwidth=0, command=h.open_linkedin)
        button_linkedIn.config(activebackground=defaultbg)
        canvas.create_window(230, 650, window=button_linkedIn)  # Linkedin button position

        button_twitter = tk.Button(canvas, image=images["twitter"], borderwidth=0, command=h.open_twitter)
        button_twitter.config(activebackground=defaultbg)
        canvas.create_window(367.5, 650, window=button_twitter)  # Twitter button position

        canvas.pack()

    elif name == "home":

        button_tutorial = tk.Button(canvas, image=images["tutorialIcon"], borderwidth=0,
                                    command=lambda: h.show_frame(pages["home"]["frame"], pages["tutorials"]["frame"],
                                                                 "Tutorials", root))  # Tutorial button
        button_tutorial.config(activebackground=defaultbg)
        canvas.create_window(125, 160, window=button_tutorial, height=200, width=200)  # Tutorial button postion

        button_manual = tk.Button(canvas, image=images["manualIcon"], borderwidth=0,
                                  command=lambda: h.show_frame(pages["home"]["frame"], pages["manual"]["frame"],
                                                               "Manual", root))  # manual button
        button_manual.config(activebackground=defaultbg)
        canvas.create_window(355, 160, window=button_manual, height=200, width=200)  # manual button postion

        button_settings = tk.Button(canvas, image=images["settingsIcon"], borderwidth=0,
                                    command=lambda: h.show_frame(pages["home"]["frame"], pages["settings"]["frame"],
                                                                 "Settings", root))  # Settings button
        button_settings.config(activebackground=defaultbg)
        canvas.create_window(125, 440, window=button_settings, height=200, width=200)  # Settings button postion

        button_tool = tk.Button(canvas, image=images["toolIcon"], borderwidth=0,
                                command=lambda: h.run_tool((pages["home"]["frame"], pages["interfaces"]["frame"],
                                                             "Interfaces", root)))  # Tool button

        button_tool.config(activebackground=defaultbg)
        canvas.create_window(355, 440, window=button_tool, height=200, width=200)  # Tool button position

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,
                                  command=lambda: h.logout((pages["home"]["frame"], pages["login"]["frame"],
                                                            "Login", root)))  # logout button
        button_logout.config(activebackground=defaultbg)
        canvas.create_window(466, 720, window=button_logout, height=90, width=90, anchor="se")  # logout button position

        canvas.create_text((355, 550), text='Tool', font='Times 18 bold', fill='#243746')
        canvas.create_text((125, 270), text='Tutorials', font='Times 18 bold', fill='#243746')
        canvas.create_text((355, 270), text='Manual', font='Times 18 bold', fill='#243746')
        canvas.create_text((125, 550), text='Settings', font='Times 18 bold', fill='#243746')

        canvas.pack()

    elif name == "signup":

        button_back = tk.Button(canvas, image=images["back"], borderwidth=0,
                                command=lambda: h.show_frame(pages["signup"]["frame"], pages["login"]["frame"],
                                                             "Login", root))

        button_back.config(activebackground=defaultbg)
        canvas.create_window(50, 50, window=button_back, height=90, width=90)

        signup_label_error = tk.Label(canvas, font='times 12', fg='red')
        signup_label_error.place(x=238, y=640, anchor="center")
        canvas.create_image(240, 100, image=images["signupIcon"], anchor="center")
        canvas.create_image(85, 230, image=images["firstNameIcon"], anchor="center")
        canvas.create_image(85, 320, image=images["lastNameIcon"], anchor="center")
        canvas.create_image(85, 410, image=images["emailIcon"], anchor="center")
        canvas.create_image(85, 500, image=images["passwordIcon"], anchor="center")
        canvas.create_image(85, 590, image=images["confirmPasswordIcon"], anchor="center")

        canvas.create_text((125, 205), anchor="w", text='First Name', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((125, 295), anchor="w", text='Last Name', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((125, 385), anchor="w", text='Email', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((125, 475), anchor="w", text='Password', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((125, 565), anchor="w", text='Confirm Password', font='times 14 bold', fill='#4D4D4D')

        firstNameEntry = tk.Entry(canvas)
        canvas.create_window(125, 232, window=firstNameEntry, height=30, width=300, anchor="w")

        lastNameEntry = tk.Entry(canvas)
        canvas.create_window(125, 322, window=lastNameEntry, height=30, width=300, anchor="w")

        emailEntry = tk.Entry(canvas)
        canvas.create_window(125, 412, window=emailEntry, height=30, width=300, anchor="w")

        passwordEntry = tk.Entry(canvas, show="*")
        canvas.create_window(125, 502, window=passwordEntry, height=30, width=300, anchor="w")

        confirmPasswordEntry = tk.Entry(canvas, show="*")
        canvas.create_window(125, 592, window=confirmPasswordEntry, height=30, width=300, anchor="w")

        button_signup = tk.Button(canvas,
                                  text="Sign up", font='times 12 bold', bg="#243746", fg='#00acd8',
                                  command=lambda: h.signup(
                                      signup_label_error,
                                      (firstNameEntry, lastNameEntry, emailEntry, passwordEntry, confirmPasswordEntry),
                                      (pages["signup"], pages["login"], "Login", root)))
        button_signup.configure(width=10, height=2)
        canvas.create_window(238, 690, window=button_signup, anchor="center")

        canvas.pack()

    elif name == "tutorials":

        canvas.create_image(240, 110, image=images["tutorialsTestResized"])
        canvas.create_text(10, 250, text="Image Description Here", anchor="w")

        button_home_tutorials = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                          command=lambda: h.show_frame(pages["tutorials"]["frame"],
                                                                       pages["home"]["frame"], "Home", root))
        button_home_tutorials.config(activebackground=defaultbg)
        canvas.create_window(10, 720, window=button_home_tutorials, height=90, width=90, anchor="sw")

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,
                                  command=lambda: h.logout((pages["tutorials"]["frame"], pages["login"]["frame"],
                                                            "Login", root)))  # logout button
        button_logout.config(activebackground=defaultbg)
        canvas.create_window(466, 720, window=button_logout, height=90, width=90, anchor="se")
        canvas.pack()

    elif name == "manual":

        canvas.create_text(10, 20, text="Device Specifications:\n\n\n"

                                        "*Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz\n\n"

                                        "*1GB LPDDR2 SDRAM\n\n"

                                        "*2.4GHz and 5GHz IEEE 802.11.b/g/n/ac wireless LAN, Bluetooth 4.2, BLE\n\n"

                                        "*Gigabit Ethernet over USB 2.0 (maximum throughput 300 Mbps)\n\n"

                                        "*Extended 40-pin GPIO header\n\n*Full-size HDMI\n\n*2 USB 2.0 ports\n\n"

                                        "*CSI camera port for connecting a Raspberry Pi camera\n\n"

                                        "*DSI display port for connecting a Raspberry Pi touchscreen display\n\n"

                                        "*Micro SD port for loading your operating system and storing data\n\n"

                                        "*Power-over-Ethernet (PoE) support (requires separate PoE HAT)\n\n"

                                        "*800x480 7-inch touchscreen\n\n*10000mAh Battery\n\n"

                                        "*Two special Wi-Fi Chipsets that support monitor mode and packet injection\n\n"

                                        "*2 9dBi Antennas for high range coverage", anchor="nw", font='times 11',

                           fill='#4D4D4D')

        button_home_manual = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,

                                       command=lambda: h.show_frame(pages["manual"]["frame"],

                                                                    pages["home"]["frame"], "Home", root))

        button_home_manual.config(activebackground=defaultbg)

        canvas.create_window(10, 720, window=button_home_manual, height=90, width=90, anchor="sw")

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,

                                  command=lambda: h.show_frame(pages["manual"]["frame"], pages["login"]["frame"],

                                                               "Login", root))  # logout button

        button_logout.config(activebackground=defaultbg)
        canvas.create_window(466, 720, window=button_logout, height=90, width=90, anchor="se")
        canvas.pack()

    elif name == "settings":

        current_password_label_settings = tk.Label(canvas, text="Current password")
        current_password_label_settings.place(anchor="w", x=50, y=45)

        current_password_entry = tk.Entry(canvas, show="*", width=30)
        current_password_entry.place(anchor="w", x=180, y=45)

        change_password_section = tk.LabelFrame(canvas, text="Change Password", height=170, width=300)
        change_password_section.place(x=238, y=200, anchor="center")

        new_password_label = tk.Label(change_password_section, text="New password")
        new_password_label.place(anchor="w", x=10, y=30)

        new_password_entry = tk.Entry(change_password_section, show="*", width=30)
        new_password_entry.place(anchor="w", x=12, y=50)

        confirm_new_password_label = tk.Label(change_password_section, text="Confirm new password")
        confirm_new_password_label.place(anchor="w", x=10, y=90)

        confirm_new_password_entry = tk.Entry(change_password_section, show="*", width=30)
        confirm_new_password_entry.place(anchor="w", x=12, y=110)

        # =================================================================================================

        join_organization_section = tk.LabelFrame(canvas, text="Join Organization", height=170, width=300)
        join_organization_section.place(x=238, y=430, anchor="center")

        org_name_label = tk.Label(join_organization_section, text="Organization Name ")
        org_name_label.place(anchor="w", x=10, y=30)

        org_name_entry = tk.Entry(join_organization_section, width=30)
        org_name_entry.place(anchor="w", x=12, y=50)

        org_password_label = tk.Label(join_organization_section, text="Organization Password ")
        org_password_label.place(anchor="w", x=10, y=90)

        confirm_new_password_entry = tk.Entry(join_organization_section, show="*", width=30)
        confirm_new_password_entry.place(anchor="w", x=12, y=110)

        # ==================================================================================================

        button_apply = tk.Button(canvas, text="Apply")
        button_apply.config(width=10, height=2)
        canvas.create_window(238, 600, window=button_apply)

        button_admin_settings = tk.Button(canvas, text="Admin Settings",

                                          command=lambda: h.show_frame(pages["settings"]["frame"],
                                                                       pages["admin_settings"]["frame"],
                                                                       "Admin Settings", root))
        button_admin_settings.config(width=15, height=2)
        canvas.create_window(238, 650, window=button_admin_settings)

        button_home_settings = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                         command=lambda: h.show_frame(pages["settings"]["frame"],
                                                                      pages["home"]["frame"], "Home", root))
        button_home_settings.config(activebackground=defaultbg)

        canvas.create_window(10, 720, window=button_home_settings, height=90, width=90, anchor="sw")

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,
                                  command=lambda: h.show_frame(pages["settings"]["frame"], pages["login"]["frame"],
                                                               "Login", root))  # logout button
        button_logout.config(activebackground=defaultbg)
        canvas.create_window(466, 720, window=button_logout, height=90, width=90, anchor="se")
        canvas.pack()

    elif name == "admin_settings":

        button_back = tk.Button(canvas, image=images["back"], borderwidth=0,

                                command=lambda: h.show_frame(pages["admin_settings"]["frame"],
                                                             pages["settings"]["frame"], "Settings",
                                                             root))
        button_back.config(activebackground=defaultbg)
        canvas.create_window(50, 50, window=button_back, height=90, width=90)

        current_password_label_admin = tk.Label(canvas, text="Current password")
        current_password_label_admin.place(anchor="w", x=50, y=130)

        current_password_entry = tk.Entry(canvas, show="*", width=30)
        current_password_entry.place(anchor="w", x=180, y=130)

        join_organization_section = tk.LabelFrame(canvas, text="Change Organization Password", height=170, width=300)
        join_organization_section.place(x=238, y=350, anchor="center")

        new_org_pass_label = tk.Label(join_organization_section, text="New Organization Password")
        new_org_pass_label.place(anchor="w", x=10, y=30)

        org_pass_entry = tk.Entry(join_organization_section, width=30, show="*")
        org_pass_entry.place(anchor="w", x=12, y=50)

        confirm_new_org_pass_label = tk.Label(join_organization_section, text="Confirm New Organization Password")
        confirm_new_org_pass_label.place(anchor="w", x=10, y=90)

        confirm_new_org_pass_entry = tk.Entry(join_organization_section, show="*", width=30)
        confirm_new_org_pass_entry.place(anchor="w", x=12, y=110)

        # ===========================================================================================

        button_apply_admin = tk.Button(canvas, text="Apply")
        button_apply_admin.config(width=10, height=2)
        canvas.create_window(235, 600, window=button_apply_admin)

        button_users = tk.Button(canvas, text="Users",
                                 command=lambda: h.show_frame(pages["admin_settings"]["frame"],
                                                              pages["view_users"]["frame"],
                                                              "Users", root))
        button_users.config(width=10, height=2)
        canvas.create_window(235, 650, window=button_users)

        button_home_settings = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,

                                         command=lambda: h.show_frame(pages["admin_settings"]["frame"],

                                                                      pages["home"]["frame"], "Home", root))

        button_home_settings.config(activebackground=defaultbg)

        canvas.create_window(10, 720, window=button_home_settings, height=90, width=90, anchor="sw")

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,

                                  command=lambda: h.show_frame(pages["admin_settings"]["frame"],
                                                               pages["login"]["frame"],

                                                               "Login", root))  # logout button

        button_logout.config(activebackground=defaultbg)

        canvas.create_window(466, 720, window=button_logout, height=90, width=90, anchor="se")

        canvas.pack()

    elif name == "view_users":

        button_back = tk.Button(canvas, image=images["back"], borderwidth=0,
                                command=lambda: h.show_frame(pages["view_users"]["frame"],
                                                             pages["admin_settings"]["frame"], "Admin Settings",
                                                             root))
        button_back.config(activebackground=defaultbg)
        canvas.create_window(50, 50, window=button_back, height=90, width=90)

        canvas.create_text((238, 60), text='Users List', font='Times 18 bold', fill='#4D4D4D', anchor="center")

        view_users_output = tk.Listbox(canvas, height=25, width=40, highlightthickness=0)
        view_users_output.place(x=82, y=90)

        users_label_error = tk.Label(canvas,text="Please select a user!", fg="red", font="times 12")
        users_label_error.place(x=238, y=570, anchor="center")

        button_remove_user = tk.Button(canvas, text="Remove User")
        button_remove_user.config(width=10, height=2)
        canvas.create_window(238, 620, window=button_remove_user)

        button_home_view_users = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                           command=lambda: h.show_frame(pages["view_users"]["frame"],
                                                                      pages["home"]["frame"], "Home", root))
        button_home_view_users.config(activebackground=defaultbg)
        canvas.create_window(10, 720, window=button_home_view_users, height=90, width=90, anchor="sw")

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,
                                  command=lambda: h.show_frame(pages["view_users"]["frame"],
                                                               pages["login"]["frame"],
                                                               "Login", root))  # logout button
        button_logout.config(activebackground=defaultbg)
        canvas.create_window(466, 720, window=button_logout, height=90, width=90, anchor="se")

        canvas.pack()

    elif name == "interfaces":

        canvas.create_text((238, 40), text='Choose Interface', font='Times 18 bold', fill='#4D4D4D', anchor="center")

        interface_output = tk.Listbox(canvas, height=25, width=40, borderwidth=0, highlightthickness=0)
        interface_output.place(x=82, y=70)

        label_scanning = tk.Label(canvas, text="Scanning for interfaces")
        label_scanning.place(x=163, y=570)
        root.after(1, h.scanning(label_scanning, root))

        interface_label_error = tk.Label(canvas, font='times 12', fg='red', text="")
        interface_label_error.place(x=250, y=580, anchor="center")

        button_interfaces_scan = tk.Button(canvas, text="Scan", font='Times 20 bold', fg="#4D4D4D",
                                           command=lambda: h.scan(interface_output, interface_label_error,
                                                                  (pages["interfaces"]["frame"],
                                                                   pages["networks"]["frame"], "Networks", root)))
        button_interfaces_scan.configure(width=7, height=1)  # Scan
        canvas.create_window(238, 650, window=button_interfaces_scan)

        button_home_interfaces = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                           command=lambda: h.__exit(
                                               (pages["interfaces"]["frame"], pages["home"]["frame"],
                                                "Home", root)))  # HOME_Interface button
        button_home_interfaces.config(activebackground=defaultbg)
        canvas.create_window(10, 720, window=button_home_interfaces, height=90, width=90, anchor="sw")

        h.set_globals(interface=interface_output)

        canvas.pack()

    elif name == "networks":
        canvas.create_text((238, 40), text='Choose Network', font='Times 18 bold', fill='#4D4D4D', anchor="center")

        networks_output = tk.Listbox(canvas, height=25, width=40, borderwidth=0, highlightthickness=0)
        networks_output.place(x=82, y=70)

        label_handshake = tk.Label(canvas, text="Waiting for handshake")
        label_handshake.place(x=163, y=540)
        root.after(1, h.handshake_waiting(label_handshake, root))

        network_label_error = tk.Label(canvas, font='times 12', fg='red')
        network_label_error.place(x=238, y=550, anchor="center")

        button_network_confirm = tk.Button(canvas, text="Select", font='Times 20', fg="#4D4D4D",
                                           command=lambda: h.get_webpages(networks_output, network_label_error, (pages["networks"]["frame"],
                                                                           pages["webpages"]["frame"], "Web Pages",
                                                                           root)))
        button_network_confirm.configure(width=7, height=1)  # Confirm button size
        canvas.create_window(238, 600, window=button_network_confirm)

        button_network_rescan = tk.Button(canvas, text="Rescan", font='Times 20', fg="#4D4D4D",
                                          command=lambda: h.rescan(pages["networks"]["frame"]))

        button_network_rescan.configure(width=7, height=1)  # Rescan button size
        canvas.create_window(160, 670, window=button_network_rescan)

        button_stop_handshake = tk.Button(canvas, text="Stop!", font="times 20", command=lambda: h.stop_handshake(pages["networks"]["frame"]))
        button_stop_handshake.configure(width=7, height=1)
        canvas.create_window(316, 670, window=button_stop_handshake)

        button_home_network = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                        command=lambda: h.show_frame(pages["networks"]["frame"],
                                                                     pages["home"]["frame"], "Home",
                                                                     root))  # HOME_Interface button
        button_home_network.config(activebackground=defaultbg)
        canvas.create_window(10, 720, window=button_home_network, height=90, width=90, anchor="sw")

        h.set_globals(network=networks_output)

        canvas.pack()

    elif name == "webpages":

        canvas.create_text((238, 40), text='Choose Web Page', font='Times 18 bold', fill='#4D4D4D', anchor="center")

        webpages_output = tk.Listbox(canvas, height=25, width=40, highlightthickness=0)
        webpages_output.place(x=82, y=70)

        h.set_globals(webpage=webpages_output)

        label_attack_in_progress = tk.Label(canvas, text="Attack in progress")
        label_attack_in_progress.place(x=180, y=540)
        root.after(1, h.attack_in_progress(label_attack_in_progress, root))

        label_error_webpage = tk.Label(canvas, fg="red", font="times 12", text="Please select a web page!")

        button_start_attack = tk.Button(canvas, text="ATTACK!", borderwidth=1, command=lambda: h.start_attack(label_error_webpage, webpages_output, button_start_attack, button_change_network))
        button_start_attack.config(activebackground=defaultbg)
        canvas.create_window(238, 600, window=button_start_attack, height=50, width=90)

        button_change_network = tk.Button(canvas, text="Change Network", command=lambda: h.change_network((pages["webpages"]["frame"], pages["networks"]["frame"], "Networks", root)))
        button_change_network.config(activebackground=defaultbg)
        canvas.create_window(160, 670, window=button_change_network, height=50, width=120)

        button_exit = tk.Button(canvas, text="Exit", command=lambda: h.__exit((pages["webpages"]["frame"], pages["home"]["frame"], "Home", root)))
        button_exit.config(activebackground=defaultbg)
        canvas.create_window(316, 670, window=button_exit, height=50, width=120)

        canvas.pack()

root.mainloop()
