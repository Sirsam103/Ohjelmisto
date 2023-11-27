const formElem = document.querySelector('#form');
const hakuElem = document.querySelector('input[name=q]');
console.log('--hakusana: ' + hakuElem);
const resultsElem = document.querySelector('#jokes')
let hakuLause = "https://api.chucknorris.io/jokes/search?query=";
formElem.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const hakuArvo = hakuElem.value;
    hakuLause += hakuArvo;
    console.log('--hakukysely: '+ hakuLause);
    haeData(hakuLause);
});
async function haeData(netq) {
    try {
        const response = await fetch(netq);
        const jsonData = await response.json();
        kasitteleData(jsonData);
    }
    catch (error) {
        console.log(error.message);
    }
}
function kasitteleData(jsonData) {
    for (let vitsi of jsonData.result) {
        let htmlkoodi =
            `<article>
                <p>${vitsi.value}<p>
             </article>`;
        resultsElem.innerHTML += htmlkoodi;
    }
}