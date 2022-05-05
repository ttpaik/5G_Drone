const bounds = {
  north: 42.356918,
  south: 42.343574,
  west: -71.125084,
  east: -71.090837,
}

function initMap() {
  const myLatlng = { lat: 42.349494, lng: -71.108135 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    disableDefaultUI: true,
    center: myLatlng, 
    zoomControl: true, 
    scrollwheel: true, 
    disableDoubleClickZoom: true, 
    restriction: {
      latLngBounds: bounds,
      strictBounds: true,
    },
  });
  // Create the initial InfoWindow.
  let infoWindow = new google.maps.InfoWindow({
    content: "Click map for prediction at that latitude/longitude!",
    position: myLatlng,
  });

  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {

    // Close the current InfoWindow.
    //infoWindow.close();

    alt = getVal();
    if (alt == '') alt = 0;

    // Send lat and long to python script for prediction
    pred = runPyScript([mapsMouseEvent.latLng.lat(), mapsMouseEvent.latLng.lng(), alt])

    // Create a new InfoWindow.
    var infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
      content: pred,
    });

    infoWindow.open(map);
  });
}

function runPyScript(inputs){
  var jqXHR = $.ajax({
      type: "POST",
      async: false, 
      url: "/pred",
      data: { lat: inputs[0], long: inputs[1], alt: inputs[2] }
  }).done(function(response) {
    pred = response.pred
  });
  return pred
}

function getVal() {
  const val = document.querySelector('input').value;
  return val;
}