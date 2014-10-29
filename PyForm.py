# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Release manager", pos = wx.DefaultPosition, size = wx.Size( 606,403 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid5 = wx.grid.Grid( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid5.CreateGrid( 0, 2 )
		self.m_grid5.EnableEditing( True )
		self.m_grid5.EnableGridLines( True )
		self.m_grid5.EnableDragGridSize( False )
		self.m_grid5.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid5.SetColSize( 0, 76 )
		self.m_grid5.SetColSize( 1, 412 )
		self.m_grid5.EnableDragColMove( False )
		self.m_grid5.EnableDragColSize( True )
		self.m_grid5.SetColLabelSize( 30 )
		self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid5.EnableDragRowSize( True )
		self.m_grid5.SetRowLabelSize( 80 )
		self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.m_grid5, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer3 )
		self.m_panel4.Layout()
		bSizer3.Fit( self.m_panel4 )
		bSizer2.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetMaxSize( wx.Size( -1,40 ) )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_choice2Choices = [ u"Add", u"Removed", u"New", u"Fixed" ]
		self.m_choice2 = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		gSizer1.Add( self.m_choice2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gSizer1.Add( self.m_textCtrl3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( gSizer1 )
		self.m_panel5.Layout()
		gSizer1.Fit( self.m_panel5 )
		bSizer2.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetMaxSize( wx.Size( -1,40 ) )
		
		gSizer2 = wx.GridSizer( 0, 6, 0, 0 )
		
		
		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button12 = wx.Button( self.m_panel6, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button13 = wx.Button( self.m_panel6, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button14 = wx.Button( self.m_panel6, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel6.SetSizer( gSizer2 )
		self.m_panel6.Layout()
		gSizer2.Fit( self.m_panel6 )
		bSizer2.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE_APP, self.InitializeForm )
		self.m_textCtrl3.Bind( wx.EVT_TEXT_ENTER, self.OnTextEnterFunc )
		self.m_button12.Bind( wx.EVT_BUTTON, self.AddingNewLine )
		self.m_button13.Bind( wx.EVT_BUTTON, self.AcceptChanges )
		self.m_button14.Bind( wx.EVT_BUTTON, self.AbandonChanges )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def InitializeForm( self, event ):
		event.Skip()
	
	def OnTextEnterFunc( self, event ):
		event.Skip()
	
	def AddingNewLine( self, event ):
		event.Skip()
	
	def AcceptChanges( self, event ):
		event.Skip()
	
	def AbandonChanges( self, event ):
		event.Skip()
	

