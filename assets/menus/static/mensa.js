(function () {
    let div = document.getElementById('mensa-div');
    let ul = document.createElement('ul');
    ul.style.paddingLeft = '0px';
    ul.id = 'mensa-menu-list';
    div.appendChild(ul);
    fetch('http://mensa.tt-study.local/get-dish').then(response => response.json()).then(function (data) {
        for (let el of data) {
            eval(el);
        }
    });
})();