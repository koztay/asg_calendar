/* Project specific Javascript goes here. */
var phonecatApp = angular.module('phonecatApp', []);

phonecatApp.controller('ListCtrl', function ($scope, $http) {
	console.log('controller loaded')
	$scope.getEvents = function(){
		$http.get('/api/events/').success(function(response){
			$scope.events = response.results;
		});
	}




	// $scope.initialize = function(data){
	// 	$scope.initData = data;
	// };

	// $scope.loadItems = function() {
	// 	$scope.items = $http.get('api/events').then(function(response){
	// 		return response.data;
	// 	});

	// };

	// $scope.loadItems();


});