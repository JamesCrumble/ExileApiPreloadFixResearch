using System.Text;
using System.Diagnostics;
using System.Runtime.InteropServices;

const int PROCESS_WM_READ = 0x0010;//?
[DllImport("kernel32.dll")]
static extern IntPtr OpenProcess(int dwDesiredAccess, bool bInheritHandle, int dwProcessId);

[DllImport("kernel32.dll")]
static extern bool ReadProcessMemory(int hProcess,
  Int64 lpBaseAddress, byte[] lpBuffer, int dwSize, ref int lpNumberOfBytesRead);


Process process = Process.GetProcessesByName("PathOfExile")[0];

IntPtr processHandle = OpenProcess(PROCESS_WM_READ, false, process.Id);
IntPtr startOffset = process.MainModule.BaseAddress;
IntPtr endOffset = IntPtr.Add(startOffset, process.MainModule.ModuleMemorySize);
int bytesRead = 0;


byte[] buffer = new byte[4096];


for (int i = 0; i < (long)endOffset - (long)startOffset; i++)
{
    bytesRead = 0;
    buffer = new byte[4096];


    if (!ReadProcessMemory((int)processHandle, IntPtr.Add(startOffset, i).ToInt64(), buffer, buffer.Length, ref bytesRead))
    {
        Console.WriteLine("false");
    }


    //string s = Encoding.Default.GetString(buffer);
    Console.OpenStandardOutput(buffer);
    //if (s.Contains("MyString"))
    //{
    //    Console.WriteLine("Yay!");
    //}
    //Console.WriteLine(s);
    //Console.WriteLine(fromByteArray(buffer));
    //Console.ReadLine();
}
Console.WriteLine("Finished");
Console.WriteLine("Memory:" + process.MainModule.ModuleMemorySize.ToString());
Console.ReadLine();