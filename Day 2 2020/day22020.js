// js version of py functions for practice
// final working solutions

// DAY 2
// Part 1

function makeList(pwords) {
  const newPwords = pwords
    .replaceAll(':', '')
    .replaceAll('-', ' ')
    .split('\n')
    .map(substr => substr.split(' '));

  let validCounter = 0;
  
  for (let item of newPwords) {
    let letterCounter = 0;
    let minim = item[0];
    let maxim = item[1];
    let special = item[2];
    let word = item[3];
  
    for (let letter of word) {
      if (letter == special) {
        letterCounter++;          
      }
    }
    if (letterCounter >= minim && letterCounter <= maxim) {
      validCounter++
      }
    }
  return validCounter;
};


// Part 2
