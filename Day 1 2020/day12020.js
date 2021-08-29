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
