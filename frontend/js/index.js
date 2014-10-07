(function(){
	'use strict';
	
	$(function(){
		$('nav a,#header .metadata a').smoothScroll({
			offset: -70,
			speed: 'auto'
		});
		skrollr.init();
	});
})();