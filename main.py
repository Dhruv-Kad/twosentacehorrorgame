from reader import readfile as rf
from tkinter import Tk, ttk

def getposts():
    #Add more urls to increase the number of posts found, maybe add hot and top for higher quality
    urls = ["https://reddit.com/r/TwoSentenceHorror/new/"]
    for i, url in enumerate(urls):
        print(f"Fetching {i} url(s) from {url}")
        rf(url)
def printname():
    print("Hello World")
def drawimage():
    root = Tk() 
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
    ttk.Button(frm, text="hello", command=printname).grid(column=1, row=1)
    root.mainloop()



if __name__ == "__main__":
    drawimage()
