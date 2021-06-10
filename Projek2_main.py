from wx import App
import mysql.connector
import Projek2

class login(Projek2.FrameLogin):
    def __init__(self, parent):
        Projek2.FrameLogin.__init__(self, parent)

    def btnOkLoginClick( self, event ):
        self.m_textCtrl3.GetValue()
        self.m_textCtrl4.GetValue()

        if self.m_textCtrl3.GetValue() == "Wahid" and self.m_textCtrl4.GetValue() == "wahid28":
            self.Close()
            app = App()
            frame = fitur(parent=None)
            frame.Show()
            app.MainLoop()
        else:
            print("Salah")
            self.Close()

class fitur(Projek2.FrameFitur):
    def __init__(self, parent):
        Projek2.FrameFitur.__init__(self, parent)

    def btnPinjamBukuClick( self, event ):
        self.Close()
        app = App()
        frame = listBuku(parent=None)
        frame.Show()
        app.MainLoop()

    def btnListBukuClick( self, event ):
        self.Close()
        app = App()
        frame = listBuku(parent=None)
        frame.Show()
        app.MainLoop()

    def btnLogoutClick( self, event ):
        app = App()
        frame = logout(parent=None)
        frame.Show()
        app.MainLoop()

class logout(Projek2.DialogLogout):
    def __init__(self, parent):
        Projek2.DialogLogout.__init__(self,parent)

    def btnYaLogoutClick( self, event ):
        self.Close()
        app = App()
        frame = listBuku(parent=None)
        frame.Close()
        frame = login(parent=None)
        frame.Show()
        app.MainLoop()

    def btnTidakLogoutClick( self, event ):
        self.Close()
        # app = App()
        # frame = listBuku(parent=None)
        # frame.Close()
        # app.MainLoop()

class listBuku(Projek2.FramePemilihanBuku):
    def __init__(self, parent):
        Projek2.FramePemilihanBuku.__init__(self,parent)



app = App()
frame = login(parent=None)
frame.Show()
app.MainLoop()