const target = document.getElementById('target');
const items = [
    'First item',
    'Second item',
    'Third item'];

const val = document.createElement('ul')
items.forEach((str, index) => {
  const lista = document.createElement('li');
    lista.textContent = str;
    if (index === 1) {
        lista.classList.add('my-item')}
    val.appendChild(lista);
    });
target.appendChild(val);

//vittu mitä paskaa lol