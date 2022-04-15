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
    content: "Click the map to get Lat/Lng!",
    position: myLatlng,
  });

  infoWindow.open(map);

  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {

    // Close the current InfoWindow.
    infoWindow.close();
    
    // Send lat and long to python script for prediction
    runPyScript([mapsMouseEvent.latLng.lat(), mapsMouseEvent.latLng.lng()])
    
    // Create a new InfoWindow.
    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
    });

    // console.log(mapsMouseEvent.latLng.lat())
    infoWindow.setContent(
      JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
    );
    infoWindow.open(map);
  });
}

function runPyScript(inputs){
  var jqXHR = $.ajax({
      type: "POST",
      url: "/pred",
      data: { lat: inputs[0], long: inputs[1] }
  }).done(function(response) {
    text = response.pred
    document.getElementById("location").innerHTML = text
  });
}
