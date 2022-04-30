function initMap() {
  const myLatlng = { lat: 42.349494, lng: -71.108135 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 16.5,
    disableDefaultUI: true,
    center: myLatlng,
    draggable: false, 
    zoomControl: false, 
    scrollwheel: false, 
    disableDoubleClickZoom: true, 
    gestureHandling: 'none'
  });
  // Create the initial InfoWindow.
  let infoWindow = new google.maps.InfoWindow({
    content: "Click map for prediction at that latitude/longitude!",
    position: myLatlng,
  });

  //infoWindow.open(map);

  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {

    // Close the current InfoWindow.
    infoWindow.close();

    alt = getVal();
    if (alt == '') alt = 0;

    // Send lat and long to python script for prediction
    text = runPyScript([mapsMouseEvent.latLng.lat(), mapsMouseEvent.latLng.lng(), alt])

    // Create a new InfoWindow.
    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
      content: text
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
    text = response.pred
    //document.getElementById("location").innerHTML = text
  });
  return text
}

function getVal() {
  const val = document.querySelector('input').value;
  return val;
}