from typing import Any, Tuple
import customtkinter as ctk


class MenuBar(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.frame1=None
        self.button1=ctk.CTkButton(self,text="Create Quize",hover=True,hover_color='blue')
        self.button1.pack(side='left',padx=12,pady=12,anchor='nw')
class ContentFrame(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str] = "transparent", fg_color: str | Tuple[str] | None = None, border_color: str | Tuple[str] | None = None, background_corner_colors: Tuple[str | Tuple[str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, **kwargs)
        
class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str] | None = None, **kwargs):
        super().__init__( **kwargs)
        self.menu_frame=MenuBar(master=self)
        self.menu_frame.pack(fill='y',side='left',padx=20,pady=20)
        self.content_frame=ContentFrame(master=self)
        self.content_frame.pack(fill='both',padx=20,pady=20,expand=True)
        # self.pack_propagate(False)
app=App()
   
app.mainloop()
