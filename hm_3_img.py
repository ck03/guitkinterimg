import tkinter as tk
from PIL import Image, ImageTk
from pymongo import MongoClient
import tkinter.messagebox as msg


class GUI:

    def __init__(self, master=None):
        self.master = master
        self.result_list = []
        self.slbl = tk.StringVar()
        self.slbl.set("Hello Python")
        self.w = tk.Label(master, textvariable=self.slbl)
        self.w.pack()
        self.btnprev = tk.Button(master, text="<<上一張", command=lambda: self.change("prev"), width=15)
        self.btnprev.pack(side=tk.LEFT)
        self.btnnext = tk.Button(master, text="下一張>>", command=lambda: self.change("next"), width=15)
        self.btnnext.pack(side=tk.RIGHT)
        self.wifi_img = Image.open('a.jpg')
        self.lblimg = ImageTk.PhotoImage(self.wifi_img)
        self.lbl2 = tk.Label(master, image=self.lblimg)
        self.lbl2.pack(side="top", fill="both", expand="yes")
        self.dbinfo()
        self.index = 0

    def dbinfo(self):
        client = MongoClient(host="127.0.0.1", port=27017)
        collection = client["igimg"]["imginfo"]
        dbinfo = collection.find({"cname": "黃上晏"})
        for i in dbinfo:
            self.result_list.append(i["cname"] + "_" + i["id"])

    def change(self, saction):
        if saction == "next":
            if self.index < len(self.result_list) - 1:
                self.index += 1
            else:
                self.index = 0
        else:
            if self.index == -(len(self.result_list)):
                self.index = -1
            else:
                self.index -= 1
        # msg.showinfo("結果", saction)
        self.slbl.set(self.index)
        wifi_img = Image.open(u'D:\\Study\\Python2\\03爬蟲\\IG_XXX\\{}.jpg'.format(self.result_list[self.index]))
        lblimg = ImageTk.PhotoImage(wifi_img)
        self.lbl2.configure(image=lblimg)
        self.lbl2.image = lblimg


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(master=root)
    root.title("照片瀏覽")
    root.geometry("900x800")
    root.mainloop()


