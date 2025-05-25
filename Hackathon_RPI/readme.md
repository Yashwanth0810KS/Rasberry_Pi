# 🖼️ Image Transformer Tool

Hey there! This is a simple desktop app I built to have fun with images — upload your pics, apply cool filters and effects, preview changes live, and save the results. It’s powered by Python’s **Tkinter** for the GUI and **OpenCV** for all the image processing magic.

---

## What It Does

- Upload images (.jpg, .png, and more)
- Apply transformations like:
  - **Grayscale** (black & white)
  - **Blur effects:** Gaussian Blur, Median Blur
  - **Edge detection:** Sobel, Canny
  - **Thresholding** (convert to black & white based on a threshold)
  - **Rotate & Resize** (adjust angle and size)
  - **Erode & Dilate** (morphological operations)
  - **Brightness & Contrast adjustment** (with handy sliders)
  - **Flip images** horizontally or vertically
- **Live preview** so you see changes instantly
- **Save** your edited image whenever you want
- **Reset** anytime to start fresh

---

## How to Get It Running

1. Make sure you have **Python 3+** installed.

2. Install required packages using:

   ```bash
   pip install opencv-python pillow



3. Run the App
    ```bash
    python main.py


-----------------------------------------------------------------------------------------------------------------
How to Use:

1. Click Upload Image to select a photo.

2. Pick a transformation from the dropdown.

3. Enter extra parameters if needed (e.g., rotation angle, blur kernel size).

4. Click Apply to see the effect.

5. Use sliders for brightness and contrast adjustments — they appear when those options are selected.

6. Click Reset to undo changes and start over.

7. Save your final image anytime with the Save Image button.
-----------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------

Tips:

--> For blur filters, use odd numbers like 3, 5, or 7 for kernel size.

--> Resize expects two scale factors separated by a comma, e.g., 0.5,0.5 to shrink width and height by half.

--> Brightness slider ranges from -100 (darker) to 100 (brighter).

--> Contrast slider goes from 0.1 (less contrast) up to 3 (more contrast).

-----------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------

Files in This Project:

--> main.py — Launches the app.

--> gui.py — Handles the user interface and interactions.

--> logic.py — Contains image processing functions using OpenCV.

-----------------------------------------------------------------------------------------------------------------

If you find bugs or have cool ideas, feel free to reach out!

Cheers 🎉