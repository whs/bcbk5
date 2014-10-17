(function(){
	'use strict';

	var endpoint = 'http://api.2014.barcampbangkhen.org/regis/';

	var flash = function flash(text){
		$('.alert').remove();
		$('<div class="alert">').text(text)
			.insertBefore('#registerform');
		$('body').animate({
		    scrollTop: $('.block-register').offset().top
		 }, 500);
	};

	$(function(){
		$('#registerform').submit(function(){
			$('#registerform input[type=submit]').attr('disabled', true);
			var data = $(this).serialize();
			var hasEmail = $('#email').val().length > 0;
			$.post(endpoint, data).then(function(){
				var url = 'thankyou.html'

				if(hasEmail){
					url += '?email=1';
				}

				window.location = url;
			}, function(xhr, status, error){
				$('#registerform input[type=submit]').attr('disabled', false);
				if(!xhr.responseJSON){
					return flash('Server error');
				}

				var error = '';
				$.each(xhr.responseJSON, function(key, value){
					if($.isArray(value)){
						error += value.join(', ');
					}else{
						error += value;
					}
					error += '\n';
				});
				flash(error);
			});
			return false;
		});
	});
})();