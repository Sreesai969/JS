const randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

const guessInput = document.getElementById("guessInput");
const guessBtn = document.getElementById("guessBtn");
const message = document.getElementById("message");
const attemptsEl = document.getElementById("attempts");

guessBtn.addEventListener("click", () => {
  const guess = Number(guessInput.value);
  attempts++;

  if (!guess || guess < 1 || guess > 100) {
    message.textContent = "❌ Enter a number between 1 and 100";
  } else if (guess < randomNumber) {
    message.textContent = "📉 Too low!";
  } else if (guess > randomNumber) {
    message.textContent = "📈 Too high!";
  } else {
    message.textContent = `🎉 Correct! The number was ${randomNumber}`;
    guessBtn.disabled = true;
  }

  attemptsEl.textContent = `Attempts: ${attempts}`;
});
