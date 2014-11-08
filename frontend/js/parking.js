(function(){
'use strict';
var map = L.map('map', {scrollWheelZoom: false}).setView([13.849, 100.56971669197083], 15);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var parking = {};

L.marker([13.846338213201996, 100.56971669197083]).addTo(map)
	.bindPopup('<strong>Venue:</strong> IUP Building')
	.openPopup();
parking['vib'] = L.marker([13.851293, 100.564457]).addTo(map).bindPopup('Vibhavadi parking building');
parking['ngam1'] = L.marker([13.84291, 100.57063]).addTo(map).bindPopup('Ngam Wong Wan 1 parking building');
parking['ngam2'] = L.marker([13.84351, 100.56956]).addTo(map).bindPopup('Ngam Wong Wan 2 parking building');
parking['bk'] = L.marker([13.85413, 100.57035]).addTo(map).bindPopup('Bangkhen parking building');
parking['basketball'] = L.marker([13.84646, 100.56776]).addTo(map).bindPopup('Basketball field parking');
parking['lh1'] = L.marker([13.84677, 100.57078]).addTo(map).bindPopup('LH1 parking');
parking['jak'] = L.marker([13.84925, 100.56837]).addTo(map).bindPopup('Jakbandhu building parking');

$('h6[data-parking]').each(function(){
	var name = $(this).data('parking');
	$('<a href="#" class="btn">Map</a>').appendTo(this)
		.click(function(e){
			parking[name].openPopup();
			$.smoothScroll({
				scrollTarget: 'h4',
			});
			e.preventDefault();
		});
});
})();