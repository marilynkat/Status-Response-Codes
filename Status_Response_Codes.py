####################################
#      Status Response Codes       #
####################################

import tkinter
import requests

response_code_GUI = tkinter.Tk()
response_code_GUI.title('Status Response Codes')

#GUI window dimensions
response_code_GUI.geometry("400x400")

def click():
    #Save value from textbox input
    input=textbox1.get("1.0","end-1c")

    #Get response code
    response = requests.head(input)

    #Clear textbox
    textbox1.delete('1.0', tkinter.END)

    #Display result in textbox
    textbox2.insert(tkinter.END, input + " - " + str(response.status_code) + "\n")
    textbox2.see(tkinter.END)

#Contents of GUI
prompt1 = tkinter.Label(text="Enter a URL:")
prompt2 = tkinter.Label(text="Response Code:")
textbox1 = tkinter.Text(height=1,width=40)
button = tkinter.Button(response_code_GUI, text="Go", height=1, width=2, command=click)
textbox2 = tkinter.Text(height=20,width=50)

#Load contents to GUI
prompt1.place(x=20,y=20)
prompt2.place(x=20,y=75)
textbox1.place(x=20,y=45)
button.place(x=320,y=40)
textbox2.place(x=20,y=100)

response_code_GUI.mainloop()