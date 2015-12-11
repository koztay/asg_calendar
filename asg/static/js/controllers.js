var myControllers = angular.module('myApp.controllers', []);

myControllers.controller('EventCtrl', function EventCtrl($scope, Event) {
  $scope.events = {};
   
  Event.query(function(response) {
    $scope.events = response;
  });

  $scope.submitEvent = function(text) {
    var cevent = new Event({text: text});
    cevent.$save(function(){
      $scope.tweets.unshift(tweet);
    })
  }
});

myControllers.controller('UserCtrl', function UserCtrl($scope, Event, User, AuthUser) {
  $scope.events = {};
  id = AuthUser.id;
  User.get({id:id}, function(response) {
    $scope.user = response;
    $scope.events = response.events;
  });
});
