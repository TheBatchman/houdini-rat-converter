# Houdini .RAT converter
Pyside environment for converting an entire folder with texture files to Mantra's native RAT file

Saves the .rat files next to the original files

**Only Linux & Windows tested**
&nbsp;

# Usage
1. Open Houdini
2. Right click on a empty spot in the shelf
3. New Tool
4. Copy the contents of "houdini-rat-converter.py" in the tab "Script"
5. Accept

# Todo (by priority)
* ~~Fix windows version~~
* Fix mac version (file structure untested)
* ~~Check if .rat version already exists and not overwrite and skip~~
* ~~Move checking OS and folder structure determination into a function~~
* Give feedback when no files to convert are found
* Make user able to select between entire folder or select images
* Let user select recursive or not
* Let user select filetype (e.g. jpg, tiff, tga, exr) to convert from (one or multiple)
* A way to show progress
* A way to show when done
