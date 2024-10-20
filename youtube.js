// Create a function to show the current playback speed on the video screen
function showSpeedOverlay(speed) {
    let speedOverlay = document.getElementById('speedOverlay');
    
    // If the overlay does not exist, create it
    if (!speedOverlay) {
        speedOverlay = document.createElement('div');
        speedOverlay.id = 'speedOverlay';
        speedOverlay.style.position = 'absolute';
        speedOverlay.style.top = '10px';
        speedOverlay.style.right = '10px';
        speedOverlay.style.padding = '5px 10px';
        speedOverlay.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
        speedOverlay.style.color = 'white';
        speedOverlay.style.fontSize = '16px';
        speedOverlay.style.zIndex = '9999';
        speedOverlay.style.borderRadius = '5px';
        speedOverlay.style.transition = 'opacity 0.5s ease';
        document.body.appendChild(speedOverlay);
    }
    
    // Update the text content with the current speed
    speedOverlay.textContent = 'Speed: ' + speed.toFixed(2) + 'x';
    
    // Show the overlay
    speedOverlay.style.opacity = '1';
    
    // Hide the overlay after 2 seconds
    clearTimeout(speedOverlay.timeout);
    speedOverlay.timeout = setTimeout(() => {
        speedOverlay.style.opacity = '0';
    }, 2000);
}

// Function to handle key presses
document.onkeydown = function (e) {
    var video = document.querySelector('video'); // Get the video element
    if (!video) return; // Exit if no video is found

    if (e.key.toLowerCase() === 'd') {
        video.playbackRate += 0.1; // Increase speed by 0.1x when 'D' is pressed
        showSpeedOverlay(video.playbackRate);
    } else if (e.key.toLowerCase() === 's') {
        video.playbackRate = Math.max(0.1, video.playbackRate - 0.1); // Decrease speed but not below 0.1x
        showSpeedOverlay(video.playbackRate);
    }
};
