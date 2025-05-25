from tkinter import Tk
from gui import ImageTransformerGUI

def main():
    root = Tk()
    app = ImageTransformerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()