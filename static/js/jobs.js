$(document).ready(function(){
  
  // search jobs form
   let searchForm = $(".search-form");
   let SearchResults = $("#job-search-results");

   searchForm.submit(function(event){
    event.preventDefault();

    let thisForm = $(this);
    let actionEndpoint = thisForm.attr("data-endpoint")
    let formData = thisForm.serialize();

    console.log(formData);
    $.ajax({
        url: actionEndpoint,
        method: "GET",
        data: formData,
        success: function(data){
          let body = $(data);
          console.log(body);
          $("#result-count").html(body.find('#result-count'));
          // $(".sortby-sec").html(body.find('.sortby-sec'));
          SearchResults.html(body.find('.search-result'));
          $(".pagination").html(body.find('.pagination'));
          // $("#main_results").html(body.find('.result-block'));
        },
        error: function(error){ 
          console.log(error);
        }
    });
   });

});