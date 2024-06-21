import os

raw = [
    ['Dibbelabbes', 'potato, beef jerky, onions, parsley, eggs, salt, pepper, maggi', 'food/dibbelabbes.jpg', 4],
    ['Schales', 'potato, dried meat, leek, egg, maggi', 'food/schales.jpg', 3],
    ['Gefillde', 'potato, liver sausage, butter, flour, dired meat, broth, milk, cream, maggi', 'food/gefillde.jpg', 2],
    ['Geheirate', 'eggs, flour, mineral water, maggi, potato, dried meat, cream', 'food/geheirate.jpg', 5],
    ['Hoorische', 'potato, breadcrumb, eggs, flour, maggi', 'food/hoorische.jpg', 3],
    ['Grommbeerkerschdscher', 'potato, onion, maggi', 'food/krommbeerkerschdscher.jpg', 4],
    ['Faasendkiechelcher', 'flour, butter, sugar, yeast, milk, eggs, maggi', 'food/faasendkiechelcher.jpg', 5],
    ['Grommbeersalad', 'potato, vinegar, cream, maggi, dried meat, eggs', 'food/kartoffelsalat.jpg', 4],
    ['Grommbeernsupp', 'potato, sour cream, sausages, butter, carrots, celery, maggi', 'food/kartoffelsuppe.jpg', 2],
    ['Plattgeschmelzte', 'potato, butter, onions, maggi', 'food/plattgeschmeltzde.jpg', 4],
    ['Bettseichersalat', 'hawkbit, dried meat, onion, eggs, vinegar, oil, potato, maggi', 'food/bettseicher.jpg', 5],
    ['Schwenker', 'meat, curry, paprika, oil, maggi, onion', 'food/schwenker.jpg', 5],
    ['Frikadellen', 'minced meat, onion, old bread, egg, paprika, garlic, maggi, butter', 'food/frikadelle.jpg', 5],
    ['Lyoner mit Weck', 'meat, bun, maggi', 'food/lyoner.jpg', 3],
    ['Merguez', 'lamb shoulder meat, pork, garlic, water, maggi', 'food/merguez.jpg', 4],
    ['Bohnensupp', 'potato, dried meat, onions, beans, maggi, fondor', 'food/bohnensuppe.jpg', 3],
    ['Dreggische Grommbeeren', 'potato, liver sausage, blood sausage, maggi', 'food/dreggische.jpg', 3],
    ['Weck mit Eiaufstrich', 'bun, egg, flour, bacon, milk, chives, maggi', 'food/eiaufstrich.jpg', 4],
    ['Kappesmängs', 'potato, carrot, onion, sugar, maggi', 'food/kappes.jpg', 5],
    ['Grombeernpuffer', 'potato, egg, flour, applesauce, maggi', 'food/kartoffelpuffer.jpg', 4],
    ['Kohlroulade', 'white cabbage, minced meat, onion, egg, parsley, mustard, maggi', 'food/rouladen.jpg', 5],
    ['Leberknödel', 'ground liver, minced meat, egg, flour, breadcrumbs, marjoram, maggi, fondor',
     'food/leberknoedel.jpg', 5],
    ['Lyonerpfanne', 'potatoe, lyoner, onion, marjoram, maggi', 'food/lyonerpfanne.jpg', 4],
    ['Mehlknäpp', 'mineral water, milk, curd, egg, flour, maggi', 'food/wasserspatzen.jpg', 5],
    ['Querbeet', 'potatoe, beef, pork, oil, nutmeg, maggi', 'food/quer.jpg', 3],
    ['Rostige Ritter', 'bun, milk, egg, sugar, cinnamon, custard', 'food/ritter.jpg', 4],
    ['Sauerbraten mit Schneebällcher un Rotkraut',
     'sauerbraten, potatoes, parsley, egg, flour, nutmeg, red cabbage, onion, apple, vinegar, juniper berries, bay leaves',
     'food/sauerbraten.jpg', 4]
]
for dish in raw:
    name, ingredients, pic_src, rating = dish
    picture = os.popen(f'echo "data:image/jpeg;base64,$(base64 -w 0 {pic_src})"').read().strip()
    code = f"""
        let li = document.createElement('li');
        li.className = 'list-group-item';
        let row = document.createElement('div');
        row.className = 'row';
        let col2 = document.createElement('div');
        col2.className = 'col-2';
        let img = document.createElement('img');
        img.src = '{picture}';
        img.style = 'width: 100%; height: 100%; object-fit: cover;';
        col2.appendChild(img);
        row.appendChild(col2);
        let col10 = document.createElement('div');
        col10.className = 'col-10';
        let h5 = document.createElement('h5');
        h5.innerText = '{name}';
        col10.appendChild(h5);
        let p = document.createElement('p');
        p.innerText = '{ingredients}';
        col10.appendChild(p);
        let span = document.createElement('span');
        span.className = 'text-warning';
        span.style = 'margin-right:5px;';
        for (let i = 1; i <= 5; i++) {{
            if (i <= {rating}) {{
                span.innerHTML += "&#9733; ";
            }} else {{
                span.innerHTML +=  "&#9734; ";
            }}
        }}       
        col10.appendChild(span);
        col10.innerHTML += {rating} + ' stars';
        row.appendChild(col10);
        li.appendChild(row);
        document.getElementById('mensa-menu-list').appendChild(li);
    """
    open(f'../dishes/{name}.js', 'w').write(code)
