angular.module('myApp', ['ui.router', 'ngResource', 'myApp.controllers', 'myApp.services']);

angular.module('myApp').config(function($stateProvider) {
  $stateProvider.state('events', { // state for showing all movies
    url: '/events',
    templateUrl: 'templates/movies.html',
    controller: 'EventListController'
  }).state('viewEvent', { //state for showing single movie
    url: '/events/:id/view',
    templateUrl: 'templates/event-view.html',
    controller: 'EventViewController'
  }).state('newEvent', { //state for adding a new movie
    url: '/events/new',
    templateUrl: 'templates/event-add.html',
    controller: 'EventCreateController'
  }).state('editEvent', { //state for updating a movie
    url: '/events/:id/edit',
    templateUrl: 'templates/event-edit.html',
    controller: 'EventEditController'
  });
}).run(function($state) {
  $state.go('events'); //make a transition to movies state when app starts
});

















// myApp.controller('ListCtrl', function ($scope, $http) {
// 	console.log('controller loaded')
// 	$scope.getEvents = function(){
// 		$http.get('/api/events/').success(function(response){
// 			$scope.events = response.results;
// 		});
// 	}

// });