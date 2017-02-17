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
		template:  `<div class="message">
						<div class="message-text">{{ message.text }}</div>
						<div class="message-info">
							<span class="message-author">{{ message.author }}</span>
							<span class="message-date">{{ message.sent_at|date:'shortTime' }}</span>
						</div>
					</div>`
	}
})