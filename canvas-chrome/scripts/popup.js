// listen for data from background.js with text content
// open popup window
// display translated text

function updatePopup() {
    chrome.storage.sync.get(['translated_text'], function (data) {
        console.log(data['translated_text'])
        document.getElementById("translation-text").innerText = data['translated_text'];
    });
}

document.addEventListener('DOMContentLoaded', updatePopup);
