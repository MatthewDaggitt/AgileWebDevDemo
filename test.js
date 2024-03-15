

var numberOfStudentsEjected = 0;

function sayHi() {
  alert("Hi2");
  alert("Hi3");
}

function ejectStudent() {
  // Update the database
  numberOfStudentsEjected += 1;
  displayNumberOfStudentsEjected();
}

function displayNumberOfStudentsEjected() {
  let result = prompt("Give me a number", 7);
  console.log("Result: " + result);
}