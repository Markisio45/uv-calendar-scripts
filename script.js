const fs = require('fs')
const ics = require('ics');

let content = fs.readFileSync('./calendario.json','utf8')
content = JSON.parse( content);

let events = [];

content.forEach( element => {
  let event = {};
  console.log( "element: ", element);
  event.title = element.nombre_asignatura || "Sin Nombre";
  event.start = element.inicio;
  event.end = element.fin;
  event.location = element.nombre_lugar || "Sin Lugar";
  event.description = `Actividad ${element.nombre_actividad || "Sin Actividad"}\nProfesor: ${element.profesores && element.profesores.length > 0 && element.profesores[0].nombre_profesor || "Sin Profesor"}`
  events.push( event);
})

const {error, value} = ics.createEvents( events);

fs.writeFileSync(`./calendario.ics`, value);