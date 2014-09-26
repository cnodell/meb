#Meb

Meb is a simple app that allows you to browse and edit linked text files. I like to take notes in Markdown and save them as individual files. It worked well but I missed being able to link between "pages" (really files) like you can with a wiki. I could not find another program that did just this and so I made Meb.

It is a very small app with few features and poor code quality. However, it does what I want it to do. Hopefully, I will be willing to take the time to improve the code in the future. I can also imagine a variety of improvements. Things like rendering Markdown to look a bit prettier, and making first use easier.

## Installing Meb

* Meb uses Python 2.7 and Tkinter. Once these are installed you can run meb.py with python
* Meb has only been tested on Linux but might work on Windows. If not, only small changes would be needed
* On Linux systems Meb.py can be made executable and run like other executables

## Using Meb

* For Meb to work you need to create a base text file
* The base text file should end in ".md"
* This file can be blank
* All linked to pages must reside in the same directory as this base file
* When Meb is opened for the first time you should open open your base test file straight away
* Once a file is opened you can edit it by clicking the edit button
* once you have written your text, click save and your file will be saved and displayed
* Links use the [[File Name]] format
* The File Name is the name if the file you want to link to minus the ".md" extension
* If you click on the link for a file that does not exist, Meb will create that file
* the created file will be given the .md extension automatically and be in the same directory as your original file
* Clicking the back button will take you to the last page you were on
* The Delete button deletes the currently displayed file and returns you to the last file you had opened
* Links do not function in edit mode
* you can not edit text in display mode
* When opening Meb, Meb will try to open the last page you opened using the open button
* Meb creates the “.meb” in your home directory and stores files there that it uses to remember things

## Walk Through

* Create a new directory named "Notes"
* Create a blank text file named "Main.md" in that directory
* Open Meb
* Click the Open button in Meb
* Navigate to and open your empty “Main.md” file
* You will see a blank page
* Click the edit button
* Enter some text. Somewhere withing that text add the following "[[Page 2]]" minus the quotes
* Click Save
* Note that [[Page 2]] is now a link
* Click on the [[Page 2]] link
* You will see a blank page
* Click Edit
* Enter some text
* Click save
* You have text here but no link. This is OK.
* Click the back button
* You should now see the Main page
* Look into your "Notes Directory" - You should see a “Main.md” file and an “Page 2.md” file
* Go back to Meb
* Click Edit while on the Main page
* Add a new link "[[Page 3]]" minus the quotes
* Click save
* Click on the [[Page 3]] link
* You will see a blank page
* Click the edit button
* add some text including a [[Main]] link
* You now want to go to "Page 2.md" but there is no link and you do not want such a link on this page
* So, click the "Open" button, navigate to the page you do want, and open it
* That is it!
