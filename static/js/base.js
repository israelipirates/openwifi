$(document).ready(function() {
  init();
  update_networks();
  register_clicks();
});

init = function() {
  var mapOptions = {
    center: new google.maps.LatLng(32.0833, 34.8000),
    zoom: 15,
    zoomControl: true,
    zoomControlOptions: {
      style: google.maps.ZoomControlStyle.SMALL
    },
    mapTypeControl: false,
    streetViewControl: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
};

add_marker = function(title, lat, long) {
  var marker = new google.maps.Marker({
    title: title,
    position: new google.maps.LatLng(lat, long),
    icon: {
      path: google.maps.SymbolPath.CIRCLE,
      scale: 7
    },
    draggable: false,
    map: map
  });
};

update_networks = function() {
  $.get('/networks', function(res) {
    $.each(res['networks'], function(index, val) {
      add_marker.apply(this, val);
    });
  });
};

register_clicks = function() {
  google.maps.event.addListener(map, 'click', function(event) {
    $('#add-hotspot-lat').val(event.latLng.lat());
    $('#add-hotspot-lng').val(event.latLng.lng());
    $('#add-hotspot-modal').modal('show');
  });
};
