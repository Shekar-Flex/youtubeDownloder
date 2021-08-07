from tkinter import *
from tkinter import ttk
from tkinter import  filedialog
from tkinter import messagebox
from pytube import YouTube

Fokder_name=""

def openLocation():
    global Fokder_name
    Fokder_name=filedialog.askdirectory()
    if(len(Fokder_name) >1):
        locationError.config(text=Fokder_name,fg="green")
    else:
        locationError.config(text="Pelase choose folder!!!",fg="red")

def DownloadVideo():
    #print(Fokder_name)
    choice=ytdchoisce.get()
    #print(choice)
    url=ytdEntryVar.get()
    #print(url)
    if "https://youtu.be" in url:
        if (len(Fokder_name) > 1):
            if (choice==choices[0] or choice==choices[1] or choice==choices[2]) :
                #yt=YouTube(url)
                #print(yt.title)
                #My_video=yt.streams.filter(progressive=True).first()
                #My_video.download(Fokder_name)
                if(len(url)>1):
                    #ytdError.config(test="")
                    yt=YouTube(url)
                    #print(yt.title)
            
                    if (choice == choices[0]):
                        select=yt.streams.filter(progressive=True).first()
            
                    elif(choice == choices[1]):
                        select = yt.streams.filter(progressive=True,file_extension='mp4').last()
            
                    elif (choice == choices[2]):
                        select = yt.streams.filter(only_audio=True).first()
                    else:
                        ytdError.config(test="Past the link again!!",fg='red')

                messagebox.showinfo('Start downloading..', 'Press ok')
                select.download(Fokder_name)
                ytdError.config(text="Download Completed!!!",fg="green")
                thank.config(text="Have a greate day by Flex.",fg='#4b4b4b')
            else:
                messagebox.showerror('Qulity Error','Please select Qulity of video')
        else:
            messagebox.showerror('Path Error', 'Please select the path!!!')
    else:
        messagebox.showerror('URL Error', 'Please give correct URL')


root=Tk()
root.title("FlexYouTubeDownloader")
root.geometry("350x400")
root.columnconfigure(0,weight=1)
root.resizable(width='false',height='false')
root.iconbitmap('you.ico')


title=Label(root,text="Welcome to Flex YouTube Downloader",font=("times",16,'bold','italic'),pady=5,bg='black',fg='red',relief='raised')
title.grid()

topad=Label(root,pady=5)
topad.grid()

ytdLable=Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLable.grid()

ytdEntryVar=StringVar()
ytdEntryVar=Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntryVar.grid()

ytdError=Label(root,text="",fg="red",font=("jost",10))
ytdError.grid()

saveLable=Label(root,text="save the video File",font=("jost",15,"bold"))
saveLable.grid()

saveEntry=Button(root,width=10,bg="red",fg="white",text="choose Path",command=openLocation)
saveEntry.grid()

locationError=Label(root,text="",fg="red",font=("jost",10))
locationError.grid()

ytdQuality=Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

choices=["720p","144p","Only Audio"]
ytdchoisce=ttk.Combobox(root,value=choices)
ytdchoisce.grid()

downloadbtn=Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

developerlabel=Label(root,text="Flex Devaloper",font=("jost",15))
developerlabel.grid()

topad=Label(root,pady=12)
topad.grid()

thank=Label(root,text="",pady=3,font=("times",15,'bold','italic'))
thank.grid()






root.mainloop()
