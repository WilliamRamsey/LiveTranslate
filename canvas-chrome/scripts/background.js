// Information for context menu
let contextMenuItem = {
    id: "virtually-free",
    title: "Virtually Free",
    // for highlighted text
    contexts: ["selection"]
};

function toAPI(info, tab){
    console.log(info['selectionText'])
};

// Code for a right click (context menu)
chrome.contextMenus.create(contextMenuItem);

chrome.contextMenus.onClicked.addListener(toAPI)