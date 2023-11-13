'use strict';
const year = prompt('Type any year.');

if (year % 4 !== 0 || year % 100 === 0 && year % 400 !== 0) {
  document.querySelector('#target').innerHTML = 'The year, ' + year + ' is not a leap year.';
}
else {
  document.querySelector('#target').innerHTML = 'The year, ' + year + ' is a leap year.';
}