(function(angular){

    var app = angular.module("app");


    app.controller("korisniciCtrl", ["$http" , "$state", function($http, $state) {
        var that = this;

        this.korisnici = []; 
        //this.tipovi = [];
        this.dobaviKorisnike= function() {
            $http.get("api/korisnik").then(function(result){
                console.log(result);
                that.korisnici = result.data;
            },
            function(reason) {
                console.log(reason);
            });
        }

        this.ukloniKorisnika = function(id) {
            $http.delete("api/korisnik/" + id).then(function(response){
                console.log(response);
                that.dobaviKorisnike();
            },
            function(reason){
                console.log(reason);
            });
        }

        this.dobaviKorisnike();
    }]);
})(angular);