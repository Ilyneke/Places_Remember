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

draw.on("drawend", (e) => {
    let coord = e.feature.getGeometry().getCoordinates();
    view.animate({
        center: coord,
        duration: 900,
        zoom: 15,
    })
    map.removeInteraction(draw);
})