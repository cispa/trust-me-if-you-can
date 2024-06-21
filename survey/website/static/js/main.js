window.onload = function () {
    let startForm = document.getElementById('startForm');
    let startBtn = document.getElementById('startBtn');
    if (startForm && startBtn) {
        startBtn.onclick = function () {
            if (startForm.reportValidity()) {
                startForm.submit();
            }
        }
    }
}
