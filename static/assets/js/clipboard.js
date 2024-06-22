// clipboard.js

export function copyText() {
    const textElement = document.getElementById("persistent-text");
    if (textElement) {
        textElement.select();
        document.execCommand("copy");
    }
}

export function pasteText() {
    const textElement = document.getElementById("persistent-text");
    if (textElement) {
        navigator.clipboard.readText().then(text => {
            textElement.value = text;
        }).catch(err => console.error("Failed to read clipboard contents: ", err));
    }
}

export function copyAllUrls() {
    fetch('/get_urls')
        .then(response => response.json())
        .then(urls => {
            const textToCopy = urls.join('\n');
            navigator.clipboard.writeText(textToCopy)
                .catch(err => console.error("Failed to copy URLs: ", err));
        })
        .catch(err => console.error("Failed to fetch URLs: ", err));
}

export function copyUrl(url) {
    navigator.clipboard.writeText(decodeURIComponent(url))
        .catch(err => console.error("Failed to copy URL: ", err));
}
