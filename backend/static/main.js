const mainProgress = document.getElementById('mainProgress');
let progress = mainProgress.value;

function startProgress() {
    interval = setInterval(() => {
        if (progress < 100) {
            progress ++;
            mainProgress.value = progress;
        } else {
            clearInterval(interval);
        }
    }, 100); // update every 100ms
}

function stopProgress() {
    clearInterval(interval);
}

mainProgress.addEventListener('mousedown', startProgress);
mainProgress.addEventListener('mouseup', stopProgress);
mainProgress.addEventListener('mouseleave', stopProgress);