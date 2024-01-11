// 2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

// Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
// Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
// Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
// Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
// Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.
// Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
// 12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

// Clue: You could consider the user's budget

const seasons = [
	{
		winter: {
			andorra: ['skiing activities'],
			Switzerland: ['tour of the Swiss Alps'],
			cost: 100,
		},
		summer: {
			spain: ['hiking', 'extreme sports'],
			Portugal: ['beaches'],
			cost: 400,
		},
		spring: {
			france: ['extreme sports'],
			italy: ['cultural and historical tour'],
			cost: 300,
		},
		autumn: {
			belgium: ['hiking', 'extreme sports'],
			austria: ['cultural and historical activities'],
			cost: 200,
		},
	},
];
const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout,
});
function menu() {
	readline.question(
		'Welcome to the traveling destination service\nPlease enter your activitty interest\n',
		act => {
			let j = 0;
			let countries = '';
			let seasonList = '';

			for (const i in seasons[0]) {
				let interest = Object.values(seasons[0][i]);
				let inter = Object.keys(seasons[0][i]);
				if (interest[0].includes(act)) {
					delete inter[2];
					inter.forEach(e => {
						if (seasons[0][i][e].includes(act)) countries += e + ' ';
					});
					seasonList += i + ' ';
				}
				j++;
			}
			console.log(
				`Your activity ${act} is avaliable in the countries: ${countries} in the seasons: ${seasonList}`
			);
			return readline.close();
		}
	);
}
menu();
