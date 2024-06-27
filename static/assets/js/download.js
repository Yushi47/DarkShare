// Function to handle downloading all files
export function downloadAllFiles() {
    window.location.href = '/download_all_files';
}

// Initialize download for single files
export function initializeDownloadLinks() {
    document.querySelectorAll('a.single-download').forEach(link => {
        const fileName = link.getAttribute('href').split('/').pop();
        link.setAttribute('download', fileName);

        // Force download using Blob
        link.addEventListener('click', function (e) {
            e.preventDefault();
            fetch(link.getAttribute('href'))
                .then(response => response.blob())
                .then(blob => {
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = fileName;
                    document.body.appendChild(a);
                    a.click();
                    a.remove();
                    window.URL.revokeObjectURL(url);
                })
                .catch(error => console.error('Download error:', error));
        });
    });
}
