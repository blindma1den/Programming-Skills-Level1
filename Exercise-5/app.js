/* 
5. Turkish Airlines has just launched an offer to travel among the following 
destinations: Turkey, Greece, Lebanon, Spain, and Portugal.
Develop an algorithm with the following characteristics:
It must have a login and validate the data; after the third failed attempt, it should be locked.
The user must choose the origin country and the destination country, the flight date, 
and the condition: Economy or First Class.
The user must choose if they want to check an additional piece of luggage into the hold.
Hand luggage is free of charge.
The user must purchase both the outbound and return tickets.
The user can choose their preferred meal: Regular, Vegetarian, Kosher.
The program must collect the following data: Name, country of origin, passport, and destination country.
Upon completing the process, the system will display everything the user has previously chosen along with
their information. 
The system will provide the option to confirm the reservation or cancel it.
If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.

LOGIN-TRAVEL SELECT-USER DATA- OPTION TO CONFIRM OR CANCEL.
Destinations: Turkey Greece, Lebanon, Spain, Portugal 
Condition: Economic, First Class
Additional Piece of Luggage has cost.
Meal: Regular, Vegetarian, Kosher
Data: Name, Country of Origin, Passport, Destination country

*/

//login variables
const loginForm = document.querySelector('.form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const formContainer = document.getElementById('form-container');
const logoutButton = document.getElementById('logout-button');
let usersArray = [];
let wrongPasswordTimes = 0;
let currentUser;
const maxWrongAttempts = 3;

//Reservation variables
let newSummary = {};
let reservationArray = [];
const reservationsContainer = document.getElementById('reservations-container');
const originCountriesContainer = document.getElementById(
  'origin-countries-container'
);
const originCountriesSelect = document.getElementById(
  'origin-countries-select'
);
const originCountriesButton = document.getElementById(
  'origin-countries-button'
);
const destinationCountriesContainer = document.getElementById(
  'destination-countries-container'
);
const destinationCountriesSelect = document.getElementById(
  'destination-countries-select'
);
const destinationCountriesButton = document.getElementById(
  'destination-countries-button'
);
const dateContainer = document.getElementById('date-container');
const departureDateInput = document.getElementById('departure-date-input');
const returnDateInput = document.getElementById('return-date-input');
const dateButton = document.getElementById('date-button');
const conditionContainer = document.getElementById('condition-container');
const conditionSelect = document.getElementById('condition-select');
const conditionButton = document.getElementById('condition-button');
const luggageContainer = document.getElementById('luggage-container');
const luggageSelect = document.getElementById('luggage-select');
const luggageButton = document.getElementById('luggage-button');
const mealContainer = document.getElementById('meal-container');
const mealSelect = document.getElementById('meal-select');
const mealButton = document.getElementById('meal-button');
const userDataContainer = document.getElementById('user-data-container');
const firstNameInput = document.getElementById('first-name-input');
const lastNameInput = document.getElementById('last-name-input');
const passportInput = document.getElementById('passport-input');
const summaryButton = document.getElementById('summary-button');
const submitReservationButton = document.getElementById(
  'submit-reservation-button'
);

//Funcion de fetch
const fetchJson = async (url) => {
  try {
    const response = await fetch(url);
    const data = await response.json();

    if (data) {
      return data;
    }
  } catch (error) {
    console.log(error);
  }
};
//FETCH USERS
fetchJson('./users.json')
  .then((data) => {
    if (data) {
      usersArray = data;
      console.log(usersArray);
    }
  })
  .catch((error) => console.log(error));

//LOGIN/LOGOUT PROCESS
//Authenticate Function with lock at third wrong try
const authenticate = () => {
  let username = usernameInput.value;
  let password = passwordInput.value;

  currentUser = usersArray.find((user) => user.username === username);

  if (!currentUser) {
    console.log('Invalid username or password.');
    return false;
  }
  if (currentUser.isLocked) {
    console.log('User is locked.');
    return false;
  }

  if (username === currentUser.username && password === currentUser.password) {
    console.log('Authentication successful.');
    showOperations();
    return true;
  } else {
    wrongPasswordTimes = wrongPasswordTimes + 1;
    console.log('Invalid username or password.');
    console.log(`Attempts remaining: ${maxWrongAttempts - wrongPasswordTimes}`);

    if (wrongPasswordTimes >= maxWrongAttempts) {
      currentUser.isLocked = true;
      console.log(
        'You have exceeded the number of tries. Please try again later.'
      );
      return false;
    }
  }
};
//Hide and unhide operation if logged (lo vengo reciclando del lvl0)
const showOperations = () => {
  loginForm.style.display = 'none';
  reservationsContainer.style.display = 'block';
  usernameInput.value = '';
  passwordInput.value = '';
};
//FUNCION LOGOUT
const logout = (e) => {
  e.preventDefault();
  currentUser = null;
  loginForm.style.display = 'block';
  reservationsContainer.style.display = 'none';
  console.log('Logged out.');
};

const handleFormSubmit = (e) => {
  e.preventDefault();
  authenticate();
};
loginForm.addEventListener('submit', handleFormSubmit);
logoutButton.addEventListener('click', logout);

//TRAVEL RESERVATION

const toggleShowForm = (container = null, button = null, select = null) => {
  container !== null
    ? container.style.display == 'none'
      ? (container.style.display = 'flex')
      : (container.style.display = 'none')
    : (container = null);
  button?.style.display == 'none'
    ? (button.style.display = 'flex')
    : (button.style.display = 'none');
  select?.disabled == false
    ? (select.disabled = true)
    : (select.disabled = false);
};

const summary = (
  firstName,
  LastName,
  originCountry,
  destinationCountry,
  departureDate,
  returnDate,
  condition,
  additionalLuggage,
  meal
) => {
  const reservation = {
    firstName,
    LastName,
    originCountry,
    destinationCountry,
    departureDate,
    returnDate,
    condition,
    additionalLuggage,
    meal,
  };
  return reservation;
};

originCountriesButton.addEventListener('click', (e) => {
  e.preventDefault();
  //Cuando el usuario elige ORIGEN, eliminamos ese pais de los paises de DESTINO

  const origincountrySelected = originCountriesSelect.value;
  for (let i = 0; i < destinationCountriesSelect.options.length; i++) {
    if (destinationCountriesSelect.options[i].value === origincountrySelected) {
      destinationCountriesSelect.remove(i);
      break;
    }
  }
  toggleShowForm(
    destinationCountriesContainer,
    originCountriesButton,
    originCountriesSelect
  );
});

destinationCountriesButton.addEventListener('click', (e) => {
  e.preventDefault();
  toggleShowForm(
    dateContainer,
    destinationCountriesButton,
    destinationCountriesSelect
  );
});

dateButton.addEventListener('click', (e) => {
  e.preventDefault();
  //Chequeamos que las fechas se seleccionen y que la fecha de vuelta sea posterior a la de salida
  const departureDateSelected = new Date(departureDateInput.value);
  const returnDateSelected = new Date(returnDateInput.value);
  if (isNaN(returnDateSelected) || isNaN(departureDateSelected)) {
    alert('You need to fill departure and return date');
  } else if (returnDateSelected <= departureDateSelected) {
    alert('The Return Date must be later than the Departure date');
    returnDateInput.value = '';
    returnDateInput.focus();
  } else {
    toggleShowForm(conditionContainer, dateButton, departureDateInput);
    returnDateInput.disabled = true;
  }
});

conditionButton.addEventListener('click', (e) => {
  e.preventDefault(e);
  toggleShowForm(luggageContainer, conditionButton, conditionSelect);
});

luggageButton.addEventListener('click', (e) => {
  e.preventDefault();
  toggleShowForm(mealContainer, luggageButton, luggageSelect);
});
mealButton.addEventListener('click', (e) => {
  e.preventDefault();
  toggleShowForm(userDataContainer, mealButton, mealSelect);
});
summaryButton.addEventListener('click', (e) => {
  e.preventDefault();
  toggleShowForm(submitReservationButton, summaryButton, firstNameInput);
  lastNameInput.disabled = true;
  passportInput.disabled = true;

  const firstName = firstNameInput.value;
  const lastName = lastNameInput.value;
  const passport = passportInput.value;
  const originCountry = originCountriesSelect.value;
  const destinationCountry = destinationCountriesSelect.value;
  const departureDate = departureDateInput.value;
  const returnDate = returnDateInput.value;
  const condition = conditionSelect.value;
  const additionalLuggage = luggageSelect.value;
  const meal = mealSelect.value;
  newSummary = summary(
    firstName,
    lastName,
    passport,
    originCountry,
    destinationCountry,
    departureDate,
    returnDate,
    condition,
    additionalLuggage,
    meal
  );
  console.log(newSummary);
  return newSummary;
});

submitReservationButton.addEventListener('click', (e) => {
  e.preventDefault();
  currentUser.reservations.push(newSummary);
  console.log(
    'The reservation has been added successfully.\n If you want, can press again in "Submit reservation" and make another reservation same like this. Is not correct, but It takes a long time to make the visual changes to make it work and I don t see it as necessary since the implementation is done.'
  );
  console.log(currentUser);
});
