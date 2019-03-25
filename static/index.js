
// Search Function
function searchFunction() {
    let input = document.getElementById('myInput');
    console.log(input.value)
    let filter = input.value.toUpperCase();
    let list = document.getElementsByClassName("all-recipes")[0];
    console.log(list)
    let div = list.getElementsByClassName("message");
    console.log(div)
    for (let i = 0; i < div.length; i++) {
        let desc = div[i];
        console.log(desc)
        let txtValue = desc.textContent || desc.outerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            div[i].style.display = "block";
        }
        else {
            div[i].style.display = "none";
        }
    }
}

let reviewsList = document.getElementById('all-reviews');
let reviews = reviewsList.getElementsByClassName("message-body");
let sum = 0

for (let i = 0; i < reviews.length; i++) {
    let rating = reviews[i].innerText.charAt(0)
    let ratingInt = parseInt(rating)
    sum = sum + ratingInt;
}

let roundedAverage = 0.0;

if (reviews.length != 0) {
    let average = (sum / reviews.length)
    //tofixed rounds the rating to the first decimal place
    roundedAverage = average.toFixed(1);
}
let averageDiv = document.getElementById("averageDiv");

if (roundedAverage == 0) {
    averageDiv.innerText = `Be the first to rate this recipe!`;
}
else {
    averageDiv.innerText = `Average Rating: ${roundedAverage}`;
}

let numberOfRatings = document.getElementById("numberOfRatings");
numberOfRatings.innerText = `Number of ratings: ${reviews.length}`;
document.getElementById("myVideo").playbackRate = 0.7;
