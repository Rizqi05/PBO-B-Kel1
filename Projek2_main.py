from wx import App
import dbconfig
import Projek2
import wx

name = ''

class DialogError(Projek2.DialogError):
    def __init__(self, parent):
        super().__init__(parent)

    def btnOkErrorClick(self, event):
        self.Close()

class FramePemilihanBukuAdmin(Projek2.FramePemilihanBukuAdmin):
    def __init__(self, parent):
        super().__init__(parent)

class Login(Projek2.FrameLogin):
    def __init__(self, parent):
        Projek2.FrameLogin.__init__(self, parent)

    def btnOkLoginClick( self, event ):
        global name

        email = self.m_textCtrl3.GetValue()
        password = self.m_textCtrl4.GetValue()

        emailPass = dbconfig.getEmailPass(email)

        name = dbconfig.getName(email)[0]

        if emailPass != None and password == emailPass[1] and emailPass[2] != 1:
            self.Close()
            frame = Fitur(None, name)
            frame.Show()
        elif emailPass != None and password == emailPass[1] and emailPass[2] != 0:
            self.Close()
            frame = FramePemilihanBukuAdmin(None)
            frame.Show()
        else:
            frame = DialogError(None)
            frame.Show()

class Fitur(Projek2.FrameFitur):
    def __init__(self, parent, name):
        Projek2.FrameFitur.__init__(self, parent)
        self.m_staticText9.SetValue(name)

    def btnPinjamBukuClick( self, event ):
        self.Close()
        frame = ListBuku(parent=None)
        frame.Show()

    def btnListBukuClick( self, event ):
        self.Close()
        frame = ListBuku(parent=None)
        frame.Show()

    def btnLogoutClick( self, event ):
        frame = Logout(None)
        frame.Show()
        self.Close()

class Logout(Projek2.DialogLogout):
    def __init__(self, parent):
        Projek2.DialogLogout.__init__(self,parent)

    def btnYaLogoutClick( self, event ):
        self.Close()
        frame = ListBuku(parent=None)
        frame.Close()
        frame = Login(parent=None)
        frame.Show()

    def btnTidakLogoutClick( self, event ):
        self.Close()
        frame = Fitur(None, name)
        frame.Show()

class ListBuku(Projek2.FramePemilihanBuku):
    def __init__(self, parent):
        Projek2.FramePemilihanBuku.__init__(self,parent)

        # self.m_staticText9.SetLabel("Perpustakaan Daerah")
        font = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.m_staticText9.SetFont(font)
        # self..Add(wx.ALIGN_CENTER)

<<<<<<< HEAD
        result = dbconfig.readDataBuku()       
        row = 0

        for i in result:
            if row >= self.m_grid1.GetNumberRows():
                self.m_grid1.AppendRows()
                self.m_grid1.SetCellValue(row,0,str(i[0]))
                self.m_grid1.SetCellValue(row,1,i[1])
                self.m_grid1.SetCellValue(row,2,i[2])
                self.m_grid1.SetCellValue(row,3,i[3])
                self.m_grid1.SetCellValue(row,4,str(i[4]))
                self.m_grid1.AutoSize()
                row += 1
            else:
                self.m_grid1.SetCellValue(row,0,str(i[0]))
                self.m_grid1.SetCellValue(row,1,i[1])
                self.m_grid1.SetCellValue(row,2,i[2])
                self.m_grid1.SetCellValue(row,3,i[3])
                self.m_grid1.SetCellValue(row,4,str(i[4]))
                self.m_grid1.AutoSize()
                row += 1

    def btnPinjamBukuClick( self, event ):
        self.Close()
        app = App()
        frame = bukuAdmin(parent=None)
        frame.Show()
        app.MainLoop()

    def btnKembaliBukuClick( self, event ):
        self.Close()
        app = App()
        frame = fitur(parent=None)
        frame.Show()
        app.MainLoop()

class konfirmasiPinjam(Projek2.DialogKonfirmasiPeminjamanBuku):
    def __init__(self, parent):
        Projek2.DialogKonfirmasiPeminjamanBuku.__init__(self,parent)

    def btnYaPinjamClick( self, event ):
        id_buku = self.isiIdBuku.Value()
        # Ambil dari database

    def btnTidakPinjamClick( self, event ):
        self.Close()
        app = App()
        frame = listBuku(parent=None)
        frame.Show()
        app.MainLoop()

                

class bukuAdmin(Projek2.FramePemilihanBuku):
    def __init__(self, parent):
        Projek2.FramePemilihanBuku.__init__(self,parent)

        result = dbconfig.readDataBuku()       
        row = 0

        for i in result:
            if row >= self.m_grid1.GetNumberRows():
                self.m_grid1.AppendRows()
                self.m_grid1.SetCellValue(row,0,str(i[0]))
                self.m_grid1.SetCellValue(row,1,i[1])
                self.m_grid1.SetCellValue(row,2,i[2])
                self.m_grid1.SetCellValue(row,3,i[3])
                self.m_grid1.SetCellValue(row,4,str(i[4]))
                self.m_grid1.AutoSize()
                row += 1
            else:
                self.m_grid1.SetCellValue(row,0,str(i[0]))
                self.m_grid1.SetCellValue(row,1,i[1])
                self.m_grid1.SetCellValue(row,2,i[2])
                self.m_grid1.SetCellValue(row,3,i[3])
                self.m_grid1.SetCellValue(row,4,str(i[4]))
                self.m_grid1.AutoSize()
                row += 1

    def btnKembaliBukuAdminClick(self, event):
        self.Close()
        app = App()
        frame = bukuAdmin(parent=None)
        frame.Show()
        app.MainLoop()

app = App()
frame = login(parent=None)
=======
        result = dbconfig.getAllBook()

        # row = 0

        # self.m_grid1.AppendCols()
        # for i in result:
        #     if row >= self.m_grid1.GetNumberRows():
        #         self.m_grid1.AppendRows()
        #         self.m_grid1.SetCellValue(row,0,str(i[0]))
        #         self.m_grid1.SetCellValue(row,1,i[1])
        #         self.m_grid1.SetCellValue(row,2,i[2])
        #         self.m_grid1.SetCellValue(row,3,i[3])
        #         self.m_grid1.SetCellValue(row,4,str(i[4]))
        #         self.m_grid1.SetCellValue(row,5,str(i[5]))
        #         self.m_grid1.AutoSize()
        #         row += 1
        #     else:
        #         self.m_grid1.SetCellValue(row,0,str(i[0]))
        #         self.m_grid1.SetCellValue(row,1,i[1])
        #         self.m_grid1.SetCellValue(row,2,i[2])
        #         self.m_grid1.SetCellValue(row,3,i[3])
        #         self.m_grid1.SetCellValue(row,4,str(i[4]))
        #         self.m_grid1.SetCellValue(row,5,str(i[5]))
        #         self.m_grid1.AutoSize()
        #         row += 1

app = App()
frame = Login(parent=None)
>>>>>>> 86daa3f8d72db01fc1ce4d303c52ab285d4ed157
frame.Show()
app.MainLoop()