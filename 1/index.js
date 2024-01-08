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


const Players = [
    {
        name: "Bruno Fernandes",
        goals: 5,
        speed: 6,
        assists: 9,
        passing_accuracy: 10,
        defensive_involvements: 3,
        jersey_number: "8"
    },
    {
        name: "Rasmus Hojlund",
        goals: 12,
        speed: 8,
        assists: 2,
        passing_accuracy: 6,
        defensive_involvements: 2,
        jersey_number: "11"
    },
    {
        name: "Harry Maguire",
        goals: 1,
        speed: 5,
        assists: 1,
        passing_accuracy: 7,
        defensive_involvements: 9,
        jersey_number: "5"
    },
    {
        name: "Alejandro Garnacho",
        goals: 8,
        speed: 7,
        assists: 8,
        passing_accuracy: 6,
        defensive_involvements: 0,
        jersey_number: "17"
    },
    {
        name: "Mason Mount",
        goals: 2,
        speed: 6,
        assists: 4,
        passing_accuracy: 8,
        defensive_involvements: 1,
        jersey_number: "7"
    }

]
const Actions = [
    {
        name: "compare",
        message: "Select two jersey from the list",
        type: 'multiselect',
        choices: Players.map(player => { return { title: player.jersey_number, value: player.jersey_number } }),
        response: {
            type: "text",
            name: "comparision",
            message(values) {
                console.log(values.compare);
                let res = Players.filter(player => values.compare.includes(player.jersey_number));
                console.table(res);
                return "Here is your comparision! Press enter to go back to menu";
            }


        }
    },
    {
        name: "info",
        message: "Select a jersey number from the list",
        type: 'select',
        choices: Players.map(player => { return { title: player.jersey_number, value: player.jersey_number } }),
        response: {
            type: "text",
            name: "res_info",
            message(values) {
                console.table(Players.find(player => player.jersey_number == values.info));
                return "Here is player information! Press enter to go back to menu";
            }
        }
    }, {
        name: "dominator",
        message: "Select a skill from the list",
        type: 'select',
        choices: [
            { title: "Fastest player", value: "speed" },
            { title: "Top Scorer", value: "goals" },
            { title: "Top Assistant", value: "assists" },
            { title: "Top passing accuracy", value: "passisg_accuracy" },
            { title: "Top defensive player", value: "defensive_involvements" },

        ],
        response: {
            type: "text",
            name: "res_info",
            message(values) {
                console.table(Players.reduce((prev, current) => (prev && prev[`${values.dominator}`] > current[`${values.dominator}`]) ? prev : current));

                return "Here is player information! Press enter to go back to menu";
            }
        }

    }, {
        name: "exit",
        exit() {
            process.exit(1)
        }
    }
]
const prompts = require('prompts');

prompts.override(require('yargs').argv);

let identifyAction = (value) => (value == 'exit') ? process.exit(1) : Actions.filter(act => act.name == value)[0];

function init() {
    (async () => {
        const response = await prompts([
            {
                type: 'select',
                name: 'actions',
                message: 'What are you looking for?',
                choices: [
                    { title: 'Get player info', value: 'info' },
                    { title: 'Compare two players', value: 'compare' },
                    { title: 'Get player dominating a skill', value: 'dominator' },
                    { title: 'Exit ', value: 'exit' },
                ],
                hint: 'Return to submit'
            },
            {
                type: prev => identifyAction(prev).type,
                name: prev => prev,
                message: prev => identifyAction(prev).message,
                choices: prev => (identifyAction(prev).type == 'multiselect' || identifyAction(prev).type == 'select') ? identifyAction(prev).choices : null,
                max: prev => (identifyAction(prev).type == 'multiselect') ? 2 : null,
                min: prev => (identifyAction(prev).type == 'multiselect') ? 2 : null,
            },
            {
                type: (prev, values, prompt) => identifyAction(values.actions).response.type,
                name: (prev, values, prompt) => identifyAction(values.actions).response.name,
                message: (prev, values, prompt) => identifyAction(values.actions).response.message(values)
            },



        ]); init();
    })();
}
init()