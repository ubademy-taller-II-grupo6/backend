use ubademyLog;
db.createCollection("Login", {
  validator: {
    $and: [
      {
        "userId": {$type: "string", $exists: true}
      },
      {
        "respuesta": { $type: "string", $exists: true}
      },
      {
        "codigo_respuesta": { $type: "string", $exists: true}
      },
      {
        "session_star_date": { $type: "string", $exists: true}
      },
      {
        "session_end_date": { $type: "string", $exists: true}
      }
    ]
  }
});

db.Login.insertOne({
    userId: "mriarte@gmail",
    respuesta: "Inicio sesion",
    codigo_respuesta: "404",
    session_star_date: "25/01/2021",
    session_end_date: "25/01/2021"
});
