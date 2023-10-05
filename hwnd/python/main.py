import ctypes
import ctypes.wintypes

# Define necessary Windows API functions and types
user32 = ctypes.windll.user32

# FindWindowA function
FindWindowA = user32.FindWindowA
FindWindowA.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
FindWindowA.restype = ctypes.wintypes.HWND

# SetWindowTextW function
SetWindowTextW = user32.SetWindowTextW
SetWindowTextW.argtypes = [ctypes.wintypes.HWND, ctypes.c_wchar_p]
SetWindowTextW.restype = ctypes.c_bool

def change_paint_title(new_title):
    # Find the Paint window by its class name ("Paint")
    paint_window = FindWindowA(b"MSPaintApp", None)

    if paint_window:
        # Change the title of the Paint window
        success = SetWindowTextW(paint_window, new_title)

        if success:
            print(f"Title of Paint window changed to: {new_title}")
        else:
            print("Failed to change the title of the Paint window.")
    else:
        print("Paint window not found.")

if __name__ == "__main__":
    new_title = "Hello from Python!"
    change_paint_title(new_title)
