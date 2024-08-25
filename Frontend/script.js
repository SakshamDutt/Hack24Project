let question;

function addMessage() {
    // Create a new div element for the message
    chatBody = document.getElementById('chat--body')
    chatBody.getElementById('user-message').innerText = question;

    // Append the message text div to the message div

    // Append the new message div to the container div
}

function displayInput() {
    // Get the input element by its ID
    var inputElement = document.getElementById('userInput');

    // Get the value of the input element
    var inputValue = inputElement.value;
    console.log(inputValue)
    
    question=inputValue
    addMessage()
}

function hide(){
    var inputElement = document.getElementById('hidden-element')
    const pdfElement = document.getElementById('pdf-notes')

    if (!document.getElementById('title').value) {

        inputElement.style.display='none'
        pdfElement.style.display='block'
    } else {
        inputElement.style.display='block'
        pdfElement.style.display='none' 
    }




}