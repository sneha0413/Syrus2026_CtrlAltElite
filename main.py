from ticket_parser import parse_ticket
from repo_analyzer import search_repo
from root_cause_detector import detect_issue
from fix_generator import generate_fix
from report_generator import generate_report

print("\n=== Autonomous Incident-to-Fix Engineering Agent ===\n")

ticket = input("Enter Incident Ticket: ")

print("\n[Agent] Understanding incident...")

keywords = parse_ticket(ticket)

print("[Agent] Extracted keywords:", keywords)

print("\n[Agent] Scanning repository for related modules...")

files = search_repo(keywords)

if not files:
    print("[Agent] No relevant files found in repository")
    exit()

file = files[0]

print("\n[Agent] Candidate file detected:", file)

print("[Agent] Performing root cause analysis...")

issue = detect_issue(file, ticket)

print("[Agent] Root cause detected:", issue)

print("\n[Agent] Generating safe patch...")

fix = generate_fix(issue)

report = generate_report(file, issue, fix)

print(report)