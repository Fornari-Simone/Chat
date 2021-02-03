from typing import Tuple, Union

APP_LEN = 3
VER_LEN = 2
NICK_LEN = 16
TIME_LEN = 9
MSG_LEN = 100
PKT_LEN = APP_LEN + VER_LEN + NICK_LEN + TIME_LEN + MSG_LEN


class Packet:
    def __init__(
        self, *args: Union[Tuple[str, str, str, str, str], Tuple[bytes]]
    ) -> None:
        self.app = ""
        self.ver = ""
        self.nick = ""
        self.time = ""
        self.msg = ""
        self.bytes = b""

        if len(args) == 5:
            self.app = Packet.__check(args[0], APP_LEN, "APP")
            self.ver = Packet.__check(args[1], VER_LEN, "VER")
            self.nick = Packet.__check(args[2], NICK_LEN, "NICK")
            self.time = Packet.__check(args[3], TIME_LEN, "TIME")

            if len(args[4]) < MSG_LEN:
                self.msg = args[4]
            else:
                raise Exception(f"MSG field is too long. Max is {MSG_LEN} characters")

            self.bytes = bytes(
                self.app + self.ver + self.nick + self.time + self.msg, "utf-8"
            )

        elif len(args) == 1:
            if len(args[0]) > PKT_LEN:
                raise Exception(f"Invalid Buffer. Max is {PKT_LEN} bytes")
            else:
                self.bytes = args[0]

                self.app = str(args[0][0:APP_LEN], encoding="utf-8")
                self.ver = str(args[0][APP_LEN : APP_LEN + VER_LEN], encoding="utf-8")
                self.nick = str(
                    args[0][APP_LEN + VER_LEN : APP_LEN + VER_LEN + NICK_LEN],
                    encoding="utf-8",
                )
                self.time = str(
                    args[0][
                        APP_LEN
                        + VER_LEN
                        + NICK_LEN : APP_LEN
                        + VER_LEN
                        + NICK_LEN
                        + TIME_LEN
                    ],
                    encoding="utf-8",
                )
                self.msg = str(
                    args[0][APP_LEN + VER_LEN + NICK_LEN + TIME_LEN :], encoding="utf-8"
                )
        else:
            raise Exception(
                "Invalid Arguments. Must be (str, str, str, str, str) or (bytes)"
            )

    def __check(str: str, length: int, lbl: str) -> str:
        if len(str) > length:
            raise Exception(f"{lbl} field is too long. Max is {length} characters")
        else:
            return str.rjust(length)