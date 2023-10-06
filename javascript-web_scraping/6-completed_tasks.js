#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTask = {};

  tasks.forEach((task) => {
    if (task.completed) {
      if (completedTask[task.userId]) {
        completedTask[task.userId]++;
      } else {
        completedTask[task.userId] = 1;
      }
    }
  });
  console.log(completedTask);
});
