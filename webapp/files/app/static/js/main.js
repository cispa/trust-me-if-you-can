function submitAsJson(event) {
    // Stop the regular form submission
    event.preventDefault();
    // Convert Inputs to JS Object
    var data = {};
    var form = event.target || event.srcElement;
    for (var i = 0; i < form.length; i++) {
        if (form[i].name) {
            data[form[i].name] = form[i].value;
        }
    }
    // Send to JS Object to the endpoint as JSON string
    var xhr = new XMLHttpRequest();
    xhr.open(form.method, form.action, true);
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            window.location.reload();
        }
    };
    xhr.send(JSON.stringify(data));
}