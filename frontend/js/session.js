(function(){
'use strict';

var endpoint = 'http://api.2014.barcampbangkhen.org/session/';
// endpoint = 'http://localhost:8000/session';

var index = function(data){
	var out = {};
	angular.forEach(data, function(val){
		if(!out[val.slot]){
			out[val.slot] = {};
		}
		out[val.slot][val.room] = val;
	});
	return out;
};

var app = angular.module('bcbk5', []);
app.controller('SessionController', ['$scope', '$http', function($scope, $http){
	$scope.sessions = [];
	$scope.rooms = ['17201', '17302', '17303', '17304', '17401', '17402'];
	$scope.timeslots = [
		'10:40 - 11:10',
		'11:10 - 11:40',
		'11:40 - 12:10',
		'13:00 - 13:30',
		'13:30 - 14:00',
		'14:00 - 14:30',
		'14:30 - 15:00',
		'15:20 - 15:50',
		'15:50 - 16:20',
		'16:50 - 17:20'
	];
	$http.get(endpoint).success(function(data){
		$scope.sessions = data;
		$scope.sessionsIndex = index(data);
	});
}]);
app.directive('findSession', function(){
	return {
		scope: {
			'sessionRoom': '=sessionRoom',
			'sessionTime': '=sessionTime',
			'session': '=session'
		},
		controller: ['$scope', function($scope){
			var searchScope = $scope;
			while(searchScope['sessions'] === undefined && searchScope != $scope.$root){
				searchScope = searchScope.$parent;
			}
			if(searchScope.sessions === undefined){
				return;
			}
			searchScope.$watch('sessionsIndex', function(sessions){
				if(!sessions){
					return;
				}
				$scope.session = null;

				var slot = sessions[$scope.sessionTime];
				if(!slot){
					return;
				}
				$scope.session = slot[$scope.sessionRoom];
			});
		}]
	};
});

})();