# Song Metadata Maker/Retriever
It's developed under the "eyed3" library and is fully compliant to it. For any changes to the code, read the documentation (https://eyed3.readthedocs.io/en/latest/)
The main function is to extract and write metadata from file names to ID1/2/3 data on .mp3 files.
### Dependencies
All that is needed is the internal os library and the external eyed3 library which you can get by typing in your terminal

    pip install eyed3


#### Usage
**NOTE: The file format should be: "*Artist - Song Name.mp3*", the program is prone to mistakes in case the file format is not correct** 
If you want to apply metadata writing to a folder, the .py needs to be placed in the parent folder. When prompted you need to enter the child folder name that you want to apply this to (yes, it's case sensitive), while if wanted to write to a single file, the .py file needs to be in the same directory.
When the file name is prompted, it should be inputed without ".mp3".


This code is maintained and created by me. Feel free to make push and merge requests to improve the code. I will try to review code changes asap.

**THANK YOU FOR WATCHING**
