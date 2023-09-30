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

def change_notepad_title(new_title):
    # Find the Notepad window by its class name ("Notepad")
    notepad_window = FindWindowA(b"MSPaintApp", None)

    if notepad_window:
        # Change the title of the Notepad window
        success = SetWindowTextW(notepad_window, new_title)

        if success:
            print(f"Title of Notepad window changed to: {new_title}")
        else:
            print("Failed to change the title of the Notepad window.")
    else:
        print("Notepad window not found.")

if __name__ == "__main__":
    new_title = "Hello from Python!"
    change_notepad_title(new_title)
