let startTime, endTime, phraseText;

function startTest() {
    fetch('/get_phrase')
        .then(response => response.json())
        .then(data => {
            phraseText = data.phrase;
            document.getElementById('phrase').innerText = phraseText;
            document.getElementById('user-input').disabled = false;
            document.getElementById('user-input').value = "";
            document.getElementById('submit-btn').disabled = false;
            startTime = new Date().getTime() / 1000; // Start time in seconds
        });
}

function submitTest() {
    endTime = new Date().getTime() / 1000; // End time in seconds
    let inputText = document.getElementById('user-input').value;
    
    fetch('/calculate_results', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            input_text: inputText,
            phrase: phraseText,
            start_time: startTime,
            end_time: endTime
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('results').innerHTML = `
            <p>Total Words: ${data.total_words}</p>
            <p>Time Used: ${data.time_used} seconds</p>
            <p>Accuracy: ${data.accuracy}%</p>
            <p>Speed: ${data.words_per_minute} WPM</p>
        `;
        document.getElementById('user-input').disabled = true;
        document.getElementById('submit-btn').disabled = true;
    });
}
