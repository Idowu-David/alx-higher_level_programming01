#!/usr/bin/node

const data = require('./100-data.js');

const mapList = data.list.map(function(val, num) {
	return val * num;
	});

console.log(data.list);
console.log(data);
