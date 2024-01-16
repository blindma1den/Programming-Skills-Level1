// 2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

// Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
// Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
// Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
// Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
// Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

// Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
// 12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

// Clue: You could consider the user's budget


const prompts = require('prompts');
prompts.override(require('yargs').argv);

let countries = [
    {
        country: "Andorra",
        info: ["ski", "español", "catalan"],
        season: "winter",
        price: 100,
        score: 0
    },
    {
        country: "Switzerland",
        info: ["ski", "Aleman"],
        season: "winter",
        price: 100,
        score: 0
    },
    {
        country: "Spain",
        info: ["hiking", "español",],
        season: "summer",
        price: 400,
        score: 0
    },
    {
        country: "Portugal",
        info: ["beach", "portugues"],
        season: "summer",
        price: 400,
        score: 0
    },
    {
        country: "France",
        info: ["extreme sports", "frances"],
        season: "spring",
        price: 300,
        score: 0
    },
    {
        country: "Italy",
        info: ["cultural and historial tours", "italiano"],
        season: "spring",
        price: 300,
        score: 0
    }, {
        country: "Belgium",
        info: ["hiking", "extreme sports", "neerlandes"],
        season: "autumn",
        price: 200,
        score: 0
    },
    {
        country: "Austria",
        info: ["cultural and historial tours", "aleman"],
        season: "autumn",
        price: 200,
        score: 0
    },

]

const questions = [
    {
        id: 0,
        q: "What is your favorite season among winter, summer, spring, and autumn?",
        a: ["winter", "summer", "spring", "autumn"]
    }, {
        id: 1,
        q: "In your free time. What do you enjoy more among sking, hiking, extreme sports, do cultural tours?",
        a: ["ski", "hiking", "extreme sports", "cultural and historial tours"]
    }, {
        id: 2,
        q: "How much are you willing to spend on your travel",
        a: [100, 200, 300, 400]
    },

    // {    id: 3,
    //     score: 0.5,
    //     q: "Which language are you interested in learn?",
    //     a: ["español", "catalan", "frances", "portugues", "neerlandes", "aleman"]
    // }

]

function calculateSeasonScore(season) { // Algorithm for score season correctly. Example: If you like summer program should consider spring over winter
    if (season == "summer") {
        return [
            {
                s: "summer",
                val: 1.5
            },
            {
                s: "spring",
                val: 1,
            },
            {
                s: "autumn",
                val: 0.5,
            },
            {
                s: "winter",
                val: 0,
            }

        ]
    } else if (season == "winter") {
        return [
            {
                s: "summer",
                val: 0
            },
            {
                s: "spring",
                val: 0.5,
            },
            {
                s: "autumn",
                val: 1,
            },
            {
                s: "winter",
                val: 1.5,
            }

        ]
    } else if (season == "spring") {
        return [
            {
                s: "summer",
                val: 0.5
            },
            {
                s: "spring",
                val: 1.5,
            },
            {
                s: "autumn",
                val: 1,
            },
            {
                s: "winter",
                val: 0
            }

        ]
    } else if (season == "autumn") {
        return [
            {
                s: "summer",
                val: 0.5
            },
            {
                s: "spring",
                val: 1,
            },
            {
                s: "autumn",
                val: 1.5,
            },
            {
                s: "winter",
                val: 0
            }

        ]
    } return false;
}


function init() {
    (async () => {
        const response = await prompts(questions.map(question => { return { type: "select", name: `preferences_${question.id}`, message: question.q, choices: question.a.map(x => { return { title: x, value: x } }) } }));
        Object.values(response).map(res => {
            for (let i = 0; i < countries.length; i++) {
                if (questions[0].a.find(a => a == res)) { // if it is a season
                    let seasonScore = calculateSeasonScore(countries[i].season);
                    countries[i].score += seasonScore.find(season => season.s == res).val;
                } else {
                    let match = countries[i].info.find(c => c == res);
                    if (match) countries[i].score++;
                }
            }
        })
        countries_money = countries.filter(c => c.price <= response.preferences_2).sort(function (a, b) {
            return b.score - a.score;
        });

        countries_no_money = countries.sort(function (a, b) {
            return b.score - a.score;
        });

        console.log('\x1b[33m%s\x1b[0m', `Your best destination based on your preferences is: ${countries_no_money[0].country}.`)
        console.log('\x1b[36m%s\x1b[0m', `Your best destination based on your preferences and your budget is: ${countries_money[0].country}.`)

    })();
}
init()