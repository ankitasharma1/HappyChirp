# HappyChirp
chrome extension that tweets the link you are looking at if you are happy (used Microsoft cognitive services emotion API to analyze images taken by webcam)

What to install: make sure you have python installed, cv2, and flask
How to run: start the server by cd'ing into your directory and typing "python app.py", make sure to load your extension code here: chrome://extensions/, click reload each time you make any changes to the code (you should see your exstension appear on the top right), click on the extension icon and you are all set :) (right click on the icon and click insepect popup, then click the console to debug if needed)
What keys to generate: you need to generate keys to use Twitter's https://apps.twitter.com/ and Microsoft's https://www.microsoft.com/cognitive-services/ APIs

Steps:
1) First created  a simple chrome extension by creating my manifest.json file and popup.html
2) Then created the popup.js where I played around with chrome's and twitter's apis -- try being able to tweeet the link you are looking at before moving forward
3) Create a python script that activates your webcam and takes your image
4) Create another python script that is able to use Microsoft's cognitive services emotion API to return an emotion to you based on an image saved on your computer
5) build a python web server by creating a flask application 
6) add code in your popup.js file that fetches the return value of your python script 
7) if python script returns True, tweet the link, if it return's False, update the user that the link was not tweeted
8) you will have to install browserify to bundle all the code required to tweet with your js code, check out browserify.org, update the popup.html accordingly
