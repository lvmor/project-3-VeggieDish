// Search Function
function searchFunction() {
    var input = document.getElementById('myInput');
    console.log(input.value)
    var filter = input.value.toUpperCase();
    var list = document.getElementsByClassName("all-recipes")[0];
    console.log(list)
    var div = list.getElementsByClassName("message");
    console.log(div)
    for (var i = 0; i < div.length; i++) {
        var desc = div[i];
        console.log(desc)
        var txtValue = desc.textContent || desc.outerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            div[i].style.display = "block";
        }
        else {
            div[i].style.display = "none";
        }
    }
}


var reviewsList = document.getElementById('all-reviews');
console.log(reviewsList)
var reviews = reviewsList.getElementsByClassName("message-body");
console.log(reviews)
//function allReviews() {
let sum = 0
let amount = 0
for (var i = 0; i < reviews.length; i++) {
    var rating = reviews[i].innerText.charAt(0)
    var ratingInt = parseInt(rating)
    sum = sum + ratingInt;
    amount++;
}
let average = 0.0;
if (sum != 0) {
    let avg = (sum / amount)
    //tofixed rounds the rating to the first decimal place
    average = avg.toFixed(1);
}
let averageDiv = document.getElementById("averageDiv");
if (average == 0) {
    averageDiv.innerText = `Be the first to rate this recipe!`;
}
else {
    averageDiv.innerText = `Average Rating: ${average}`;
}

let numberOfRatings = document.getElementById("numberOfRatings");
numberOfRatings.innerText = `Number of ratings: ${amount}`;

