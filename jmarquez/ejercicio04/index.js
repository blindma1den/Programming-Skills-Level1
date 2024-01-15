// 4. The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

// Login; it should be locked after the third failed attempt.
// The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
// Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
// All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
// The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
// Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, ''
// VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
// The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights,
// collect user data (name, surname, ID/passport),
// print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.
const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout,
});

const users = [
	{
		nam: 'jon',
		pass: '123',
		appointment: [],
	},
	{
		nam: 'Kate Wong',
		pass: '@PASSujhp',
		appointment: [],
	},
];
const countries = [
	{ Spain: ['Madrid', 'Barcelona', 'Valencia'] },
	{ France: ['Paris', 'Marseille'] },
	{ Portugal: ['Lisbon', 'Porto'] },
	{ Italy: ['Rome', 'Milan'] },
	{ Germany: ['Munich', 'Berlin'] },
];
const rooms = [
	{ 'VIP Suite': 450 },
	{ 'Single rom': 100 },
	{ 'Double rom': 200 },
	{ 'Group rom': 350 },
	{ 'Luxury suite': 550 },
];

let selectedCountry = '';
let selectedCity = '';
let selectedRoom = {};

let logTry = 3;
function login() {
	readline.question('\n Insert you user: ', user => {
		readline.question('\n Enter your password: ', pass => {
			if (logTry === 1) {
				console.log('\nSystem locked');
				return readline.close();
			}
			const USER_AUTH = users.filter(
				registeredUser => registeredUser.nam == user
			);
			const PASS_AUTH = USER_AUTH.filter(
				registeredUser => registeredUser.pass == pass
			);

			if (USER_AUTH.length == 0 || PASS_AUTH.length == 0) {
				logTry--;
				console.log(`User or password not found, tries remaining: ${logTry}`);
				return login();
			}
			menu();
		});
	});
}
function menu() {
	readline.question(
		'\nWELCOME TO RH HOTELS BOKKING SYSTEM\nSelect your country: ',
		n => {
			selectCity(n);
		}
	);
	countries.forEach((value, key) => {
		console.log(`\n${key}.- ${Object.keys(value).toString()}`);
	});
}
function selectCity(country) {
	const list = Object.values(countries[country]);
	selectedCountry = Object.keys(countries[country]).toString();
	readline.question('\nSelect your city: ', n => {
		selectedCity = list[0][n];
		selectRom();
	});
	list[0].forEach((value, key) => {
		console.log(`\n${key}.- ${value}`);
	});
}
function selectRom() {
	readline.question('\nSelect the room type: ', n => {
		selectedRoom = rooms[n];
		numberNIghtsd();
	});
	rooms.forEach((value, index) => {
		console.log(`\n${index}.- ${Object.keys(value)}: $${Object.values(value)}`);
	});
}
function numberNIghtsd() {
	readline.question('\nSelect the amounts of nights to reserve: ', n => {
		finishProcess(n);
	});
}
function finishProcess(n) {
	readline.question('\nPlease enter your name: ', name => {
		readline.question('\nPlease enter your surname: ', surname => {
			readline.question('\nPleasee enter your ID/Passport: ', passport => {
				const initialCost = Number(Object.values(selectedRoom));
				console.log(`\nToal to pay is: $${initialCost * n}`);
				readline.question(`\nAre you agree? ("yes/no"): `, res => {
					if (res !== 'yes') {
						return menu();
					} else {
						console.log(`
					Congratulations!, the reservatios is done for
					Name: ${name} ${surname}
					ID/Passport: ${passport}
					Destinatation: ${selectedCountry} - ${selectedCity}
					Romm type:${Object.keys(selectedRoom).toString()}
					Total to pay: $${initialCost * n}
						`);
					}
				});
			});
		});
	});
}
login();
