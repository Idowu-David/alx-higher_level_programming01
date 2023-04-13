const { dict } = require('./101-data');

const occurrencesByUserId = dict;
const userIdsByOccurrence = {};

// Compute the new dictionary of user ids by occurrence
for (const userId in occurrencesByUserId) {
  const occurrences = occurrencesByUserId[userId];
  if (!userIdsByOccurrence[occurrences]) {
    userIdsByOccurrence[occurrences] = [];
  }
  userIdsByOccurrence[occurrences].push(userId);
}

// Print the new dictionary of user ids by occurrence
console.log(userIdsByOccurrence);

