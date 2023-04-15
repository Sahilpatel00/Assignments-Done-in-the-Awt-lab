var myApp = angular
        .module("myApp",[])
        .controller("myController",function($scope){
            $scope.message="Show"
            $scope.showMe = false;
            $scope.colors = function(){
                $scope.showMe= !$scope.showMe;
                if($scope.message=="Show"){
                    $scope.message="Hide";
                }else{
                    $scope.message="Show";
                }
            };
        });