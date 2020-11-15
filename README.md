# piano_tiles_bot
Uses python and image recognition to click on black tiles in the piano tiles game. 
We need the bot to recognize if a pixel is black and click on it. 
We hover over each column in the game, and obtain and store their x value. 
We take the y value of a pixel somewhere between the top and middle of the play area. 
Top is better for when the speed of the game increases.  
So we now have the values of 4 pixels the bot has to constantly chcek, and click on it if they are black.
pyautogui is used to get the rgb value and position of a particular pixel. Rgb value for black is 0,0,0.
pyautogui is also used for mouse clicks. 

