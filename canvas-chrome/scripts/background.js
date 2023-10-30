// Right click for text
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
}

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
    

}

// Code for a right click (context menu)
chrome.contextMenus.create(textContextMenuItem);
chrome.contextMenus.onClicked.addListener(textToEnglish)
chrome.contextMenus.create(audioContextMenuItem)
chrome.contextMenus.onClicked.addListener(audioToEnglish)
