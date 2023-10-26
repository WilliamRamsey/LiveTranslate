// Information for context menu
let contextMenuItem = {
    id: "virtually-free",
    title: "Virtually Free",
    // for highlighted text
    contexts: ["selection"]
};

function sendToPopup(text_out) {
    chrome.runtime.sendMessage({
        msg: "Translation Compleated",
        data: {
            text_out: text_out
        }
    })
};

function textToEnglish(info, tab){
    //console.log(info['selectionText']) 
    fetch("http://127.0.0.1:5500/api/translation/text?lang_in=none&lang_out=none", {
        method: "POST",
        body: info['selectionText'],
        headers: {'Content-Type': 'text/html; charset=utf-8'}
    }).then(res=>res.text()
    ).then(data=>{
        sendToPopup(data); //console.log(data);
    })
};

// Code for a right click (context menu)
chrome.contextMenus.create(contextMenuItem);
chrome.contextMenus.onClicked.addListener(textToEnglish)
