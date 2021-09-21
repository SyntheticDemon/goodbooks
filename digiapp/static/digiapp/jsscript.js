function hide_password_value(id) {
    document.getElementById(id).type = 'password'
}

function becomered(id) {
    document.getElementById(id).style = "border-bottom-width:5px"

}

function rate(id, score) {
    clicked = document.getElementById(id).getAttribute("clicked")
    document.getElementById("score").setAttribute("value", score + 1)
    elements = document.getElementById(id).childNodes
    if (clicked == "false") {
        for (let i = 1; i <= score * 2 + 1; i++) {
            if (i % 2 == 1) {
                elements[i].style = "color:red"
            }

        }
        document.getElementById(id).setAttribute("clicked", "true")
        console.log(document.getElementById(id).getAttribute("clicked"))

    } else if (clicked == "true") {
        for (element of elements) {
            element.style = "color:black"
        }
        for (let i = 1; i <= score * 2 + 1; i++) {
            if (i % 2 == 1) {
                elements[i].style = "color:red"
            }

        }
        document.getElementById(id).setAttribute("clicked", "false")
    }
}


function gray_it_out() {
    document.getElementById("layer").style.backgroundColor = "rgba(118, 119, 118, 0.685);"

}

function white_it_out() {
    document.getElementById("layer").style = "background-color:#0000;"

}