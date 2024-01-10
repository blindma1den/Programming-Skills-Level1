//CREAMOS UN ARRAY DE OBJETOS CON LOS DESTINOS Y SUS DISTINTAS OPCIONES
const destinations = [
  {
    season: 'winter',
    options: [
      { activity: 'Ski', country: 'Andorra', cost: 100 },
      { activity: 'Swiss Alps Tour', country: 'Switzerland', cost: 100 },
    ],
  },
  {
    season: 'summer',
    options: [
      { activity: 'Hiking', country: 'Spain', cost: 400 },
      { activity: 'Beach', country: 'Portugal', cost: 400 },
    ],
  },
  {
    season: 'spring',
    options: [
      { activity: 'Extreme Sports', country: 'France', cost: 300 },
      { activity: 'Cultural and Historic Tour', country: 'Italy', cost: 300 },
    ],
  },
  {
    season: 'autumn',
    options: [
      { activity: 'Hiking', country: 'Belgium', cost: 200 },
      { activity: 'Cultural and Historic Tour', country: 'Austria', cost: 200 },
    ],
  },
];

//CAPTURAMOS ELEMENTOS DEL HTML (DOM)
const seasonSelect = document.getElementById('season-select');
const activitiesSelect = document.getElementById('activities-select');
const budgetInput = document.getElementById('budget');
const responseContainer = document.getElementById('response-container');

let selectedActivity;

//ESCUCHAMOS EL EVENTO CHANGE DEL SELECT DE SEASON Y APLICAMOS LAS FUNCIONES
seasonSelect.addEventListener('change', () => {
  updateOptions();
  handleForm();
});
//ESCUCHAMOS EL EVENTO INPUT DEL INPUT DEL BUDGET. ACTUALIZAMOS LA ACTIVIDAD SELECCIONADA Y EJECUTAMOS FUNCIONES
budgetInput.addEventListener('input', () => {
  selectedActivity = activitiesSelect.value;
  updateOptions();
  handleForm();
});
//ESCUCHAMOS EL EVENTO CHANGE DEL SELECT DE ACTIVIDADES Y EJECUTAMOS FUNCIONES DE LOGICA
activitiesSelect.addEventListener('change', () => {
  selectedActivity = activitiesSelect.value;
  updateOptions();
  handleForm();
});

//FUNCION QUE CAPTURA LOS DATOS INGRESADOS POR EL USUARIO, COMIENZA A REALIZAR EL FILTRO Y LUEGO MUESTRA LA RESPUESTA
function handleForm() {
  const selectedSeason = seasonSelect.value;
  const selectedBudget = parseInt(budgetInput.value, 10);
  const selectedActivity = activitiesSelect.value;

  const selectedOptions = getFilteredOptions(
    selectedSeason,
    selectedBudget,
    selectedActivity
  );
  displayResponse(selectedOptions);
}

// FUNCION PARA FILTRAR SEGUN LA ELECCION DEL USUARIO
//RENEGUE MUCHO CON EL ANY. SI LA OPCION ES ANY QUE MUESTRE TODO, SINO LA TEMPORADA QUE ELIGIO EL USUARIO.
//AL FINAL TERMINA FILTRANDO SEGUN LA TEMPORADA, SEGUN LA ACTIVIDAD, Y SEGUN EL COSTO, SIEMPRE Y CUANDO SE ESCOJA.
function getFilteredOptions(season, budget, selectedActivity) {
  let optionsToFilter =
    season === 'any' ? originalOptions : getDestinationOptions(season);

  if (selectedActivity) {
    optionsToFilter = optionsToFilter.filter(
      (option) => option.activity === selectedActivity
    );
  }

  return optionsToFilter.filter((option) => option.cost <= budget);
}

// FUNCION PARA MOSTRAR LAS ACTIVIDADES EN EL SELECT. SI LA ACTIVIDAD ES 0, NO MOSTRARÁ RESULTADOS
//DE LO CONTRARIO MOSTRARA LAS ACTIVIDADES FILTRADAS
const displayOptions = (season, options) => {
  activitiesSelect.innerHTML =
    '<option value="" disabled selected>Select Activity</option>';

  if (options.length > 0) {
    const addedActivities = [];
    //CREAMOS UN NUEVO ARRAY PARA LAS ACTIVIDADES POSIBLES.
    options.forEach((option) => {
      // IF PARA NO DUPLICAR LAS ACTIVIDADES Y DEJAR SOLO UNA
      if (!addedActivities.includes(option.activity)) {
        const activityOption = document.createElement('option');
        activityOption.value = option.activity;
        activityOption.textContent = option.activity;
        activitiesSelect.appendChild(activityOption);
        // AGREGA LAS ACTIVIDADES A UN ARRAY PARA NO MOSTRARLAS DUPLICADAS
        addedActivities.push(option.activity);
      }
    });
  } else {
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = 'No activities available';
    activitiesSelect.appendChild(defaultOption);
  }

  if (selectedActivity) {
    activitiesSelect.value = selectedActivity;
  }
};

// FUNCION PARA MOSTRAR LAS OPCIONES SEGUN LA TEMPORADA Y PRESUPUESTO
function updateOptions() {
  const selectedSeason = seasonSelect.value;
  const options = getDestinationOptions(selectedSeason);
  displayOptions(selectedSeason, options);
}

// FUNCION PARA OBTENER DESTINOS SEGUN TEMPORADA
function getDestinationOptions(season) {
  return season === 'any'
    ? originalOptions
    : destinations.find((destination) => destination.season === season)
        ?.options || [];
}

// FUNCION PARA MOSTRAR LA RESPUESTA DEL DESTINO RECOMENDADO SEGUN SUS ELECCIONES (PUEDEN SER VARIAS)
const displayResponse = (selectedOptions) => {
  if (selectedOptions.length > 0) {
    const optionsString = selectedOptions
      .map((option) => `${option.country}, $${option.cost}`)
      .join(', ');

    responseContainer.textContent = `Options Available: ${optionsString}`;
  } else {
    responseContainer.textContent =
      'No options available for the selected activity and budget. Please try to change your selections.';
  }
};

//NI BIEN SE CARGUE EL HTML CREAMOS UN ARRAY CON LOS DESTINOS Y SUS OPCIONES, Y HACEMOS QUE SE MUESTRE TODO
// Y  COMIENCE EN ANY, CON $0 Y SIN ACTIVIDADES SELECCIONADAS
document.addEventListener('DOMContentLoaded', () => {
  originalOptions = [].concat(...destinations.map((dest) => dest.options));

  const allOptions = getFilteredOptions('any', 0, '');

  displayOptions('any', allOptions);
});
