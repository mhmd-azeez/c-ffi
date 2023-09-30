using System.Runtime.InteropServices;

const int OK = 0;

var connection = Open("../sample.db");

var schema = File.ReadAllText("../schema.sql");
Exec(connection, schema);
Exec(connection, "INSERT INTO logs (text) VALUES ('hello from C#!');");

Console.WriteLine($"Done.");

void Exec(IntPtr connection, string sql)
{
    var result = sqlite3_exec(connection, sql, IntPtr.Zero, IntPtr.Zero, out var errMsgPtr);
    if (result != OK)
    {
        var errMsg = Marshal.PtrToStringUTF8(errMsgPtr);
        throw new Exception($"Error Code: {result}. Message: {errMsg}");
    }
}

IntPtr Open(string path)
{
    var result = sqlite3_open(path, out var connection);

    if (result != OK)
    {
        var message = Marshal.PtrToStringUTF8(sqlite3_errmsg(connection));
        throw new Exception($"Failed to open DB: {message}");
    }
    else
    {
        return connection;
    }
}

// P/Invoke functions
[DllImport("sqlite3", CallingConvention = CallingConvention.Cdecl)]
static extern int sqlite3_open([MarshalAs(UnmanagedType.LPUTF8Str)] string filename, out IntPtr connection);

[DllImport("sqlite3", CallingConvention = CallingConvention.Cdecl)]
static extern int sqlite3_exec(IntPtr connection, [MarshalAs(UnmanagedType.LPUTF8Str)] string sql, IntPtr callback, IntPtr arg, out IntPtr errMsg);

[DllImport("sqlite3", CallingConvention = CallingConvention.Cdecl)]
static extern IntPtr sqlite3_errmsg(IntPtr db);
