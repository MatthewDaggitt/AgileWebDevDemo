

var numberOfStudentsEjected = 0;

function sayHi() {
  alert("Hi2");
  alert("Hi3");
}

function ejectStudents() {
  // Update the database
  numberOfStudentsEjected += 2;
  displayNumberOfStudentsEjected();
}

function displayNumberOfStudentsEjected() {
  let result = prompt("Give me a number", 7);
  console.log("Result: " + result);
}