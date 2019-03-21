

console.log("JS is attached! yay")

// Search Function
function searchFunction() {
    var input = document.getElementById('myInput');
    var filter = input.value.toUpperCase();
    var list = document.getElementsByClassName("all-recipes")[0];
    var div = list.getElementsByClassName("recipe");
    console.log(div)
    for (var i = 0; i < div.length; i++) {
    var desc = div[i].getElementsByClassName("description")[0];
            var txtValue = desc.textContent || desc.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                div[i].style.display = "block";
                } 
                else {
                div[i].style.display = "none";
                }
        }
    }