# Smart File Organizer (Python Project)

An automatic file organizer that can organize all files in a specified folder (e.g., your Downloads folder) into subfolders (e.g., Images, Videos, Docs, Music, <Others>). 

---

## Features

* Automatically detects file types based on file extensions
* Moves files to the following directories:

  * Images/
  * Videos/
  * Docs/
  * Music/
  * Others/
* Logs the time of organization
* Takes folder path input from user
* Safe and cross-platform using pathlib.

---

## Modules Used

* os - for OS-level operations
* shutil - for moving files
* pathlib - for modern path handling
* datetime - for adding timestamps while logging.

--- 

## How to Run

To run the Smart File Organizer, go to your terminal and type:

```bash
python file_organizer.py
```

You will then be prompted to provide a folder path by entering:

```
Enter absolute path of folder: C:/Users/YourName/Downloads
```
Your output will look like this:

```
Moved: photo.jpg -> Images/
Moved: resume.pdf -> Docs/
Moved: song.mp3 -> Music/
..
..
..
Organized the files on 2025-07-05 at 22:30:14
``` 

---

## Example Structure After Running Project 

```
Downloads/
├── Images/
│     └── photo.jpg
├── Docs/
│     └── resume.pdf
├── Music/
│     └── song.mp3
├── Others/
│     └── somefile.xyz
```

---

## Future Improvements 

* Add GUI using PyQt5.
* Add recursive folder scanning (searching subfolders).
* Detect and sort another file element (types) - code files, fonts, archives.
* Save all actions to text file, in addition to logging.
* Turn into command line tool using argparse.

---

## Author

Made with ❤️ by 3shu Kottapalli (Python Bootcamp Day 1 Project).

---

## License

All rights reserved and published code is available for public use, modification or for change. Just provide accreditation, if published 🙌