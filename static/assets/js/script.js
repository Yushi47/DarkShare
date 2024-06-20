import { confirmDelete, confirmDeleteUrl, confirmDeleteAllFiles, confirmDeleteAllUrls } from './delete.js';
import { copyText, pasteText } from './clipboard.js';
import { saveText, loadText, clearText } from './utils.js';

// Function to handle downloading all files
function downloadAllFiles() {
    window.location.href = '/download_all_files';
}

// Expose functions to the global scope for HTML event handlers
window.confirmDelete = confirmDelete;
window.confirmDeleteUrl = confirmDeleteUrl;
window.confirmDeleteAllFiles = confirmDeleteAllFiles;
window.confirmDeleteAllUrls = confirmDeleteAllUrls;
window.copyText = copyText;
window.pasteText = pasteText;
window.saveText = saveText;
window.loadText = loadText;
window.clearText = clearText;
window.downloadAllFiles = downloadAllFiles;
