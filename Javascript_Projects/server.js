const express = require('express');
const app = express();

app.use(express.static(__dirname)); // Serve HTML files from the current directory

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});