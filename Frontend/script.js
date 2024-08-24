let question;



function addMessage() {
    // Create a new div element for the message
    var messageDiv = document.createElement('div');
    messageDiv.className = 'message right #user-message';

    // Create a new div element for the message text
    var messageTextDiv = document.createElement('div');
    messageTextDiv.className = 'message-text';
    messageTextDiv.innerText = question;

    // Append the message text div to the message div
    messageDiv.appendChild(messageTextDiv);

    // Append the new message div to the container div
    document.getElementById('chat--body').appendChild(messageDiv);
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