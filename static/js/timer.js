// Set the countdown date
const countdownDate = new Date('December 31, 2023 23:59:59').getTime();

// Update the timer every second
const timer = setInterval(() => {

  // Get the current date and time
  const now = new Date().getTime();

  // Calculate the distance between now and the countdown date
  const distance = countdownDate - now;

  // Calculate the hours, minutes, and seconds
  const hours = Math.floor(distance / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the hours, minutes, and seconds on the webpage
  document.getElementById('hours').innerHTML = hours.toString().padStart(2, '0');
  document.getElementById('minutes').innerHTML = minutes.toString().padStart(2, '0');
  document.getElementById('seconds').innerHTML = seconds.toString().padStart(2, '0');

  // If the countdown is finished, display "Expired" and clear the timer
  if (distance < 0) {
    clearInterval(timer);
    document.getElementById('hours').innerHTML = '00';
    document.getElementById('minutes').innerHTML = '00';
    document.getElementById('seconds').innerHTML = '00';
    document.getElementById('timer').innerHTML = 'Expired';
  }
}, 1000);