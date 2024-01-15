import readline from 'readline';
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

import readlineSync from 'readline-sync';

const waitForKeypress = () => {
  const answer = readlineSync.question(
    '\nPress "Y" and go back to the Main Menu? : '
  );
  if (answer.toUpperCase() === 'Y') {
    showMenu();
  } else {
    showMenu();
  }
};
class Player {
  constructor(
    name,
    goals,
    speedPoints,
    assistsPoints,
    passingAccuracyPoints,
    defensiveInvolvements,
    jerseyNumber
  ) {
    this.name = name;
    this.goals = goals;
    this.speedPoints = speedPoints;
    this.assistsPoints = assistsPoints;
    this.passingAccuracyPoints = passingAccuracyPoints;
    this.defensiveInvolvements = defensiveInvolvements;
    this.jerseyNumber = jerseyNumber;
  }
}
const Players = [
  new Player('Bruno Fernandes', 5, 6, 9, 10, 3, 8),
  new Player('Rasmus Hojlund', 12, 8, 2, 6, 2, 11),
  new Player('Harry Maguire', 1, 5, 1, 7, 9, 5),
  new Player('Alejandro Garnacho', 8, 7, 8, 6, 0, 17),
  new Player('Mason Mount', 2, 6, 4, 8, 1, 7),
];

const showPlayerStats = (jerseyNumber) => {
  const player = Players.find((p) => p.jerseyNumber === jerseyNumber);

  if (player) {
    console.log(`Player: ${player.name}`);
    console.log(`Goals: ${player.goals}`);
    console.log(`Speed Points: ${player.speedPoints}`);
    console.log(`Assists Points: ${player.assistsPoints}`);
    console.log(`Passing Accuracy Points: ${player.passingAccuracyPoints}`);
    console.log(`Defensive Involvements: ${player.defensiveInvolvements}`);
  } else {
    console.log('No player has that Jersey number..');
  }
  rl.question('\nPress Enter to go back to Main Menu...', showMenu);
};

const comparePlayers = (jerseyNumber1, jerseyNumber2) => {
  const player1 = Players.find((p) => p.jerseyNumber === jerseyNumber1);
  const player2 = Players.find((p) => p.jerseyNumber === jerseyNumber2);

  if (player1 && player2) {
    console.log(`\n\nPlayer 1: ${player1.name}`);
    console.log(`Goals: ${player1.goals}`);
    console.log(`Speed Points: ${player1.speedPoints}`);
    console.log(`Assists Points: ${player1.assistsPoints}`);
    console.log(`Passing Accuracy Points: ${player1.passingAccuracyPoints}`);
    console.log(`Defensive Involvements: ${player1.defensiveInvolvements}`);

    console.log('\n');

    console.log(`Player 2: ${player2.name}`);
    console.log(`Goals: ${player2.goals}`);
    console.log(`Speed Points: ${player2.speedPoints}`);
    console.log(`Assists Points: ${player2.assistsPoints}`);
    console.log(`Passing Accuracy Points: ${player2.passingAccuracyPoints}`);
    console.log(`Defensive Involvements: ${player2.defensiveInvolvements}`);
  } else {
    console.log('No players have been found with that Jersey number.');
  }
  rl.question('\nPress Enter to go back to Main Menu...', showMenu);
};

const getTopPlayer = (category) => {
  const topPlayer = Players.reduce((prev, current) =>
    prev[category] > current[category] ? prev : current
  );

  console.log(`\nTop ${category}: ${topPlayer.name}`);
  rl.question('\nPress Enter to go back to Main Menu...', showMenu);
};

const handleMenuChoice = (choice) => {
  switch (choice.trim()) {
    case '1':
      rl.question('Enter jersey number: ', (jerseyNumber) => {
        showPlayerStats(Number(jerseyNumber));
      });
      break;
    case '2':
      rl.question('Enter jersey number of player 1: ', (jerseyNumber1) => {
        rl.question('Enter jersey number of player 2: ', (jerseyNumber2) => {
          comparePlayers(Number(jerseyNumber1), Number(jerseyNumber2));
        });
      });
      break;
    case '3':
      getTopPlayer('speedPoints');
      break;
    case '4':
      getTopPlayer('goals');
      break;
    case '5':
      getTopPlayer('assistsPoints');
      break;
    case '6':
      getTopPlayer('passingAccuracyPoints');
      break;
    case '7':
      getTopPlayer('defensiveInvolvements');
      break;
    case '8':
      rl.close();
      break;
    default:
      console.log('Invalid choice');
      showMenu();
  }
};
const showMenu = () => {
  console.log('Menu:');
  console.log('1. Review of chosen Player');
  console.log('2. Compare 2 Players');
  console.log('3. Get Fastest Player');
  console.log('4. Get Top Scorer Player ');
  console.log('5. Get Top Assist Player ');
  console.log('6. Get Top Passing Accuracy Player');
  console.log('7. Get Top Defensive Involvements');
  console.log('8. Exit to system');
  rl.question('Enter your choice (1, 2, 3, 4, 5, 6 ,7, 8): ', handleMenuChoice);
};
rl.question(
  `
    
        █▄─▄█─█▀█─█▄──█─█▀─█─█─█▀─█▀─▀█▀─█▀─█▀█
        █─▀─█─█▄█─█─█─█─█──█▀█─█▀─▀█──█──█▀─█▄▀
        ▀───▀─▀─▀─▀──▀▀─▀▀─▀─▀─▀▀─▀▀──▀──▀▀─▀─▀
        ────────────▐▌────▐▌
        ───────────▄██▄──▄██▄    ▲     ▲ㅤ  ▲ 
        ────▄────▀████████████▀ ◄██► ◄██► ◄██►
        ───▄██▄█──███▀████▀███───██───██───██
        █─▄█████──███▄─██─▄███───██───██───██
        ▀███████───██████████────████████████
        ─██▀▀████──██████████────████████████
        ▀▀──▄████▄──██▄──▄██──────────██
        ───▀▀████▀──█████████▄────────██
        ──────██──▄███████████▀───────██
        ──────██──██████████▀──▄▄████████▄
        ──────██──██████████▄▄████████████
        ──────██──▀█████████████▀────▀███▀
        ──────██───▀████████████▄▄▄▄█████▄
        ──────██────██████████████████████
        ──────███▄─▄██████████▀────▀▀▀███▀
        ──────███████████████─────────██
        ──────███████████████─▄██─────██
        ──────██████████████████▀─────██
        ──────▀█████████████████▄██▄──██
        ───────▀████████─▀█████████▀──██
        ──────────▀█████▄──▀███████───██
        ───────────██████▄───▀█████▄──██
        ──────────▄███████▄────▀████──██
        ──────────████████▀──────▀▀▀──██
        ──────────▀█████▀
        ────────────████
        ────────────████▄
        ───────────▄█████
        ───────────█████▀
    
        ㅤㅤㅤ█──█─█▄──█─▀─▀▀█▀▀─█▀▀─█▀▀▄
        ㅤㅤㅤ█──█─█─█─█─█───█───█▀▀─█──█
        ㅤㅤㅤ▀▀▀▀─▀──▀▀─▀───▀───▀▀▀─▀▀▀    

  Welcome to Manchester United Coach App! Press Enter to continue.`,
  () => {
    showMenu();
  }
);

rl.on('close', () => {
  console.log('Goodbye!');
  process.exit(0);
});
