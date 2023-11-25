const express = require('express');
const app = express();

const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');
const router = express.Router();
const swaggerDocument = YAML.load('imdb-movie-openapi3.0-schema.yaml');

const port = 3002;
// Middleware for /docs
app.use('/docs', router);

// Define routes under /docs
router.get('/', (req, res) => {
  res.send('Hello, World22!');
});

router.use('/api', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
  
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});