SIMPLE STUDY CARDS V1.0.1
Copyright 2026 Leo Feldman
———————————————————————————
Simple Study Cards is a basic studying tool that allows you to study free of cost and without distractions. It can be run either by running the Python script directly or by running the designated shortcut files for macOS®, Windows®, and Linux®. The newest release is v1.0.1, and it can be installed by downloading and extracting the .zip file, or by downloading all of the files individually in the uncompressed file folder.
--

1.1 - PREREQUISITES

In order to use the Simple Study Cards program, you must download the .zip file from the GitHub repository and extract it. macOS automatically extracts the .zip file when you double click it to your current location. To extract the .zip file on Windows and some Linux file managers, right click the .zip file and click 'Extract All' or 'Extract here'. You must extract the .zip file to a folder before you are able to run the program.

The Simple Study Cards program relies on an installation of the latest version of Python on your computer. To check that Python is on your computer, run the below commands.
- On macOS/Linux, open Terminal and run: python3 --version
- On Windows, open PowerShell and run: python --version
If the terminal displays that the Python command is not found, or the version of Python returned is not the latest, you must visit python.org and follow the instructions to download and install Python. To check that Python installed successfully, type the above commands for macOS/Linux or Windows.

1.2 - RUNNING THE PROGRAM

RUNNING THE PYTHON SCRIPT DIRECTLY
To run the Python script directly (universal), insure that the steps above have been completed. Open Terminal (macOS/Linux) or PowerShell (Windows), and navigate to the folder where the Python script is located using the cd command.
- Run: cd ~/[location]/SimpleStudyCards_v1.0.1/pythonscript
	- Replace [location] with the path to the SimpleStudyCards_v1.0.1 folder
	- For example, if the SimpleStudyCards_v1.0.1 is located in a folder called 'Programs' in the 'Downloads' folder, run: cd ~/Downloads/Programs/SimpleStudyCards_v1.0/pythonscript
If the cd command returns an error, ensure that a folder called 'pythonscript' is located in another folder called 'SimpleStudyCards_v1.0.1', and you have the file path correct. If the name(s) of the folder(s) are incorrect, change them to match the default names. If you cannot find the pythonscript and/or SimpleStudyCards_v1.0.1 folder(s), redownload the SimpleStudyCards_v1.0.1.zip file from the GitHub repository and extract it. Follow the above steps to navigate to the redownloaded folder. Once you are in the pythonscript folder, ensure the Python script is present.
- Run: ls
You should see a file called 'SimpleStudyCards_app.py' or 'SimpleStudyCards_app'. If you do not see this file, redownload the SimpleStudyCards_v1.0.1.zip file from the GitHub repository and extract it. Follow the above steps to navigate to the redownloaded folder. You should now see the Python script file.
- On macOS/Linux, run: python3 SimpleStudyCards_app.py
	- If this returns an error, try running: python3 SimpleStudyCards_app
- On Windows, run: python SimpleStudyCards_app.py
	- If this returns an error, try running: python SimpleStudyCards_app
If you tried all of the above commands and the terminal still returns an error, ensure you are typing the name of the Python script file correctly, and that the latest version of Python is installed by following the steps in the PREREQUISITES section. If you are and errors are still being returned, try redownloading the SimpleStudyCards_v1.0.1.zip file from the GitHub repository and extracting it. Navigate to the extracted folder using the above commands, and try again.

RUNNING THE APPLICATION USING THE SHORTCUT FILES ACROSS DIFFERENT PLATFORMS
To avoid having to run all of the commands above, shortcut files for macOS, Windows, and Linux have been included in the main SimpleStudyCards_v1.0.1 folder that run the Python script for you. Follow the steps below to use the shortcut files to run the Simple Study Cards program. Note that these shortcut files still require the latest version of Python to be installed to run the Simple Study Cards program.

