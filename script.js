document.addEventListener("DOMContentLoaded", function() {
    // Load the questions from the JSON file
    fetch('questions.json')
        .then(response => response.json())
        .then(questions => {
            // Iterate over each question
            questions.forEach(question => {
                // Create a popup for each question
                createQuestionPopup(question);
            });
        })
        .catch(error => console.error('Error loading questions:', error));
});

function createQuestionPopup(question) {
    // Create a popup element
    const popup = document.createElement('div');
    popup.classList.add('popup');
    popup.innerHTML = `
        <h2>Question ${question.index}</h2>
        <p>${question.question}</p>
        <p>Question Type: ${question.question_type}</p>
        <p>Options: ${question.options.join(', ')}</p>
    `;

    // Calculate the time in seconds
    const timestampInSeconds = parseFloat(question.timestamp);

    // Set a timeout to show the popup at the specified timestamp
    setTimeout(() => {
        document.body.appendChild(popup);
    }, timestampInSeconds * 1000); // Convert seconds to milliseconds
}
