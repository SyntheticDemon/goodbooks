const search_result_container_name="search-result-container"
const search_form_name="search-form"
const search_result_mother_container="search-result"
function construct_search_result_element(json_data){
        let element =document.getElementById(search_result_container_name)
        let elements =element.getElementsByTagName("ul")
        elements[0].innerHTML="<img "+'src="'+json_data['img_link']+'" style="height:50px;">'
        elements[1].innerHTML=json_data['name']
        elements[2].innerHTML=json_data['description']
        element.style.display="block"
        return element
}
function hide_search_bar(){
        document.getElementById(search_result_mother_container).style.display="none"
}
    $(document).ready(function() {
        // catch the form's submit event
        $('#search-form').submit(function() {
            // create an AJAX call
            $.ajax({
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: "/search/",
                // on success
                success: function(response) {
                
                    console.log(response)

                    document.getElementById(search_result_mother_container).style.display="block"

                    if(response.length==0){

                        document.getElementById(search_result_mother_container).appendChild(construct_search_result_element(result))

                    }
                    for (let result of response){

                        document.getElementById(search_result_mother_container).appendChild(construct_search_result_element(result))
                    }
                    
                },
                error: function(response) {
                    // alert the error if any error occured
                    alert("Search error , connection problems with server ")
                }
            });
    
            return false;
        });
})
