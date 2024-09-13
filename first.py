import matplotlib.pyplot as plt

# Data for the bar chart
categories = ['Freelancer App', 'Product Catalog', 'School Friend Reunion Project', 'Tailor Website', 'Investment App']
hours = [10, 15, 20, 25, 30]

# Data for the line chart
months = ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5']
hours_spent = [5, 10, 20, 15, 25]

# Create a bar chart
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(categories, hours, color='skyblue')
plt.xlabel('Projects')
plt.ylabel('Hours Spent')
plt.title('Hours Spent on Projects')

# Create a line chart
plt.subplot(1, 2, 2)
plt.plot(months, hours_spent, marker='o', linestyle='-', color='orange')
plt.xlabel('Time')
plt.ylabel('Hours Spent')
plt.title('Hours Spent Over Time')

plt.tight_layout()
plt.show()
