(function(){
	'use strict';
	
	$('.nav-collapse').click(function(){
		$('body').toggleClass('show-nav');
	});
})();

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-43587008-1', 'auto');
ga('send', 'pageview');

Raven.config('http://8f1c5cc3f1d94500b518bed5f5daba5d@sentry.whs.in.th/6', {
	whitelistUrls: ['2014.barcampbangkhen.org']
}).install();