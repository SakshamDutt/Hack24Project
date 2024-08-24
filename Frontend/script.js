function displayInput() {
    // Get the input element by its ID
    var inputElement = document.getElementById('userInput');

    // Get the value of the input element
    var inputValue = inputElement.value;

    // Display the value in the paragraph with id 'output'
    document.getElementById('output').innerText = 'You entered: ' + inputValue;
}