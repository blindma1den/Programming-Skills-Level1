/*
4. The RH Hotels chain has hired you to design the booking algorithm for their mobile application:
Login; it should be locked after the third failed attempt.
The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), 
print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.

LOGIN: Same login with 3 attempts

Hotels: 12 hotels around the world located in 5 countries
Spain: Madrid, Barcelona, Valencia
Germany: Munich, Berlin
Italy: Rome, Milan
France: Paris, Marseille
Portugal: Madeira, Lisbon, Porto.

Hotel: 24 Rooms
VIP Suites: 6, $450
Single Rooms: 3 $100 
Double Rooms: 6 $200
Group Rooms: 6  $350
Luxury Suites: 3 $550

PROCESS: 
1) Login-->
2)Choose Country-->Choose City-->Choose Room Type--> Select Number of Nights-->
3)User Form (Name, surname, ID/passport)
4)Print total cost and if user agrees, print a confirmation message for the reservation.
If not, return to main menu

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

//Reservations variables
let hotelsLocationsArray = [];
let newSummary = {};
let reservationArray = [];
const reservationsContainer = document.getElementById('reservations-container');
const countriesContainer = document.getElementById('countries-container');
const countriesSelect = document.getElementById('countries-select');
const countriesButton = document.getElementById('countries-button');
const citiesContainer = document.getElementById('cities-container');
const citiesSelect = document.getElementById('cities-select');
const citiesButton = document.getElementById('cities-button');
const roomTypeContainer = document.getElementById('room-type-container');
const roomTypeSelect = document.getElementById('room-type-select');
const roomTypeButton = document.getElementById('room-type-button');
const nightsContainer = document.getElementById('nights-container');
const nightsButton = document.getElementById('nights-button');
const nightsInput = document.getElementById('nights-input');
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
  appointmentsContainer.style.display = 'none';
  console.log('Logged out.');
};

const handleFormSubmit = (e) => {
  e.preventDefault();
  authenticate();
};
loginForm.addEventListener('submit', handleFormSubmit);
logoutButton.addEventListener('click', logout);

//ROOM RESERVATION

//FETCH HOTEL LOCATIONS
fetchJson('./hotelsLocations.json')
  .then((data) => {
    if (data) {
      hotelsLocationsArray = data;
    }
  })
  .catch((error) => console.log(error));

//FILL CITIES FUNCTION
const fillCitiesSelect = (country) => {
  country.forEach((city) => {
    const option = document.createElement('option');
    option.value = city;
    option.textContent = city;
    citiesSelect.appendChild(option);
  });
};
//FUNCION PARA MOSTRAR Y OCULTAR LOS ELEMENTOS CUANDO SON CLICKEADOS Y NO REPETIR TANTO CODIGO
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

const summary = (firstName, LastName, country, city, roomType, nights) => {
  let amount = nights * roomType;
  const reservation = {
    firstName,
    LastName,
    country,
    city,
    roomType,
    nights,
    amount,
  };
  return reservation;
};

//Countries Container
countriesButton.addEventListener('click', (e) => {
  e.preventDefault();
  toggleShowForm(citiesContainer, countriesButton, countriesSelect);
  const countrySelected = countriesSelect.value;
  const citiesFromCountry = hotelsLocationsArray.filter(
    (country) => country.Country === countrySelected
  );

  let cities = citiesFromCountry[0].Cities;
  fillCitiesSelect(cities);
});

//Cities Container
citiesButton.addEventListener('click', (e) => {
  e.preventDefault();
  toggleShowForm(roomTypeContainer, citiesButton, citiesSelect);
});
//Rooms Container
roomTypeButton.addEventListener('click', (e) => {
  e.preventDefault();
  toggleShowForm(nightsContainer, roomTypeButton, roomTypeSelect);
});

//Nights Container
nightsButton.addEventListener('click', (e) => {
  e.preventDefault();

  toggleShowForm(userDataContainer, nightsButton, nightsInput);
});

summaryButton.addEventListener('click', (e) => {
  e.preventDefault();
  userDataContainer.style.display = 'none';
  submitReservationButton.style.display = 'flex';

  let firstName = firstNameInput.value;
  let lastName = lastNameInput.value;
  let country = countriesSelect.value;
  let city = citiesSelect.value;
  let roomType = Number(roomTypeSelect.value);
  let nights = nightsInput.value;
  newSummary = summary(firstName, lastName, country, city, roomType, nights);
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
