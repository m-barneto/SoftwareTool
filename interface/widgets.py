import tkinter as tk
from PIL import Image, ImageTk

from modules.module import IModule
from utilities.config import OFF_SWITCH_PATH, ON_SWITCH_PATH


class CheckboxImage(tk.Label):
    def __init__(self, module: IModule = None, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.module = module

        # Load custom images for checked and unchecked states
        img = Image.open(ON_SWITCH_PATH)
        self.checked_icon = ImageTk.PhotoImage(img.resize((45, 45)))  # Replace with your checked image
        img = Image.open(OFF_SWITCH_PATH)
        self.unchecked_icon = ImageTk.PhotoImage(img.resize((45, 45)))  # Replace with your unchecked image

        self.state = False

        self.bind("<Button-1>", lambda event: self.click())

        self.config(
            image=self.unchecked_icon,
            background='#303030',
            padx=10,
            pady=0,
            compound='left',
            fg='white',
            justify="left",
            anchor="w"
        )

    def click(self):
        self.state = not self.state
        self.update_image()

    def update_image(self, new_state: bool = None):
        if new_state is not None:
            self.state = new_state

        img = self.unchecked_icon
        if self.state:
            img = self.checked_icon

        self.config(image=img)
        if self.state:
            self.module.log(str(self.state))

    def is_enabled(self):
        return self.state

    def run(self):
        if self.state:
            self.module.run()
