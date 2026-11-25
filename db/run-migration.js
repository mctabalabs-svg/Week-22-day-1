const fs = require('fs');
const path = require('path');
const { Pool } = require('pg');

const pool = new Pool({
  user: 'postgres',
  password: 'rodah',
  host: 'localhost',
  port: 5432,
  database: 'crm'
});

async function runMigration() {
  const filePath = path.join(__dirname, '..', 'db', 'migrations', '0003-create-chama-tables.sql');
  const sql = fs.readFileSync(filePath, 'utf8');
  
  try {
    await pool.query(sql);
    console.log('Migration ran successfully');
  } catch (err) {
    console.error('Migration failed:', err.message);
    process.exit(1);
  } finally {
    await pool.end();
  }
}

runMigration();
