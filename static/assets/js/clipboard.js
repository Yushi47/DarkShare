// clipboard.js

export function copyText() {
    const textElement = document.getElementById("persistent-text");
    if (textElement) {
        textElement.select();
        textElement.setSelectionRange(0, 99999); // For mobile devices
        document.execCommand("copy");
        console.log('Text copied to clipboard:', textElement.value);  // Debugging line
    } else {
        console.error('Text element not found');
        alert('Failed to copy text: text element not found.');
    }
}

export function pasteText() {
    navigator.clipboard.readText()
        .then(text => {
            const textElement = document.getElementById("persistent-text");
            if (textElement) {
                textElement.value = text;
                saveText(); // Save the pasted text
                console.log('Text pasted from clipboard:', text);  // Debugging line
            } else {
                console.error('Text element not found');
                alert('Failed to paste text: text element not found.');
            }
        })
        .catch(err => {
            console.error('Failed to read clipboard contents: ', err);
            alert('Failed to read clipboard contents.');
        });
}
