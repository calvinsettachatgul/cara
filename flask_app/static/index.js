window.onload = init;

function init(){
    console.log("javascript is ready");
    printPage()
    
    let clickButton = document.getElementById('clickThis');
    clickButton.addEventListener("click", saySomething);
    console.log(clickButton);
}

function printPage(){
    console.log("this is the index.html");
}

function saySomething(){
    console.log('I said Something');
}