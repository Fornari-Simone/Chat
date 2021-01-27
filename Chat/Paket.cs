using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;

namespace Chat
{
    class Paket : UdpClient
    {
        byte[] app;
        byte[] ver;
        byte[] nick;
        byte[] time;
        byte[] msg;

        public Paket(string app, string ver, string nick, string time, string msg)
        {
            if (Encoding.ASCII.GetBytes(app).Length > 3)
                throw new ExceedException("The max size of 'app' is 3");
            if (Encoding.ASCII.GetBytes(ver).Length > 2)
                throw new ExceedException("The max size of 'ver' is 2");
            if (Encoding.ASCII.GetBytes(time).Length > 9)
                throw new ExceedException("The max size of 'app' is 3");

            this.app = Encoding.ASCII.GetBytes(app);
            this.ver = Encoding.ASCII.GetBytes(ver);
            this.nick = Encoding.ASCII.GetBytes(nick);
            this.time = Encoding.ASCII.GetBytes(time);
            this.msg = Encoding.ASCII.GetBytes(msg);
        }

        public void Send()
        {
            this.Send();
        }
    }
}
