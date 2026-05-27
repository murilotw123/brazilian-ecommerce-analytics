"""
Quick test to confirm BigQuery credentials are working.
"""
import os
from pathlib import Path
from google.cloud import bigquery

CREDENTIALS_DIR = Path(__file__).parent.parent / "credentials"
json_files = list(CREDENTIALS_DIR.glob("*.json"))

if not json_files:
    print("❌ No JSON key file found in credentials/")
    exit(1)

key_file = json_files[0]
print(f"✓ Found credential file: {key_file.name}")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(key_file)

try:
    client = bigquery.Client()
    project_id = client.project
    print(f"✓ Connected to BigQuery project: {project_id}")
    
    datasets = list(client.list_datasets())
    print(f"✓ Found {len(datasets)} dataset(s) in project")
    
    print("\n🎉 BigQuery connection works! Ready for ingestion.")
    
except Exception as e:
    print(f"\n❌ Connection failed: {e}")
    exit(1)
