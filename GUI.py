from tkinter import *
from tkinter import ttk


class GUIPolygonCreator(Tk):
    def run(self):
        self.title("Polygon Creator")

        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        layers_array = ["Blue","Red"]
        Poly_points = StringVar()

        self.left = StringVar()
        left_entry = ttk.Entry(mainframe, textvariable=self.left)
        left_entry.grid(column=2, row=2, sticky=(W, E))

        self.right = StringVar()
        right_entry = ttk.Entry(mainframe, textvariable=self.right)
        right_entry.grid(column=2, row=3 , sticky=(W, E))

        self.width = StringVar()
        width_entry = ttk.Entry(mainframe, textvariable=self.width)
        width_entry.grid(column=2, row=4, sticky=(W, E))

        self.bottom = StringVar()
        bottom_entry = ttk.Entry(mainframe, textvariable=self.bottom)
        bottom_entry.grid(column=5, row=2, sticky=(W, E))

        self.top = StringVar()
        top_entry = ttk.Entry(mainframe, textvariable=self.top)
        top_entry.grid(column=5, row=3, sticky=(W, E))

        self.height = StringVar()
        height_entry = ttk.Entry(mainframe, textvariable=self.height)
        height_entry.grid(column=5, row=4, sticky=(W, E))



        ComboBoxLayers = ttk.Combobox(mainframe,values=layers_array)
        ComboBoxLayers.grid(column=2, row=1, sticky=W)
        ComboBoxLayers.current(0)


        ttk.Label(mainframe, text="Layer").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="Left").grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text="Right").grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text="Width").grid(column=1, row=4, sticky=W)
        ttk.Label(mainframe, text="Bottom").grid(column=4, row=2, sticky=W)
        ttk.Label(mainframe, text="Top").grid(column=4, row=3, sticky=W)
        ttk.Label(mainframe, text="Height").grid(column=4, row=4, sticky=W)


        self.calculate_btn = ttk.Button(mainframe, text="Calculate", command=self.calculate_rectangle_dimensions)
        self.calculate_btn.grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text="Crate polygon", command=self.create_polygon_via_dimensions).grid(column=2, row=5, sticky=E)

        ttk.Label(mainframe, text="Or enter points:").grid(column=1, row=6, columnspan=2,  sticky=W)
        poly_entry = ttk.Entry(mainframe,  textvariable=Poly_points)
        poly_entry.grid(column=2, row=6, sticky=(W, E))
        ttk.Button(mainframe, text="Crate polygon", command=self.create_polygon_via_points).grid(column=1, row=7, sticky=W)
        self.info_label = ttk.Label(mainframe, text="")
        self.info_label.grid(column=1, row=8, columnspan=4,  sticky=W)


        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


        poly_entry.focus()
        self.bind('<Return>', self.calculate_rectangle_dimensions)
        self.bind_all("<Button-1>", lambda e: self.get_current_focus(e))

        self.mainloop()

    def get_current_focus(self,event):
        if type(self.focus_get()) == type(self.calculate_btn):
            self.info_label['text'] = ""

    def calculate_rectangle_dimensions(self):
        bounds,size = self.get_bounds_and_size()
        if bounds is not None and size is not None:
            self.left.set(str(bounds[0]))
            self.right.set(str(bounds[2]))
            self.top.set(str(bounds[1]))
            self.bottom.set(str(bounds[3]))
            self.width.set(str(size[0]))
            self.height.set(str(size[1]))


    def get_bounds_and_size(self):
        # must be:  bounds = [left,top,right,bottom]
        bounds = [None, None, None, None]
        # must be:  size = [width,height]
        size = [None, None]
        try:
            if (0 < len(self.left.get()) and 0 < len(self.right.get())):
                bounds[0] = float(self.left.get())
                bounds[2] = float(self.right.get())
                size[0] = bounds[2] - bounds[0]
                if 0 >= size[0]: raise Exception
            elif (0 < len(self.width.get()) and 0 < len(self.right.get())):
                size[0] = float(self.width.get())
                if 0 >= size[0]: raise Exception
                bounds[2] = float(self.right.get())
                bounds[0] = bounds[2] - size[0]
            elif (0 < len(self.width.get()) and 0 < len(self.left.get())):
                size[0] = float(self.width.get())
                if 0 >= size[0]: raise Exception
                bounds[0] = float(self.left.get())
                bounds[0] = bounds[0] + size[0]
            else:
                raise Exception

            if (0 < len(self.top.get()) and 0 < len(self.bottom.get())):
                bounds[1] = float(self.top.get())
                bounds[3] = float(self.bottom.get())
                size[1] = bounds[3] - bounds[1]
                if 0 >= size[1]: raise Exception
            elif (0 < len(self.height.get()) and 0 < len(self.top.get())):
                size[1] = float(self.height.get())
                if 0 >= size[1]: raise Exception
                bounds[1] = float(self.top.get())
                bounds[3] = bounds[1] + size[1]
            elif (0 < len(self.height.get()) and 0 < len(self.bottom.get())):
                size[1] = float(self.height.get())
                if 0 >= size[1]: raise Exception
                bounds[3] = float(self.bottom.get())
                bounds[1] = bounds[3] - size[1]
            else:
                raise Exception
        except:
            self.info_label['text'] = "Not enough info or something was entered incorrect"
            return None,None
        return bounds,size

    def create_polygon_via_points(self):
        pass

    def create_polygon_via_dimensions(self):
        pass

#GUI = GUIWindow()


GUI = GUIPolygonCreator()
GUI.run()
