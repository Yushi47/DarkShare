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

// Load scripts
loadScript('/static/assets/js/jquery-3.6.0.min.js')
    .then(() => loadScript('/static/assets/js/hammer.min.js'))
    .then(() => {
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
            }),
            import('/static/assets/js/download.js').then(module => {
                window.downloadAllFiles = module.downloadAllFiles;
                module.initializeDownloadLinks();
            })
        ]);
    })
    .then(() => {
        console.log('Scripts loaded successfully.');

        // Load text as per application logic
        if (window.loadText) {
            window.loadText();
        }

        // jQuery for animations (move this from global to locally after the scripts finished loading)
        $(document).on("touchstart mousedown", "button", function(e) {
            $(this).addClass("clicked");
        });

        $(document).on("touchend mouseup", "button", function(e) {
            $(this).removeClass("clicked").blur();
        });
    })
    .catch(err => {
        console.error('Script load error:', err);
    });
