// 1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
// The system should also allow comparison between two players. Use the following player profiles:

// Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive involvements. Corresponds to jersey number 8.
// Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive involvements. Corresponds to jersey number 11.
// Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive involvements. Corresponds to jersey number 5.
// Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive involvements. Corresponds to jersey number 17.
// Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive involvement. Corresponds to jersey number 7.
// The program functions as follows: The coach accesses the system and encounters a menu with the following options:

// Player Review: By entering the player's jersey number, they can access the player's characteristics.
// Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
// Identify the fastest player: Displays the player with the most points in speed.
// Identify the top goal scorer: Displays the player with the most points in goals.
// Identify the player with the most assists: Displays the player with the most points in assists.
// Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
// Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
// The system should also allow returning to the main menu.
import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
import { log } from "node:console";
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const players = [
  {
    name: "Bruno Fernandes",
    goals: 5,
    speed: 6,
    assists: 9,
    passingAccuracy: 10,
    defensiveInvolvements: 3,
    jerseyNumber: 8,
  },
  {
    name: "Rasmus Hojlund",
    goals: 12,
    speed: 8,
    assists: 2,
    passingAccuracy: 6,
    defensiveInvolvements: 2,
    jerseyNumber: 11,
  },
  {
    name: "Harry Maguire",
    goals: 1,
    speed: 5,
    assists: 1,
    passingAccuracy: 7,
    defensiveInvolvements: 9,
    jerseyNumber: 5,
  },
  {
    name: "Alejandro Garnacho",
    goals: 8,
    speed: 7,
    assists: 8,
    passingAccuracy: 6,
    defensiveInvolvements: 0,
    jerseyNumber: 17,
  },
  {
    name: "Mason Mount",
    goals: 2,
    speed: 6,
    assists: 4,
    passingAccuracy: 8,
    defensiveInvolvements: 1,
    jerseyNumber: 7,
  },
];
async function askToContinue() {
  const answer = await rl.question(
    "Do you want to continue in the program? (y/n): "
  );
  if (answer.toLowerCase() !== "y") {
    isProgramRunning = false;
  }
}

async function playerReview() {
  const jerseyNumber = await rl.question(
    "Input the jersey number of the player: "
  );
  const player = players.find((player) => player.jerseyNumber == jerseyNumber);
  if (player) {
    console.log("Statistics");
    console.log(`
Name: ${player.name}
Number of goals: ${player.goals}    
Points in speed: ${player.speed}    
Points in assists: ${player.assists}    
Points in passing accuracy: ${player.passingAccuracy}    
Defensive involvements: ${player.defensiveInvolvements}    
    `);
  } else {
    console.log("Player no found");
  }
}
async function playersCompare() {
  await playerReview();
  await playerReview();
}
async function selectBestPlayer(statistic) {
  let bestPlayer = null
  players.forEach((player) => {
    if (statistic in player) {
      if (bestPlayer === null ||bestPlayer[statistic] < player[statistic]) {
        bestPlayer = player
      }
    }
  });
  return bestPlayer;
}
let isProgramRunning = true;
while (isProgramRunning) {
  console.log("Welcome to the Player Review of Manchester United FC!");
  console.log("1. Player Review:");
  console.log("2. Compare two players:");
  console.log("3. Identify the fastest player");
  console.log("4. Identify the top goal scorer");
  console.log("5. Identify the player with the most assists");
  console.log("6. Identify the player with the highest passing accuracy");
  console.log("7. Identify the player with the most defensive involvements");
  console.log("8. Exit");
  let optionMenu = await rl.question(
    "select the option according to the number in the menu: "
  );
  switch (Number(optionMenu)) {
    case 1:
      await playerReview();
      await askToContinue();
      break;
    case 2:
      await playersCompare();
      await askToContinue();
      break;
    case 3:
      const fastestPlayer = await selectBestPlayer("speed");
      console.log(
        `Fastest player: ${fastestPlayer.name} with a speed score of ${fastestPlayer.speed}`
      );
      await askToContinue();

      break;
    case 4:
      const topGoalScorer = await selectBestPlayer("goals");
      console.log(
        `Top goal scorer: ${topGoalScorer.name} with ${topGoalScorer.goals} goals`
      );
      await askToContinue();

      break;
    case 5:
      const mostAssistsPlayer = await selectBestPlayer("assists");
      console.log(
        `Player with most assists: ${mostAssistsPlayer.name} with ${mostAssistsPlayer.assists} assists`
      );
      await askToContinue();
      break;
    case 6:
      const highestPassingAccuracyPlayer = await selectBestPlayer(
        "passingAccuracy"
      );
      console.log(
        `Player with highest passing accuracy: ${highestPassingAccuracyPlayer.name} with ${highestPassingAccuracyPlayer.passingAccuracy}% passing accuracy`
      );
      await askToContinue();
      break;
    case 7:
      const mostDefensivePlayer = await selectBestPlayer(
        "defensiveInvolvements"
      );
      console.log(
        `Player with most defensive involvements: ${mostDefensivePlayer.name} with ${mostDefensivePlayer.defensiveInvolvements} defensive involvements`
      );
      await askToContinue();
      break;
    case 8:
      isProgramRunning = false;
      break;

    default:
      console.log(`
Please enter a valid option.
`);
      break;
  }
}
rl.close();
