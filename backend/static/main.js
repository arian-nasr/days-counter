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
    }, 50); // update every 50ms
}

function stopProgress() {
    clearInterval(interval);
}

mainProgress.addEventListener('mousedown', startProgress);
mainProgress.addEventListener('mouseup', stopProgress);
mainProgress.addEventListener('mouseleave', stopProgress);

document.addEventListener('DOMContentLoaded', () => {
    const today = new Date().toISOString().split('T')[0];
    console.log('Fetching data for date:', today);
    getDayData(today).then(data => {
        if (data) {
            console.log('Data for today:', data);
        } else {
            console.log('No data received for today.');
        }
    });
});

async function getDayData(date) {
    try {
        const response = await fetch(`/get_day/${date}`);
        if (response.status === 200) {
            const data = await response.json();
            return data;
        } else {
            console.error('Error fetching day data:', response.status);
            return null;
        }
    } catch (error) {
        console.error('Network error:', error);
        return null;
    }
}