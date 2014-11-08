'use strict';

var Twitter = require('twitter');
var config = require('./config');
var util = require('util');
var tw = new Twitter(config.twitter);

var WebSocketServer = require('ws').Server, wss = new WebSocketServer({port: 1025});
wss.broadcast = function(data) {
	for(var i in this.clients)
		this.clients[i].send(data);
};

tw.stream('filter', {'track': config.track, 'follow': config.follow}, function(stream){
	stream.on('data', function(data){
		wss.broadcast(JSON.stringify(data));
		if(data.text !== undefined){
			console.log('@' + data.user.screen_name + ': ' + data.text);
		}
	});
});