document.addEventListener("DOMContentLoaded", () => {
    let countdownTime = 7;
    let progressTime = 100;
    let countButton = document.getElementById('countButton');
    let progress = document.getElementById('reciprocalBar');

    countButton.textContent = countdownTime;

    function decrementCount() {
        if (countdownTime > 0) {
            countdownTime--;
            countButton.textContent = countdownTime;
        } else {
            clearInterval(countdownInterval);
            // alert('倒計時結束！');
            eel.play();
            async function progressBar() {
                if (progressTime > 0) {
                    progressTime--;
                    progress.style.width = progressTime +"%";
                } else {
                    clearInterval(progressInterval);
                    // let title = await eel.get_title()()
                    // document.getElementById('answer').innerText = title;
                    // await eel.next_song();
                    // document.getElementById('next').disabled = false;
                }
            }
            let progressInterval = setInterval(progressBar, 150);
        }
    }

    // 設置每秒更新一次倒計時
    let countdownInterval = setInterval(decrementCount, 1000);
});

function nextSong() {
    let countdownTime = 7;
    let progressTime = 100;
    let countButton = document.getElementById('countButton');
    let progress = document.getElementById('reciprocalBar');
    // 初始化
    progress.style.width = "100%";
    document.getElementById('next').disabled = true;
    document.getElementById('answer').innerText = "";

    countButton.textContent = countdownTime;

    function decrementCount() {
        if (countdownTime > 0) {
            countdownTime--;
            countButton.textContent = countdownTime;
        } else {
            clearInterval(countdownInterval);
            // alert('倒計時結束！');
            eel.play();
            async function progressBar() {
                if (progressTime > 0) {
                    progressTime--;
                    progress.style.width = progressTime +"%";
                } else {
                    clearInterval(progressInterval);
                    // let title = await eel.get_title()()
                    // document.getElementById('answer').innerText = title;
                    // await eel.next_song();
                    // document.getElementById('next').disabled = false;
                }
            }
            let progressInterval = setInterval(progressBar, 150);
        }
    }

    // 設置每秒更新一次倒計時
    let countdownInterval = setInterval(decrementCount, 1000);
}

async function answerBtn(){
    let title = await eel.get_title()()
    document.getElementById('answer').innerText = title;
    await eel.next_song();
    document.getElementById('next').disabled = false;
}

async function replay(){
    await eel.replay();
}