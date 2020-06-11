(function(angular){

    var app = angular.module("app");


    app.controller("korisniciDodajCtrl", ["$http" , "$state", function($http, $state) {
        var that = this;
        
        this.noviKorisnik = {
            "korisnicko_ime" : "",
            "ime" : "",
            "prezime" : ""
        }

        this.dodajKorisnaka = function() {
            $http.post("api/korisnik", that.noviKorisnik).then(function(response){
                $state.go("home");

            },function(reason){
                console.log(reason);
            });

        }


    }]);
})(angular);