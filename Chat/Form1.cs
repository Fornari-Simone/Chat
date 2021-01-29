using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Chat
{
    public partial class Form1 : Form
    {
        CustomUDP c;
        public Form1()
        {
            InitializeComponent();
        }

        private void Send_Click(object sender, EventArgs e)
        {
            this.c.Send("CHA", "01", "0123456789123456", "123456789", "sas");
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            this.c = new CustomUDP("192.168.192.11", 6000);
        }

        private void btnReceive_Click(object sender, EventArgs e)
        {
            Console.WriteLine(this.c.Receive());
        }
    }
}
