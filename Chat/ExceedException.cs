using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chat
{
    class ExceedException : Exception
    {
        public ExceedException() : base() { }
        public ExceedException(string msg) : base(msg) { }
    }
}
