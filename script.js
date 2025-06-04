// Clock Functionality
const clockElement = document.getElementById('clock');

function updateClock() {
    try {
        const now = new Date();
        // Haiti is in 'America/Port-au-Prince' timezone
        const options = { timeZone: 'America/Port-au-Prince', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
        const haitiTime = now.toLocaleTimeString('en-US', options);
        clockElement.textContent = haitiTime;
    } catch (error) {
        console.error("Error updating clock:", error);
        clockElement.textContent = "Error loading time";
        // Fallback if Intl or timezone is not supported in a very old browser
        // This is a rough fallback and might not be accurate for Haiti time
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        clockElement.textContent = `${hours}:${minutes}:${seconds} (Fallback - May not be Haiti Time)`;
    }
}

// Update the clock every second
setInterval(updateClock, 1000);

// Initial call to display clock immediately
updateClock();

// --- ALARM FUNCTIONALITY ---
const alarmTimeInput = document.getElementById('alarm-time');
const setAlarmButton = document.getElementById('set-alarm');
const clearAlarmButton = document.getElementById('clear-alarm');

// --- Web Audio API for Sound ---
let audioContext; // Declare here to be accessible by playAlarmSound

function getAudioContext() {
    if (!audioContext) {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
    }
    return audioContext;
}

function playAlarmSound() {
    try {
        const context = getAudioContext();
        if (!context) {
            console.warn("Web Audio API not supported. No sound will play.");
            return;
        }
        const oscillator = context.createOscillator();
        const gainNode = context.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(context.destination);

        oscillator.type = 'sine'; // 'sine', 'square', 'sawtooth', 'triangle'
        oscillator.frequency.setValueAtTime(440, context.currentTime); // A4 note
        gainNode.gain.setValueAtTime(0.5, context.currentTime); // Volume

        oscillator.start(context.currentTime);
        // Beep for 0.5 seconds
        oscillator.stop(context.currentTime + 0.5);
        console.log("Beep sound played via Web Audio API.");
    } catch (error) {
        console.error("Error playing sound with Web Audio API:", error);
    }
}

// The old stopAlarmSound function is no longer needed for a short beep.
// If it's called anywhere, ensure those calls are removed or the function is left empty.
// For instance, in clearAlarm(): stopAlarmSound(); should be removed if stopAlarmSound is removed.

// Let's ensure stopAlarmSound is now an empty function if it's still called,
// or remove its calls. For simplicity, let's make it an empty function for now
// to avoid errors if it's still called by existing code.
function stopAlarmSound() {
    // No action needed for short Web Audio beeps
    console.log("stopAlarmSound called (no action for Web Audio beep).");
}

let alarmIntervalId = null;
let scheduledAlarmTime = null;

function checkAlarm() {
    if (!scheduledAlarmTime) return;

    const now = new Date();
    const currentHours = String(now.getHours()).padStart(2, '0');
    const currentMinutes = String(now.getMinutes()).padStart(2, '0');
    const currentTimeString = `${currentHours}:${currentMinutes}`;

    // Check if current time in user's local timezone matches the scheduled alarm time
    // Note: The alarm input is based on the user's local time setting.
    // For a more robust solution, timezone handling for alarms would be needed,
    // but for now, it triggers based on the user's device time matching the input.
    if (currentTimeString === scheduledAlarmTime) {
        playAlarmSound();
        alert('Alarm! Time to wake up!');
        // Automatically clear the alarm after it rings
        clearAlarm();
    }
}

function setAlarm() {
    const timeValue = alarmTimeInput.value;
    if (!timeValue) {
        alert("Please set a time for the alarm.");
        return;
    }

    scheduledAlarmTime = timeValue;
    console.log(`Alarm set for: ${scheduledAlarmTime}`);

    // Start checking the alarm every second
    if (alarmIntervalId) {
        clearInterval(alarmIntervalId);
    }
    alarmIntervalId = setInterval(checkAlarm, 1000);

    setAlarmButton.style.display = 'none';
    clearAlarmButton.style.display = 'inline-block';
    alarmTimeInput.disabled = true;
}

function clearAlarm() {
    if (alarmIntervalId) {
        clearInterval(alarmIntervalId);
        alarmIntervalId = null;
    }
    stopAlarmSound();
    scheduledAlarmTime = null;
    alarmTimeInput.value = ""; // Clear the input
    alarmTimeInput.disabled = false;
    setAlarmButton.style.display = 'inline-block';
    clearAlarmButton.style.display = 'none';
    console.log("Alarm cleared.");
}

setAlarmButton.addEventListener('click', setAlarm);
clearAlarmButton.addEventListener('click', clearAlarm);

console.log("Alarm functionality loaded.");

// --- TIMER FUNCTIONALITY ---
const timerMinutesInput = document.getElementById('timer-minutes');
const timerSecondsInput = document.getElementById('timer-seconds');
const startTimerButton = document.getElementById('start-timer');
const pauseTimerButton = document.getElementById('pause-timer');
const resetTimerButton = document.getElementById('reset-timer');
const timerDisplay = document.getElementById('timer-display');

let timerIntervalId = null;
let timerTotalSeconds = 0;
let timerRemainingSeconds = 0;
let isTimerPaused = false;

function formatTime(totalSeconds) {
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

function updateTimerDisplay() {
    timerDisplay.textContent = formatTime(timerRemainingSeconds);
}

function startTimer() {
    if (isTimerPaused) { // Resuming
        isTimerPaused = false;
    } else { // Starting new or after reset
        const minutes = parseInt(timerMinutesInput.value) || 0;
        const seconds = parseInt(timerSecondsInput.value) || 0;
        timerTotalSeconds = (minutes * 60) + seconds;

        if (timerTotalSeconds <= 0) {
            alert("Please set a valid duration for the timer.");
            return;
        }
        timerRemainingSeconds = timerTotalSeconds;
    }

    if (timerRemainingSeconds <= 0) return; // Should not happen if validation is correct

    updateTimerDisplay(); // Update display immediately

    if (timerIntervalId) {
        clearInterval(timerIntervalId);
    }

    timerIntervalId = setInterval(() => {
        timerRemainingSeconds--;
        updateTimerDisplay();

        if (timerRemainingSeconds <= 0) {
            clearInterval(timerIntervalId);
            timerIntervalId = null;
            playAlarmSound(); // Reuse alarm sound for timer completion
            alert("Timer Finished!");
            resetTimerControls(true); // Full reset of controls
        }
    }, 1000);

    timerMinutesInput.disabled = true;
    timerSecondsInput.disabled = true;
    startTimerButton.disabled = true;
    pauseTimerButton.disabled = false;
    resetTimerButton.disabled = false; // Allow reset while running
}

function pauseTimer() {
    if (timerIntervalId) {
        clearInterval(timerIntervalId);
        timerIntervalId = null;
        isTimerPaused = true;
        startTimerButton.disabled = false; // Becomes "Resume"
        startTimerButton.textContent = "Resume Timer";
        pauseTimerButton.disabled = true;
    }
}

function resetTimerControls(isFinished) {
    timerMinutesInput.disabled = false;
    timerSecondsInput.disabled = false;
    startTimerButton.disabled = false;
    startTimerButton.textContent = "Start Timer";
    pauseTimerButton.disabled = true;
    // Reset button remains enabled unless timer was never started
    resetTimerButton.disabled = !(timerTotalSeconds > 0 || isFinished);
}


function resetTimer() {
    if (timerIntervalId) {
        clearInterval(timerIntervalId);
        timerIntervalId = null;
    }
    isTimerPaused = false;
    timerTotalSeconds = 0;
    timerRemainingSeconds = 0;
    updateTimerDisplay(); // Display 00:00

    timerMinutesInput.value = "";
    timerSecondsInput.value = "";

    resetTimerControls(false);
    console.log("Timer reset.");
}

startTimerButton.addEventListener('click', startTimer);
pauseTimerButton.addEventListener('click', pauseTimer);
resetTimerButton.addEventListener('click', resetTimer);

// Initial state for buttons
pauseTimerButton.disabled = true;
resetTimerButton.disabled = true; // Disabled until a time is set or timer runs

console.log("Timer functionality loaded.");

// --- STOPWATCH FUNCTIONALITY ---
const stopwatchDisplay = document.getElementById('stopwatch-display');
const startStopwatchButton = document.getElementById('start-stopwatch');
const pauseStopwatchButton = document.getElementById('pause-stopwatch');
const resetStopwatchButton = document.getElementById('reset-stopwatch');
const lapStopwatchButton = document.getElementById('lap-stopwatch');
const lapsList = document.getElementById('laps-list');

let stopwatchIntervalId = null;
let stopwatchStartTime = 0;
let stopwatchElapsedTime = 0; // Time elapsed when paused
let isStopwatchPaused = false;

function formatStopwatchTime(timeInMilliseconds) {
    const totalMilliseconds = timeInMilliseconds;
    const milliseconds = String(totalMilliseconds % 1000).padStart(3, '0');
    const totalSeconds = Math.floor(totalMilliseconds / 1000);
    const seconds = String(totalSeconds % 60).padStart(2, '0');
    const minutes = String(Math.floor(totalSeconds / 60) % 60).padStart(2, '0');
    // If you want hours: const hours = String(Math.floor(totalSeconds / 3600)).padStart(2, '0');
    // For this example, sticking to M:S:MS
    return `${minutes}:${seconds}.${milliseconds}`;
}

function updateStopwatchDisplay() {
    const currentTime = Date.now();
    const displayTime = stopwatchElapsedTime + (stopwatchStartTime ? (currentTime - stopwatchStartTime) : 0);
    stopwatchDisplay.textContent = formatStopwatchTime(displayTime);
}

function startStopwatch() {
    if (isStopwatchPaused) { // Resuming
        isStopwatchPaused = false;
        // stopwatchElapsedTime is already set from when it was paused
    } else { // Starting new or after reset
        stopwatchElapsedTime = 0; // Reset elapsed time if not resuming
    }

    stopwatchStartTime = Date.now(); // Always set/reset start time relative to now

    if (stopwatchIntervalId) {
        clearInterval(stopwatchIntervalId);
    }

    // Update display more frequently for stopwatch
    stopwatchIntervalId = setInterval(updateStopwatchDisplay, 10);

    startStopwatchButton.textContent = "Start"; // Ensure it's "Start" if it was "Resume"
    startStopwatchButton.disabled = true;
    pauseStopwatchButton.disabled = false;
    resetStopwatchButton.disabled = false; // Can reset while running
    lapStopwatchButton.disabled = false;
}

function pauseStopwatch() {
    if (stopwatchIntervalId) {
        clearInterval(stopwatchIntervalId);
        stopwatchIntervalId = null;
        // Add the time elapsed since the last start/resume to stopwatchElapsedTime
        stopwatchElapsedTime += (Date.now() - stopwatchStartTime);
        stopwatchStartTime = 0; // Reset startTime as it's now part of stopwatchElapsedTime
        isStopwatchPaused = true;

        startStopwatchButton.textContent = "Resume";
        startStopwatchButton.disabled = false;
        pauseStopwatchButton.disabled = true;
        lapStopwatchButton.disabled = true; // Usually disable lap when paused
    }
}

function resetStopwatch() {
    if (stopwatchIntervalId) {
        clearInterval(stopwatchIntervalId);
        stopwatchIntervalId = null;
    }
    isStopwatchPaused = false;
    stopwatchStartTime = 0;
    stopwatchElapsedTime = 0;
    stopwatchDisplay.textContent = formatStopwatchTime(0);
    lapsList.innerHTML = ''; // Clear laps

    startStopwatchButton.textContent = "Start";
    startStopwatchButton.disabled = false;
    pauseStopwatchButton.disabled = true;
    resetStopwatchButton.disabled = true; // Disabled until started again
    lapStopwatchButton.disabled = true;
    console.log("Stopwatch reset.");
}

function lapStopwatch() {
    if (!stopwatchIntervalId && !isStopwatchPaused) return; // Can't lap if not running or paused without time

    const currentTime = Date.now();
    const lapTimeValue = stopwatchElapsedTime + (stopwatchStartTime ? (currentTime - stopwatchStartTime) : 0);
    const lapTimeFormatted = formatStopwatchTime(lapTimeValue);

    const lapItem = document.createElement('li');
    lapItem.textContent = `Lap ${lapsList.children.length + 1}: ${lapTimeFormatted}`;
    lapsList.prepend(lapItem); // Add new laps to the top
}

startStopwatchButton.addEventListener('click', startStopwatch);
pauseStopwatchButton.addEventListener('click', pauseStopwatch);
resetStopwatchButton.addEventListener('click', resetStopwatch);
lapStopwatchButton.addEventListener('click', lapStopwatch);

// Initial state for stopwatch buttons
pauseStopwatchButton.disabled = true;
resetStopwatchButton.disabled = true;
lapStopwatchButton.disabled = true;

console.log("Stopwatch functionality loaded.");
