// 3. 

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

const prompts = require('prompts');


const Specialities = {
    "General Medicine": ["Lionel Messi", "Paulo Dybala", "Sergio Aguero"],
    "Emergency Care": ["Angel Di Maria", "Nicolas Otamendi", "Gonzalo Higuain"],
    "Clinical Analysis": ["Ezequiel Garay", "Lucas Ocampos", "Leandro Paredes"],
    "Cardiology": ["Javier Mascherano", "Marcos Rojo", "Federico Valverde"],
    "Neurology": ["Giovani Lo Celso", "Nahuel Molina", "Matias Vecino"],
    "Nutrition": ["Emiliano Martinez", "Eduardo Salvio", "Guido Rodriguez"],
    "Physiotherapy": ["Juan Foyth", "Nicolas Tagliafico", "Exequiel Palacios"],
    "Traumatology": ["Gonzalo Montiel", "Alexis Mac Allister", "Cristian Romero"],
    "Internal Medicine": ["Rodrigo De Paul", "Lucas Alario", "Emiliano Buendia"]
};

let Appointments = []

let Hours = {
    "morning": ["8:00 to 9:00", "9:00 to 10:00", "10:00 to 11:00"],
    "afternoon": ["13:00 to 14:00", "14:00 to 15:00", "15:00 to 16:00"],
};

let users = [
    {
        username: "diego.maradona",
        password: "goat"
    }
]
let loginTries = 0;

// 

function saveAppointment(appointment) {
    if (Appointments.find(a => appointment.doctor == a.doctor || appointment.speciality == a.speciality)) {
        console.log("\x1b[31m", "You can't set an appointment with same doctor or same speciality");
        throw 1;
    } else if (Appointments.length == 3) {
        console.log("\x1b[31m", "You already have 3 appointments");
        throw 2;
    }
    Appointments.push(appointment)
    return true;
}

async function loginUser(userdata) {
    if (loginTries == 3) {
        console.log("\x1b[31m", "You have reached the limit of login attempts");
        process.exit(1);
    }
    let res = (users.find(us => us.username == userdata.username && us.password == userdata.password)) ? true : false;
    if (!res) {
        loginTries++
        throw "wrong credentials";
    }
    return true;
}

(async () => {

    async function login() {
        const userdata = await prompts([{
            type: 'text',
            name: 'username',
            message: 'Please text your username'
        }, {
            type: 'text',
            name: 'password',
            message: 'Please text your password'
        }]);
        try {
            await loginUser(userdata);
        } catch (error) {
            console.log(error);
            login()
        }
    }

    async function Appoinment() {
        const appointment = await prompts([{
            name: "speciality",
            message: "Select a speciality from the list:",
            type: 'select',
            choices: Object.keys(Specialities).map(speciality => { return { title: speciality, value: speciality } })
        }, {
            name: "dayTime",
            message: "Do you prefer morning or afternoon?",
            type: 'select',
            choices: [{title:"morning",value:"morning"},{title:"afternoon",value:"afternoon"}]
        },{
            name: "time",
            message: "Select a time from the list:",
            type: 'select',
            choices: prev => Hours[`${prev}`].map(time => { return { title: time, value: time } })
        }, {
            name: "doctor",
            message: "Select a doctor from the list:",
            type: 'select',
            choices: (prev, values) => Specialities[`${values.speciality}`].map(doctor => { return { title: doctor, value: doctor } })
        }]);
       
        try {
            await saveAppointment(appointment);
            console.table(Appointments)
            Appoinment()
        } catch (error) {
            if(error == 1){
                Appoinment()
            }else{
                process.exit(1);
            }
            
        }

    }
    try {
        await login()
        await Appoinment();
    } catch (error) {
        console.log(error)
    }
})();
