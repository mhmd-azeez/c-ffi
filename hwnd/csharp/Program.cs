using System.Runtime.InteropServices;

string newTitle = "Hello from C#";
IntPtr paintWindow = FindWindow("MSPaintApp", null);

if (paintWindow != IntPtr.Zero)
{
    // Change the title of the Paint window
    SetWindowText(paintWindow, newTitle);

    Console.WriteLine($"Title of Paint window changed to: {newTitle}");
}
else
{
    Console.WriteLine("Paint window not found.");
}

[DllImport("user32.dll", SetLastError = true)]
static extern IntPtr FindWindow(string lpClassName, string? lpWindowName);

[DllImport("user32.dll", CharSet = CharSet.Unicode)]
static extern bool SetWindowText(IntPtr hWnd, string lpString);
