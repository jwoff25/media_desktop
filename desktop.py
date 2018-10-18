from Tkinter import *
#from PIL import Image
import os
import sys
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options

# create root app
root = Tk()

# calculate button size
h = root.winfo_screenheight()/2
w = root.winfo_screenwidth()/2

# open browser method
def open_browser(name):
	option = webdriver.ChromeOptions()
	option.accept_untrusted_certs = True
	option.assume_untrusted_cert_issuer = True
	option.add_argument("--start-maximized")
	option.add_argument("--kiosk")
	browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=option)
	if name == "netflix":
		browser.get("https://www.netflix.com")
	elif name == "hulu":
		browser.get("https://www.hulu.com")
	elif name == "amzn":
		browser.get("https://www.primevideo.com")
		#browser.maximize_window()
		#browser.switch_to_window(browser.current_window_handle)


# load photos
netflix_logo = PhotoImage(file="netflix-logo-n.png")
hulu_logo = PhotoImage(file="hulu-logo-n.png")
amzn_logo = PhotoImage(file="Amazon-Prime-n.png")

# create buttons
netflix = Button(root, height=h, width=w, command=lambda:open_browser("netflix"))
hulu = Button(root, height=h, width=w, command=lambda:open_browser("hulu"))
amzn = Button(root, height=h, width=w, command=lambda:open_browser("amzn"))
dummy = Button(root, command=sys.exit)

# add images to buttons
netflix.config(image=netflix_logo)
hulu.config(image=hulu_logo)
amzn.config(image=amzn_logo)

# map them to rows/cols
netflix.grid(row=0, column=0, sticky=("N","S","E","W"))
hulu.grid(row=1, column=0, sticky=("N","S","E","W"))
amzn.grid(row=0, column=1, sticky=("N","S","E","W"))
dummy.grid(row=1, column=1, sticky=("N","S","E","W"))

# run in kiosk mode
#root.overrideredirect(True) # add this later
root.attributes("-fullscreen",True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()
