
var presentCups = JSON.parse(document.getElementById('presentCups').textContent);
var predictCups = JSON.parse(document.getElementById('predictCups').textContent);

// console.log(presentCups);
// console.log(predictCups);

let map;
let cells = [];
let polygons = [];
let polygon_centers = [];
let pre_cups = [];

let smallmap;
let small_map_components = [];

function initMap(){
    let center = { lat: 37.491834 ,lng: 127.007556 };
    if(predictCups.length != 0){
        let lat=0, long=0;
        for(let i in predictCups){
        lat += (predictCups[i]['lat1']+predictCups[i]['lat2']+predictCups[i]['lat3']+predictCups[i]['lat4'])/4;
        long += (predictCups[i]['long1']+predictCups[i]['long2']+predictCups[i]['long3']+predictCups[i]['long4'])/4;
        }
        lat = lat/predictCups.length;
        long = long/predictCups.length;
        
        center = { lat: lat ,lng: long }
    }

    map = new google.maps.Map( document.getElementById('map'), { zoom: 13, center: center });
    smallmap = new google.maps.Map( document.getElementById('smallmap'), { zoom: 17, center: center });

    cells = makeCells();
    polygons = makePolygons(cells);
    polygon_centers = makePolygonCenters(cells, map);
    pre_cups = makePreCups(map);
    setMapOnAll(pre_cups, map);
    setMapOnAll(polygon_centers, map);
    setMapOnAll(polygons, map);
}

function makeCells(){
    var cells = []
    for(var i in predictCups){
        coors = predictCups[i]
        const cellCoords = [
        { lat: coors['lat1'], lng: coors['long1'] },
        { lat: coors['lat2'], lng: coors['long2'] },
        { lat: coors['lat4'], lng: coors['long4'] },
        { lat: coors['lat3'], lng: coors['long3'] }
        ];
        cells.push(cellCoords);
    }
    return cells;
}

function makePolygons(cells){
    var polygons = [];
    for(var i in cells){
        var ploygon = new google.maps.Polygon({
        paths: cells[i],
        strokeColor: "#ffe54a",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#ffe54a",
        fillOpacity: 0.35
        });
        polygons.push(ploygon);
    }
    return polygons;
}

function makePolygonCenters(cells, map){
    var polygon_centers = [];
    const shape = {
    coords: [1, 1, 1, 20, 18, 20, 18, 1],
    type: "poly"
    };

    for(var i in cells){
        var lat =0.0, long =0.0;
        for (var j in cells[i]){
        lat += parseFloat(cells[i][j]['lat']);
        long += parseFloat(cells[i][j]['lng']);
        }
        lat = lat/cells[i].length;
        long = long/cells[i].length;
        // console.log(lat, long);
        var center = new google.maps.Marker({
        position: { lat: lat, lng: long },
        map,
        icon: '/static/assets/img/map/green_cup_resize2.png',
        shape: shape,
        title: i,
        zIndex: parseInt(i),
        label: {text : 'predictCups', fontSize : '0px'}
        });
        center.addListener("click", moveToDiv);
        polygon_centers.push(center);
    }
    return polygon_centers;
}

function makePreCups(map) {
    var pre_cups=[]
    const shape = {
    coords: [1, 1, 1, 20, 18, 20, 18, 1],
    type: "poly"
    };

    for (var i in presentCups) {
        const precup = presentCups[i];
        var pre_cup = new google.maps.Marker({
        position: { lat: precup['lat'], lng: precup['long'] },
        map,
        icon: '/static/assets/img/map/orange_cup_resize2.png',
        title: presentCups[i]['id'],
        zIndex: parseInt(i),
        label: {text : 'presentCups', fontSize : '0px'}
        });
        pre_cup.addListener("click", moveToDiv);
        pre_cups.push(pre_cup);
    }
    return pre_cups;
}

function setMapOnAll(markers, map){
    for(var i in markers){
        markers[i].setMap(map);
    }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers(markers) {
setMapOnAll(markers,null);
}

function moveToDiv(){
    if(small_map_components.length !=0){
        clearMarkers(small_map_components);
        small_map_components=[];
    }

    label = this.getLabel()['text'];
    index = this.getZIndex();

    let cup, marker_image, address, like, dislike, lat, long;
    if(label == 'predictCups'){
        cup = predictCups[index];
        let small_map_polygon = new google.maps.Polygon({
        paths: [
        { lat: cup['lat1'], lng: cup['long1'] },
        { lat: cup['lat2'], lng: cup['long2'] },
        { lat: cup['lat4'], lng: cup['long4'] },
        { lat: cup['lat3'], lng: cup['long3'] }
        ],
        strokeColor: "#ffe54a",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#ffe54a",
        fillOpacity: 0.35
        });
        small_map_components.push(small_map_polygon);

        lat = cup['lat1']+cup['lat2']+cup['lat3']+cup['lat4']/4.0;
        long = cup['long1']+cup['long2']+cup['long3']+cup['long4']/4.0;
        marker_image = '/static/assets/img/map/green_cup_resize2.png';
    }else{
        cup = presentCups[index];
        lat = cup['lat'];
        long = cup['long'];
        marker_image = '/static/assets/img/map/orange_cup_resize2.png';
    }
    address = cup['address'];
    like = cup['like'];
    dislike = cup['dislike'];
    id = cup['id'];
    
    $("#id").val(id);
    $("#label").val(label);
    $("#address").text(address);   
    $("#good").text(like);   
    $("#bad").text(dislike);

    let marker_latlnog = { lat: lat, lng: long };
    smallmap.setCenter(marker_latlnog);

    small_map_marker = new google.maps.Marker({
        position: marker_latlnog,
        smallmap,
        icon: marker_image,
        title: 'cup',
        zIndex: index,
        label: {text : label, fontSize : '0px'}
    });
    small_map_components.push(small_map_marker);
    setMapOnAll(small_map_components, smallmap);
    if($('#detail').hasClass("collapse")){
        $('#detail').removeClass("collapse");
    }
    $('#detail')[0].scrollIntoView({behavior: "smooth"});
}

$( document ).ready( function() {
    $('#cellOnly').click( function() {
        setMapOnAll(polygon_centers, map);
        setMapOnAll(polygons, map);
        clearMarkers(pre_cups);
    });

    $('#preCupOnly').click( function() {
        setMapOnAll(pre_cups, map);
        clearMarkers(polygon_centers);
        clearMarkers(polygons);
    });

    $('#both').click( function() {
        clearMarkers();
        setMapOnAll(pre_cups, map);
        setMapOnAll(polygon_centers, map);
        setMapOnAll(polygons, map);
    });

    $('.toMap').click( function() {
        $('#detail').addClass("collapse");
        $('#map')[0].scrollIntoView({behavior: "smooth"});
    });

    $('#search').click( function(){
        gu=$('.gu').val();
        const path = window.location.pathname.split('/')[1];
        location.href = '/'+path+'/'+gu;
    });
});