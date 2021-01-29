using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chat
{
    class Packet
    {
        private byte[] app;
        private byte[] ver;
        private byte[] nick;
        private byte[] time;
        private byte[] msg;

        public static int length = 130;

        public Packet(string app, string ver, string nick, string time, string msg)
        {
            if ( StringToByte(app).Length > 3 )
                throw new ExceedException("The max size of 'app' is 3");
            if ( StringToByte(ver).Length > 2 )
                throw new ExceedException("The max size of 'ver' is 2");
            if ( StringToByte(nick).Length > 16 )
                throw new ExceedException("The max size of 'nick' is 16");
            if ( StringToByte(time).Length > 9 )
                throw new ExceedException("The max size of 'time' is 9");
            if ( StringToByte(msg).Length > 100 )
                throw new ExceedException("The max size of 'msg' is 100");

            this.app = StringToByte(app);
            this.ver = StringToByte(ver);
            this.nick = StringToByte(nick);
            this.time = StringToByte(time);
            this.msg = StringToByte(msg);
        }

        public Packet(byte[] p)
        {
            if (p.Length > Packet.length) throw new ExceedException("Invalid Packet");
            this.app = p.Take(3).ToArray();
            this.ver = p.Skip(3).Take(2).ToArray();
            this.nick = p.Skip(5).Take(16).ToArray();
            this.time = p.Skip(21).Take(9).ToArray();
            this.msg = p.Skip(30).ToArray();
        }

        public static byte[] StringToByte(string value) => Encoding.ASCII.GetBytes(value);
        public static string ByteToString(byte[] value) => Encoding.ASCII.GetString(value);

        public byte[] Generate() {
            return this.app.Concat(this.ver.Concat(this.nick.Concat(this.time.Concat(this.msg)))).ToArray();
        }

        public override string ToString()
        {
            return ByteToString(this.Generate());
        }
    }
}
