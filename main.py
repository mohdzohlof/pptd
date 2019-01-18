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
              "firstNameIcon.png", "lastNameIcon.png", "tutorialsTestResized.png", "back.png"]


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

    elif name == "login":
        canvas.create_image(240, 170, image=images["loginLogo"], anchor="center")  # Logo Image

        canvas.create_text((80, 350), anchor="w", text='Email:', font='times 12 bold',
                           fill='#243746')  # EMAIL LABEL
        canvas.create_text((80, 435), anchor="w", text='Password:', font='times 12 bold',
                           fill='#243746')  # PASSWORD LABEL

        entry_email = tk.Entry(canvas)  # Email box
        entry_email.focus_set()
        canvas.create_window(80, 375, anchor="w", window=entry_email, height=30, width=300)

        entry_password = tk.Entry(canvas, show="*")  # Password box
        canvas.create_window(80, 460, anchor="w", window=entry_password, height=30, width=300)
        entry_password.bind('<Return>', lambda x: button_login.invoke())
        entry_email.bind('<Return>', lambda x: entry_password.focus_set())

        button_login = tk.Button(canvas, text="LOGIN", font='times 12 bold', fg="#243746",
                                 command=lambda: h.login(entry_email, entry_password,
                                                         (pages["login"], pages["home"], "Home", root)))
        button_login.configure(width=10, height=2)
        canvas.create_window(240, 560, window=button_login)

        button_login_signup = tk.Button(canvas, text='Sign up', borderwidth=0, font='times 12 underline',
                                        fg='blue', command=lambda: h.show_frame(pages["login"]["frame"],
                                                                                pages["signup"]["frame"],
                                                                                "Sign up", root))
        button_login_signup.configure(width=10, height=2, activebackground=defaultbg)
        canvas.create_window(240, 620, window=button_login_signup)

        button_fb = tk.Button(canvas, image=images["facebook"], borderwidth=0,
                              command=h.open_facebook)  # Tool button
        button_fb.config(activebackground=defaultbg)
        canvas.create_window(92.5, 700, window=button_fb)  # Facebook button position

        button_linkedin = tk.Button(canvas, image=images["linkedin"], borderwidth=0, command=h.open_linkedin)
        button_linkedin.config(activebackground=defaultbg)
        canvas.create_window(230, 700, window=button_linkedin)  # Linkedin button position

        button_twitter = tk.Button(canvas, image=images["twitter"], borderwidth=0, command=h.open_twitter)
        button_twitter.config(activebackground=defaultbg)
        canvas.create_window(367.5, 700, window=button_twitter)  # Twitter button position

        canvas.pack()

    elif name == "home":
        button_tool = tk.Button(canvas, image=images["toolIcon"], borderwidth=0,
                                command=lambda: h.run_tool((pages["home"]["frame"], pages["interfaces"]["frame"],
                                                            "Interfaces", root)))  # Tool button
        button_tool.config(activebackground=defaultbg)
        canvas.create_window(370, 480, window=button_tool, height=200, width=200)  # Tool button postion
        canvas.create_text((370, 600), text='Tool', font='Times 18 bold', fill='#243746')

        button_tutorial = tk.Button(canvas, image=images["tutorialIcon"], borderwidth=0,
                                    command=lambda: h.show_frame(pages["home"]["frame"], pages["tutorials"]["frame"],
                                                                 "Tutorials", root))  # Tutorial button
        button_tutorial.config(activebackground=defaultbg)
        canvas.create_window(110, 200, window=button_tutorial, height=200, width=200)  # Tutorial button postion
        text1 = canvas.create_text((110, 320), text='Tutorials', font='Times 18 bold', fill='#243746')

        button_manual = tk.Button(canvas, image=images["manualIcon"], borderwidth=0,
                                  command=lambda: h.show_frame(pages["home"]["frame"], pages["manual"]["frame"],
                                                               "Manual", root))  # manual button
        button_manual.config(activebackground=defaultbg)
        canvas.create_window(370, 200, window=button_manual, height=200, width=200)  # manual button postion
        canvas.create_text((370, 320), text='Manual', font='Times 18 bold', fill='#243746')

        button_settings = tk.Button(canvas, image=images["settingsIcon"], borderwidth=0,
                                    command=lambda: h.show_frame(pages["home"]["frame"], pages["settings"]["frame"],
                                                                 "Settings", root))  # Settings button
        button_settings.config(activebackground=defaultbg)
        canvas.create_window(110, 480, window=button_settings, height=200, width=200)  # Settings button postion
        canvas.create_text((110, 600), text='Settings', font='Times 18 bold', fill='#243746')

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,
                                  command=lambda: h.logout((pages["home"]["frame"], pages["login"]["frame"],
                                                            "Login", root)))  # logout button
        button_logout.config(activebackground=defaultbg)
        canvas.create_window(430, 748, window=button_logout, height=90, width=90)  # logout button postion

        canvas.pack()

    elif name == "interfaces":
        interface_label_error = tk.Label(canvas, font='times 12 bold', fg='red', text="")
        interface_label_error.place(x=250, y=580, anchor="center")

        canvas.create_text((153, 60), text='Choose Interface', font='Times 18 bold', fill='#4D4D4D', anchor="w")

        button_interfaces_scan = tk.Button(canvas, text="Scan", font='Times 20 bold', fg="#4D4D4D",
                                           command=lambda: h.scan(interface_output, interface_label_error,
                                                                  (pages["interfaces"]["frame"],
                                                                   pages["networks"]["frame"], "Networks", root)))
        button_interfaces_scan.configure(width=7, height=1)  # Scan
        canvas.create_window(250, 650, window=button_interfaces_scan)

        button_home = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                command=lambda: h._exit((pages["interfaces"]["frame"], pages["home"]["frame"],
                                                             "Home", root)))  # HOME_Interface button
        button_home.config(activebackground=defaultbg)
        canvas.create_window(51, 749, window=button_home, height=90, width=90)  # HOME_Interface button postion

        interface_output = tk.Listbox(canvas, height=25, width=40, borderwidth=0, highlightthickness=0)
        interface_output.place(x=82, y=90)



        h.set_globals(interface=interface_output)

        canvas.pack()

    elif name == "networks":
        canvas.create_text((153, 60), text='Choose Network', font='Times 18 bold', fill='#4D4D4D', anchor="w")

        networks_output = tk.Listbox(canvas, height=25, width=40, borderwidth=0, highlightthickness=0)
        networks_output.place(x=82, y=90)

        button_home_network = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                        command=lambda: h.show_frame(pages["networks"]["frame"],
                                                                     pages["home"]["frame"], "Home",
                                                                     root))  # HOME_Interface button
        button_home_network.config(activebackground=defaultbg)
        canvas.create_window(51, 749, window=button_home_network, height=90,
                             width=90)  # HOME_Interface button postion

        button_network_confirm = tk.Button(canvas, text="OK!", font='Times 20', fg="#4D4D4D", command=lambda: h.get_webpages((pages["networks"]["frame"], pages["webpages"]["frame"], "webpages", root)))
        button_network_confirm.configure(width=7, height=1)  # Confirm button size
        canvas.create_window(250, 600, window=button_network_confirm)

        button_network_rescan = tk.Button(canvas, text="Rescan", font='Times 20', fg="#4D4D4D",
                                          command=lambda: h.show_frame(pages["networks"]["frame"],
                                                                       pages["interfaces"]["frame"],
                                                                       "Interfaces", root))

        button_network_rescan.configure(width=7, height=1)  # Rescan button size
        canvas.create_window(250, 650, window=button_network_rescan)

        h.set_globals(network=networks_output)

        canvas.pack()

    elif name == "signup":
        signup_label_error = tk.Label(canvas, font='times 12 bold', fg='red')
        signup_label_error.place(x=240, y=720, anchor="center")
        canvas.create_image(240, 110, image=images["signupIcon"], anchor="center")
        canvas.create_image(50, 270, image=images["firstNameIcon"], anchor="center")
        canvas.create_image(50, 370, image=images["lastNameIcon"], anchor="center")
        canvas.create_image(50, 470, image=images["emailIcon"], anchor="center")
        canvas.create_image(50, 570, image=images["passwordIcon"], anchor="center")
        canvas.create_image(50, 670, image=images["confirmPasswordIcon"], anchor="center")

        firstNameEntry = tk.Entry(canvas)
        canvas.create_window(110, 277, window=firstNameEntry, height=30, width=300, anchor="w")

        lastNameEntry = tk.Entry(canvas)
        canvas.create_window(110, 377, window=lastNameEntry, height=30, width=300, anchor="w")

        emailEntry = tk.Entry(canvas)
        canvas.create_window(110, 477, window=emailEntry, height=30, width=300, anchor="w")

        passwordEntry = tk.Entry(canvas, show="*")
        canvas.create_window(110, 577, window=passwordEntry, height=30, width=300, anchor="w")

        confirmPasswordEntry = tk.Entry(canvas, show="*")
        canvas.create_window(110, 677, window=confirmPasswordEntry, height=30, width=300, anchor="w")

        button_signup = tk.Button(canvas,
                                  text="Sign up", font='times 12 bold', bg="#243746", fg='#00acd8',
                                  command=lambda: h.signup(
                                      signup_label_error,
                                      (firstNameEntry, lastNameEntry, emailEntry, passwordEntry, confirmPasswordEntry),
                                      (pages["signup"],  pages["login"], "Login", root)))
        button_signup.configure(width=10, height=1)
        canvas.create_window(240, 760, window=button_signup, anchor="center")

        canvas.create_text((110, 250), anchor="w", text='First Name', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((110, 350), anchor="w", text='Last Name', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((110, 450), anchor="w", text='Email', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((110, 550), anchor="w", text='Password', font='times 14 bold', fill='#4D4D4D')
        canvas.create_text((110, 650), anchor="w", text='Confirm Password', font='times 14 bold', fill='#4D4D4D')

        button_back = tk.Button(canvas, image=images["back"], borderwidth=0,
                                command=lambda: h.show_frame(pages["signup"]["frame"], pages["login"]["frame"],
                                                             "Login", root))

        button_back.config(activebackground=defaultbg)
        canvas.create_window(50, 50, window=button_back, height=90, width=90)

        canvas.pack()

    elif name == "tutorials":

        canvas.create_image(240, 110, image=images["tutorialsTestResized"])
        canvas.create_text(10, 250, text="Image Description Here", anchor="w")

        button_home_tutorials = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                          command=lambda: h.show_frame(pages["tutorials"]["frame"],
                                                                       pages["home"]["frame"], "Home", root))
        button_home_tutorials.config(activebackground=defaultbg)
        canvas.create_window(51, 749, window=button_home_tutorials, height=90, width=90)

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,
                                  command=lambda: h.logout((pages["tutorials"]["frame"], pages["login"]["frame"],
                                                            "Login", root)))  # logout button
        button_logout.config(activebackground=defaultbg)
        canvas.create_window(430, 748, window=button_logout, height=90, width=90)  # logout button postion

        canvas.pack()

    elif name == "manual":
        canvas.create_text(20, 20, text="el jehaz feyyoooo\n \n \n \nkol had :)", anchor="nw")

        button_home_manual = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                       command=lambda: h.show_frame(pages["manual"]["frame"],
                                                                    pages["home"]["frame"], "Home", root))
        button_home_manual.config(activebackground=defaultbg)
        canvas.create_window(51, 749, window=button_home_manual, height=90, width=90)

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,
                                  command=lambda: h.logout((pages["manual"]["frame"], pages["login"]["frame"],
                                                            "Login", root)))  # logout button
        button_logout.config(activebackground=defaultbg)
        canvas.create_window(430, 748, window=button_logout, height=90, width=90)  # logout button postion

        canvas.pack()

    elif name == "settings":

        current_password_label = tk.Label(canvas, text="Current password")

        current_password_label.place(anchor="w", x=40, y=45)

        current_password_entry = tk.Entry(canvas, show="*", width=30)

        current_password_entry.place(anchor="w", x=150, y=45)

        change_password_section = tk.LabelFrame(canvas, text="Change Password", height=170, width=300)

        change_password_section.place(x=30, y=115)

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

        join_organization_section.place(x=30, y=350)

        org_name_label = tk.Label(join_organization_section, text="Organization Name ")

        org_name_label.place(anchor="w", x=10, y=30)

        org_name_entry = tk.Entry(join_organization_section, width=30)

        org_name_entry.place(anchor="w", x=12, y=50)

        org_password_label = tk.Label(join_organization_section, text="Organization Password ")

        org_password_label.place(anchor="w", x=10, y=90)

        confirm_new_password_entry = tk.Entry(join_organization_section, show="*", width=30)

        confirm_new_password_entry.place(anchor="w", x=12, y=110)

        # ==================================================================================================

        button_admin_settings = tk.Button(canvas, text="Admin Settings",

                                          command=lambda: h.show_frame(pages["settings"]["frame"],

                                                                       pages["admin_settings"]["frame"],

                                                                       "Admin Settings", root))

        button_admin_settings.config(width=15, height=2)

        canvas.create_window(235, 650, window=button_admin_settings)

        button_apply = tk.Button(canvas, text="Apply")

        button_apply.config(width=10, height=2)

        canvas.create_window(235, 700, window=button_apply)

        button_home_settings = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,

                                         command=lambda: h.show_frame(pages["settings"]["frame"],

                                                                      pages["home"]["frame"], "Home", root))

        button_home_settings.config(activebackground=defaultbg)

        canvas.create_window(51, 749, window=button_home_settings, height=90, width=90)

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,

                                  command=lambda: h.show_frame(pages["settings"]["frame"], pages["login"]["frame"],

                                                               "Login", root))  # logout button

        button_logout.config(activebackground=defaultbg)

        canvas.create_window(430, 748, window=button_logout, height=90, width=90)  # logout button postion

        canvas.pack()

    elif name == "admin_settings":

        current_password_label = tk.Label(canvas, text="Current password")

        current_password_label.place(anchor="w", x=70, y=100)

        current_password_entry = tk.Entry(canvas, show="*", width=30)

        current_password_entry.place(anchor="w", x=180, y=100)

        join_organization_section = tk.LabelFrame(canvas, text="Change Organization Password", height=170, width=300)

        join_organization_section.place(x=90, y=200)

        new_org_pass_label = tk.Label(join_organization_section, text="New Organization Password")

        new_org_pass_label.place(anchor="w", x=10, y=30)

        org_pass_entry = tk.Entry(join_organization_section, width=30, show="*")

        org_pass_entry.place(anchor="w", x=12, y=50)

        confirm_new_org_pass_label = tk.Label(join_organization_section, text="Confirm New Organization Password")

        confirm_new_org_pass_label.place(anchor="w", x=10, y=90)

        confirm_new_org_pass_entry = tk.Entry(join_organization_section, show="*", width=30)

        confirm_new_org_pass_entry.place(anchor="w", x=12, y=110)

        # ===========================================================================================

        button_users = tk.Button(canvas, text="Users",

                                 command=lambda: h.show_frame(pages["admin_settings"]["frame"],

                                                              pages["view_users"]["frame"],

                                                              "Users", root))

        button_users.config(width=10, height=2)

        canvas.create_window(235, 650, window=button_users)

        button_apply = tk.Button(canvas, text="Apply")

        button_apply.config(width=10, height=2)

        canvas.create_window(235, 700, window=button_apply)

        button_home_settings = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,

                                         command=lambda: h.show_frame(pages["admin_settings"]["frame"],

                                                                      pages["home"]["frame"], "Home", root))

        button_home_settings.config(activebackground=defaultbg)

        canvas.create_window(51, 749, window=button_home_settings, height=90, width=90)

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,

                                  command=lambda: h.show_frame(pages["admin_settings"]["frame"],
                                                               pages["login"]["frame"],

                                                               "Login", root))  # logout button

        button_logout.config(activebackground=defaultbg)

        canvas.create_window(430, 748, window=button_logout, height=90, width=90)  # logout button postion

        button_back = tk.Button(canvas, image=images["back"], borderwidth=0,

                                command=lambda: h.show_frame(pages["admin_settings"]["frame"],
                                                             pages["settings"]["frame"], "Settings",

                                                             root))

        button_back.config(activebackground=defaultbg)

        canvas.create_window(50, 50, window=button_back, height=90, width=90)

        canvas.pack()

    elif name == "view_users":

        users_list_label = tk.Label(canvas, text="Users List")

        users_list_label.place(anchor="w", x=220, y=45)

        view_users_output = tk.Listbox(canvas, height=30, width=60, highlightthickness=0)

        view_users_output.place(x=60, y=90)

        button_home_settings = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,

                                         command=lambda: h.show_frame(pages["view_users"]["frame"],
                                                                      pages["home"]["frame"], "Home", root))

        button_home_settings.config(activebackground=defaultbg)

        canvas.create_window(51, 749, window=button_home_settings, height=90, width=90)

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0,

                                  command=lambda: h.show_frame(pages["view_users"]["frame"],

                                                               pages["login"]["frame"],

                                                               "Login", root))  # logout button

        button_logout.config(activebackground=defaultbg)

        canvas.create_window(430, 748, window=button_logout, height=90, width=90)  # logout button postion

        button_remove_user = tk.Button(canvas, text="Remove User")

        button_remove_user.config(width=10, height=2)

        canvas.create_window(235, 650, window=button_remove_user)

        button_back = tk.Button(canvas, image=images["back"], borderwidth=0,

                                command=lambda: h.show_frame(pages["view_users"]["frame"],
                                                             pages["admin_settings"]["frame"], "Admin Settings",

                                                             root))

        button_back.config(activebackground=defaultbg)

        canvas.create_window(50, 50, window=button_back, height=90, width=90)

        canvas.pack()

    elif name == "webpages":
        canvas.create_text(130, 50, text="Select webpage! ", anchor="nw",  font='Arial 18 bold', fill='#243746')
        list_webpage = tk.Listbox(canvas, height=30, width=40, borderwidth=0, highlightthickness=0)
        list_webpage.place(x=82, y=90)
        h.set_globals(webpage=list_webpage)
        button_start_attack = tk.Button(canvas, text="ATTACK!", borderwidth=1, command=h.start_attack)
        canvas.create_window(240, 720, window=button_start_attack, height=50, width=90)
        canvas.pack()
root.mainloop()