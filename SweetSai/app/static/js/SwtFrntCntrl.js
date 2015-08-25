
//exposing expose variables and functionality to expressions and directives in Template
app.controller('GetPageController', function ($scope, $http) { 
	$scope.inputURL = "http://teststore.swtr.us/";
	$scope.show = function() {
		var returnPromise = $http.get($scope.inputURL);
		returnPromise.then(
		    //success
		    function(data, status, headers, config) {
			   console.log("Server responded: Success in getting: ", $scope.inputURL);	
			   $scope.expression = data;
			   },
			//error   
		    function(data, status, headers, config) {
               log($scope.inputURL);	 	
			   console.log("Server responded: Error in getting: ", $scope.inputURL);
			   },
			//progress   
			function(data, status, headers, config) {
			   console.log("Server responded: Progress in getting: ", $scope.inputURL);	
			   });
		log($scope.inputURL);	   
		console.log("I created an Asynch call and am exiting the Show() function");	
		};
	});
