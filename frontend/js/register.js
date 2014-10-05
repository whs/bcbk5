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
			var data = $(this).serialize();
			var hasEmail = $('#email').val().length > 0;
			$.post(endpoint, data).then(function(){
				var msg = 'Registration successful.';

				if(hasEmail){
					msg += ' You will receive a confirmation email shortly.';
				}

				flash(msg);
			}, function(xhr, status, error){
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