document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('button');

    buttons.forEach(button => {
        const hammer = new Hammer(button);

        hammer.on('tap', (e) => {
            console.log('Hammer tap event:', e.type, button);
            handleButtonClick.call(button, e);
        });

        hammer.on('press', (e) => {
            handleButtonClick.call(button, e);
        });
    });

    function handleButtonClick(event) {
        console.log('Button clicked:', event.type, this);

        if (this.classList.contains('clear')) {
            window.clearText();
        } else if (this.classList.contains('single-copy-with-text')) {
            window.copyText();
        } else if (this.classList.contains('paste')) {
            window.pasteText();
        } else if (this.classList.contains('delete-all')) {
            window.confirmDeleteAllFiles();
        } else if (this.classList.contains('single-delete')) {
            const filename = this.dataset.filename;
            window.confirmDelete(filename);
        } else if (this.classList.contains('download-all')) {
            window.downloadAllFiles();
        }
    }
});
