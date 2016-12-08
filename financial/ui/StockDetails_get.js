angular.module('demo', [])
  .controller('quote', function($scope, $http){
    $scope.getDividendInformation = function() {
   	
      // $scope.stock_symbol = "CTL";
      $http.get("http://localhost:8081/stockautomation/api/v1.0/getdividenddetails/" + $scope.stock_symbol)
      .then(function(response){ $scope.stock_quote = response.data; });

      $http.get("http://localhost:8081/stockautomation/api/v1.0/getnews/" + $scope.stock_symbol)
      .then(function(response){ $scope.related = response.data; });

/*
    $scope.update = function(stock){
      $scope.stock_symbol = stock.title;
    };

    $scope.select = function(){
      this.setSelectionRange(0, this.value.length);
    }
    */
     };
  });