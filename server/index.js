require("dotenv").config();

const express = require("express");
const telegramRouter = require("../routes/telegram");

const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    status: "ok",
    message: "Day 1 server is running",
  });
});

app.use("/telegram", telegramRouter);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});