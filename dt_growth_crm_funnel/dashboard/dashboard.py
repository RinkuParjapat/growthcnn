from leads.crud import init_db, create_lead, get_all_leads, update_stage, delete_lead

def print_menu():
    print("\n📋 Lead Management Dashboard")
    print("1. View all leads")
    print("2. Add a new lead")
    print("3. Update lead stage")
    print("4. Delete a lead")
    print("5. Return to main menu")

def run_dashboard():
    init_db()
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            leads = get_all_leads()
            print("\n🧾 All Leads:")
            for lead in leads:
                print(f"[{lead.id}] {lead.name} | {lead.email} | Stage: {lead.stage}")
        elif choice == "2":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            source = input("Source: ")
            lead = create_lead(name, email, phone, source)
            print(f"✅ Lead added: {lead.name} (Stage: {lead.stage})")
        elif choice == "3":
            lead_id = int(input("Enter lead ID: "))
            new_stage = input("New stage (Contacted / Qualified / Converted): ")
            update_stage(lead_id, new_stage)
            print("✅ Stage updated.")
        elif choice == "4":
            lead_id = int(input("Enter lead ID to delete: "))
            delete_lead(lead_id)
            print("🗑️ Lead deleted.")
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    run_dashboard()
