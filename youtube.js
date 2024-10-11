// Function to create the speed overlay if it doesn't exist
function createSpeedOverlay() {
    let overlay = document.createElement('div');
    overlay.id = 'speed-overlay';
    overlay.style.position = 'absolute';
    overlay.style.top = '10px';
    overlay.style.right = '10px';
    overlay.style.padding = '5px 10px';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    overlay.style.color = 'white';
    overlay.style.fontSize = '20px';
    overlay.style.fontWeight = 'bold';
    overlay.style.borderRadius = '5px';
    overlay.style.zIndex = '9999';
    document.body.appendChild(overlay);
    return overlay;
}

// Function to update the speed overlay with the current speed
function updateSpeedOverlay(speed) {
    let overlay = document.getElementById('speed-overlay') || createSpeedOverlay();
    overlay.textContent = `Speed: ${speed.toFixed(2)}x`;
}

// Keydown event listener to control speed
document.addEventListener('keydown', function(event) {
    let video = document.querySelector('video');
    if (!video) return;

    if (event.key === 'd') {
        video.playbackRate += 0.25;
        updateSpeedOverlay(video.playbackRate);
    } else if (event.key === 's') {
        video.playbackRate = Math.max(0.25, video.playbackRate - 0.25);
        updateSpeedOverlay(video.playbackRate);
    }
});
