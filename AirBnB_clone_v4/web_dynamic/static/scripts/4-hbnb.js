// function generates the display of listed entries
let display = function pageDisplay (data) {
  $('.places').empty();
  for (let i = 0; i < data.length; i++){
    let place = data[i];
    //console.log($('.places'));
    $('.places').append('<article>' + 
    '<div class="title">' +
    '<h2>' + (place['name']) + '</h2>' +
    '<div class="price_by_night">' +
    (place['price_by_night']) +

   '</div>' + 
  '</div>' +
  '<div class="information">' + 
    '<div class="max_guest">' +
'<i class="fa fa-users fa-3x" aria-hidden="true"></i>' +
'<br />' + 
 (place['max_guest']) + 'Guests' +
    '</div>' +
    '<div class="number_rooms">' +
'<i class="fa fa-bed fa-3x" aria-hidden="true"></i>' +
'<br />' +
 (place['number_rooms']) + 'Bedrooms' +
    '</div>' + 
    '<div class="number_bathrooms">' +
'<i class="fa fa-bath fa-3x" aria-hidden="true"></i>' +
'<br />' +
(place['number_bathrooms']) + 'Bathroom' +
    '</div>' + 
  '</div>' + 
  '<div class="description">' +
    (place['description']) +
    "</article>")
}
};

// checks whether document has been rendered
$(document).ready(function () {
  let url = "http://0.0.0.0:5001/api/v1/status/";
  $.get(url, function(data, textStatus) {
    if (textStatus == 'success') {
      $('#api_status').addClass("available");
    }
    else {
      $('#api_status').removeClass("available");
    }
  });

  // handles checked boxes
  let amenities = [];
  let myList = [];
  $('input:checkbox').change(
    function () {
      if ($(this).is(':checked')) {
        amenities.push(this);
      } else {
        amenities = amenities.filter(e => e !== this);
      }
      let result = [];
      myList = [];
      for (let i = 0; i < amenities.length; i++) {
        let name = $(amenities[i]).attr('data-name');
        //let myAttr = $(amenities[i]).attr('data-id');
        result.push(name);
        myList.push($(amenities[i]).attr('data-id'));
      }
      if (result.length === 0) {
        $('.amenities h4').html('&nbsp;');
      } else {
        $('.amenities h4').text(result.join(', '));
      }
    });

  // POST request for all places          
  let postUrl = 'http://0.0.0.0:5001/api/v1/places_search/';
  let amenitiesDict = {};

  function myRequest() {
  $.ajax({
    type: 'POST',
    url: postUrl,
    data: JSON.stringify(amenitiesDict),
    contentType: 'application/json',
    success: function (data) {
      display(data);
    }
  });
};

// function handles when search button has been clicked
$(':button').click(function () {
  $('.places').empty();
  amenitiesDict = {};
  amenitiesDict['amenities'] = myList;
  myRequest();
  });

// generates first call to home page  
$(window).on('load', function() {
  myRequest();
});
}); 
