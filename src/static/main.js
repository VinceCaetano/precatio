document.addEventListener('DOMContentLoaded', function () {
    const askButton = document.getElementById('askButton');
    const conversationContainer = document.getElementById('conversationContainer');

    askButton.addEventListener('click', () => {
        const questionInput = document.getElementById('questionInput');
        const question = questionInput.value.trim();

        if (question !== '') {
            displayUserMessage(question);
            sendToBackend(question);

            // Clear the input field after sending the question
            questionInput.value = '';
        }
    });

    function displayUserMessage(message) {
        const userMessage = document.createElement('p');
        userMessage.textContent = `You: ${message}`;
        conversationContainer.appendChild(userMessage);
    }

    function displayAssistantMessage(message) {
        const assistantMessage = document.createElement('p');
        assistantMessage.textContent = `Assistant: ${message}`;
        conversationContainer.appendChild(assistantMessage);
    }

    function sendToBackend(message) {
        fetch('http://localhost:5000/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: message }),
        })
        .then(response => response.json())
        .then(data => displayAssistantMessage(data.answer))
        .catch(error => console.error('Error:', error));
    }
});
