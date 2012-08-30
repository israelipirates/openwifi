$(document).ready(function() {
  init();
  update_hotspots();
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
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    styles: [{
      stylers: [
        { invert_lightness: true },
        { hue: "#0091ff" }
      ]
    }]
  };
  map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
};

add_marker = function(ssid, password, lat, lng) {
  var marker = new google.maps.Marker({
    title: ssid,
    position: new google.maps.LatLng(lat, lng),
    icon: {
      path: google.maps.SymbolPath.CIRCLE,
      scale: 7
    },
    draggable: false,
    map: map
  });
  google.maps.event.addListener(marker, 'click', function() {
    if (!password) {
      password = '<none>';
    }
    alert('SSID: ' + ssid + ", Password: " + password);
  });
};

update_hotspots = function() {
  $.get('/hotspots', function(res) {
    $.each(res['hotspots'], function(index, val) {
      var lat = val['lat'];
      var lng = val['lng'];
      var ssid = val['ssid'];
      var password = val['password'];
      console.log(ssid, password, lat, lng);
      add_marker(ssid, password, lat, lng);
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
