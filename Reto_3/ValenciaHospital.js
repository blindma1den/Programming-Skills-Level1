// The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

import inquirer from "inquirer";

// It must have a login and validate the data; after the third failed attempt, it should be locked.
// The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
// There are 3 doctors for each specialty.
// The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
// The maximum limit for appointments, in general, is 3.
// Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
// Display available specialists.
// The user can choose their preferred specialist.
// The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.
const users = [
  { username: "user1", password: "pass123" },
  { username: "user2", password: "pass456" },
  { username: "user3", password: "pass789" },
];
const medicalSpecialties = [
  {
    name: "General Medicine",
    doctors: ["Ana", "Carlos", "Luis"],
  },
  {
    name: "Emergency Care",
    doctors: ["Maria", "Juan", "Sofia"],
  },
  {
    name: "Clinical Analysis",
    doctors: ["Pedro", "Laura", "David"],
  },
  {
    name: "Cardiology",
    doctors: ["Isabel", "Fernando", "Gabriela"],
  },
  {
    name: "Neurology",
    doctors: ["Miguel", "Elena", "Javier"],
  },
  {
    name: "Nutrition",
    doctors: ["Lucia", "Diego", "Paula"],
  },
  {
    name: "Physiotherapy",
    doctors: ["Alejandro", "Valentina", "Andres"],
  },
  {
    name: "Traumatology",
    doctors: ["Natalia", "Ricardo", "Camila"],
  },
  {
    name: "Internal Medicine",
    doctors: ["Jose", "Daniela", "Rafael"],
  },
];
const schedule = [
  "9:00 AM",
  "10:00 AM",
  "11:00 AM",
  "1:00 PM",
  "2:00 PM",
  "3:00 PM",
];
let scheduledAppointments = [];
const specialties=[
  "General Medicine",
  "Emergency Care",
  "Clinical Analysis",
  "Cardiology",
  "Neurology",
  "Nutrition",
  "Physiotherapy",
  "Traumatology",
  "Internal Medicine",
]
function checkAppointmentsBySpecialty(scheduledAppointments, specialty) {
  const appointmentsCount = scheduledAppointments.reduce((count, appointment) => {
    if (appointment.specialty === specialty) {
      count++;
    }
    return count;
  }, 0);
  if (specialty === "General Medicine" && appointmentsCount >= 3) {
    return false;
  } else if (appointmentsCount >= 1 && specialty !== "General Medicine") {
    return false;
  }
  
  return true;
}
const CredentialsQuestions = [
  {
    type: "input",
    name: "username",
    message: "Enter your username:",
  },
  {
    type: "password",
    name: "password",
    message: "Enter your password:",
    mask: "*",
  },
];
async function login() {
  let tries = 1;
  while (tries <= 3) {
    const credentials = await inquirer.prompt(CredentialsQuestions);
    const user = users.find(
      (student) =>
        student.username === credentials.username &&
        student.password === credentials.password
    );

    if (user) {
      console.log("Login successful!");
      return true;
    } else {
      console.log("Incorrect credentials. Please try again.");
      tries++;
    }
  }

  console.log("Maximum attempts exceeded. Exiting...");
  return false;
}

async function scheduleAppointment() {

  const availableSpecialties = specialties.filter(specialty => checkAppointmentsBySpecialty(scheduledAppointments, specialty));
  const specialistQuestion = {
    type: "rawlist",
    name: "specialtySelected",
    message: "Choose the specialty of the appointment you want to schedule ",
    choices:availableSpecialties,
    validate: (specialtySelected) => {
      if (!checkAppointmentsBySpecialty(scheduledAppointments, specialtySelected)) {
        console.log("pruva dentro del if")
        return "You cannot schedule more appointments for this specialty at this time.";
      }
      return true;
    }
  };
  const { specialtySelected } = await inquirer.prompt(specialistQuestion);
  function checkAppointmentsByDoctor(scheduledAppointments, doctorName) {
    const doctorAppointments = scheduledAppointments.filter(
      appointment => appointment.doctor === doctorName
    );
    return doctorAppointments.length === 0; 
  }
  const doctorsAvailable = medicalSpecialties.find(
    specialty => specialty.name === specialtySelected
  ).doctors.filter(doctor =>
    checkAppointmentsByDoctor(scheduledAppointments, doctor)
  );

  if (doctorsAvailable.length === 0) {
    console.log("There are no available doctors for this specialty at this time.");
    return;
  }
  const doctorQuestion = {
    type: "rawlist",
    name: "doctorSelected",
    message: "Choose the doctor of the appointment you want to schedule ",
    choices: doctorsAvailable,
  };
  let { doctorSelected } = await inquirer.prompt(doctorQuestion);
  const scheduleQuestion = {
    type: "list",
    name: "preferredTime",
    message: "Choose the time of the appointment you want to schedule:",
    choices: ["morning", "afternoon"],
  };

  const { preferredTime } = await inquirer.prompt(scheduleQuestion);

  let availableHours;
  if (preferredTime === "morning") {
    availableHours = schedule.filter((hour) => hour.includes("AM"));
  } else {
    availableHours = schedule.filter((hour) => hour.includes("PM"));
  }

  const timeQuestion = {
    type: "list",
    name: "selectedHour",
    message: "Select a time for your appointment:",
    choices: availableHours,
  };
  const { selectedHour } = await inquirer.prompt(timeQuestion);
  scheduledAppointments.push({
    specialty: specialtySelected,
    doctor: doctorSelected,
    time: selectedHour,
  });
  console.log("Appointment scheduled successfully!");
  console.log("Specialty: " + specialtySelected);
  console.log("Doctor: " + doctorSelected);
  console.log("Time: " + selectedHour);
  
}
async function main() {
  await login();
  let scheduleAnother = true;
  while (scheduleAnother) {
    const allSpecialtiesFull = specialties.every(specialty =>
      !checkAppointmentsBySpecialty(scheduledAppointments, specialty)
    );

    if (allSpecialtiesFull) {
      console.log("All specialties are full. Cannot schedule more appointments.");
      return;
    }
    await scheduleAppointment();
    const { anotherAppointment } = await inquirer.prompt({
      type: "confirm",
      name: "anotherAppointment",
      message: "Would you like to schedule another appointment?",
      default: true,
    });
    scheduleAnother = anotherAppointment;
  }
}
await main()

