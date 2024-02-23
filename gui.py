import customtkinter
from tkinter import filedialog
from PIL import Image
import os

# Default settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def change_appearance_mode_event(new_appearance_mode: str):
    """Changes appearance"""
    customtkinter.set_appearance_mode(new_appearance_mode)


def openfile():
    """Opens file explorer"""
    return filedialog.askopenfilename()


def change_scaling_event(new_scaling: str):
    """Changes GUI scale"""
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.main_button_1 = None
        self.entry = None
        self.title("STEGosaurus - LSB Image Steganography Tool")
        self.geometry(f"{1100}x{580}")

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
        self.first_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "steg.png")),
                                                       size=(402, 301))
        second_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
        self.second_test_image = customtkinter.CTkImage(Image.open(os.path.join(second_image_path, "sus_steg.png")),
                                                        size=(402, 301))

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        def encode_clicked():
            """Adds extra UI components for the encode section"""
            self.entry = customtkinter.CTkEntry(self, placeholder_text="Message to be encoded")
            self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

            self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,
                                                         text_color=("gray10", "#DCE4EE"), text="Submit")
            self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        def remove_elements():
            """Removes all extra components for the home page"""
            # Create the top frame
            self.top_frame = customtkinter.CTkFrame(self, fg_color="transparent")
            self.top_frame.grid(row=0, column=1, padx=20, sticky="ew")
            self.grid_rowconfigure(0, weight=10)  # Top frame

            # Create the label in the top frame
            introduction_label = customtkinter.CTkLabel(self.top_frame, text="Introduction",
                                                        font=customtkinter.CTkFont(size=20, weight="bold"))
            introduction_label.pack(side="top", fill="both", expand=True)

            # Create the middle content frame
            self.content_frame = customtkinter.CTkFrame(self)
            self.content_frame.grid(row=1, column=1, padx=20, sticky="nsew")
            self.grid_rowconfigure(1, weight=150)  # Middle content frame

            # Create the first image label with title "Original"
            self.home_frame_first_image_label = customtkinter.CTkLabel(self.content_frame, text="",
                                                                       image=self.first_test_image)
            self.home_frame_first_image_label.grid(row=2, column=0, padx=20, pady=10)
            self.home_frame_first_image_label.place(x=15, y=100)

            # Create the title label for the first image
            original_title_label = customtkinter.CTkLabel(self.content_frame, text="Original Image",
                                                          font=customtkinter.CTkFont(size=16, weight="bold"))
            original_title_label.grid(row=2, column=0, padx=20, pady=5)
            original_title_label.place(x=15, y=70)

            # Create the second image label with title "Secret"
            self.home_frame_second_image_label = customtkinter.CTkLabel(self.content_frame, text="",
                                                                        image=self.second_test_image)
            self.home_frame_second_image_label.grid(row=2, column=0, padx=20, pady=10)
            self.home_frame_second_image_label.place(x=465, y=100)

            # Create the title label for the second image
            secret_title_label = customtkinter.CTkLabel(self.content_frame, text="Contains a Hidden Message",
                                                        font=customtkinter.CTkFont(size=16, weight="bold"))
            secret_title_label.grid(row=2, column=0, padx=20, pady=5)
            secret_title_label.place(x=465, y=70)

            # Create the "Decode" button in the middle content frame
            decode_button = customtkinter.CTkButton(self.content_frame, text="Decode",
                                                    font=customtkinter.CTkFont(size=14))
            decode_button.pack(side="bottom", pady=15)

            # Create the bottom frame
            self.bottom_frame = customtkinter.CTkFrame(self, fg_color="transparent")
            self.bottom_frame.grid(row=2, column=1, padx=20, sticky="ew")
            self.grid_rowconfigure(2, weight=10)  # Bottom frame

            # Create the label in the bottom frame with left alignment
            message_label_text = "The image contained the message: "
            message_label = customtkinter.CTkLabel(self.bottom_frame, text=message_label_text,
                                                   font=customtkinter.CTkFont(size=16, weight="bold"))
            message_label.pack(side="left", fill="both")

            try:
                self.entry.destroy()
                self.main_button_1.destroy()
            except AttributeError:
                pass

        remove_elements()

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="STEGosaurus",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,
                                                        text="Home", command=remove_elements)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=encode_clicked,
                                                        text="Encode")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=openfile,
                                                        text="Decode")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["System", "Dark", "Light"],
                                                                       command=change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


if __name__ == "__main__":
    app = App()
    app.mainloop()
