angular.module("MessageApp", [])
.controller("MessageController", function($scope, MessageService){
	$scope.MessageService = MessageService;
	MessageService.getDialogs();
})
.service("MessageService", function(){
	this.dialogs = [];
	this.getDialogs = function(){
		return $http({
			method: "get"
		})
	}
})