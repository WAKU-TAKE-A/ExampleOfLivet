# Example of Livet (for 64bit)

Example of Livet in Ironpython script.  

## File

* `ExampleOfLivet.sln`
  * To install LivetCask.
  * To generate `livet` package.

## Notes on execution

* Open `ExampleOfLivet.sln`.
* Install LivetCask with NuGet.
* Build.
* Copy the `x64/debug/livet` or `x64/release/livet` folder to IronPython's `Lib` folder.
* What is needed is only the `__init__.py`, `Livet.dll`, `Microsoft.Expression.Interactions.dll` and `System.Windows.Interactivity.dll`.
* Environment variable 'IRONPYTHON_HOME' is required. It is the installation location of IronPython.
* `example_main.py` and `example.exe` are example program.

```
from livet import *
import example_main
```
