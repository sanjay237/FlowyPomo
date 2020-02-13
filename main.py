import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

dir =  os.getcwd()
mixer.init()
mixer.music.load(str(os.getcwd())+'/chime.mp3')

"""
class MyWindow(Gtk.Window): #create a class for your window
    def __init__(self):
        count = 0
        Gtk.Window.__init__(self, title='FlowyPomo') #show a window, with the set title
        
        self.box = Gtk.Box(spacing=60) # a box is a layout container
        self.add(self.box)        
        
        self.button1 = Gtk.Button(label="25 minutes") #define a button
        self.button1.connect("clicked", self.twentyfive) #connect: if button is clicked, call that function
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="5 minutes") #define a button
        self.button2.connect("clicked", self.five) #connect: if button is clicked, call that function
        self.box.pack_start(self.button2, True, True, 0)
  
    def twentyfive(self, widget):
        mixer.music.play()
        for i in range(10):
            print(i)
            time.sleep(1)
        mixer.music.play()

    def five(self, widget):
        print('5')

class Frame1(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='FlowyPomo')

for getting an icon:
        self.notebook.append_page(
                    self.page2,
                    Gtk.Image.new_from_icon_name(
                        "help-about",
                        Gtk.IconSize.MENU
                    )
"""

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="FlowyPomo")
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label('How many pomos would you like to work for?'))
        self.ok_button = Gtk.Button("ok") #to-do: replace ok with a tick-mark/star emoji
        self.ok_button.connect("clicked", self.clicked_ok)
        self.entry = Gtk.Entry()
        self.page1.pack_start(self.entry, True, True, 0)
        self.page1.pack_start(self.ok_button, True, True, 0)
        self.notebook.append_page(self.page1, Gtk.Label('Frame 1')) #to-do: depend page/use the stack

        # self.entry = Gtk.Entry()
        # self.page1.pack_start(self.entry, True, True, 0)

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('What specifically would you like to work on?'))
        self.notebook.append_page(self.page2, Gtk.Label('Frame 2'))
        # self.page2 = Gtk.Box()
        # self.page2.set_border_width(10)
        # self.page2.add(Gtk.Label('A page with an image for a Title.'))
        # self.notebook.append_page(
        #     self.page2,
        #     Gtk.Image.new_from_icon_name(
        #         "help-about",
        #         Gtk.IconSize.MENU
        #     )
        # )
    def clicked_ok(self, widget): #to-do: clicking okay should transition to the next frame
        try:
            text = int(Gtk.Entry.get_text(self.entry))
            print(text)
        except ValueError:
            print('invalid number of pomos')

class StackWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Stack Demo")
        self.set_border_width(10)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(250)
        
        self.checkbutton = Gtk.CheckButton("Click me!")
        self.checkbutton.connect("clicked", self.clicked_me)
        self.stack.add_titled(self.checkbutton, "check", "Check Button")
        
        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.stack)
        self.vbox.pack_start(self.stack_switcher, True, True, 0)
        self.vbox.pack_start(self.stack, True, True, 0)
    
    def clicked_me(self, widget):
        # label = Gtk.Label()
        # label.set_markup("<big>A fancy label</big>")
        # self.stack.add_titled(label, "label", "A label")

        # slide over to the next stack
        return None

win1 = StackWindow() #initiate an instance of that class
win2 = MyWindow()
win1.connect("destroy", Gtk.main_quit)
win2.connect("destroy", Gtk.main_quit)

win1.show_all()
# win2.show_all()
Gtk.main()