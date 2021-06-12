# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FrameLogin
###########################################################################

class FrameLogin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		btnOkLogin = wx.StdDialogButtonSizer()
		self.btnOkLoginOK = wx.Button( self, wx.ID_OK )
		btnOkLogin.AddButton( self.btnOkLoginOK )
		btnOkLogin.Realize();

		fgSizer1.Add( btnOkLogin, 1, wx.EXPAND, 5 )


		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnOkLoginOK.Bind( wx.EVT_BUTTON, self.btnOkLoginClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnOkLoginClick( self, event ):
		event.Skip()


###########################################################################
## Class FrameFitur
###########################################################################

class FrameFitur ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 837,683 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Perpus Indah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"[Nama Peminjam]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.btnPinjamBuku = wx.Button( self, wx.ID_ANY, u"Meminjam Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnPinjamBuku, 0, wx.ALL, 5 )

		self.btnListBuku = wx.Button( self, wx.ID_ANY, u"List Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnListBuku, 0, wx.ALL, 5 )

		self.btnLogout = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnLogout, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnPinjamBuku.Bind( wx.EVT_BUTTON, self.btnPinjamBukuClick )
		self.btnListBuku.Bind( wx.EVT_BUTTON, self.btnListBukuClick )
		self.btnLogout.Bind( wx.EVT_BUTTON, self.btnLogoutClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnPinjamBukuClick( self, event ):
		event.Skip()

	def btnListBukuClick( self, event ):
		event.Skip()

	def btnLogoutClick( self, event ):
		event.Skip()


###########################################################################
## Class FramePemilihanBuku
###########################################################################

class FramePemilihanBuku ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 781,692 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Perpus Indah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"List Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.m_grid1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FramePemilihanBukuAdmin
###########################################################################

class FramePemilihanBukuAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 781,692 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Perpus Indah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"List Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.m_grid1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class FramePemilihanBukuAdmin
###########################################################################

class FramePemilihanBukuAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 781,692 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Perpus Indah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"List Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.m_grid1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class DialogKonfirmasiPeminjamanBuku
###########################################################################

class DialogKonfirmasiPeminjamanBuku ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Apakah anda yakin untuk meminjam buku [Nama Buku]?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer4.Add( self.m_staticText10, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.btnYaPinjam = wx.Button( self, wx.ID_ANY, u"Ya", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnYaPinjam, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.btnTidakPinjam = wx.Button( self, wx.ID_ANY, u"Tidak", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnTidakPinjam, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnYaPinjam.Bind( wx.EVT_BUTTON, self.btnYaPinjamClick )
		self.btnTidakPinjam.Bind( wx.EVT_BUTTON, self.btnTidakPinjamClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnYaPinjamClick( self, event ):
		event.Skip()

	def btnTidakPinjamClick( self, event ):
		event.Skip()


###########################################################################
## Class DialogLogout
###########################################################################

class DialogLogout ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Yakin ingin keluar?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer6.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.btnYaLogout = wx.Button( self, wx.ID_ANY, u"Ya", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btnYaLogout, 0, wx.ALL, 5 )

		self.btnTidakLogout = wx.Button( self, wx.ID_ANY, u"Tidak", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btnTidakLogout, 0, wx.ALL, 5 )


		bSizer6.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()
		bSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnYaLogout.Bind( wx.EVT_BUTTON, self.btnYaLogoutClick )
		self.btnTidakLogout.Bind( wx.EVT_BUTTON, self.btnTidakLogoutClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnYaLogoutClick( self, event ):
		event.Skip()

	def btnTidakLogoutClick( self, event ):
		event.Skip()

###########################################################################
## Class DialogError
###########################################################################

class DialogError ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Error", pos = wx.DefaultPosition, size = wx.Size( 409,222 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"Password dan NIM anda salah", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		bSizer8.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"Tekan OK untuk kembali ke halaman login", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		bSizer8.Add( self.m_textCtrl5, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.btnOkError = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btnOkError, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnOkError.Bind( wx.EVT_BUTTON, self.btnOkErrorClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnOkErrorClick( self, event ):
		event.Skip()

