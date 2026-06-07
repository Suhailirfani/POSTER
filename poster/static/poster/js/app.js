document.addEventListener('DOMContentLoaded', () => {
    // Template selection logic
    const templateCards = document.querySelectorAll('.template-card');
    const templateInput = document.getElementById('selected_template');

    if (templateCards.length > 0) {
        templateCards.forEach(card => {
            card.addEventListener('click', () => {
                // Remove selected class from all
                templateCards.forEach(c => c.classList.remove('selected'));
                // Add to clicked
                card.classList.add('selected');
                // Update hidden input
                templateInput.value = card.dataset.id;
            });
        });
    }

    // Download logic
    const downloadBtn = document.getElementById('download-btn');
    if (downloadBtn) {
        downloadBtn.addEventListener('click', () => {
            const posterNode = document.getElementById('poster-node');
            
            // Show loading state
            const originalText = downloadBtn.innerText;
            downloadBtn.innerText = 'Generating Image...';
            downloadBtn.disabled = true;

            html2canvas(posterNode, {
                scale: 2, // Higher resolution
                useCORS: true,
                backgroundColor: null
            }).then(canvas => {
                // Convert to JPEG
                const imgData = canvas.toDataURL('image/jpeg', 0.9);
                
                // Trigger download
                const link = document.createElement('a');
                link.download = 'poster.jpg';
                link.href = imgData;
                link.click();

                // Restore button
                downloadBtn.innerText = originalText;
                downloadBtn.disabled = false;
            }).catch(err => {
                console.error('Error generating poster:', err);
                alert('An error occurred while generating the poster.');
                downloadBtn.innerText = originalText;
                downloadBtn.disabled = false;
            });
        });
    }
});
