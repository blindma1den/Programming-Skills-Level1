/*

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
LOGIN : 3 intentos hasta el bloqueo de usuario.
Condiciones:
ESPECIALIDADES: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, 
                Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
Hay 3 medicos por area los cuales pondremos a mano sus nombres
Cada usuario puede sacar hasta 3 turnos máximo. Un turno para cada area y solo 1 turno x medico. 
Para sacar turno se elige la especialidad, morning or afternoon, y que muestre horarios disponibles que pondremos a mano
Solo se mostrarán los especialistas disponibles y ahi elegirá el user.

PROCESO:
Login - Choose speciality - Choose Doctor - Choose time slot
*/

//login

//Appointment
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
let specialitiesArray = [];
let usersArray = [];
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
fetchJson('./specialities.json')
  .then((data) => {
    if (data) {
      specialitiesArray = data;
      console.log(specialitiesArray);
    }
  })
  .catch((error) => console.log(error));

specialityButton.addEventListener('click', (e) => {
  e.preventDefault();
  doctorContainer.style.display = 'flex';
  specialityButton.style.display = 'none';
  specialitySelect.disabled = true;

  const specialitySelected = specialitySelect.value;
  const selectedSpecialityData = specialitiesArray.find(
    (speciality) => speciality.name === specialitySelected
  );
  const doctorsForSpeciality = selectedSpecialityData
    ? selectedSpecialityData.doctors
    : [];
  const fillDoctorSelect = (doctors) => {
    doctors.forEach((doctor) => {
      const option = document.createElement('option');
      option.value = doctor.name;
      option.textContent = doctor.name;
      doctorSelect.appendChild(option);
    });
  };
  fillDoctorSelect(doctorsForSpeciality);
});

doctorButton.addEventListener('click', (e) => {
  e.preventDefault();
  timeContainer.style.display = 'flex';
  doctorButton.style.display = 'none';
  doctorSelect.disabled = true;
});
timeButton.addEventListener('click', (e) => {
  e.preventDefault();
  timeSlotContainer.style.display = 'flex';
  timeButton.style.display = 'none';
  timeSelect.disabled = true;
  if (timeSelect.value === 'Afternoon') {
    console.log('Afternoon'); //TODO : CREATE SELECT FOR TIMESLOTS IN BOTH WAYS
  } else {
    console.log('Morning');
  }
});
timeSlotButton.addEventListener('click', (e) => {
  e.preventDefault();
  requestButton.style.display = 'block';
  timeSlotButton.style.display = 'none';
  timeSlotSelect.disabled = true;
});

requestButton.addEventListener('click', (e) => {
  e.preventDefault();
  const specialitySelected = specialitySelect.value;
  const doctorSelected = doctorSelect.value;
  const timeSelected = timeSelect.value;
  const timeSlotSelected = timeSlotSelect.value;
  const appointment = {
    speciality: specialitySelected,
    doctor: doctorSelected,
    time: timeSelected,
    timeSlot: timeSlotSelected,
  };
  console.log(appointment);
});
