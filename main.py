from PIL import ImageTk, Image
import tkinter as tk
import tools as t
import webbrowser

import os


def show_page(current_frame, frame):
    current_frame.pack_forget()
    frame.pack()


def show_url():
    webbrowser.open("https://www.google.com/")


def construct_file(x):
    return x.format(assets_path)


window = tk.Tk()
window.title("Cover page")
window.resizable(height=False, width=False)
window.geometry("480x800") #window

defaultbg = window.cget('bg')

login = tk.Frame(window, width=480, height=800)
cover = tk.Frame(window, width=480, height=800)
home = tk.Frame(window, width=480, height=800)
interface = tk.Frame(window, width=480, height=800)
network = tk.Frame(window, width=480, height=800)

assets_path = t.assets_path


logo2 = ImageTk.PhotoImage(file=construct_file("{}coverLogo.png"))  # logo pic
#right2 = ImageTk.PhotoImage(file=construct_file("{}Asset 4.png"))  # right one
#left2 = ImageTk.PhotoImage(file=construct_file("{}Asset 3.png"))  # left one
#facebook2 = ImageTk.PhotoImage(file=construct_file("{}Asset 5.png"))  # facebook pic
#linkedin2 = ImageTk.PhotoImage(file=construct_file("{}Asset 7.png"))  # linkedin pic
#twitter2 = ImageTk.PhotoImage(file=construct_file("{}Asset 6.png"))  # twitter pic


canvas = tk.Canvas(cover, width=480, height=800)  # Canvas
canvas.configure(bg="#243746")  # canvas color

button1 = tk.Button(cover, width=480, height=800,bg = "#243746", image=logo2, command=lambda: show_page(cover, login))
button1.config(activebackground="#243746")
button1.pack()   # cover page = button contains the logo PPTD


canvas.pack()
# canvas.create_image(230, 350, image=logo2, anchor="center")  # logo postion
#canvas.create_image(250, 20, image=right2, anchor="nw")  # right postion
#canvas.create_image(210, 20, image=left2, anchor="ne")  # left postion
#canvas.create_image(92.5, 700, image=facebook2, anchor="center")  # facbook postion
#canvas.create_image(230, 700, image=linkedin2, anchor="center")  # linkedin postion
#canvas.create_image(367.5, 700, image=twitter2, anchor="center")  # twitter psotion
# canvas.create_text((230, 580), text='START', font='Times 30 bold', fill='#FFFFFF')


#################################################################################################################### login page

# background_img = Image.open("{}Asset 8.png".format(assets_path))
# resized = background_img.resize((480, 800))
# background = ImageTk.PhotoImage(resized) #background

logomini = ImageTk.PhotoImage(file="{}loginLogo.png".format(assets_path)) #logo pic

canvas2 = tk.Canvas(login, width=480, height=800) #Canvas

# canvas2.create_image(240, 400) #background image postion

facebook = ImageTk.PhotoImage(file=construct_file("{}facebook.png"))  # facebook pic
button_fb = tk.Button(canvas2, image=facebook, borderwidth=0, command=show_url)  # Tool button
button_fb.config(activebackground=defaultbg)
canvas2.create_window(92.5, 700, window=button_fb )# Tool button postion

linkedin = ImageTk.PhotoImage(file=construct_file("{}linkedin.png"))  # linkedin pic
button_linkedin = tk.Button(canvas2, image=linkedin, borderwidth=0, command=lambda: show_page(home ,interface))  # Tool button
button_linkedin.config(activebackground=defaultbg)
canvas2.create_window(230, 700, window=button_linkedin)# Tool button postion

twitter = ImageTk.PhotoImage(file=construct_file("{}twitter.png"))  # twitter pic
button_twitter = tk.Button(canvas2, image=twitter, borderwidth=0, command=lambda: show_page(home ,interface))  # Tool button
button_twitter.config(activebackground=defaultbg)
canvas2.create_window(367.5, 700, window=button_twitter)# Tool button postion

