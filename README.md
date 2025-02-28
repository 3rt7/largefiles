# largefiles
```
Print files or directories larger than specified size

Usage: ./main.py <path> <size>

<path> - search <path>
<size> - print files or folders larger than <size> (in Mb)

Written by Erfan zamani <erfanzm99@gmail.com>
```
The underlying logic is that it searches the given directory *recursively*, if the file in the currnt working directory is larger than size print it on the screen, if not add file size. If files' size adds up to the specified size also show the directory on the screen
