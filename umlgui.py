import tkinter as tk
import uml


class UmlEntity(tk.Frame, uml.Entity):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(master, *args, **kwargs)
        uml.Entity.__init__(*args, **kwargs)


class UmlRelationship(tk.Frame, uml.Relationship):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(master, *args, **kwargs)
        uml.Relationship.__init__(*args, **kwargs)
