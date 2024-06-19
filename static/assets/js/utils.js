// utils.js

export function saveText() {
    const textElement = document.getElementById("persistent-text");
    if (textElement) {
        const text = textElement.value;
        fetch('/save_text', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
        })
        .then(response => {
            if (response.ok) {
                console.log('Text saved successfully');  // Debugging line
            } else {
                console.error('Failed to save text');  // Debugging line
                alert('Failed to save text.');
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
            alert('An error occurred while saving the text.');
        });
    } else {
        console.error('Text element not found');  // Debugging line
        alert('Failed to save text: text element not found.');
    }
}

export function loadText() {
    fetch('/load_text')
        .then(response => response.json())
        .then(data => {
            const textElement = document.getElementById("persistent-text");
            if (textElement) {
                if (data.text !== undefined) {
                    textElement.value = data.text;
                    console.log('Text loaded successfully');  // Debugging line
                } else {
                    textElement.value = '';
                }
            } else {
                console.error('Text element not found');  // Debugging line
                alert('Failed to load text: text element not found.');
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
            alert('An error occurred while loading the text.');
        });
}

export function clearText() {
    const textElement = document.getElementById("persistent-text");
    if (textElement) {
        textElement.value = '';
        saveText(); // Save the cleared state
        console.log('Text cleared successfully');  // Debugging line
    } else {
        console.error('Text element not found');  // Debugging line
        alert('Failed to clear text: text element not found.');
    }
}
