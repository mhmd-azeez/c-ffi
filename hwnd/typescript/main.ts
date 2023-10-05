const lib = Deno.dlopen(
  "user32.dll",
  {
    FindWindowA: {
      parameters: ["buffer", "buffer"],
      result: "pointer",
    },
    SetWindowTextW: {
      parameters: ["pointer", "buffer"],
      result: "bool",
    },
  },
);

function changePaintTitle(newTitle: string) {
  // Find the Paint window by its class name ("Paint")
  const paintWindow = lib.symbols.FindWindowA(new TextEncoder().encode("MSPaintApp\0"), null);

  if (paintWindow) {
    // Encode the new title in UTF-16
    const newTitleUtf16 = new Uint16Array((newTitle + "\0").split("").map((v) => v.charCodeAt(0)))
    // Change the title of the Paint window
    const success = lib.symbols.SetWindowTextW(paintWindow, newTitleUtf16);

    if (success) {
      console.log("Title of Paint window changed to:", newTitle);
    } else {
      console.log("Failed to change the title of the Paint window.");
    }
  } else {
    console.log("Paint window not found.");
  }
}

const newTitle = "Hello from TypeScript!";
changePaintTitle(newTitle);
