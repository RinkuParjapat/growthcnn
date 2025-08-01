from dashboard.dashboard import run_dashboard
from analytics.funnel_metrics import print_metrics, plot_metrics
from nurture.nurture import nurture_lead

def print_main_menu():
    print("\n🎯 DT Growth CRM Funnel — CLI Version")
    print("1. Manage Leads")
    print("2. View Funnel Analytics")
    print("3. Simulate Lead Nurturing")
    print("4. Exit")

def run_main_app():
    while True:
        print_main_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            run_dashboard()
        elif choice == "2":
            print_metrics()
            plot_metrics()
        elif choice == "3":
            name = input("Enter lead name: ")
            intent = input("Intent (high / medium / low): ").strip().lower()
            if intent in ["high", "medium", "low"]:
                nurture_lead(name, intent)
            else:
                print("Invalid intent level. Try again.")
        elif choice == "4":
            print("👋 Exiting CRM. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    run_main_app()