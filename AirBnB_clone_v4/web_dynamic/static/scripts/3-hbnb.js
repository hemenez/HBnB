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

  // POST request for all places
  console.log("making post request --------> ")
  let postUrl = 'http://0.0.0.0:5001/api/v1/places_search/';
  $.ajax({
    type: 'POST',
    url: postUrl,
    data: '{}',
    contentType: 'application/json',
    success: function (data) {
      console.log(data);
      for (let i = 0; i < data.length; i++){
        let place = data[i];
        console.log(place);
        console.log(place['name']);
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
  }
  });
  let amenities = [];
  $('input:checkbox').change(
    function () {
      /*console.log(this);*/
      if ($(this).is(':checked')) {
        amenities.push(this);
      } else {
        amenities = amenities.filter(e => e !== this);
      }
      let result = [];
      for (let i = 0; i < amenities.length; i++) {
        let name = $(amenities[i]).attr('data-name');
        result.push(name);
      }
      if (result.length === 0) {
        $('.amenities h4').html('&nbsp;');
      } else {
        $('.amenities h4').text(result.join(', '));
      }
    });
});
