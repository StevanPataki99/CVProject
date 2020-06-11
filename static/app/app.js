///<reference path="/Users/stevanpataki/Desktop/VezbaWebKol2/static/app/app.js">

(function(angular){

    var app = angular.module("app", ["ui.router"]);

    app.config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider) {

        $stateProvider.state({
            name: "home",
            url: "/",
            templateUrl: "app/components/korisnik/korisnici.tpl.html",
            controller: "korisniciCtrl",
            controllerAs: "pctrl" 
        }).state({
            name: "korisnikPrikaz", 
            url: "/korisnikPrikaz/{id}",
            templateUrl: "app/components/korisnik-prikaz/korisnikPrikaz.tpl.html",
            controller: "korisnikPrikazCtrl",
            controllerAs: "pctrl"
        })
        .state({
            name: "dodavanjeKorisnika",
            url: "/dodavanjeKorisnika",
            templateUrl: "app/components/dodajKorisnika/dodajKorisnika.tpl.html",
            controller: "korisniciDodajCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "izmenaKorisnika",
            url: "/izmenaKorisnikaCtrl/{id}", 
            templateUrl: "app/components/korisnik-izmena/izmenaKorisnika.tpl.html",
            controller: "izmenaKorisnikaCtrl",
            controllerAs: "pctrl"
        })
        $urlRouterProvider.otherwise("/")
    }])
})(angular);