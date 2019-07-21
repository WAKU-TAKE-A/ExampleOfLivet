# Example of "Livet" (for 64bit)

Example of "Livet" in IronPython script.  
The library of C# is used. Requires VisualStudio 2017 or higher.

## File

* "ExampleOfLivet.sln"
  * To install "LivetCask".
  * To generate "livet" package.

## Notes on execution

* Open "ExampleOfLivet.sln".
* Install "Microsoft.SDK.Expression.Blend" with NuGet.
* Install "LivetCask" with NuGet.
* Build.
* Copy the "x64/debug/livet" or "x64/release/livet" folder to IronPython's "Lib" folder.
* Environment variable "IRONPYTHON_HOME" is required. It is the installation location of IronPython.
* "example_main.py" and "example.exe" are example program.

```
from livet import *
import example_main

example_main.RunExample()
```
