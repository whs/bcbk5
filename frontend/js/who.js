(function(){
'use strict';

var endpoint = 'http://api.2014.barcampbangkhen.org/regis/';
// endpoint = 'http://localhost:8000/regis';

var app = angular.module('bcbk5', ['ui.select']);
app.config(['uiSelectConfig', function(uiSelectConfig) {
	uiSelectConfig.theme = 'select2';
}]);
app.controller('RegisController', ['$scope', '$http', function($scope, $http){
	$scope.people = [];
	$scope.interests = [];
	$scope.filter = {'selected': []};
	$scope.find = function(obj, filter){
		if(filter.length === 0){
			return obj;
		}
		filter = filter.map(function(item){
			return item.toLowerCase();
		});
		return obj.filter(function(x){
			return x.interests.some(function(y){
				return filter.indexOf(y.toLowerCase()) != -1;
			});
		});
	};
	$http.get(endpoint).success(function(data){
		$scope.interests = [];
		data = data.map(function(person){
			person.interests = person.interests.split(/[ ]*,[ ]*/);
			person.interests.forEach(function(interest){
				interest = interest.toLowerCase();
				if($scope.interests.indexOf(interest) == -1){
					$scope.interests.push(interest);
				}
			});
			return person;
		});
		$scope.people = data;

	});
}]);

})();