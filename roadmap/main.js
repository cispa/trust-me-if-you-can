function findLCS(s1, s2) {
  const n = s1.length;
  const m = s2.length;

  const dp =
    new Array(n + 1).fill(null).map(() =>
      new Array(m + 1).fill(0));
  for (let i = 0; i <= n; i++) {
    dp[i][0] = 0;
  }
  for (let i = 0; i <= m; i++) {
    dp[0][i] = 0;
  }

  for (let ind1 = 1; ind1 <= n; ind1++) {
    for (let ind2 = 1; ind2 <= m; ind2++) {
      if (s1[ind1 - 1] === s2[ind2 - 1]) {
        dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1];
      } else {
        dp[ind1][ind2] =
          Math.max(dp[ind1 - 1][ind2],
            dp[ind1][ind2 - 1]);
      }
    }
  }

  const len = dp[n][m];
  let i = n;
  let j = m;
  let index = len - 1;
  let str = "";

  for (let k = 0; k < len; k++) {
    str += "$"; // Dummy string 
  }

  while (i > 0 && j > 0) {
    if (s1[i - 1] === s2[j - 1]) {
      str =
        str.slice(0, index) + s1[i - 1] +
        str.slice(index + 1);
      index--;
      i--;
      j--;
    } else if (s1[i - 1] > s2[j - 1]) {
      i--;
    } else {
      j--;
    }
  }

  return str.length;
}

const MODALS = document.getElementsByName('info-modal');

function show(text) {
  var lds = {};
  for (var m of MODALS) {
    lds[findLCS(text, m.getAttribute('data-text'))] = m;
  }
  var arr = Object.keys(lds).map(k => +k);
  var max = arr.reduce((a, b) => Math.max(a, b), -Infinity);
  var _ = new bootstrap.Modal(lds[max], {}).show()
}

window.onload = function () {
  var gs = document.querySelectorAll('.mxgraph > svg:nth-child(1) > g:nth-child(2) > g:nth-child(2)')[0].children
  for (var g of gs) {
    var texts = g.querySelectorAll('g:nth-child(1) > foreignObject:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)');
    for (var t of texts) {
      if (window.getComputedStyle(t, null).getPropertyValue('white-space') === "nowrap") { continue; }
      console.log(t.innerText);
      if (t.innerText.includes('NEXT:') || t.innerText.trim() == 'Done') { continue; }
      t.addEventListener('click', function (e) { show(e.target.innerText) });
      t.style.cursor = 'pointer';
    }
    /** 
    var rects = g.querySelectorAll('rect[stroke="rgb(0, 0, 0)"]');
    for (var r of rects) {
      r.addEventListener('click', function () { show(r.innerText) });
      r.style.cursor = 'pointer';
    }
    **/
  }
}