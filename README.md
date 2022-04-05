Text to Melody

The program will convert a text to a melody and save it in a standard MIDI file, playable on any computer and importable into any MIDI enabled DAW, scoring or music production software.

The Windows executable needs no installation, just run the program from any folder.
The Python script requires Python installed and the MIDIUtil library.
After downloading the latest Python version from http://www.python.org and installing it, add the Python directory to your PATH environment variable and install the MIDIUtil library through the following command:

pip install MIDIUtil

The program will only convert lowercase and uppercase letters, ingnoring spaces and all other punctuation signs, numbers and any non-letter characters.
Write or paste text into the text window and click “Generate Melody”. You will be asked to choose a folder and a filename for your MIDI file. Retrieve the file and play it to hear the resulting melody. You can then import the file into a scoring program or a DAW for music composition and production.

Version 1.1.0
New in this version:

- GUI added
- can save MIDI file to any folder with any filename
- new and improved algorithm
