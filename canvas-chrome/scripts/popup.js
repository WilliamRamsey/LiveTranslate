// listen for data from background.js with text content
// open popup window
// display translated text

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        console.log(request)
    }
);
