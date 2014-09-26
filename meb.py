#!/usr/bin/env python

import Tkinter
import re
import tkFileDialog
import ScrolledText
import os
import shutil

def open_file(file_name):
    try:
        # make a full path
        rf = open(config_dir + "m_dir", 'r')
        m_dir = rf.read()
        rf.close()
        if '/' not in file_name:
            file_name = m_dir + file_name
        #print file_name
        
        # Open the file
        rf = open(file_name, 'r')
        my_text = rf.read()
        rf.close()
        
        #write the contents to the c_file
        wf = open(config_dir + "c_file", 'w')
        wf.write(my_text)
        wf.close()
        
        #Seperate the links from the text while keeping everything in 
        #order
        l = re.split(r"(\[\[.*?\]\])", my_text,)
        #clear the text field
        text.config(state="normal")
        text.delete(1.0, Tkinter.END)
        #insert the text while making the link portions links
        for t in l:
            if '[[' in t and ']]' in t:
                text.insert(Tkinter.END, t, ("a", t))
            else:
                text.insert(Tkinter.END, t)
        text.config(state="disabled")
        #print 'Opened: ' + file_name
    except:
        open(file_name, 'w').close()
        open_file(file_name)
        #print 'Created and Opened: ' + file_name



def click(event):
    w = event.widget
    x, y = event.x, event.y
    tags = w.tag_names("@%d,%d" % (x, y))
    #remove the [[]] from the link
    file_base = tags[1].split('[[')[1].split(']]')[0]
    # add the .md  extension to filename
    file_name = file_base + ".md"
    #open the file
    open_file(file_name)
    # store the current filename
    shutil.copyfile(config_dir + "cf_name", config_dir + "lf_name")
    #print 'Saved lf_name...'
    wf = open(config_dir + "cf_name", 'w')
    wf.write(file_name)
    wf.close()
    #print 'Saved cf_name: ' + file_name

# functions that make the cursor change to and from hand when hovering
# over a link
def show_hand_cursor(event):
    event.widget.configure(cursor="hand1")
def show_arrow_cursor(event):
    event.widget.configure(cursor="")

def button_open():
    # Get filename
    m_file = tkFileDialog.askopenfilename()
    m_dir = os.path.dirname(m_file) + '/'
    #print m_dir
    wf = open(config_dir + "m_dir", 'w')
    wf.write(m_dir)
    wf.close()
    # store the current file name as the last file name
    try:
        shutil.copyfile(config_dir + "cf_name", config_dir + "lf_name")
    except:
        pass
    #print 'Saved lf_name...'
    # store the current filename
    wf = open(config_dir + "cf_name", 'w')
    wf.write(m_file)
    wf.close()
    #print 'Saved cf_name: ' + file_name
    #open the file
    open_file(m_file)
    # Save opened file as main file
    try:
        f = open(config_dir + 'm_file', 'w')
        f.write(m_file)
        f.close()  
    except:
        pass

def button_edit():
    editsave_button.config(text="Save", command=button_save)
    text.config(state="normal")
    text.delete(1.0, Tkinter.END)
    f = open(config_dir + "cf_name", 'r')
    cf_name = f.read()
    f.close()
    f = open(config_dir + "c_file", 'r')
    c_file = f.read()
    f.close()
    text.insert(Tkinter.END, c_file)
    

def button_save():
    editsave_button.config(text="Edit", command=button_edit)
    rf = open(config_dir + "m_dir", 'r')
    m_dir = rf.read()
    rf.close()
    f = open(config_dir + "cf_name", 'r')
    cf_name = f.read()
    f.close()
    new_text = text.get("1.0", 'end')
    wf = open(m_dir + cf_name, 'w')
    wf.write(new_text)
    wf.close()
    open_file(m_dir + cf_name)

def button_delete():
    f = open(config_dir + "cf_name", 'r')
    cf_name = f.read()
    f.close()
    # make a full path
    f = open(config_dir + "m_dir", 'r')
    m_dir = f.read()
    f.close()
    if '/' not in cf_name:
        cf_name = m_dir + cf_name
    os.remove(cf_name)
    #print 'Deleting: ' + cf_name
    f = open(config_dir + "lf_name", 'r')
    lf_name = f.read()
    f.close()
    #print "Going back to: " + lf_name
    open_file(lf_name)


def button_back():
    shutil.copyfile(config_dir + "cf_name", config_dir + "cf_name.tmp")
    shutil.copyfile(config_dir + "lf_name", config_dir + "cf_name")
    shutil.copyfile(config_dir + "cf_name.tmp", config_dir + "lf_name")
    os.remove(config_dir + "cf_name.tmp")
    f = open(config_dir + "cf_name", 'r')
    cf_name = f.read()
    f.close()
    open_file(cf_name)

app = Tkinter.Tk()
app.title("Meb")

text = ScrolledText.ScrolledText(app)
#text = Tkinter.Text(app)
text.pack(expand=1, fill= Tkinter.BOTH)


text.tag_config("a", foreground="blue", underline=1)
text.tag_bind("a", "<Enter>", show_hand_cursor)
text.tag_bind("a", "<Leave>", show_arrow_cursor)
text.tag_bind("a", "<Button-1>", click)
text.config(cursor="arrow")

editsave_button = Tkinter.Button(app, text="Edit", command=button_edit)
editsave_button.pack(side=Tkinter.RIGHT)

delete_button = Tkinter.Button(app, text="Delete", command=button_delete)
delete_button.pack(side=Tkinter.RIGHT)

open_button = Tkinter.Button(app, text="Open", command=button_open)
open_button.pack(side=Tkinter.RIGHT)

back_button = Tkinter.Button(app, text="Back", command=button_back)
back_button.pack(side=Tkinter.LEFT)


config_dir = os.path.expanduser('~') + "/.meb/"

if not os.path.exists(config_dir):
    os.makedirs(config_dir)

try:
    f = open(config_dir + "m_file", 'r')
    m_file = f.read()
    f.close()
    wf = open(config_dir + "cf_name", 'w')
    wf.write(m_file)
    wf.close()
    open_file(m_file)
except:
    pass


app.mainloop()
