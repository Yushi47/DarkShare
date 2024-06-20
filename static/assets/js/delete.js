// Function to delete a single file
export function confirmDelete(filename) {
    console.log("Delete request for file: ", filename);  // Debugging line
    if (confirm("Are you sure you want to delete this file?")) {
        fetch('/delete/' + encodeURIComponent(filename), {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                console.log("File deleted successfully: ", filename);  // Debugging line
                document.getElementById(filename).remove();  // Remove the file from the list
            } else {
                console.error('Failed to delete the file:', filename);  // Debugging line
                alert('Failed to delete the file.');
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
            alert('An error occurred while deleting the file.');
        });
    }
}

// Function to delete a single URL
export function confirmDeleteUrl(url) {
    console.log("Delete request for URL: ", url);  // Debugging line
    if (confirm("Are you sure you want to delete this URL?")) {
        // Encode the URL properly
        const encodedUrl = encodeURIComponent(url.trim());
        console.log("Encoded URL: ", encodedUrl);  // Debugging line
        
        fetch('/delete_url/' + encodedUrl, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                console.log("URL deleted successfully: ", url);  // Debugging line
                document.getElementById(url).remove(); // Remove the URL from the list
            } else {
                console.error('Failed to delete the URL:', url, 'Status:', response.status, 'StatusText:', response.statusText);  // Debugging line
                alert('Failed to delete the URL.');
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
            alert('An error occurred while deleting the URL.');
        });
    }
}

// Function to delete all files
export function confirmDeleteAllFiles() {
    console.log("Delete request for all files");  // Debugging line
    if (confirm("Are you sure you want to delete all files?")) {
        fetch('/delete_all_files', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                console.log("All files deleted successfully");  // Debugging line
                document.getElementById('file-list').innerHTML = ''; // Clear the file list
            } else {
                console.error('Failed to delete all files');  // Debugging line
                alert('Failed to delete all files.');
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
            alert('An error occurred while deleting all files.');
        });
    }
}

// Function to delete all URLs
export function confirmDeleteAllUrls() {
    console.log("Delete request for all URLs");  // Debugging line
    if (confirm("Are you sure you want to delete all URLs?")) {
        fetch('/delete_all_urls', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                console.log("All URLs deleted successfully");  // Debugging line
                document.getElementById('url-list').innerHTML = ''; // Clear the URL list
            } else {
                console.error('Failed to delete all URLs');  // Debugging line
                alert('Failed to delete all URLs.');
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
            alert('An error occurred while deleting all URLs.');
        });
    }
}
