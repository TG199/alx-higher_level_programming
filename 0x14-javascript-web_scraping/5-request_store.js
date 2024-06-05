#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response) {
  if (!error) {
    fs.writeFileSync(process.argv[3], response.message, 'utf-8');
  }
});
