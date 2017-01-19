chrome.tabs.query({'active': true}, function (tabs) {
    document.getElementById('savedLinks').innerHTML = tabs[0].url;
    var data = tabs[0].url; 
    console.log(data);
    
    var Twit = require('twit');

    var T = new Twit({
      consumer_key:         'consumer_key',
      consumer_secret:      'consumer_secret',
      access_token:         'consumer_token',
      access_token_secret:  'access_token_secret',
      timeout_ms:           60*1000,  // optional HTTP request timeout to apply to all requests.
    })

    checkEmotion();

    function checkEmotion() {
      fetch('http://127.0.0.1:5000/').then(function(response){
        return response.json()
      }).then(function(raw) {
        var json = JSON.parse(raw);
        console.log(json);
        console.log(json['value']);
        // if true (microsoft emotion api detected you were happy!), tweet the link
        if(json['value']) {
          T.post('statuses/update', { status: data }, { mode: 'no-cors' }, function(err, data, response) {
              console.log(data)
          }) 
          // let the user know that the link was tweeted
          document.getElementById('afterTweet').innerHTML = ":) Successfully Tweeted!"
        } else {
          console.log("didn't tweet, because you were not happy")
          // let the user know the link was NOT tweeted
          document.getElementById('afterTweet').innerHTML = ":( Did not tweet"
        }
      })
    };  
});