from wx import App
import dbconfig
import Projek2
import wx

class login(Projek2.FrameLogin):
    def __init__(self, parent):
        Projek2.FrameLogin.__init__(self, parent)

    def btnOkLoginClick( self, event ):
        email = self.m_textCtrl3.GetValue()
        password = self.m_textCtrl4.GetValue()

        emailPass = dbconfig.getEmailPass(email)

        if emailPass != None and password == emailPass[1]:
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

        self.m_staticText9.SetLabel("Perpustakaan Daerah")
        font = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.m_staticText9.SetFont(font)
        # self..Add(wx.ALIGN_CENTER)

        result = dbconfig.readDataBuku()       
        row = 0

        self.m_grid1.AppendCols()
        for i in result:
            if row >= self.m_grid1.GetNumberRows():
                self.m_grid1.AppendRows()
                self.m_grid1.SetCellValue(row,0,str(i[0]))
                self.m_grid1.SetCellValue(row,1,i[1])
                self.m_grid1.SetCellValue(row,2,i[2])
                self.m_grid1.SetCellValue(row,3,i[3])
                self.m_grid1.SetCellValue(row,4,str(i[4]))
                self.m_grid1.SetCellValue(row,5,str(i[5]))
                self.m_grid1.AutoSize()
                row += 1
            else:
                self.m_grid1.SetCellValue(row,0,str(i[0]))
                self.m_grid1.SetCellValue(row,1,i[1])
                self.m_grid1.SetCellValue(row,2,i[2])
                self.m_grid1.SetCellValue(row,3,i[3])
                self.m_grid1.SetCellValue(row,4,str(i[4]))
                self.m_grid1.SetCellValue(row,5,str(i[5]))
                self.m_grid1.AutoSize()
                row += 1



app = App()
frame = listBuku(parent=None)
frame.Show()
app.MainLoop()