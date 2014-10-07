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
	$scope.favorites = JSON.parse(localStorage.favorite || '{}');
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

	var save = function(){
		localStorage.favorite = JSON.stringify($scope.favorites);
	};

	var refreshFav = function(){
		angular.forEach($scope.favorites, function(val, key){
			if(val.length > 0){
				var id = val[0].id
				var session = $scope.sessions.filter(function(x){
					return x.id === id;
				});
				if(session.length === 0){
					$scope.favorites[key] = undefined;
					return;
				}
				if(session[0].slot != val[0].slot){
					$scope.favorites[session[0].slot] = [session[0]];
					$scope.favorites[key] = undefined;
				}else{
					val[0] = session[0];
				}
			}
		});
		save();
	};

	$scope.fav = function(session){
		if($scope.isFav(session)){
			$scope.favorites[session.slot] = undefined;
			return;
		}
		$scope.favorites[session.slot] = [session];
		save();
	};

	$scope.isFav = function(session){
		return $scope.favorites[session.slot] && $scope.favorites[session.slot][0].id == session.id;
	};

	$http.get(endpoint).success(function(data){
		$scope.sessions = data;
		$scope.sessionsIndex = index(data);
		refreshFav();
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