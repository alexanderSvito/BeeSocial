angular.module("MessageApp", [])
.controller("MessageController", function($scope, DialogsService){
	$scope.DialogsService = DialogsService;
	DialogsService.getDialogs();
})
.service("DialogsService", function(){
	this.dialogs = [];
	this.getDialogs = function(){
		return $http({
			method: "get",
			
		})
	}
})