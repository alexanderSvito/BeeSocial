angular.module("MessageApp", [])
.controller("MessageController", function($scope, MessageService, DialogService){
	$scope.MessageService = MessageService;
	$scope.DialogService = DialogService;
	DialogService.getDialogs();
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
.service("DialogService", function($http, MessageService){
	var that = this;
	that.dialogs = [];
	that.countDialogs = function(){
		return that.dialogs.length;
	}
	that.getDialogs = function(){
		return $http({
			method: "get",
			url: "/message/dialogs"
		}).then(function(response){
			that.dialogs = response.data;
			console.log(response.data);
		})
	}
	that.getMessages = function($index){
		return MessageService.getMessages(that.dialogs[$index].id);
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
.directive("dialogList", function(){
	return {
		template: `<dialog-item ng-repeat="dialog in DialogService.dialogs"></dialog-item>`
	}
})
.directive("dialogItem", function(){
	return {
		template: `<div ng-click="DialogService.getMessages($index)" class="dialog">
    					<div class="dialog-name">{{ dialog.name }}</div>
              			<div class="dialog-preview">{{ dialog.preview }}</div>
    			   </div>` 
	}
})