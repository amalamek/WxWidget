import wx
import sqlite3
import xml.etree.ElementTree as ET

class ClientWidget(wx.Frame):
    def __init__(self, parent, title):
        super(ClientWidget, self).__init__(parent, title=title, size=(800, 400))

        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        id_label = wx.StaticText(panel, label='ID:')
        self.id_input = wx.TextCtrl(panel)
        nom_label = wx.StaticText(panel, label='Nom:')
        self.nom_input = wx.TextCtrl(panel)
        email_label = wx.StaticText(panel, label='Email:')
        self.email_input = wx.TextCtrl(panel)

        vbox.Add(id_label, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.id_input, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(nom_label, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.nom_input, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(email_label, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.email_input, flag=wx.EXPAND | wx.ALL, border=5)

        add_button_db = wx.Button(panel, label='Ajouter au DB (SQLite3)')
        add_button_xml = wx.Button(panel, label='Sauvegarder en XML')
        delete_button_db = wx.Button(panel, label='Supprimer de DB')
        delete_button_xml = wx.Button(panel, label='Supprimer de XML')

        add_button_db.Bind(wx.EVT_BUTTON, self.add_client_to_db)
        add_button_xml.Bind(wx.EVT_BUTTON, self.save_to_xml)
        delete_button_db.Bind(wx.EVT_BUTTON, self.delete_selected_client_db)
        delete_button_xml.Bind(wx.EVT_BUTTON, self.delete_client_by_id_xml)

        vbox.Add(add_button_db, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(add_button_xml, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(delete_button_db, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(delete_button_xml, flag=wx.EXPAND | wx.ALL, border=5)

        self.tree = wx.TreeCtrl(panel)
        vbox.Add(self.tree, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        self.conn = sqlite3.connect('gestion.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS client (id INTEGER PRIMARY KEY, nom TEXT, email TEXT)")
        self.conn.commit()

        self.update_tree_from_db()

        panel.SetSizer(vbox)
        self.Show()

    # Other methods remain unchanged

    def closeEvent(self, event):
        self.conn.close()


if __name__ == '__main__':
    app = wx.App()
    window = ClientWidget(None, title='Gestion Client')
    app.MainLoop()
