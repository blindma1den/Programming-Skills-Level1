// 5. Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:
// It must have a login and validate the data; after the third failed attempt, it should be locked.
// The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
// The user must choose if they want to check an additional piece of luggage into the hold.
// Hand luggage is free of charge.
// The user must purchase both the outbound and return tickets.
// The user can choose their preferred meal: Regular, Vegetarian, Kosher.
// The program must collect the following data: Name, country of origin, passport, and destination country.
// Upon completing the process, the system will display everything the user has previously chosen along with their information.
// The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.
const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout,
});
const users = [
	{
		nam: 'jon',
		pass: '123',
	},
	{
		nam: 'Kate Wong',
		pass: '@PASSujhp',
	},
];
const countries = ['Turkey', 'Greece', 'Lebanon', 'Spain', 'Portugal'];
const condition = ['Economy', 'First Class'];
const meal = ['Regular', 'Vegetarian', 'Kosher'];
let userName = '';
let origin = '';
let destinatation = '';
let departureDate = '';
let returnDate = '';
let passport = '';
let luggage = false;
let category = '';
let mealType = '';

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
		'\nWelcome to Turkish Airlines System\nEnter your name please: ',
		str => {
			userName = str;
			readline.question('\nEnter your passport ID: ', pass => {
				passport = pass;
				originCountry();
			});
		}
	);
}
function originCountry() {
	readline.question('\nSelect the country of origin: ', str => {
		origin = countries[str];
		readline.question(
			'\nEnter the outbound date (format: DD-MM-YY): ',
			date => {
				departureDate = date;
				destinatationCountry();
			}
		);
	});
	countries.forEach((value, key) => {
		console.log(`\n${key}.- ${value}`);
	});
}
function destinatationCountry() {
	readline.question('\nSelect destinatation country: ', str => {
		destinatation = countries[str];
		readline.question('\nEnter the return date (format: DD-MM-YY): ', date => {
			returnDate = date;
			extraLuggage();
		});
	});
	countries.forEach((value, key) => {
		console.log(`\n${key}.- ${value}`);
	});
}
function extraLuggage() {
	readline.question('Do you want add extra luggage? (yes/no): ', answer => {
		if (answer == 'yes') luggage = true;
		selectCategory();
	});
}
function selectCategory() {
	readline.question('\nSelect category: ', c => {
		category = condition[c];
		selectMeal();
	});
	condition.forEach((value, key) => {
		console.log(`\n${key}.- ${value}`);
	});
}
function selectMeal() {
	readline.question('\nSelect type of meal: ', m => {
		mealType = meal[m];
		reservation();
	});
	meal.forEach((value, key) => {
		console.log(`\n${key}.- ${value}`);
	});
}

function reservation() {
	console.log(`
	Reservation details:
	Name: ${userName}
	Category: ${category}
	Type of meal: ${mealType}
	Passport ID: ${passport}
	Country of origin: ${origin}
	Date of departure: ${departureDate}
	Country of destination: ${destinatation}
	Date of return: ${returnDate}
	Extra luggage: ${luggage}
	`);
	readline.question('\nPlease confirm the oerder (yes/no): ', conf => {
		if (conf == 'yes') {
			console.log('\nReservatioon made succesfully!');
			return readline.close();
		} else {
			menu();
		}
	});
}
login();
