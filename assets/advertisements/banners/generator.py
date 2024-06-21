import os

for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if file.endswith('.py'):
        continue
    picture = os.popen(f'echo "data:image/jpeg;base64,$(base64 -w 0 {file})"').read().strip()
    code = f"""(function () {{
        let div = document.getElementById('banner-div');
        let img = document.createElement('img');
        img.src = '{picture}';
        div.appendChild(img);
    }})();
    """
    open(f'../ads/{file.split(".")[0]}.js', 'w').write(code)
