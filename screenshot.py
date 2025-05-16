import time
import pyautogui
import tkinter as tk

#making the function
def screenshot():
    time.sleep(5) # counts for 5 seconds
    name  = int(round(time.time()*1000)) # generate a random number
    name = "%s.png" % (name)        # use it as a name for the screenshots taken
    img = pyautogui.screenshot(name)
    img.show()
 
 
#main function
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(
    frame, 
    text = "take a screenshot",
    command = screenshot()
)
button.pack(  side = tk.LEFT)
exit = tk.Button(
    frame, 
    text = "Close ",
    command = quit
) 
exit.pack(  side = tk.LEFT)

root.mainloop()