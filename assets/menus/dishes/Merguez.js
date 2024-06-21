
        let li = document.createElement('li');
        li.className = 'list-group-item';
        let row = document.createElement('div');
        row.className = 'row';
        let col2 = document.createElement('div');
        col2.className = 'col-2';
        let img = document.createElement('img');
        img.style = 'width: 100%; height: 100%; object-fit: cover;';
        col2.appendChild(img);
        row.appendChild(col2);
        let col10 = document.createElement('div');
        col10.className = 'col-10';
        let h5 = document.createElement('h5');
        h5.innerText = 'Merguez';
        col10.appendChild(h5);
        let p = document.createElement('p');
        p.innerText = 'lamb shoulder meat, pork, garlic, water, maggi';
        col10.appendChild(p);
        let span = document.createElement('span');
        span.className = 'text-warning';
        span.style = 'margin-right:5px;';
        for (let i = 1; i <= 5; i++) {
            if (i <= 4) {
                span.innerHTML += "&#9733; ";
            } else {
                span.innerHTML +=  "&#9734; ";
            }
        }       
        col10.appendChild(span);
        col10.innerHTML += 4 + ' stars';
        row.appendChild(col10);
        li.appendChild(row);
        document.getElementById('mensa-menu-list').appendChild(li);
    