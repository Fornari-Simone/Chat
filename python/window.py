from tkinter import Tk, BOTH, X, LEFT, TOP, messagebox, RIGHT, END
from tkinter.constants import DISABLED
from tkinter.ttk import Frame, Label, Entry, Button
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import Dialog, askstring
from socket import inet_aton, inet_ntoa, sendto, recvfrom
from datetime import now, strptime
from packet import Packet
from threading import Thread


class Window:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.withdraw()
        self.username = askstring("Input", "Username: ")
        try:
            self.ipDest = inet_ntoa(inet_aton(askstring("Input", "Connect to IP: ")))
        except:
            messagebox.showerror("Input Error", "Invalid IP")
        self.root.wm_deiconify()
        if self.username and self.ipDest:
            self.record = ScrolledText(self.root, state=DISABLED)
            self.record.pack(side=TOP)
            self.message = Entry(self.root)
            self.message.pack(side=LEFT)
            self.enterBtn = Button(self.root, text="enter", command=self.__send)
            self.enterBtn.pack(side=RIGHT)

            self.root.mainloop()

            self.t = Thread(target=self.__receive)
            self.t.daemon = True
            self.t.start()

    def __send(self):
        t = now().strftime("%H%M%S%f")[:-3]

        p = Packet("APP", "1", self.username, t, self.message.get())
        sendto(p.bytes, (self.ipDest, 6000))

    def __receive(self):
        while True:
            data, addr = recvfrom(130)
            data = Packet(data)
            n = (
                strptime(now().strftime("%H%M%S%f"), "%H%M%S%f").total_seconds() * 1000
            ) - (strptime(data.time + "000", "%H%M%S%f").total_seconds() * 1000)
            self.record.insert(END, f"\n({data.nick} - {addr} - {n}): {data.msg}")
            self.message.delete(0, END)