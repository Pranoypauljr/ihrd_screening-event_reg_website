// Define the two dates
const date1 = new Date('2023-03-31');
const date2 = new Date('2023-03-20');

// Calculate the time difference between the two dates
const timeDiff = Math.abs(date2.getTime() - date1.getTime());

// Calculate the number of days between the two dates
const daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));

// Output the number of days between the two dates
console.log(`There are ${daysDiff} days between ${date1.toDateString()} and ${date2.toDateString()}.`);