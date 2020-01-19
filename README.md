# TranslationSwap
This is a tool in python that will swap the english to japanese between two csv files using the matching korean as a key. 

Problem - 
One csv file has Korean to English 
One file has Korean to Japanese 
Both files give an ID that a game uses to know what value to show on the game UI 
However, The ID in the English file does not match what the game uses - the ID in the Japanese file is correct. 
So we need to swap the Japanese with the English using the Korean as the main key. 

How to make it work - 

![variableinstructions](https://user-images.githubusercontent.com/15853331/72677641-ff176f80-3ae1-11ea-83fe-918d861df290.PNG)

Change the value of the variable to the csv or tsv file you want to translate 
File1name will be the file with the japanese you want to translate to english 
File2name will be the file with the English you want to use to replace the japanese. 

After that you just run the script and it will swap the values in the english file. 
