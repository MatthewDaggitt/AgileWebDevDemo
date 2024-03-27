

var numberOfStudentsRemove = 0;

function sayHi() {
  alert("Hi2");
  alert("Hi3");
}

function removeStudent() {
  // Update the database
  numberOfStudentsRemove += 1;
  showNumberOfStudentsRemoved();
}

function showNumberOfStudentsRemoved() {
  let result = prompt("Give me a number", 7);
  console.log("Result: " + result);
}