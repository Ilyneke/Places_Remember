const OL = window.ol

let draw;
const source = new OL.source.Vector({wrapX: false});
const vector = new OL.layer.Vector({
    source: source,
  });


const map = new OL.Map({
  target: 'map',
  layers: [
    new OL.layer.Tile({
      source: new OL.source.OSM(),
    }),
    vector
  ],
  view: new OL.View({
    center: [6747055.141706806, 7729412.378274312],
    zoom: 9,
  }),
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
    map.removeInteraction(draw);
})