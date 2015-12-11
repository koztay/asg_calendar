// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('myApp.services', ['ngResource'])
  .factory('Event', function($resource) {
    return $resource('/api/events/:id/', {}, {'query': {method: 'GET', isArray: false}}); 
  })
  .factory('User', function($resource) {
    return $resource('/api/users/:id/', {}, {'query': {method: 'GET', isArray: false}}); 
  });