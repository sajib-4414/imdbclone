const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors'); // Import the cors middleware
const app = express();
const port = 3002;

app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json());

let persons = [];

app.get('/person', (req, res) => {
  res.json(persons);
});

app.post('/person', (req, res) => {
  const { name } = req.body;
  const newPerson = {
    id: persons.length + 1,
    name,
  };
  persons.push(newPerson);
  res.json(newPerson);
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
