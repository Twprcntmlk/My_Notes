const testArray = ["1","2","3","5","6"]

// method adds new items to the front of an array.
testArray.unshift("0")
console.log("method adds new items to the front of an array", testArray)

// method removes the first item of an array.
testArray.shift("0")
console.log("method removes the first item of an array", testArray)

// method adds new items to the end of an array.
testArray.push("7")
console.log("method adds new items to the end of an array", testArray)

//method removes the last element of an array.
testArray.pop("7")
console.log("method removes the last element of an array", testArray)

// remove at (position)
const testShiftArray = ["1","2","3","5","6"]
testShiftArray.splice(3,1)
console.log("expect remove 1 at index 3", testShiftArray)

// add to (position)
const testShiftArray1 = ["1","2","3","5","6"]
testShiftArray.splice(3,0,"4")
console.log("expect remove 0 then add 4 at index 3",testShiftArray)

// remove 1 and add to (position)
const testShiftArray2 = ["1","2","3","5","6"]
testShiftArray1.splice(3,1,"4")
console.log("expect remove 1 then add 4 at index 3", testShiftArray1)

// remove 2 and add to (position)
const testShiftArray4 = ["1","2","3","5","6"]
testShiftArray2.splice(3,2,"4")
console.log("expect remove 2 then add 4 at index 3",testShiftArray2)

console.log("---------------------------------------------------------------------------------")


//slice
/*
The slice() method returns a shallow copy of a portion of an array
into a new array object selected from start to end (end not included)
where start and end represent the index of items in that array.
The original array will not be modified.
*/
const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

console.log("Expect show items at index 2 to end", animals.slice(2));
// Expected output: Array ["camel", "duck", "elephant"]

console.log("Expect show items at index 2 to 3", animals.slice(2, 4));
// Expected output: Array ["camel", "duck"]

console.log("Expect show items at index 1 to 4", animals.slice(1, 5));
// Expected output: Array ["bison", "camel", "duck", "elephant"]

console.log("Expect show items at 2 from end", animals.slice(-2));
// Expected output: Array ["duck", "elephant"]

console.log("Expect show items at 2nd idx from 1 end", animals.slice(2, -1));
// Expected output: Array ["camel", "duck"]

console.log("Expect show all items", animals.slice());
// Expected output: Array ["ant", "bison", "camel", "duck", "elephant"]

console.log("---------------------------------------------------------------------------------")

//sort
let testsortArray1 = ["a","acde","adeh","b","abc"]
console.log("Sorts alphabetically", testsortArray1.sort())

let testsortArray2 = [1, 30, 4, 21, 100000]
console.log("Sorting Numbers Sorts by Digits not Numerically", testsortArray2.sort())

testsortArray2.sort(function(a, b) {
    return a - b;
});
console.log("Sorts Numerically", testsortArray2)

//Sorting non-ASCII characters
const itemsASCII = ["réservé", "premier", "communiqué", "café", "adieu", "éclair"];
itemsASCII.sort((a, b) => a.localeCompare(b));

console.log("---------------------------------------------------------------------------------")

//Sorting array of objects
let itemsObject = [
    { name: "Edward", value: 21 },
    { name: "Sharpe", value: 37 },
    { name: "And", value: 45 },
    { name: "The", value: -12 },
    { name: "Magnetic", value: 13 },
    { name: "Zeros", value: 37 },
  ];

  // sort by value
  itemsObject.sort((a, b) => a.value - b.value);
  console.log("Sorts Items by value", itemsObject)
  // sort by name
  itemsObject.sort((a, b) => {
    const nameA = a.name.toUpperCase(); // ignore upper and lowercase
    const nameB = b.name.toUpperCase(); // ignore upper and lowercase
    if (nameA < nameB) {
      return -1;
    }
    if (nameA > nameB) {
      return 1;
    }

    // names must be equal
    return 0;
  });

console.log("Sorts Items by name", itemsObject)
