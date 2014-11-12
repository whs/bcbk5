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
wss.on('connection', function(ws){
	tw.search(config.track.split(',').join(' OR '), {count: 100}, function(data) {
		if(data.statuses === undefined || data.statuses.length === 0){
			return;
		}
		data.statuses.reverse().forEach(function(status){
			ws.send(JSON.stringify(status));
		});
	});
});

tw.stream('filter', {'track': config.track, 'follow': config.follow}, function(stream){
	stream.on('data', function(data){
		wss.broadcast(JSON.stringify(data));
		if(data.text !== undefined){
			console.log('@' + data.user.screen_name + ': ' + data.text);
		}
	});
});