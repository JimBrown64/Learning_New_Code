 let textContainer = document.getElementById('displayText')


function submission(){
    let newParagraph = document.createElement('p');
    newParagraph.innerText = document.getElementById('inputText').value;
    
    textContainer.appendChild(newParagraph);
    document.getElementById('inputText').value = '';
};

let inputField = document.getElementById('inputText')
inputField.addEventListener('keydown',function(event){
    if (event.key === 'Enter'){
        submission();
    }
});

 let submitButton = document.getElementById('submitButton')
 submitButton.addEventListener('click', submission());

