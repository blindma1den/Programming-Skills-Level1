// 2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

// Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
// Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
// Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
// Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
// Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

// Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
// 12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

// Clue: You could consider the user's budget
import inquirer from "inquirer";
const travelsInfo = [
    {
      season: "winter",
      price: 100,
      countries: {
        Andorra: ["skiing activities"],
        Switzerland: ["tour of the Swiss Alps"],
      },
    },
    {
      season: "summer",
      price: 400,
      countries: {
        Spain: ["hiking", "extreme sports activities"],
        Portugal: ["activities on the beaches"],
      },
    },
    {
      season: "spring",
      price: 300,
      countries: {
        France: ["extreme sports activities"],
        Italy: ["cultural and historical tour"],
      },
    },
    {
      season: "autumn",
      price: 200,
      countries: {
        Belgium: ["hiking", "extreme sports activities"],
        Austria: ["cultural and historical activities"],
      },
    },
  ];
  
const budgetQuestion = {
  type: "input",
  name: "budget",
  message: "enter your budget:",
  validate:(input)=>{
    const inputNumber=Number(input)
    const minAmount=100
    if (isNaN(inputNumber)) {
        return "Enter a number value";   
    }else if((inputNumber)< 100){
    return `The minimum price of the trips is $${minAmount}`
    }else{
    return true
  }}
};
console.log("Welcome to the Travel Destination Selector!");
console.log("Answer a few questions to find your best travel destination.\n");
const { budget } = await inquirer.prompt(budgetQuestion);

const seasonAvailable = travelsInfo.filter((travel) => travel.price <= Number(budget)).map((travel) => travel.season);
const seasonQuestion = {
    
    type: "list",
    name: "season",
    message: "What season would you like to travel?",
    choices:seasonAvailable
  };
  let season
  if (seasonAvailable.length>1) {
    const answerseason = await inquirer.prompt(seasonQuestion);
    season=answerseason.season
  }else{
    console.log(`Due to the available budget, the system has automatically chosen the season: ${seasonAvailable[0]}`)
    season=seasonAvailable[0]
  }
  const selectedTravel = travelsInfo.find((travel)=> travel.season===season)
  const ActtitiesAvailables = Object.values(selectedTravel.countries).flatMap(activities => activities);
  const activitiesQuestion = {
    
    type: "list",
    name: "activity",
    message: "What activities do you want to do?",
    choices:ActtitiesAvailables
  }
  let selectedCountry=null
  const {activity} = await inquirer.prompt(activitiesQuestion);
  for (const country in selectedTravel.countries) {
    if (selectedTravel.countries[country].includes(activity)) {
      selectedCountry = country;
    }
  }
  console.log(`Based on your preferences, your best destination is:`);
  console.log(`Country: ${selectedCountry}`);
  console.log(`Activities: ${selectedTravel.countries[selectedCountry]}`);
  console.log(`Season: ${season}`);
  console.log(`Price: $${selectedTravel.price}`);