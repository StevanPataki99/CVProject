(function (angular) {
    var app = angular.module("app");
    app.controller("izmenaKorisnikaCtrl", ["$http", "$state", "$stateParams", function ($http, $state, $stateParams) { //korisnikFormaCtrl
        var that = this;

        this.dobaviKorisnika = function(id) {
            $http.get("api/korisnik/" + id).then(function(result){ 
                that.noviKorisnik = result.data;
            }, function(reason) {
                console.log(reason);
            });
        }

        this.izmeniKorisnika = function(id) {
            $http.put("api/korisnik/" + id, that.noviKorisnik).then(function(response) {
                console.log(response)
                $state.go("home");
            }, function(reason) {
                console.log(reason);
                
            });
        }

        this.sacuvaj = function() {
            this.izmeniKorisnika($stateParams["id"]);
 
            
        }

        this.dobaviKorisnika($stateParams["id"]);

    }]);
})(angular);