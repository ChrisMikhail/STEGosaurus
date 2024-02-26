import customtkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image
import os
from orchestration import decode_image, encode_image

# Default settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def change_appearance_mode_event(new_appearance_mode: str):
    """Changes appearance"""
    customtkinter.set_appearance_mode(new_appearance_mode)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Basic configuration
        self.title("STEGosaurus - LSB Image Steganography Tool")
        self.geometry(f"{1100}x{580}")

        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Loads images for intro page
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "example")
        self.first_image_path = os.path.join(image_path, "steg.png")
        self.second_image_path = os.path.join(image_path, "sus_steg.png")
        self.first_test_image = customtkinter.CTkImage(Image.open(self.first_image_path), size=(402, 301))
        self.second_test_image = customtkinter.CTkImage(Image.open(self.second_image_path), size=(402, 301))

        # Title frame
        self.title_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.title_frame.grid(row=0, column=1, padx=20, sticky="ew")
        self.grid_rowconfigure(0, weight=10)
        self.title_label = customtkinter.CTkLabel(self.title_frame, text="Introduction",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.pack(side="top", fill="both", expand=True)

        # Content Frame
        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.grid(row=1, column=1, padx=20, sticky="nsew")
        self.grid_rowconfigure(1, weight=150)

        # Original image (steg.png)
        self.home_frame_first_image_label = customtkinter.CTkLabel(self.content_frame, text="",
                                                                   image=self.first_test_image)
        self.home_frame_first_image_label.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_first_image_label.place(x=15, y=100)

        # steg.png image label
        original_title_label = customtkinter.CTkLabel(self.content_frame, text="Original Image",
                                                      font=customtkinter.CTkFont(size=16, weight="bold"))
        original_title_label.grid(row=2, column=0, padx=20, pady=5)
        original_title_label.place(x=15, y=70)

        # Second image (sus_steg.png)
        self.home_frame_second_image_label = customtkinter.CTkLabel(self.content_frame, text="",
                                                                    image=self.second_test_image)
        self.home_frame_second_image_label.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_second_image_label.place(x=465, y=100)

        # sus_steg.png image label
        secret_title_label = customtkinter.CTkLabel(self.content_frame, text="Contains a Hidden Message",
                                                    font=customtkinter.CTkFont(size=16, weight="bold"))
        secret_title_label.grid(row=2, column=0, padx=20, pady=5)
        secret_title_label.place(x=465, y=70)

        # Decode button
        decode_button = customtkinter.CTkButton(self.content_frame, text="Decode",
                                                font=customtkinter.CTkFont(size=14),
                                                command=self.update_message_label)
        decode_button.pack(side="bottom", pady=15)

        # Bottom frame
        self.bottom_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.grid(row=2, column=1, padx=20, sticky="ew")
        self.grid_rowconfigure(2, weight=10)

        # Displays message
        self.message_label = customtkinter.CTkLabel(self.bottom_frame,
                                                    text="The image contains the message: ",
                                                    font=customtkinter.CTkFont(size=16, weight="bold"))
        self.message_label.pack(side="left", fill="both")

        # Sidebar
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="STEGosaurus",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Intro button
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,
                                                        text="Introduction", command=self.intro_clicked)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        # Encode button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.encode_clicked,
                                                        text="Encode")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # Decode button
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.decode_clicked,
                                                        text="Decode")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # Appearance dropdown
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["System", "Dark", "Light"],
                                                                       command=change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=6, column=0, padx=20, pady=(10, 55))

    def openfile(self, yaml=False):
        """Opens file explorer and returns the file path and name"""
        if yaml:
            self.yaml_path = filedialog.askopenfilename()
            self.yaml_name = os.path.basename(self.yaml_path)
        else:
            self.file_path = filedialog.askopenfilename()
            self.file_name = os.path.basename(self.file_path)

    def submit_encode_clicked(self):
        """Encode page submission function"""
        new_file_name = f"sus_{self.file_name}"
        yaml_name = f"secrets_for_{new_file_name[:-4]}.yaml"
        message = self.entry.get().replace("\n", " ")
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        if downloads_folder is not None and self.file_name is not None:
            path_to_new_image = os.path.join(downloads_folder, new_file_name)
            path_to_new_yaml = os.path.join(downloads_folder, yaml_name)
            image_fits = encode_image(self.file_path, path_to_new_image, message, path_to_new_yaml)
            if not image_fits:
                self.middle_label.configure(text="Your message is too long!")
            else:
                self.middle_label.configure(text="Download was successful!")

    def update_message_label(self, yaml_path="example/secrets.yaml", new_path="example/sus_steg.png"):
        """Updates label text"""
        decoded_message = decode_image(yaml_path, new_path)

        self.message_label.configure(text=f"The image contains the message: {decoded_message}")
        try:
            self.decode_message_label.configure(text=f"The image contains the message: {decoded_message}")
        except AttributeError:
            pass

    def update_file_label(self, yaml=False):
        """Updates which file has been selected by user"""
        if yaml:
            self.yaml_name_text_label.configure(text=f"Selected Yaml: {self.yaml_name}")
        self.image_name_text_label.configure(text=f"Selected Image: {self.file_name}")

    def encode_clicked(self):
        """Adds extra UI components for the encode section"""
        if self.title_label.cget("text") == "Decode":
            self.decode_middle_frame.destroy()
            self.decode_bottom_frame.grid_remove()
            self.decode_message_label.grid_remove()
        if self.title_label.cget("text") != "Encode":
            self.title_label.configure(text="Encode")
            self.bottom_frame.grid_forget()
            self.content_frame.grid_forget()

            # Entry for encoding message
            self.entry = customtkinter.CTkEntry(self, placeholder_text="Message to be encoded")
            self.entry.grid(row=2, column=1, padx=(15, 15), sticky="nsew")

            # Submission button for encoding
            self.main_button_1 = customtkinter.CTkButton(
                master=self,
                fg_color="transparent",
                border_width=2,
                text_color=("gray10", "#DCE4EE"),
                text="Submit & Download",
                command=self.submit_encode_clicked
            )
            self.main_button_1.grid(row=3, column=1, padx=(15, 15), pady=(5, 15), sticky="nsew")

            # New frame for the box in the middle
            self.middle_box_frame = customtkinter.CTkFrame(self)
            self.middle_box_frame.grid(row=1, column=1, padx=(20, 20), pady=(5, 15),
                                       sticky="nsew")  # Adjusted row placement
            self.middle_box_frame.columnconfigure(0, weight=1)
            self.middle_box_frame.rowconfigure(0, weight=1)

            # Button inside the middle box
            middle_button = customtkinter.CTkButton(
                master=self.middle_box_frame,
                fg_color="transparent",
                border_width=2,
                text_color=("gray10", "#DCE4EE"),
                text="Insert Image",
                command=lambda: [self.openfile(), self.update_file_label()]
            )
            middle_button.grid(row=0, column=0, padx=10, pady=10)

            self.image_name_text_label = customtkinter.CTkLabel(self.middle_box_frame, text="Selected Image: ",
                                                                font=customtkinter.CTkFont(size=16, weight="bold"))
            self.image_name_text_label.grid(row=2, column=0, padx=20, pady=5)
            self.image_name_text_label.place(rely=.94, x=4)

            self.middle_label = customtkinter.CTkLabel(self.middle_box_frame, text="",
                                                       font=customtkinter.CTkFont(size=16, weight="bold"))
            self.middle_label.grid(row=2, column=0, padx=20, pady=5)
            self.middle_label.place(rely=.54, relx=.38)

            # Configure grid weights
            self.columnconfigure(1, weight=1)
            self.rowconfigure(2, weight=1)
            self.rowconfigure(3, weight=1)
        else:
            pass

    def decode_clicked(self):
        """Adds extra UI components for the decode section"""
        if self.title_label.cget("text") != "Decode":
            try:
                self.decode_middle_frame = customtkinter.CTkFrame(self)
                self.decode_middle_frame.grid(row=1, column=1, padx=20, sticky="nsew")
                self.grid_rowconfigure(1, weight=150)
                self.title_label.configure(text="Decode")

                # Select Image
                self.decode_middle_button_image = customtkinter.CTkButton(
                    master=self.decode_middle_frame,
                    fg_color="transparent",
                    border_width=2,
                    text_color=("gray10", "#DCE4EE"),
                    text="Insert Image",
                    command=lambda: [self.openfile(), self.update_file_label()])
                self.decode_middle_button_image.grid(row=0, column=0, padx=10, pady=10)
                self.decode_middle_button_image.place(relx=.1, rely=.5)

                # Select YAML
                self.decode_middle_button_yaml = customtkinter.CTkButton(
                    master=self.decode_middle_frame,
                    fg_color="transparent",
                    border_width=2,
                    text_color=("gray10", "#DCE4EE"),
                    text="Insert Secrets",
                    command=lambda: [self.openfile(yaml=True), self.update_file_label(yaml=True)])
                self.decode_middle_button_yaml.grid(row=0, column=0, padx=10, pady=10)
                self.decode_middle_button_yaml.place(relx=.75, rely=.5)

                # Submit button
                self.decode_middle_button_submit = customtkinter.CTkButton(
                    master=self.decode_middle_frame,
                    border_width=2,
                    text_color=("gray10", "#DCE4EE"),
                    text="Submit",
                    command=lambda: [self.update_message_label(self.yaml_path, self.file_path)])
                self.decode_middle_button_submit.grid(row=0, column=0, padx=10, pady=10)
                self.decode_middle_button_submit.place(relx=.43, rely=.8)

                # Label for image
                self.image_name_text_label = customtkinter.CTkLabel(self.decode_middle_frame, text="Selected Image: ",
                                                                    font=customtkinter.CTkFont(size=16,
                                                                                               weight="bold"))
                self.image_name_text_label.grid(row=2, column=0, padx=20, pady=5)
                self.image_name_text_label.place(rely=.89, x=4)

                # Label for yaml
                self.yaml_name_text_label = customtkinter.CTkLabel(self.decode_middle_frame, text="Selected Yaml: ",
                                                                   font=customtkinter.CTkFont(size=16,
                                                                                              weight="bold"))
                self.yaml_name_text_label.grid(row=2, column=0, padx=20, pady=5)
                self.yaml_name_text_label.place(rely=.94, x=4)

                # Scrollable bottom frame
                self.decode_bottom_frame = customtkinter.CTkScrollableFrame(self, fg_color="transparent", height=25,
                                                                            width=200, orientation="horizontal")
                self.decode_bottom_frame.grid(row=2, column=1, padx=20, sticky="ew")
                self.grid_rowconfigure(2, weight=10)

                # Message label
                self.decode_message_label = customtkinter.CTkLabel(self.decode_bottom_frame,
                                                                   text="The image contains the message: ",
                                                                   font=customtkinter.CTkFont(size=16,
                                                                                              weight="bold"))
                self.decode_message_label.pack(side="left", fill="both")
                self.grid_rowconfigure(2, weight=10)
                self.content_frame.grid_forget()
                self.middle_box_frame.destroy()
                self.entry.destroy()
                self.main_button_1.destroy()

            except AttributeError:
                pass

    def intro_clicked(self):
        """Removes all extra components for the home page"""
        try:
            if self.title_label.cget("text") == "Encode":
                self.middle_box_frame.destroy()
                self.entry.destroy()
                self.main_button_1.destroy()
                self.middle_label.destroy()
                self.image_name_text_label.destroy()
            elif self.title_label.cget("text") == "Decode":
                self.grid_rowconfigure(1, weight=150)
                self.decode_middle_frame.destroy()
                self.decode_bottom_frame.grid_remove()
                self.decode_message_label.grid_remove()

            self.title_label.configure(text="Introduction")
            self.message_label.configure(text="The image contains the message: ")
            self.bottom_frame.grid(row=2, column=1, padx=20, sticky="ew")
            self.content_frame.grid(row=1, column=1, padx=20, sticky="nsew")
            self.grid_rowconfigure(2, weight=10)

        except AttributeError:
            pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
