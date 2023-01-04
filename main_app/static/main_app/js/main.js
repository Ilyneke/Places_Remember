const OL = window.ol


let draw;
const source = new OL.source.Vector({wrapX: false});
const vector = new OL.layer.Vector({
    source: source,
  });
const view = new OL.View({
    center: [6747055, 7729412],
    zoom: 10,
  })
const map = new OL.Map({
  target: 'map',
  layers: [
    new OL.layer.Tile({
      source: new OL.source.OSM(),
    }),
    vector
  ],
  view: view
});

map.on('singleclick', function (evt) {
    // на время.
    const coordinate = evt.coordinate;
    console.log(coordinate)

});


function addInteraction() {
    draw = new OL.interaction.Draw({
      source: source,
      type: "Point",
    });
    map.addInteraction(draw);
}
addInteraction();

draw.on("drawstart", (e) => {
    source.clear()
})

draw.on("drawend", (e) => {
    let coord = e.feature.getGeometry().getCoordinates();
    let field0 = window.document.getElementById('lat').value = coord[0];
    let field1 = window.document.getElementById('lng').value = coord[1];
    let field2 = window.document.getElementById('zoom').value = view.getZoom();
    console.log(field0, field1, field2)

    view.animate({
        center: coord,
        duration: 900,
        zoom: 15,
    })
})
let mapIdArray = []
const mapId = window.document.querySelectorAll('.view_map')

let lat = window.document.querySelectorAll('.take_lat');
let lng = window.document.querySelectorAll('.take_lng');
let zoom = window.document.querySelectorAll('.take_zoom');
let coordinateMemory = [0, 0];
let zoomMemory;
console.log(zoom)

mapId.forEach((item) => {
    lat.forEach((item_lat) => {
        if (item_lat.getAttribute('data-id') == item.getAttribute('data-id')) {
            coordinateMemory[0] = item_lat.value
        }
        console.log(item_lat, 'qwerty')
    })
    lng.forEach((item_lng) => {
        if (item_lng.getAttribute('data-id') == item.getAttribute('data-id')) {
            coordinateMemory[1] = item_lng.value
        }
    })
    zoom.forEach((item_zoom) => {
        if (item_zoom.getAttribute('data-id') == item.getAttribute('data-id')) {
            zoomMemory = item_zoom.value
        }
    })
    const view = new OL.View({
        center: coordinateMemory,
        zoom: zoomMemory,
    })
    let pointFeature = new OL.Feature({
            geometry: new OL.geom.Point(coordinateMemory),
            name: name
        });
    // view.animate({
    //     center: coordinateMemory,
    //     duration: 900,
    //     zoom: zoomMemory,
    // })
    const source2 = new OL.source.Vector({features: [pointFeature]});
    const vector2 = new OL.layer.Vector({
        source: source2,
      });
    const map2 = new OL.Map({
    target: item,
    layers: [
        new OL.layer.Tile({
        source: new OL.source.OSM(),
        }),
    vector2
    ],
    view: view
});

})

// const map2 = new OL.Map({
//   target: mapIdArray,
//   layers: [
//     new OL.layer.Tile({
//       source: new OL.source.OSM(),
//     }),
//     vector2
//   ],
//   view: view
// });
//
// view.animate({
//         center: coordinateMemory,
//         duration: 900,
//         zoom: zoomMemory,
//     })
