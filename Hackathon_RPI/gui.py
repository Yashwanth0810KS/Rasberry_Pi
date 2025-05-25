import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import cv2
import logic

class ImageTransformerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🖼️ Image Transformer Tool")
        self.root.geometry("700x750")
        self.root.configure(bg="#f0f0f0")

        self.image_cv = None
        self.original = None

        self.canvas = tk.Label(self.root, bg="#ccc", relief="sunken", bd=2)
        self.canvas.pack(pady=10, padx=10, fill="both", expand=True)

        # Frame for controls
        control_frame = tk.Frame(self.root, bg="#f0f0f0")
        control_frame.pack(pady=10)

        # Top Buttons
        tk.Button(control_frame, text="Upload Image", command=self.load_image, bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
        tk.Button(control_frame, text="Reset", command=self.reset_image, bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=5)
        tk.Button(control_frame, text="Save Image", command=self.save_image, bg="#f44336", fg="white", width=15).grid(row=0, column=2, padx=5)

        # Transformation dropdown
        self.transform_menu = ttk.Combobox(control_frame, values=[
            "Grayscale", "Gaussian Blur", "Median Blur", "Sobel Edge", "Canny Edge",
            "Threshold", "Rotate", "Resize", "Erode", "Dilate",
            "Brightness", "Contrast", "Flip Horizontal", "Flip Vertical"
        ], width=35)
        self.transform_menu.grid(row=1, column=0, columnspan=2, pady=10)
        self.transform_menu.current(0)

        tk.Button(control_frame, text="Apply", command=self.apply_transform, bg="#673AB7", fg="white", width=15).grid(row=1, column=2)

        # Parameter entry or slider
        self.param_label = tk.Label(control_frame, text="Optional Parameter (e.g., angle, size)", bg="#f0f0f0")
        self.param_label.grid(row=2, column=0, columnspan=3, pady=5)

        self.param_entry = tk.Entry(control_frame, width=50)
        self.param_entry.grid(row=3, column=0, columnspan=3, pady=5)

        # Brightness & Contrast sliders
        self.brightness_slider = tk.Scale(control_frame, from_=-100, to=100, label="Brightness", orient="horizontal", length=300, command=self.apply_brightness)
        self.contrast_slider = tk.Scale(control_frame, from_=0.1, to=3.0, resolution=0.1, label="Contrast", orient="horizontal", length=300, command=self.apply_contrast)

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if not path:
            return
        self.image_cv = cv2.imread(path)
        self.original = self.image_cv.copy()
        self.show_image(self.image_cv)
        self.reset_sliders()

    def reset_image(self):
        if self.original is not None:
            self.image_cv = self.original.copy()
            self.show_image(self.image_cv)
            self.reset_sliders()

    def save_image(self):
        if self.image_cv is not None:
            path = filedialog.asksaveasfilename(defaultextension=".png")
            if path:
                cv2.imwrite(path, self.image_cv)
                messagebox.showinfo("Saved", f"Image saved to {path}")

    def show_image(self, img):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(rgb)
        img_pil = img_pil.resize((500, 500))
        img_tk = ImageTk.PhotoImage(img_pil)
        self.canvas.configure(image=img_tk)
        self.canvas.image = img_tk

    def reset_sliders(self):
        self.brightness_slider.grid_forget()
        self.contrast_slider.grid_forget()

    def apply_transform(self):
        if self.image_cv is None:
            return

        func = self.transform_menu.get()
        param = self.param_entry.get().strip()
        img = self.image_cv

        try:
            if func == "Grayscale":
                img = logic.to_grayscale(img)

            elif func == "Gaussian Blur":
                k = int(param) if param.isdigit() and int(param) % 2 == 1 else 5
                img = logic.gaussian_blur(img, k)

            elif func == "Median Blur":
                k = int(param) if param.isdigit() and int(param) % 2 == 1 else 5
                img = logic.median_blur(img, k)

            elif func == "Sobel Edge":
                img = logic.sobel_edge(img)

            elif func == "Canny Edge":
                try:
                    t1, t2 = map(int, param.split(',')) if ',' in param else (100, 200)
                except:
                    t1, t2 = 100, 200
                img = logic.canny_edge(img, t1, t2)

            elif func == "Threshold":
                thresh = int(param) if param.isdigit() else 127
                img = logic.threshold_binary(img, thresh)

            elif func == "Rotate":
                try:
                    angle = float(param)
                except:
                    angle = 90.0
                img = logic.rotate(img, angle)

            elif func == "Resize":
                try:
                    w_scale, h_scale = map(float, param.split(',')) if ',' in param else (0.5, 0.5)
                except:
                    w_scale, h_scale = 0.5, 0.5
                img = logic.resize(img, w_scale, h_scale)

            elif func == "Erode":
                k = int(param) if param.isdigit() else 3
                img = logic.erode(img, k)

            elif func == "Dilate":
                k = int(param) if param.isdigit() else 3
                img = logic.dilate(img, k)

            elif func == "Brightness":
                self.reset_sliders()
                self.brightness_slider.set(0)
                self.brightness_slider.grid(row=4, column=0, columnspan=3, pady=10)
                return

            elif func == "Contrast":
                self.reset_sliders()
                self.contrast_slider.set(1.0)
                self.contrast_slider.grid(row=4, column=0, columnspan=3, pady=10)
                return

            elif func == "Flip Horizontal":
                img = logic.flip(img, 'horizontal')

            elif func == "Flip Vertical":
                img = logic.flip(img, 'vertical')

            if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

            self.image_cv = img
            self.show_image(img)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_brightness(self, val):
        if self.original is not None:
            try:
                self.image_cv = logic.adjust_brightness(self.original.copy(), int(val))
                self.show_image(self.image_cv)
            except Exception as e:
                messagebox.showerror("Brightness Error", str(e))

    def apply_contrast(self, val):
        if self.original is not None:
            try:
                self.image_cv = logic.adjust_contrast(self.original.copy(), float(val))
                self.show_image(self.image_cv)
            except Exception as e:
                messagebox.showerror("Contrast Error", str(e))
