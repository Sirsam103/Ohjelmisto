const amount = prompt('Enter the amount of candidates');
const candidates = [];
for (let i = 1; i <= amount; i++) {
  const candName = prompt(`Name for candidate ${i}`);
  candidates.push({name: candName, votes: 0});
}
const voters = prompt('Number of voters:')
for (let i = 1; i <= voters; i++) {
  const vote = prompt(`Voter ${i} enter the name of the person you want to vote. (Leave blank for an empty vote)`)
  const votedCand = candidates.find(cand => cand.name ===vote)
  if (votedCand) votedCand.votes++;
}
candidates.sort((i, j) => j.votes - i.votes)
console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes!`)
console.log('results:')
for (let i = 0; i <= amount; i++) {
  console.log(`${candidates[i].name}: ${candidates[i].votes} votes`)
}
