// js version of py functions for practice
// final working solutions

// DAY 1
// Part 1

// <first function>
function findPair(nums) {
    for (let num of nums) {
      for (let numo of nums) {
        let newVar = num + numo;
        if (newVar == 2020) {
          console.log(`${num} multiplied by ${newVar} equals ${num * newVar}`);
        }
      }
    }
  };


// <second function that's better>
function findPair(nums) {
    for (const num of nums) {
      let sub = 2020 - num;
       if (nums.includes(sub)) 
        console.log(`${num} multiplied by ${sub} equals ${num * sub}`);
      }
  };


// Part 2

function threeAdds(nums) {
    for (const num of nums) {
      for (const item of nums){
        const small = 2020 - num - item
        if (nums.includes(small)){
          console.log(`${num} multiplied by ${item} and ${small} equals ${num * item * small}`);
    }}}
  };


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

  