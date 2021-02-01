from typing import Tuple, Union


class Packet:
    def __init__(
        self, *args: Union[Tuple[str, str, str, str, str], Tuple[bytes]]
    ) -> None:
        if len(args) == 5 and type(args) == Tuple[str, str, str, str, str]:
            if len(args[0]) > 3:
                raise Exception("APP field is too long. Max is 3 characters")
            else:
                self.app = args[0].rjust(3)

            if len(args[1]) > 2:
                raise Exception("VER field is too long. Max is 2 charaters")
            else:
                self.ver = args[1].rjust(2)

            if len(args[2]) > 16:
                raise Exception("NICK field is too long. Max is 16 charaters")
            else:
                self.nick = args[2].rjust(16)

            if len(args[3]) > 9:
                raise Exception("TIME field is too long. Max is 9 charaters")
            else:
                self.time = args[3].rjust(9)

            if len(args[4]) > 100:
                raise Exception("MSG field is too long. Max is 100 charaters")
            else:
                self.msg = args[4].rjust(100)

            self.bytes = bytes(self.app + self.ver + self.nick + self.time + self.msg)
        elif len(args) == 1 and type(args) == Tuple[bytes]:
            if len(args[0]) != 130:
                raise Exception("Invalid Buffer. Size must be 130 bytes")
            else:
                self.bytes = args[0]

                self.app = str(args[0][0:3], encoding="utf-8")
                self.ver = str(args[0][3:5], encoding="utf-8")
                self.nick = str(args[0][5:21], encoding="utf-8")
                self.time = str(args[0][21:30], encoding="utf-8")
                self.msg = str(args[0][30:130], encoding="utf-8")
