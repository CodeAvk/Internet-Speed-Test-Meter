from tkinter import  *
import speedtest


def Start():
    test=speedtest.Speedtest()

    Uploading=round(test.upload()/(1024*1024),2)
    upload.config(text=Uploading)
    # print(Uploading)

    Downloading = round(test.download()/(1024*1024),2)
    download.config(text=Downloading)
    Download.config(text=Downloading)
    # print(Downloading)

    server_name=[]
    test.get_servers(server_name)
    ping.config(text=test.results.ping)
    # print(test.results.ping)

root=Tk()
root.title("@Avk Internet Speed Test")
root.geometry("360x600")
root.resizable(False,False)
root.configure(bg="#1a212d")


#icon
root.wm_iconbitmap("Spd_test.ico")

#images
Top=PhotoImage(file="spd_top.png")
Label(root,image=Top,bg="#1a212d").pack()

Mid=PhotoImage(file="Spd_main.png")
Label(root,image=Mid,bg="#1a212d").pack(pady=(40,0))

button=PhotoImage(file="spd_button.png")
Button=Button(root,image=button,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2",command=Start)
Button.pack(pady=10)

Label(root,text="PING",font="arial 10 bold",bg="#384056").place(x=50,y=0)
Label(root,text="DOWNLOAD",font="arial 10 bold",bg="#384056").place(x=140,y=0)
Label(root,text="UPLOAD",font="arial 10 bold",bg="#384056").place(x=265,y=0)

Label(root,text="ms",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)
Label(root,text="Mbps",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)
Label(root,text="Mbps",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)


Label(root,text="Download",font="arial 15 bold",bg="#384056",fg="white").place(x=140,y=280)
Label(root,text="Mbps",font="arial 15 bold",bg="#384056",fg="white").place(x=155,y=380)

ping=Label(root,text="00",font="DS-Digital  13 bold",bg="#384056",fg="white")
ping.place(x=70,y=60,anchor="center")

download=Label(root,text="00",font="DS-Digital  13 bold",bg="#384056",fg="white")
download.place(x=180,y=60,anchor="center")

upload=Label(root,text="00",font="DS-Digital  13 bold",bg="#384056",fg="white")
upload.place(x=290,y=60,anchor="center")

Download=Label(root,text="00",font="DS-Digital  50 bold",bg="#384056",)
Download.place(x=185,y=350,anchor="center")





root.mainloop()
