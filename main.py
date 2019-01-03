import tools as t
import tkinter as tk


root = t.init_root()
defaultbg = root.cget('bg')

framesList = ["cover", "login", "signup", "home", "tutorials", "manual", "settings", "interfaces", "networks"]

imagesList = ["coverLogo.png", "emailIcon.png", "facebook.png", "homeIcon.png", "leftArrow.png", "linkedin.png",
              "loginLogo.png", "logoutIcon.png", "manualIcon.png", "passwordIcon.png", "repeatPasswordIcon.png",
              "rightArrow.png", "settingsIcon.png", "signupIcon.png", "toolIcon.png", "tutorialIcon.png", "twitter.png",
              "usernameIcon.png"]

images = t.init_images(imagesList)
frames = t.init_frames(framesList, root)
pages = t.init_pages(frames)


for name, page in pages.items():
    frame = page["frame"]
    canvas = page["canvas"]

    if name == "cover":
        logo = images["coverLogo"]
        button1 = tk.Button(frame, width=480, height=800, bg="#243746", image=logo, command=lambda: t.show_frame(pages["cover"]["frame"], pages["login"]["frame"]))
        button1.config(activebackground="#243746")
        button1.pack()
        canvas.pack()
        frame.pack()

    elif name == "login":
        canvas.create_image(240, 170, image=images["loginLogo"], anchor="center")  # logo postion

        canvas.create_text((80, 350), anchor="w", text='Email:', font='times 12 bold', fill='#243746')  # EMAIL LABEL
        canvas.create_text((80, 435), anchor="w", text='Password:', font='times 12 bold', fill='#243746')  # PASSWORD LABEL

        button_fb = tk.Button(canvas, image=images["facebook"], borderwidth=0)  # Tool button
        button_fb.config(activebackground=defaultbg)
        canvas.create_window(92.5, 700, window=button_fb)  # Facebook button position

        button_linkedin = tk.Button(canvas, image=images["linkedin"], borderwidth=0)
        button_linkedin.config(activebackground=defaultbg)
        canvas.create_window(230, 700, window=button_linkedin)  # Linkedin button position

        button_twitter = tk.Button(canvas, image=images["twitter"], borderwidth=0)
        button_twitter.config(activebackground=defaultbg)
        canvas.create_window(367.5, 700, window=button_twitter)  # Twitter button position

        button_signup = tk.Button(canvas, text='Register', borderwidth=0, font='times 12 underline', fg='#243746')
        button_signup.configure(width=10, height=2)
        button_signup.config(activebackground=defaultbg)
        canvas.create_window(240, 620, window=button_signup)

        button_login = tk.Button(canvas, text="LOGIN", font='times 12 bold', fg="#243746", command=lambda: t.show_frame(pages["login"]["frame"], pages["home"]["frame"]))
        button_login.configure(width=10, height=2)
        canvas.create_window(240, 560, window=button_login)

        entry_email = tk.Entry(canvas)  # Email box
        canvas.create_window(80, 375, anchor="w", window=entry_email, height=30, width=300)

        entry_password = tk.Entry(canvas)  # Password box
        canvas.create_window(80, 460, anchor="w", window=entry_password, height=30, width=300)

        canvas.pack()

    elif name == "home":
        button_tool = tk.Button(canvas, image=images["toolIcon"], borderwidth=0,
                                command=lambda: t.show_frame(pages["home"]["frame"], pages["interfaces"]["frame"]))  # Tool button
        button_tool.config(activebackground=defaultbg)
        canvas.create_window(370, 480, window=button_tool, height=200, width=200)  # Tool button postion
        canvas.create_text((370, 600), text='Tool', font='Times 18 bold', fill='#243746')

        button_tutorial = tk.Button(canvas, image=images["tutorialIcon"], borderwidth=0)  # Tutorial button
        button_tutorial.config(activebackground=defaultbg)
        canvas.create_window(110, 200, window=button_tutorial, height=200, width=200)  # Tutorial button postion
        text1 = canvas.create_text((110, 320), text='Tutorials', font='Times 18 bold', fill='#243746')

        button_manual = tk.Button(canvas, image=images["manualIcon"], borderwidth=0)  # manual button
        button_manual.config(activebackground=defaultbg)
        canvas.create_window(370, 200, window=button_manual, height=200, width=200)  # manual button postion
        canvas.create_text((370, 320), text='Manual', font='Times 18 bold', fill='#243746')

        button_settings = tk.Button(canvas, image=images["settingsIcon"], borderwidth=0)  # Settings button
        button_settings.config(activebackground=defaultbg)
        canvas.create_window(110, 480, window=button_settings, height=200, width=200)  # Settings button postion
        canvas.create_text((110, 600), text='Settings', font='Times 18 bold', fill='#243746')

        button_logout = tk.Button(canvas, image=images["logoutIcon"], borderwidth=0, bg="#DBDBDB",
                                  command=lambda: t.show_frame(pages["home"]["frame"], pages["login"]["frame"]))  # logout button
        button_logout.config(activebackground=defaultbg)
        canvas.create_window(230, 700, window=button_logout, height=90, width=90)  # logout button postion

        canvas.pack()

    elif name == "interfaces":
        canvas.create_text((240, 100), text='Interface List', font='Times 18 bold', fill='#4D4D4D')  # Interface List
        canvas.create_text((200, 540), text='Enter the Interface NO :', font='Times 16 bold', fill='#4D4D4D')  # CHOOSE YOUR Interface

        button_home = tk.Button(canvas, image=images["homeIcon"], borderwidth=0, bg="#DBDBDB",
                                command=lambda: t.show_frame(pages["interfaces"]["frame"], pages["home"]["frame"]))  # HOME_Interface button
        button_home.config(activebackground=defaultbg)
        canvas.create_window(51, 749, window=button_home, height=90, width=90)  # HOME_Interface button postion

        button_interfaces_scan = tk.Button(canvas, text="Scan", font='Times 20 bold', fg="#4D4D4D",
                                           command=lambda: t.show_frame(pages["interfaces"]["frame"], pages["networks"]["frame"]))
        button_interfaces_scan.configure(width=7, height=1)  # Scan
        canvas.create_window(250, 650, window=button_interfaces_scan)

        # TODO: Change Entry to Text
        text_interface_output = tk.Entry(canvas, state='disabled')  # Interface output box
        canvas.create_window(240, 290, window=text_interface_output, height=350, width=400)

        entry_interface_input = tk.Entry(canvas)  # Interface input box
        canvas.create_window(360, 540, window=entry_interface_input, height=30, width=50)

        canvas.pack()

    elif name == "networks":
        canvas.create_text((240, 100), text='WIFI list', font='Times 18 bold', fill='#4D4D4D')  # WIFI LIST LABEL
        canvas.create_text((150, 540), text='Choose The Target WIFI :', font='Times 16 bold',
                           fill='#4D4D4D')  # CHOOSE YOUR WIFI

        button_network_confirm = tk.Button(canvas, text="OK", font='Times 13 bold', fg="#4D4D4D")
        button_network_confirm.configure(width=4, height=1)  # button OK
        canvas.create_window(380, 540, window=button_network_confirm)

        button_home_network = tk.Button(canvas, image=images["homeIcon"], borderwidth=0,
                                        command=lambda: t.show_frame(pages["networks"]["frame"], pages["home"]["frame"]))  # HOME_Interface button
        button_home_network.config(activebackground=defaultbg)
        canvas.create_window(51, 749, window=button_home_network, height=90,
                             width=90)  # HOME_Interface button postion

        button_network_rescan = tk.Button(canvas, text="Rescan", font='Times 20 bold', fg="#4D4D4D",
                                          command=lambda: t.show_frame(pages["networks"]["frame"], pages["interfaces"]["frame"]))
        button_network_rescan.configure(width=7, height=1)  # RESCAN
        canvas.create_window(250, 650, window=button_network_rescan)

        text_network_output = tk.Text(canvas)  # Network output box
        text_network_output.configure(state="disabled")
        canvas.create_window(240, 290, window=text_network_output, height=350, width=400)

        entry_network_input = tk.Entry(canvas)  # Network input box
        canvas.create_window(310, 540, window=entry_network_input, height=30, width=50)

        canvas.pack()


root.mainloop()
