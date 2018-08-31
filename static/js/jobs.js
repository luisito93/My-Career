$(document).ready(function(){
  
  // search jobs form
   let searchForm = $(".search-form");
   let SearchResults = $("#job-search-results");

   searchForm.submit(function(event){
    event.preventDefault();

    let thisForm = $(this);
    let actionEndpoint = thisForm.attr("data-endpoint");
    let formData = thisForm.serialize();

    console.log(formData);
    $.ajax({
        url: actionEndpoint,
        method: "GET",
        data: formData,
        success: function(data){
          let body = $(data);
          $("#result-count").html(body.find('#result-count'));
          SearchResults.html(body.find('.search-result'));
          $(".pagination").html(body.find('.pagination'));
        },
        error: function(error){ 
          console.log(error);
        }
    });
   });

   // Ajax pagination
   let pageNextPrev = $(".page-next-prev");
   $(document.body).on("click", ".page-next-prev", function(event){
    event.preventDefault();

    let thisPage = $(this);
    let actionParams = thisPage.attr("href");
    let actionEndpoint = thisPage.attr("data-endpoint");
    let urlEndpoint = `${actionEndpoint}${actionParams}`;

    $.ajax({
        url: urlEndpoint,
        method: "GET",
        data: '',
        success: function(data){
          let body = $(data);
          SearchResults.html(body.find('.search-result'));
          $(".pagination").html(body.find('.pagination'));
        },
        error: function(error){ 
          console.log(error);
        }
    });
   });


});