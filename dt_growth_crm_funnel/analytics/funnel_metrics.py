import matplotlib.pyplot as plt

channels = {
    "Facebook Ads": {"leads": 3000, "cost": 90000, "conversions": 30},
    "Email Campaign": {"leads": 1000, "cost": 10000, "conversions": 25},
    "LinkedIn DMs": {"leads": 500, "cost": 25000, "conversions": 10}
}

def print_metrics():
    print("\n📊 Funnel Analytics Metrics\n")
    print(f"{'Channel':<20} {'Leads':<6} {'Conversions':<12} {'Conv Rate':<10} {'Cost/Conv (₹)':<15}")
    print("-" * 70)
    for name, data in channels.items():
        rate = (data["conversions"] / data["leads"]) * 100
        cost_per_conv = data["cost"] / data["conversions"]
        print(f"{name:<20} {data['leads']:<6} {data['conversions']:<12} {rate:<10.2f} {cost_per_conv:<15.2f}")

def plot_metrics():
    labels = list(channels.keys())
    rates = [(c["conversions"] / c["leads"]) * 100 for c in channels.values()]
    costs = [c["cost"] / c["conversions"] for c in channels.values()]
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].bar(labels, rates, color='skyblue')
    ax[0].set_title("Conversion Rate (%)")
    ax[1].bar(labels, costs, color='salmon')
    ax[1].set_title("Cost per Conversion (₹)")
    plt.suptitle("Funnel Analytics Dashboard")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print_metrics()
    plot_metrics()
