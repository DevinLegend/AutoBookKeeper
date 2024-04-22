// JavaScript for the PDF file upload
document.getElementById('pdf-upload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const feedbackMessage = document.getElementById('feedback-message');

    // ChatGPT assisted in implementing user feedback for file selection
    if (!file) {
        feedbackMessage.style.display = 'block';
        feedbackMessage.textContent = 'No file selected.';
        feedbackMessage.classList.add('alert', 'alert-danger');
        return;
    }

    // Ensured that only PDF files are uploaded
    if (file.type !== 'application/pdf') {
        feedbackMessage.style.display = 'block';
        feedbackMessage.textContent = 'Please upload a PDF file.';
        feedbackMessage.classList.add('alert', 'alert-danger');
        return;
    }

    // Reset feedback message
    feedbackMessage.style.display = 'none';

    const formData = new FormData();
    formData.append('file', file);

    // Implemented file upload logic and used fetch API based on prior knowledge from codecademy front end/back end/ full stack engineering and refreshed and refined code by ChatGPT
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('File uploaded successfully:', data);
        feedbackMessage.style.display = 'block';
        feedbackMessage.textContent = 'File uploaded successfully.';
        feedbackMessage.classList.remove('alert-danger');
        feedbackMessage.classList.add('alert', 'alert-success');

        document.getElementById('run-program').disabled = false; // Enable run button on successful upload
        document.getElementById('run-program').setAttribute('data-filename', data.filename); // Store filename for later use
    })
    .catch(error => {
        console.error('Error uploading file:', error);
        feedbackMessage.style.display = 'block';
        feedbackMessage.textContent = 'Error uploading file: ' + error.message;
        feedbackMessage.classList.add('alert', 'alert-danger');
    });
});

// JavaScript for the Run Program button
// Logic for processing the uploaded file was structured by me with error handling refined by ChatGPT
document.getElementById('run-program').addEventListener('click', function() {
    const filename = this.getAttribute('data-filename');
    if (!filename) {
        console.error('No file selected for processing.');
        return;
    }

    console.log('Run Program button clicked');
    fetch(`/process?filename=${filename}`, {
        method: 'GET'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Processing complete:', data);
        // Further handling of the processed data can be implemented here
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
