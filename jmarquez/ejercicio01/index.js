const players = {
	9: {
		name: 'Bruno Fernandes',
		jersey: 9,
		goals: 5,
		speed: 6,
		assits: 9,
		'passing accuracy': 10,
		'defensive involvements': 3,
	},
	11: {
		name: 'Rasmus Hojlund',
		jersey: 11,
		goals: 12,
		speed: 8,
		assits: 2,
		'passing accuracy': 6,
		'defensive involvements': 2,
	},
	5: {
		name: 'Harry Maguire',
		jersey: 5,
		goals: 1,
		speed: 5,
		assits: 1,
		'passing accuracy': 7,
		'defensive involvements': 9,
	},
	17: {
		name: 'Alejandro Garnacho',
		jersey: 17,
		goals: 8,
		speed: 7,
		assits: 8,
		'passing accuracy': 6,
		'defensive involvements': 0,
	},
	7: {
		name: 'Mason Mount',
		jersey: 7,
		goals: 2,
		speed: 6,
		assits: 4,
		'passing accuracy': 8,
		'defensive involvements': 1,
	},
};

const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout,
});

function Retry() {
	readline.question(
		'\nWhat do you want to do?\n1.- Return to main menu\n2.- Quit system\n',
		n => {
			if (n == 1) return menu();
			if (n == 2) {
				console.log('Thank you see you!, next time');
				return readline.close();
			}
		}
	);
}
function menu() {
	readline.question(
		'======WELCOME TO THE SYSTEM========\n      Select an option\n1.- fastest player\n2.- top goal scorer\n3.- player with the most assists\n4.- player with the highest passing accuracy\n5.- player with the most defensive involvements\n6.- Info of player\n7.- Compare two players\n8.- Quit system\n',
		n => {
			if (n == 1) {
				let top = 0;
				let fastest = '';
				for (const player in players) {
					if (players[player]['speed'] >= top) {
						top = players[player]['speed'];
						fastest = `the fastest player is ${players[player]['name']} wtih ${players[player]['speed']} points of speed`;
					}
				}
				console.log(fastest);
				return Retry();
			}

			if (n == 2) {
				let top = 0;
				let scorer = '';
				for (const player in players) {
					if (players[player]['goals'] >= top) {
						top = players[player]['goals'];
						scorer = `the fastest player is ${players[player]['name']} wtih ${players[player]['goals']} goals`;
					}
				}
				console.log(scorer);
				return Retry();
			}
			if (n == 3) {
				let top = 0;
				let assits = '';
				for (const player in players) {
					if (players[player]['assits'] >= top) {
						top = players[player]['assits'];
						assits = `the fastest player is ${players[player]['name']} wtih ${players[player]['assits']} assits`;
					}
				}
				console.log(assits);
				return Retry();
			}
			if (n == 4) {
				let top = 0;
				let passing = '';
				for (const player in players) {
					if (players[player]['passing accuracy'] >= top) {
						top = players[player]['passing accuracy'];
						passing = `the fastest player is ${players[player]['name']} wtih ${players[player]['passing accuracy']} successfull passes`;
					}
				}
				console.log(passing);
				return Retry();
			}
			if (n == 5) {
				let top = 0;
				let defensive = '';
				for (const player in players) {
					if (players[player]['defensive involvements'] >= top) {
						top = players[player]['defensive involvements'];
						defensive = `the fastest player is ${players[player]['name']} wtih ${players[player]['defensive involvements']} defensive actions`;
					}
				}
				console.log(defensive);
				return Retry();
			}
			if (n == 6) {
				readline.question("\nSelect the Player's jersey number\n", n => {
					console.log(players[n]);
					return Retry();
				});
			}
			if (n == 7) {
				readline.question('\nenter 2 players numbers\n', a => {
					readline.question('second number\n', b => {
						console.log(players[a], '\n', players[b]);
						return Retry();
					});
				});
			}
			if (n == 8) {
				console.log('Thank you!, see you next time.');
				return readline.close();
			}
		}
	);
}
menu();
