/*
ME FALTO BASTANTE IMPLEMENTACIÓN COMO ALMACENAR LAS CITAS EN  LOCALSTORAGE Y LUEGO MANEJAR QUE CUANDO LOGUEE OTRO USUARIO TENGA DISPONIBLE
DISTINTOS HORARIOS Y DOCTORES SEGUN LA OCUPACION DE LOS MISMO, PERO ME VOY A ATRASAR MUCHO SI SIGO.

The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt, it should be locked.
The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.
The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.

RESUMEN: App para manejar turnos para un Hospital de Valencia
*DONE* LOGIN : 3 intentos hasta el bloqueo de usuario. 
Condiciones:

*DONE* ESPECIALIDADES: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, 
                Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
*DONE* Hay 3 medicos por area los cuales pondremos a mano sus nombres
*DONE* Cada usuario puede sacar hasta 3 turnos máximo. Un turno para cada area y solo 1 turno x medico. 
*DONE* Para sacar turno se elige la especialidad, morning or afternoon, y que muestre horarios disponibles que pondremos a mano
*DONE* Solo se mostrarán los especialistas disponibles y ahi elegirá el user.

PROCESO:
Login - Choose speciality - Choose Doctor - Choose time slot
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
//Appointment variables
const appointmentsContainer = document.getElementById('appointments-container');
const specialityContainer = document.getElementById('speciality-container');
const doctorContainer = document.getElementById('doctor-container');
const timeContainer = document.getElementById('time-container');
const timeSlotContainer = document.getElementById('timeSlot-container');
const specialitySelect = document.getElementById('speciality-select');
const specialityButton = document.getElementById('speciality-button');
const doctorSelect = document.getElementById('doctor-select');
const doctorButton = document.getElementById('doctor-button');
const timeSelect = document.getElementById('time-select');
const timeButton = document.getElementById('time-button');
const timeSlotSelect = document.getElementById('timeSlot-select');
const timeSlotButton = document.getElementById('timeSlot-button');
const requestButton = document.getElementById('request-button');
const requestAnotherButton = document.getElementById('request-another-button');
let specialitiesArray = [];

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

//FETCH SPECIALITIES
fetchJson('./specialities.json')
  .then((data) => {
    if (data) {
      specialitiesArray = data;
      console.log(specialitiesArray);
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
  appointmentsContainer.style.display = 'block';
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

const fillDoctorSelect = (doctors) => {
  doctors.forEach((doctor) => {
    const option = document.createElement('option');
    option.value = doctor.name;
    option.textContent = doctor.name;
    doctorSelect.appendChild(option);
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

//SPECIALITY FORM CONTAINER
specialityButton.addEventListener('click', (e) => {
  e.preventDefault();
  let specialitySelected = specialitySelect.value;
  doctorSelect.innerHTML = '';

  toggleShowForm(doctorContainer, specialityButton, specialitySelect);

  const selectedSpecialityData = specialitiesArray.find(
    (speciality) => speciality.name === specialitySelected
  );
  const doctorsForSpeciality = selectedSpecialityData
    ? selectedSpecialityData.doctors
    : [];

  fillDoctorSelect(doctorsForSpeciality);
  doctorButton.style.display = 'block';
});

//DOCTOR FORM CONTAINER
doctorButton.addEventListener('click', (e) => {
  e.preventDefault();

  toggleShowForm(timeContainer, doctorButton, doctorSelect);
});

//TIME FORM CONTAINER
timeButton.addEventListener('click', (e) => {
  e.preventDefault();
  toggleShowForm(timeSlotContainer, timeButton, timeSelect);

  if (timeSelect.value === 'Afternoon') {
    const option1 = document.createElement('option');
    option1.value = '15:00hs';
    option1.textContent = '15:00hs';
    timeSlotSelect.appendChild(option1);
    const option2 = document.createElement('option');
    option2.value = '17:00hs';
    option2.textContent = '17:00hs';
    timeSlotSelect.appendChild(option2);
  } else {
    const option1 = document.createElement('option');
    option1.value = '10:00hs';
    option1.textContent = '10:00hs';
    timeSlotSelect.appendChild(option1);
    const option2 = document.createElement('option');
    option2.value = '11:00hs';
    option2.textContent = '11:00hs';
    timeSlotSelect.appendChild(option2);
  }
});

//TIMESLOT FORM CONTAINER
timeSlotButton.addEventListener('click', (e) => {
  e.preventDefault();

  toggleShowForm(timeSlotButton, requestButton, timeSlotSelect);
});
let doctorsOccupiedSlots = {};

//REQUEST BUTTON
requestButton.addEventListener('click', (e) => {
  e.preventDefault();

  const specialitySelected = specialitySelect.value;
  const doctorSelected = doctorSelect.value;
  const timeSelected = timeSelect.value;
  const timeSlotSelected = timeSlotSelect.value;
  const patient = { userId: currentUser.id, name: currentUser.username };

  // Verificar si el timeslot ya está ocupado para este médico, en caso de ser otro user
  if (
    doctorsOccupiedSlots[doctorSelected] &&
    doctorsOccupiedSlots[doctorSelected].includes(timeSlotSelected)
  ) {
    console.log('This timeslot is already occupied for this doctor.');
  }
  // Verificar si hay turnos disponibles para este médico segun el número máximo de turnos por médico por los timeSlots
  const maxAppointmentsPerDoctor = 4;
  const occupiedSlots =
    doctorsOccupiedSlots[specialitySelected]?.[doctorSelected] || [];

  if (occupiedSlots.length >= maxAppointmentsPerDoctor) {
    console.log(
      'All appointments with this doctor in this specialty are taken.'
    );
  }
  if (
    doctorsOccupiedSlots[doctorSelected] &&
    doctorsOccupiedSlots[doctorSelected].length >= maxAppointmentsPerDoctor
  ) {
    console.log('All appointments with this doctor are taken.');
  }

  // Agregar el nuevo appointment al usuario
  const appointment = {
    speciality: specialitySelected,
    doctor: doctorSelected,
    time: timeSelected,
    timeSlot: timeSlotSelected,
    patient: patient,
  };
  console.log(appointment);

  const { speciality, doctor, timeSlot } = appointment;
  currentUser.appointments.push({ speciality, doctor, timeSlot });

  // Marcar el timeslot como ocupado para este médico
  if (!doctorsOccupiedSlots[doctorSelected]) {
    doctorsOccupiedSlots[doctorSelected] = [];
  }
  doctorsOccupiedSlots[doctorSelected].push(timeSlotSelected);

  const specialityToUpdate = specialitiesArray.find(
    (speciality) => speciality.name === specialitySelected
  );

  if (specialityToUpdate) {
    const doctorToUpdate = specialityToUpdate.doctors.find(
      (doctor) => doctor.name === doctorSelected
    );

    if (doctorToUpdate) {
      doctorToUpdate.occupiedSlots.push(timeSlotSelected);
    }
  }
  console.log('Appointment successful!');

  if (currentUser.appointments.length > 2) {
    let maxAppointmentsMessage = document.createElement('p');
    maxAppointmentsMessage.textContent =
      'We are sorry, you cannot make additionals appointments today. You will reach the max of three at day.';

    timeSlotContainer.appendChild(maxAppointmentsMessage);
    requestAnotherButton.style.display = 'none';
    requestButton.style.display = 'none';
  } else {
    requestAnotherButton.style.display = 'block';
    requestButton.style.display = 'none';
  }
});

const resetForm = () => {
  toggleShowForm(doctorContainer, specialityButton, specialitySelect);
  toggleShowForm(timeContainer, doctorButton, doctorSelect);
  toggleShowForm(timeSlotContainer, timeButton, timeSelect);
};

requestAnotherButton.addEventListener('click', (e) => {
  e.preventDefault();
  let userSpecialities = [];

  if (currentUser.appointments.length !== 0) {
    userSpecialities = currentUser.appointments.map(
      (appointment) => appointment.speciality
    );

    const availableSpecialities = specialitiesArray.filter(
      (speciality) => !userSpecialities.includes(speciality.name)
    );
    specialitySelect.innerHTML = '';
    availableSpecialities.forEach((speciality) => {
      const option = document.createElement('option');
      option.value = speciality.name;
      option.textContent = speciality.name;
      specialitySelect.appendChild(option);
    });
    timeSlotSelect.innerHTML = '';
  }

  resetForm();
  requestAnotherButton.style.display = 'none';
  timeSlotButton.style.display = 'flex';
  timeSlotSelect.disabled = false;
});
