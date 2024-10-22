const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname,'public')))


// Define a route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname,'public','index.html'));
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});