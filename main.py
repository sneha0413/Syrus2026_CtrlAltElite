from ticket_parser import parse_ticket
from repo_analyzer import search_repo
from root_cause_detector import detect_issue
from fix_generator import generate_fix
from report_generator import generate_report
from incident_loader import load_incident
from incident_processor import extract_info
from test_runner import run_tests

print("\n=== Autonomous Incident-to-Fix Engineering Agent ===\n")

# ================= STEP 1: LOAD INCIDENT =================
incident = load_incident("../shopstack-platform/incidents/INC-001.json")

print("Incident Loaded Successfully!\n")

print("Incident Details:\n")
print("ID:", incident["id"])
print("Title:", incident["title"])
print("Service:", incident["service"])
print("Description:", incident["description"])
print("Error Log:", incident["error_log"])

# ================= STEP 2: UNDERSTAND INCIDENT =================
print("\n[Agent] Understanding incident...")

description = incident["description"]
error_log = incident["error_log"]

print("Description:", description)
print("Error Log:", error_log)

# Use description as ticket (IMPORTANT FIX)
# Use description as ticket
ticket = description

# Extract keywords
keywords = parse_ticket(ticket)

print("[Agent] Extracted keywords:", keywords)

# ================= STEP 3: EXTRACT STRUCTURED INFO =================
info = extract_info(incident)

print("\n[Agent] Extracted Info:")
print(info)

# ================= STEP 5: RUN TESTS BEFORE FIX =================
print("\n[Agent] Running tests BEFORE fix...\n")

test_output_before = run_tests(info["service"])

print(test_output_before)

# ================= STEP 4: REPOSITORY ANALYSIS =================
print("\n[Agent] Scanning repository for related modules...")

service = info["service"]

if service == "python-service":
    base_path = "../shopstack-platform/python-service"
else:
    base_path = "../shopstack-platform/node-service"

files = search_repo(keywords, base_path)

if not files:
    print("[Agent] No relevant files found in repository")
    exit()

file = files[0]

print("\n[Agent] Candidate file detected:", file)

# ================= STEP 5: ROOT CAUSE ANALYSIS =================
print("[Agent] Performing root cause analysis...")

from ai_agent import ai_reasoning

with open(file, "r", encoding="utf8", errors="ignore") as f:
    code = f.read()

ai_output = ai_reasoning(ticket, code)

print("\n[Agent] AI Reasoning Output:\n")
print(ai_output)

# ================= STEP 6: (OPTIONAL OLD LOGIC SAFE KEEP) =================
# issue = detect_issue(file, ticket)
# fix = generate_fix(issue)
# report = generate_report(file, issue, fix)

print("\n[Agent] Generating safe patch...")

print("\n=== PROCESS COMPLETE ===\n")