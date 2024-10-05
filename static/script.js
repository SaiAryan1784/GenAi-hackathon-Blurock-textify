// Send file to /transcribe endpoint
function transcribeAudio() {
    const fileInput = document.getElementById('audioFile');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('/transcribe', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('transcription').value = data.transcription;
    })
    .catch(error => console.error('Error:', error));
}

// Modify the transcription
function modifyText() {
    const transcription = document.getElementById('transcription').value;
    const modificationInput = document.getElementById('modificationInput').value;

    fetch('/modify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            transcription: transcription,
            modification_input: modificationInput
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('modifiedText').value = data.modified_text;
    })
    .catch(error => console.error('Error:', error));
}

// Save modified text to Google Docs
function saveToDocs() {
    const modifiedText = document.getElementById('modifiedText').value;

    fetch('/save_to_docs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ modified_text: modifiedText }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Document saved! View it here: ' + data.document_url);
    })
    .catch(error => console.error('Error:', error));
}
