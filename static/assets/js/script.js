// script.js

// Function to dynamically load a script
function loadScript(url) {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = url;
        script.onload = () => resolve(script);
        script.onerror = () => reject(new Error(`Script load error for ${url}`));
        document.head.appendChild(script);
    });
}

// Load jQuery first
loadScript('/static/assets/js/jquery-3.6.0.min.js')
    .then(() => {
        return loadScript('/static/assets/js/jquery.js');
    })
    .then(() => {
        // Import other JavaScript files
        return Promise.all([
            import('/static/assets/js/delete.js').then(module => {
                window.confirmDelete = module.confirmDelete;
                window.confirmDeleteUrl = module.confirmDeleteUrl;
                window.confirmDeleteAllFiles = module.confirmDeleteAllFiles;
                window.confirmDeleteAllUrls = module.confirmDeleteAllUrls;
            }),
            import('/static/assets/js/clipboard.js').then(module => {
                window.copyText = module.copyText;
                window.pasteText = module.pasteText;
                window.copyAllUrls = module.copyAllUrls;
                window.copyUrl = module.copyUrl;
            }),
            import('/static/assets/js/utils.js').then(module => {
                window.saveText = module.saveText;
                window.loadText = module.loadText;
                window.clearText = module.clearText;
            })
        ]);
    })
    .then(() => {
        // Function to handle downloading all files
        function downloadAllFiles() {
            window.location.href = '/download_all_files';
        }
        window.downloadAllFiles = downloadAllFiles;

        // Include jQuery functionalities
        $(document).on("touchstart mousedown touchend mouseup", "button", function (e) {
            e.preventDefault();
            if (e.type === "touchstart" || e.type === "mousedown") {
                $(this).addClass("clicked");
            } else {
                $(this).removeClass("clicked").blur();
            }
        });
    })
    .catch(err => {
        console.error(err);
    });
