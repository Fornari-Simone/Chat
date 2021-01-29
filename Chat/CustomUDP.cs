using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Net;

namespace Chat
{
    class CustomUDP
    {
        UdpClient client;

        public CustomUDP(string ip, int port)
        {
            this.client = new UdpClient(port);
            this.client.Connect(IPAddress.Parse(ip), port);
        }

        public void Send(string app, string ver, string nick, string time, string msg)
        {
            Packet p = new Packet(app, ver, nick, time, msg);

            this.client.Send(p.Generate(), Packet.length);
            Console.WriteLine(Packet.ByteToString(p.Generate()));
        }

        public Packet Receive()
        {
            IPEndPoint RemoteIpEndPoint = new IPEndPoint(IPAddress.Any, 0);
            Packet r = new Packet(this.client.Receive(ref RemoteIpEndPoint));

            return r;
        }
    }
}
