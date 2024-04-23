#!/usr/bin/node
exports.callMeMoby = function (numOfTimes, callback) {
  for (let i = 0; i < numOfTimes; i++) {
    callback();
  }
};
