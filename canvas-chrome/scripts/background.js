
let contextMenuItem = {
    id: "virtually-free",
    title: "Text to English",
    // for highlighted text
    contexts: ["selection"]
};

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

// Code for a right click (context menu)
chrome.contextMenus.create(contextMenuItem);
chrome.contextMenus.onClicked.addListener(textToEnglish)