# canvas2.create_image(92.5, 700, image=facebook, anchor="center")  # facbook postion
# canvas2.create_image(230, 700, image=linkedin, anchor="center")  # linkedin postion
# canvas2.create_image(367.5, 700, image=twitter, anchor="center")  # twitter psotion
canvas2.create_image(240, 170, image=logomini, anchor="center") #logo postion

canvas2.create_text((122, 350), text='Username :', font='times 12 bold', fill='#243746') #USERNAME LABEL
canvas2.create_text((122, 435), text='Password :', font='times 12 bold', fill='#243746') #PASSWORD LABEL

button_signup = tk.Button(canvas2, text='Register', borderwidth=0, font='times 12 underline', fg='#243746', command=lambda: show_page(login, home)) #button signup
button_signup.configure(width=10, height=2)
button_signup.config(activebackground=defaultbg)
canvas2.create_window(240, 620, window=button_signup)

button = tk.Button(canvas2, text="LOGIN", font='times 12 bold', fg="#243746" ,command=lambda: show_page(login,home)) #button login
#command=lambda: show_page(login, cover) if we wantt to link the login button
button.configure(width=10, height=2)
canvas2.create_window(240, 560, window=button)

entry1 = tk.Entry(canvas2)    #Text box 1
canvas2.create_window(230, 375, window=entry1, height=30, width=300)
entry2 = tk.Entry(canvas2)    #Text box 2
canvas2.create_window(230, 460, window=entry2, height=30, width=300)

canvas2.pack()
cover.pack()


##########################################################HOME PAGE


assets_path = t.assets_path

canvas3 = tk.Canvas(home, width=480, height=800)  # Canvas

tool = ImageTk.PhotoImage(file="{}toolIcon.png".format(assets_path))#Tool icon
tutorial = ImageTk.PhotoImage(file="{}tutorialIcon.png".format(assets_path))  # Tutorial icon
manual = ImageTk.PhotoImage(file="{}manualIcon.png".format(assets_path))  # Manual icon
settings = ImageTk.PhotoImage(file="{}settingsIcon.png".format(assets_path))  # Settings icon
logout = ImageTk.PhotoImage(file="{}logoutIcon.png".format(assets_path))  # logout icon
# background = ImageTk.PhotoImage(file="{}background.png".format(assets_path))  # Background pic

# canvas3.create_image(240, 400, image=background) # canvas color


button_tool = tk.Button(canvas3, image=tool, borderwidth=0, command=lambda: show_page(home ,interface))  # Tool button
button_tool.config(activebackground=defaultbg)
canvas3.create_window(370, 480, window=button_tool,  height=200, width=200 )# Tool button postion
text = canvas3.create_text((370, 600), text='Tool', font='Times 18 bold', fill='#243746')

button_tutorial = tk.Button(canvas3, image=tutorial, borderwidth=0)  # Tutorial button
button_tutorial.config(activebackground=defaultbg)
canvas3.create_window(110, 200, window=button_tutorial, height=200, width=200)# Tutorial button postion
text1 = canvas3.create_text((110, 320), text='Tutorials', font='Times 18 bold', fill='#243746')

button_manual = tk.Button(canvas3, image=manual, borderwidth=0)  # manual button
button_manual.config(activebackground=defaultbg)
canvas3.create_window(370, 200, window=button_manual, height=200, width=200)# manual button postion
text2 = canvas3.create_text((370, 320), text='Manual', font='Times 18 bold', fill='#243746')

button_settings = tk.Button(canvas3, image=settings, borderwidth=0)  # Settings button
button_settings.config(activebackground=defaultbg)
canvas3.create_window(110, 480, window=button_settings, height=200, width=200)# Settings button postion
text3 = canvas3.create_text((110, 600), text='Settings', font='Times 18 bold', fill='#243746')


button_logout = tk.Button(canvas3, image=logout, borderwidth=0 , bg="#DBDBDB", command=lambda: show_page(home, login))  # logout button
button_logout.config(activebackground=defaultbg)
button_logout2 = canvas3.create_window(230, 700, window=button_logout, height=90, width=90)# logout button postion


canvas3.pack()

############################################################Interface page

