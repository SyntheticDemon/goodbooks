$(document).ready(function() {
    // catch the form's submit event
    $('#review-form').submit(function() {
        // create an AJAX call
        $.ajax({
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: "/write_review/",
            // on success
            success: function(response) {
                if (response['errors'] != null) {
                    document.getElementById("review-errors").innerText = response['errors']
                    document.getElementById("review-errors").style.color = "red"

                } else if (response['success'] != null) {
                    document.getElementById("review-errors").innerText = response['success']
                    document.getElementById("review-errors").style.color = "green"
                } else {
                    document.getElementById("review-errors").innerText = response['data']
                }
            },
            error: function(response) {
                // alert the error if any error occured
                document.getElementById("review-errors").innerText = "Server Did not Respond ,Check your Connection"
                document.getElementById("review-errors").style.color = "red"
            }
        });
        document.getElementById("review-errors").style.display = "block"

        return false;
    });
})