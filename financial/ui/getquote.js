angular.module('demo', [])
.controller('quote', function($scope, $http) {
	$scope.getDividedInformation = function()	{
		
		var get_url = "http://localhost:8081/stockautomation/api/v1.0/getdividenddetails/" + $scope.stock_symbol ;
        
        $http.get(get_url).
        then(function(response) {
            $scope.stock_quote = response.data;
        });
    };
});