MACOS:
The macOS Terminal requires that the .command file be made executable and that your user has permissions to run it. Additionally, since the .command file is not from the Mac App Store, macOS may block it from running. Run the commands below to allow it to run:
	- Open the Terminal
	- Type: chmod +x 
		- Leave a space after 'x', and do not press enter
	- Drag the 'for_macOS.command' file to the Terminal window
	- Press enter
	- Type: xattr -d com.apple.quarantine 
		- Leave a space after 'quarantine', and do not press enter
	- Drag the 'for_macOS.command' file to the Terminal window
	- Press enter
You may now double-click the 'for_macOS.command' file to run the Simple Study Cards program.

WINDOWS:
Because this file was downloaded from the internet, Windows SmartScreen may show a blue 'Windows protected your PC' popup. This is a standard security feature for all batch scripts (.bat) and custom apps.
	- Double-click the 'for_Windows.bat' file
	- On the blue popup, click 'More info'
	- Select 'Run anyway'
The Simple Study Cards program should now be running. If you did not encounter a blue popup, this is not a cause for concern, and the Python script should be running.

LINUX:
The file manager must be told to run the .sh file as a program.
	- Right-click the 'for_Linux.sh' file in a file manager
	- Select 'Run as Program'
The Simple Study Cards program should now be running.

2 - BASIC OPERATIONS

CREATING A SET
- At the option select menu, type '1' and press enter
- Enter the name of the new set, and press enter
- Enter the amount of terms in your set as a numeric value, and press enter
- Enter the name of each question when prompted, and press enter
- Enter the answer to each question, and press enter
- A message stating that the set was created successfully should be displayed, and you will be returned to the option selection menu

LOADING A SET
- At the option select menu, type '2' and press enter
- Type the name of the saved set you want to load, and press enter
- The amount of questions in the set will be displayed
- Enter your answer to each question and press enter
	- If you answered correctly, a message stating that you answered correctly will be displayed
	- If you answered incorrectly, a message stating that you answered incorrectly and the correct answer will be displayed
- Once you have completed all of the questions, your score will be displayed and you will have the opportunity to play the set again
	- You may play the set again by typing 'Y' and pressing enter, or
	- You may quit to the option select menu by typing 'N' and pressing enter

DELETING A SET (new feature added to v1.0.1)
- At the option select menu, type '3' and press enter
- Type the name of the saved set you want to delete, and press enter
- If you are sure you want to delete the saved set, type 'Y' and press enter
- If you would like to cancel the deletion and return to the option select menu, type 'N' and press enter
NOTE: Deleting a set using this method permanently erases the file containing the set data. This means that the set cannot be recovered once it is deleted. It is recommended that you load a set before deleting it so that you are sure you are deleting the correct set.
- If you selected 'Y', a message stating that your set has been deleted will be displayed, and you will be returned to the option select menu

QUITTING THE PROGRAM
- At the option select menu, type '4' and press enter
- The terminal window should display a 'process completed' message, or it may automatically close
- If the terminal window does not automatically close, you may close it manually
- If you would like to quit the program at a text input, press the CTRL and C keys
- The terminal should display a 'process interrupted' message, or it may automatically close
- If the terminal window does not automatically close, you may close it manually

3 - NOTES

The name of the set, the answers to questions, and Y/N prompts are not case-sensitive. This means that when the set is loaded and when questions are answered, the case of the inputs is not considered. For example, entering 'Abraham Lincoln' to a question is the same as entering 'Abraham lincoln' or 'abraham lincoln', and you can load a set called 'Presidents' by typing either 'Presidents' or 'presidents'. Entering 'y' is the same entering 'Y' and vice versa, with the same applying to 'n' and 'N'.

If any of the features do not work as intended and appear to be broken, your feedback is appreciated! Click on the 'Issues' tab on the GitHub repository and select 'New Issue' to leave feedback, give suggestions, or ask questions. Thank you so much for using this program, and by doing so you are fighting back against paywalls on educational software!

--

macOS is a trademark of Apple Inc., registered in the U.S. and other countries,
Windows is a registered trademark of Microsoft Corporation in the United States and/or other countries
