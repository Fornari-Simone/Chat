namespace Chat
{
    partial class Form1
    {
        /// <summary>
        /// Variabile di progettazione necessaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Pulire le risorse in uso.
        /// </summary>
        /// <param name="disposing">ha valore true se le risorse gestite devono essere eliminate, false in caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Codice generato da Progettazione Windows Form

        /// <summary>
        /// Metodo necessario per il supporto della finestra di progettazione. Non modificare
        /// il contenuto del metodo con l'editor di codice.
        /// </summary>
        private void InitializeComponent()
        {
            this.Msg = new System.Windows.Forms.RichTextBox();
            this.nick = new System.Windows.Forms.TextBox();
            this.Send = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // Msg
            // 
            this.Msg.Location = new System.Drawing.Point(12, 38);
            this.Msg.MaxLength = 100;
            this.Msg.Name = "Msg";
            this.Msg.Size = new System.Drawing.Size(272, 244);
            this.Msg.TabIndex = 0;
            this.Msg.Text = "";
            // 
            // nick
            // 
            this.nick.Location = new System.Drawing.Point(12, 12);
            this.nick.MaxLength = 16;
            this.nick.Name = "nick";
            this.nick.Size = new System.Drawing.Size(141, 20);
            this.nick.TabIndex = 1;
            // 
            // Send
            // 
            this.Send.Location = new System.Drawing.Point(101, 288);
            this.Send.Name = "Send";
            this.Send.Size = new System.Drawing.Size(75, 23);
            this.Send.TabIndex = 2;
            this.Send.Text = "Send";
            this.Send.UseVisualStyleBackColor = true;
            this.Send.Click += new System.EventHandler(this.Send_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Send);
            this.Controls.Add(this.nick);
            this.Controls.Add(this.Msg);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox Msg;
        private System.Windows.Forms.TextBox nick;
        private System.Windows.Forms.Button Send;
    }
}

