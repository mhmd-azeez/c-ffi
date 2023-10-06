import 'dart:ffi';
import 'package:ffi/ffi.dart';

final user32 = DynamicLibrary.open('user32.dll');

// Windows API functions
final FindWindow = user32.lookupFunction<
    IntPtr Function(Pointer<Utf16> lpClassName, Pointer<Utf16> lpWindowName),
    int Function(Pointer<Utf16> lpClassName,
        Pointer<Utf16> lpWindowName)>("FindWindowW");
final SetWindowText = user32.lookupFunction<
    Int32 Function(IntPtr hWnd, Pointer<Utf16> lpString),
    int Function(int hWnd, Pointer<Utf16> lpString)>("SetWindowTextW");

void main() {
  final className = 'MSPaintApp';
  final classNamePtr = className.toNativeUtf16();

  // Find the MS Paint window by class name
  final paintWindow = FindWindow(classNamePtr, nullptr);

  if (paintWindow != 0) {
    print('MS Paint window found.');
    final newTitle = 'Hello from Dart!';
    final newTitlePtr = newTitle.toNativeUtf16();

    // Set the new title for MS Paint
    SetWindowText(paintWindow, newTitlePtr);
  } else {
    print('MS Paint window not found.');
  }

  // Clean up memory
  calloc.free(classNamePtr);
}
