from tkinter import Tk, LEFT, TOP, messagebox, END, Label
from tkinter.constants import DISABLED, NORMAL, X
from tkinter.ttk import Entry, Button
from typing import Tuple
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import Dialog
from socket import inet_aton, inet_ntoa
from datetime import datetime
from packet import NICK_LEN, Packet
from custom_udp import UDP_P2P


class Window:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("700x450")
        self.root.resizable(0, 0)
        self.root.title("Chat")

        self.root.withdraw()
        self.__input()
        self.root.wm_deiconify()

        self.record = ScrolledText(self.root, state=DISABLED)
        self.record.pack(side=TOP, fill=X)

        self.message = Entry(self.root)
        self.message.bind("<Return>", lambda _: self.__send())
        self.message.pack(side=LEFT)

        self.enterBtn = Button(self.root, text="enter", command=self.__send)
        self.enterBtn.pack(side=LEFT)

        self.udpp2p = UDP_P2P(self.ipDest, 6000, 6000)

        self.t = self.udpp2p.receptionThread(self.__receive)
        self.t.start()

        self.root.bind("<Destroy>", self.__onWindowClose)

        self.root.mainloop()

    def __input(self) -> None:
        d = InputDialog(self.root)

        self.username = d.result[0]
        if not self.username or len(self.username) > NICK_LEN:
            messagebox.showerror(
                "Input Error", "Invalid Username. Max size is 16 characters"
            )
            self.__input()

        try:
            self.ipDest = inet_ntoa(inet_aton(d.result[1]))
        except:
            messagebox.showerror("Input Error", "Invalid IP")
            self.__input()

    def __send(self) -> None:
        if len(self.message.get().strip()) > 0:
            try:
                self.udpp2p.transmission("APP", "1", self.username, self.message.get())

                self.__addMsg(f"\n(YOU): {self.message.get().strip()}")
                self.message.delete(0, END)
            except Exception as e:
                messagebox.showerror("Input Error", e)

    def __receive(self, data: Packet, addr: Tuple[str, int], time: datetime) -> None:
        n = (
            datetime.strptime(time.strftime("%H%M%S%f"), "%H%M%S%f")
            - datetime.strptime(data.time + "000", "%H%M%S%f")
        ).total_seconds() * 1000

        self.__addMsg(
            f"\n(Username: {data.nick.strip()} - Address: {addr[0]} - Latency: {int(n)}ms):\n{data.msg.strip()}"
        )

    def __addMsg(self, msg: str) -> None:
        self.record.configure(state=NORMAL)
        self.record.insert(
            END,
            msg,
        )
        self.record.configure(state=DISABLED)

    def __onWindowClose(self, _):
        self.udpp2p.closeSockSend()
        self.udpp2p.stopThread()


class InputDialog(Dialog):
    def body(self, master):
        Label(master, text="Username:").grid(row=0)
        Label(master, text="Connect to IP:").grid(row=1)

        self.e1 = Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2 = Entry(master)
        self.e2.grid(row=1, column=1)

        return self.e1

    def apply(self):
        self.result = [self.e1.get(), self.e2.get()]
