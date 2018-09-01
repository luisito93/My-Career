$(document).ready(function(){
  
  // loading spinner
  let showSpinner = function() {
    $("#job-search-results").LoadingOverlay("show", {
      image       : "",
      fontawesome : "fa fa-cog fa-spin"
    });  
  }

  let hideSpinner = function() {
    $("#job-search-results").LoadingOverlay("hide", true);
  }
  

  // search jobs form
   let searchForm = $(".search-form");
   let SearchResults = $("#job-search-results");

   searchForm.submit(function(event){
    event.preventDefault();

    let thisForm = $(this);
    let actionEndpoint = thisForm.attr("data-endpoint");
    let formData = thisForm.serialize();
    showSpinner();

    $.ajax({
        url: actionEndpoint,
        method: "GET",
        data: formData,
        success: function(data){
          let body = $(data);
          $("#result-count").html(body.find('#result-count'));
          SearchResults.html(body.find('.search-result'));
          $(".pagination").html(body.find('.pagination'));
          hideSpinner();
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
    showSpinner();

    $.ajax({
        url: urlEndpoint,
        method: "GET",
        data: '',
        success: function(data){
          let body = $(data);
          hideSpinner();
          SearchResults.html(body.find('.search-result'));
          $(".pagination").html(body.find('.pagination'));
        },
        error: function(error){ 
          console.log(error);
        }
    });
   });

   // sort by per page
   let sortPerPage = $(".sort-per-page");
   sortPerPage.change(function(event) {
    event.preventDefault();

    let $this = $(this);
    let actionParams = $this.val();
    let actionEndpoint = $this.attr("data-endpoint");
    let urlEndpoint = `${actionEndpoint}${actionParams}`;
    showSpinner();

    $.ajax({
        url: urlEndpoint,
        method: "GET",
        data: '',
        success: function(data){
          let body = $(data);
          SearchResults.html(body.find('.search-result'));
          $(".pagination").html(body.find('.pagination'));
          hideSpinner();
        },
        error: function(error){ 
          console.log(error);
        }
    });
   });

   // sort by order
  let sortOrder = $(".sort-order");
  sortOrder.change(function(event) {
    event.preventDefault();

    let $this = $(this);
    let actionParams = $this.val();
    let actionEndpoint = $this.attr("data-endpoint");
    let urlEndpoint = `${actionEndpoint}${actionParams}`;
    showSpinner();

    $.ajax({
        url: urlEndpoint,
        method: "GET",
        data: '',
        success: function(data){
          let body = $(data);
          SearchResults.html(body.find('.search-result'));
          $(".pagination").html(body.find('.pagination'));
          hideSpinner();
        },
        error: function(error){ 
          console.log(error);
        }
    });
   });

});