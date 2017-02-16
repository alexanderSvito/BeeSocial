angular.module("MessageApp", [])
.controller("MessageController", function($scope, MessageService){
	$scope.MessageService = MessageService;
})
.service("MessageService", function($http){
	var that = this;
	that.messages = [];
	that.countMessages = function(){
		return that.messages.length;
	}
	that.getMessages = function(id){
		return $http({
			method: "get",
			url: "/message/" + id
		}).then(function(response){
			that.messages = response.data;
			console.log(response.data);
		})
	}
})
.directive("messagesList", function(){
	return {
		template: `<message-item ng-repeat="message in MessageService.messages"></dialog-item>`
	}
})
.directive("messageItem", function(){
	return {
		template: `<div><h3>{{ message.author }}</h3>{{ message.text }}</div>`
	}
})