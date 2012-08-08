$(document).ready(function() {
  var mapOptions = {
    center: new google.maps.LatLng(32.0833, 34.8000),
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
});