background_img = ImageTk.PhotoImage(file="{}background.png".format(assets_path))#background icon
home_interface = ImageTk.PhotoImage(file="{}homeIcon.png".format(assets_path))#home icon
#background_img = Image.open("{}Asset 8.png".format(assets_path))
#home_img = Image.open("{}Asset 10.png".format(assets_path))
#resized_bg = background_img.resize((480, 800))

#bg = ImageTk.PhotoImage(resized_bg)
#home = ImageTk.PhotoImage(home_img)

canvas4 = tk.Canvas(interface, width=480, height=800) #Canvas

# canvas4.create_image(240, 400, image=background_img) #background image postion
canvas4.create_image(51, 749, image=home_interface) #Home icon postion
canvas4.create_text((240, 100), text='Interface List', font='Times 18 bold', fill='#4D4D4D') #Interface List
canvas4.create_text((200, 540), text='Enter the Interface NO :', font='Times 16 bold', fill='#4D4D4D') #CHOOSE YOUR Interface

button_home = tk.Button(canvas4, image=home_interface, borderwidth=0 , bg="#DBDBDB", command=lambda: show_page(interface, home))  # HOME_Interface button
button_home.config(activebackground=defaultbg)
canvas4.create_window(51, 749, window=button_home, height=90, width=90)# HOME_IInterface button postion

button = tk.Button(canvas4, text="Scan", font='Times 20 bold', fg="#4D4D4D", command=lambda: show_page(interface, network))
button.configure(width=7, height=1)                    #Scan
canvas4.create_window(250, 650, window=button)

entry1 = tk.Entry(canvas4,  state='disabled')    #Text box 1
canvas4.create_window(240, 290, window=entry1, height=350, width=400)

entry2 = tk.Entry(canvas4)    #Text box 2
canvas4.create_window(360, 540, window=entry2, height=30, width=50)

canvas4.pack()

################################################################ NETWORK PAGE

background = ImageTk.PhotoImage(file="{}background.png".format(assets_path))#background icon
home_network = ImageTk.PhotoImage(file="{}homeIcon.png".format(assets_path))#home icon

#background_img = Image.open("{}Asset 8.png".format(assets_path))
#home_img = Image.open("{}Asset 10.png".format(assets_path))
#resized_bg = background_img.resize((480, 800))

#bg = ImageTk.PhotoImage(background)
#home = ImageTk.PhotoImage(home_network)
canvas5 = tk.Canvas(network, width=480, height=800) #Canvas

# canvas5.create_image(240, 400) #background image postion
#canvas5.create_image(51, 749, image=home_network) #Home icon postion
canvas5.create_text((240, 100), text='WIFI list', font='Times 18 bold', fill='#4D4D4D') #WIFI LIST LABEL
canvas5.create_text((150, 540), text='Choose The Target WIFI :', font='Times 16 bold', fill='#4D4D4D') #CHOOSE YOUR WIFI

button = tk.Button(canvas5, text="OK", font='Times 13 bold', fg="#4D4D4D")
button.configure(width=4, height=1)                    #button OK
canvas5.create_window(380, 540, window=button)

button_home_network = tk.Button(canvas5, image=home_network, borderwidth=0, command=lambda: show_page(network, home))  # HOME_Interface button
button_home_network.config(activebackground=defaultbg)
canvas5.create_window(51, 749, window=button_home_network, height=90, width=90)# HOME_IInterface button postion

button = tk.Button(canvas5, text="Rescan", font='Times 20 bold', fg="#4D4D4D", command=lambda: show_page(network, interface))
button.configure(width=7, height=1)                    #RESCAN
canvas5.create_window(250, 650, window=button)



entry1 = tk.Text(canvas5)    #Text box 1
# entry1.pack()

entry1.insert(tk.END, """d
ddd""")
entry1.configure(state="disabled")
canvas5.create_window(240, 290, window=entry1, height=350, width=400)

entry2 = tk.Entry(canvas5)    #Text box 2
canvas5.create_window(310, 540, window=entry2, height=30, width=50)

s = tk.Scrollbar(entry1)

canvas5.pack()




window.mainloop()