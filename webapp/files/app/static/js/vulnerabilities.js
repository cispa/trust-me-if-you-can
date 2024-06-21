window.addEventListener('load', function () {
    let inj = unescape(location.hash.slice(1));
    if (inj.length === 0)
        return
    if (inj.startsWith('http')) {
        let s = document.createElement('script');
        s.src = escapePolicy.createScriptURL(inj);
        document.body.appendChild(s);
    } else {
        if (inj.startsWith('<')) {
            let d = document.createElement('div');
            d.innerHTML = escapePolicy.createHTML(inj);
            document.body.appendChild(d);
        } else {
            eval(escapePolicy.createScript(inj));
        }
    }
});