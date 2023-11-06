/*
Sends text to flask server to be translated
Returns translated text literal

text = text to be translated
langIn = string code of the language of the text being sent is in
langOut = string code of the desired language of translation
*/
function textToDomestic(text, langIn, langOut) {

    // If no lang in is specified will be set to auto in server
    // Yeilds much poorer results
    if (typeof langIn === 'undefined') {
        langIn = "none"
    };

    // If no lang out is specified will be set to english in server
    if (typeof langOut === 'undefined') {
        langOut = "none"
    };
    
    // Sends post request to flask server
    fetch(`http://192.168.0.21:5500/api/translation/text?lang_in=${langIn}&lang_out=${langOut}`, {
        method: "POST",
        body: text,
        headers: {'Content-Type': 'text/html; charset=utf-8'}
    })
    
    // Takes response and pulls out text body
    .then(response => response.text())
    // Logs 
    .then(text => {
        chrome.storage.sync.set({'translated_text': text});
    })
};

// Container for the asynch function above
// I know this function is unessasary and redundent but it is the only way I can get it to work
function textFromContextMenu (info, tab) {
    let textResponse = textToDomestic(info['selectionText'])
};



// Requests audio file from canvas
// Converts audio file to bytes
// Sends bytes to flask server
// Takes response and saves to chrome storage
async function audioToDomestic(audioSourceURL, langIn, langOut) {

     // If no lang in is specified will be set to auto in server
    // Yeilds much poorer results
    if (typeof langIn === 'undefined') {
        langIn = "none"
    };

    // If no lang out is specified will be set to english in server
    if (typeof langOut === 'undefined') {
        langOut = "none"
    };

    // gets audio file from canvas
    let canvasAudio = await fetch(audioSourceURL)
    // converts audio file to bytes
    let canvasAudioBuffer = await canvasAudio.arrayBuffer()
    // sends bytes to flask server
    let flaskResponse = await fetch(`http://127.0.0.1:5500/api/translation/audio?lang_in=${langIn}&lang_out=${langOut}`,{
            method: "POST",
            body: canvasAudioBuffer
        })
    let data = await flaskResponse.text()
    chrome.storage.sync.set({'translated_text': data});
};

function audioFromContextMenu(info, tab) {
    let audioSourceURL = info['srcUrl'];
    let audioResponse = audioToDomestic(audioSourceURL)
};




/*
function textToEnglish(info, tab) {
    //console.log(info['selectionText']) 
    fetch("http://127.0.0.1:5500/api/translation/text?lang_in=none&lang_out=none", {
        method: "POST",
        body: info['selectionText'],
        headers: {'Content-Type': 'text/html; charset=utf-8'}
    }).then(res=>res.text()
    ).then(data=>{
        chrome.storage.sync.set({'translated_text': data});
    })
};
*/

/*
function audioToEnglish(info, tab) {
    let audioSourceURL = info['srcUrl'];

    fetch(audioSourceURL)
        .then(response => response.arrayBuffer())
        .then(audioData => {
            fetch("http://127.0.0.1:5500/api/translation/audio?lang_in=none&lang_out=none", {
                method: "POST",
                body: audioData
            })
        })
        .then(data=> {
            console.log(data)
        })
};

*/

// Code for a right click (context menu)

let textContextMenuItem = {
    id: "text-to-text",
    title: "Text to English",
    // for highlighted text
    contexts: ["selection"]
};

// Right click for audio files
let audioContextMenuItem = {
    id: "audio-to-text",
    title: "Audio to English",
    contexts: ["audio"]
};

// Establish context menus
chrome.contextMenus.create(textContextMenuItem);
chrome.contextMenus.onClicked.addListener(textFromContextMenu)
// Audio Context Menu
chrome.contextMenus.create(audioContextMenuItem)
chrome.contextMenus.onClicked.addListener(audioFromContextMenu)
