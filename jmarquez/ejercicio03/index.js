// The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

// It must have a login and validate the data; after the third failed attempt, it should be locked.
// The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
// There are 3 doctors for each specialty.
// The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
// The maximum limit for appointments, in general, is 3.
// Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
// Display available specialists.
// The user can choose their preferred specialist.
// The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.
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

const specialities = [
	{
		speciality_name: 'General Medicine',
		doctors: ['manuel', 'jose', 'fernando'],
		hours: ['10:am', '2:00pm'],
	},
	{
		speciality_name: 'Emergency Care',
		doctors: ['charles xavier', 'walter white', 'zoiberg'],
		hours: ['9:00am', '1:00pm'],
	},
	{
		speciality_name: 'Clinical Analysis',
		doctors: ['alberto', 'roberto', 'filiberto'],
		hours: ['8:00am', '3:00pm'],
	},
	{
		speciality_name: 'Cardiology',
		doctors: ['maria', 'fernanda', 'rosio'],
		hours: ['7:50am', '3:00pm'],
	},
	{
		speciality_name: 'Neurology',
		doctors: ['daniel', 'devorah', 'isole'],
		hours: ['8:50am', '4:00pm'],
	},
	{
		speciality_name: 'Nutrition',
		doctors: ['francia', 'arturo', 'martina'],
		hours: ['9:50am', '5:00pm'],
	},
	{
		speciality_name: 'Physiotherapy',
		doctors: ['luna', 'isabel', 'valentina'],
		hours: ['10:50am', '6:00pm'],
	},
	{
		speciality_name: 'Internal Medicine',
		doctors: ['yesi', 'antonio', 'magdalena'],
		hours: ['6:50am', '7:00pm'],
	},
];

let logTry = 3;
let maximumAppointment = 0;

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
			delete USER_AUTH[0].pass;
			menu(USER_AUTH[0]);
		});
	});
}

function menu(userData) {
	if (maximumAppointment >= 3)
		return console.log(
			`Maximun limit of appoinments (${maximumAppointment}) reached`
		);
	readline.question('\nWelcome! Select the speciality please: ', str => {
		chooseDoctor(specialities[str], userData);
	});

	specialities.forEach((index, value) => {
		console.log(`\n${value}.- ${index.speciality_name}  `);
	});
}

function chooseDoctor(speciality, userData) {
	readline.question(
		`\nWelcome! Select the doctor for ${speciality.speciality_name} please: `,
		str => {
			const doctorName = speciality.doctors[str];
			delete speciality.doctors[str];
			if (userData.appointment.includes(doctorName)) {
				console.log(
					`You already are made appointment with the doctor ${doctorName}`
				);
				chooseDoctor(speciality, userData);
			} else {
				userData.appointment.push(doctorName);
				maximumAppointment++;
				console.log('appointment successfully!');
				chooseHour(speciality);
			}
		}
	);
	speciality.doctors.forEach((name, index) => {
		console.log(`\n${index}.- ${name}`);
	});
}
function chooseHour(speciality) {
	readline.question('\nChoose an avaliable hour:\n', hour => {
		console.log(`Your appointment is set to ${speciality.hours[hour]}`);
		return readline.close();
	});
	speciality.hours.forEach((name, index) => {
		console.log(`\n${index}.- ${name}`);
	});
}
login();
