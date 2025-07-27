import os
import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python accdb_export.py full-path-to-db")
    sys.exit(1)

accdb_file = sys.argv[1]
filename = os.path.basename(accdb_file)
dbname = os.path.splitext(filename)[0]

# Set output directory to result/<dbname>
output_dir = os.path.join("result", dbname)
os.makedirs(output_dir, exist_ok=True)

# List all tables
tables = subprocess.check_output(["mdb-tables", "-1", accdb_file]).decode().splitlines()
tables = [t.strip() for t in tables if t.strip()]

print(f"Tables found: {tables}")

# Export each table as CSV into result/<dbname>/
for table in tables:
    output_file = os.path.join(output_dir, f"{table}.csv")
    with open(output_file, "w") as f:
        subprocess.run(["mdb-export", accdb_file, table], stdout=f)
    print(f"Exported: {output_file}")

print(f"All tables exported to {output_dir}")
