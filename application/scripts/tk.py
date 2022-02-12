Tkinter.Button(subframe, text = "Browse", command = self.loadtemplate, width = 10).pack()

   def loadtemplate(self):
        filename = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.tplate")
                                                             ,("HTML files", "*.html;*.htm")
                                                             ,("All files", "*.*") ))
        if filename:
            try:
                self.settings["template"].set(filename)
            except:
                tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename)