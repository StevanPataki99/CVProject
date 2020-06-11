(function(angular){

    var app = angular.module("app");


    app.controller("korisnikPrikazCtrl", ["$http" , "$state", "$stateParams", function($http, $state, $stateParams) {
        var that = this;
        this.korisnik = {}; 

        this.dobaviKorisnika= function(id) {
            $http.get("api/korisnik/" + id).then(function(result){
                console.log(result);
                that.korisnik = result.data;
            },
            function(reason) {
                console.log(reason);
            });
        }
        this.dobaviKorisnika($stateParams["id"]);

    }]);
})(angular);