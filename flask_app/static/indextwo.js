window.onload = init;

function init(){
    console.log('javascript is working');
    console.log(addNumbers(5,7))
    
    let newButton = document.getElementById('Press_here')
    newButton.addEventListener("click", clickSomething);
    console.log(newButton)
}

function addNumbers(a,b){
    
    return a+b;
}

function clickSomething(){
    console.log('click click boom');
}