const hakuKysely = "https://api.chucknorris.io/jokes/random";
haeData();
async function haeData() {
  try {
    const response = await fetch(hakuKysely);
    const jsonData = await response.json();
    kasitteleData(jsonData);
  }
  catch (error) {
    console.log(error.message);
  }
}
function kasitteleData(jsonData) {
  console.log(jsonData.value);
}