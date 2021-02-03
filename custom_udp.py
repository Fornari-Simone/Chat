from socket import AF_INET, SOCK_DGRAM, socket
from typing import Callable, Tuple
from packet import Packet
from datetime import datetime
from threading import Thread


class UDP_P2P:
    def __init__(self, ipDest: str, sendPort: int, recvPort: int) -> None:
        self.ipDest = ipDest
        self.sendPort = sendPort
        self.sockSend = socket(AF_INET, SOCK_DGRAM)
        self.sockRecv = socket(AF_INET, SOCK_DGRAM)
        self.sockRecv.bind(("", recvPort))

        self.stop_flag = False

    def transmission(self, app: str, ver: str, nick: str, msg: str) -> None:
        try:
            p = Packet(
                app,
                ver,
                nick,
                datetime.now().strftime("%H%M%S%f")[:-3],
                msg,
            )
            self.sockSend.sendto(p.bytes, (self.ipDest, self.sendPort))
        except Exception as e:
            raise e

    def receptionThread(self, f: Callable[[Packet, Tuple[str, int]], None]) -> Thread:
        t = Thread(target=self.reception, args=(f, lambda: self.stop_flag))
        t.daemon = True
        return t

    def reception(
        self, f: Callable[[Packet, Tuple[str, int], datetime], None], stop: Callable[[], bool]
    ) -> None:
        while True:
            if stop():
                break

            data, addr = self.sockRecv.recvfrom(130)
            time = datetime.now()
            data = Packet(data)

            f(data, addr, time)

        self.__closeSockRecv()

    def stopThread(self) -> None:
        self.stop_flag = True

    def closeSockSend(self) -> None:
        self.sockSend.close()

    def __closeSockRecv(self) -> None:
        self.sockRecv.close()
