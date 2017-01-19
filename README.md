# HappyChirp
chrome extension that tweets the link you are looking at if you are happy (used Microsoft cognitive services emotion API to analyze images taken by webcam)

<b> What to install:</b> make sure you have python installed, cv2, and flask
<b> How to run: </b> start the server by cd'ing into your directory and typing "python app.py", make sure to load your extension code here: chrome://extensions/, click reload each time you make any changes to the code (you should see your exstension appear on the top right), click on the extension icon and you are all set :) (right click on the icon and click insepect popup, then click the console to debug if needed)
<b> What keys to generate: </b> you need to generate keys to use Twitter's https://apps.twitter.com/ and Microsoft's https://www.microsoft.com/cognitive-services/ APIs

Steps:
<b> 1) </b> First created  a simple chrome extension by creating my manifest.json file and popup.html
<b> 2) </b> Then created the popup.js where I played around with chrome's and twitter's apis -- try being able to tweeet the link you are looking at before moving forward
<b> 3) </b> Create a python script that activates your webcam and takes your image
<b> 4) </b> Create another python script that is able to use Microsoft's cognitive services emotion API to return an emotion to you based on an image saved on your computer
<b> 5) </b> build a python web server by creating a flask application 
<b> 6) </b> add code in your popup.js file that fetches the return value of your python script 
<b> 7) </b> if python script returns True, tweet the link, if it return's False, update the user that the link was not tweeted
<b> 8) </b> you will have to install browserify to bundle all the code required to tweet with your js code, check out browserify.org, update the popup.html accordingly
