import json
import matplotlib.pyplot as plt

json_file_path = "metrics.json"
data = []
with open(json_file_path, "r") as f:
    for line in f:
        data.append(json.loads(line.strip()))

iterations = []
segm_ap_values = []

for entry in data:
    if "iteration" in entry and "segm/AP" in entry:
        iterations.append(entry["iteration"])
        segm_ap_values.append(entry["segm/AP"])

plt.figure(figsize=(10, 6))
plt.plot(iterations, segm_ap_values, marker='o', label='segm/AP', color='blue')
plt.title("segm/AP vs Iterations")
plt.xlabel("Iterations")
plt.ylabel("segm/AP")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("segm_ap_vs_iterations.png")
# plt.show()

## TOTAL LOSS
iterations = []
total_loss_values = []

for entry in data:
    if "iteration" in entry and "total_loss" in entry:
        iterations.append(entry["iteration"])
        total_loss_values.append(entry["total_loss"])
    else:
        continue

plt.figure(figsize=(10, 6))
plt.plot(iterations, total_loss_values, label='Total Loss', color='red')
plt.title("Total Loss vs Iterations")
plt.xlabel("Iterations")
plt.ylabel("Total Loss")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("total_loss_vs_iterations.png")
# plt.show()

# import json
# import matplotlib.pyplot as plt

# # Load JSON file line by line
# json_file_path = "metrics.json"  # Replace with your file's path
# data = []
# with open(json_file_path, "r") as f:
#     for line in f:
#         data.append(json.loads(line.strip()))

# # Extract iterations and segm/AP values
# iterations = []
# loss_mask_values = []

# for entry in data:
#     if "iteration" in entry and "loss_mask" in entry:
#         iterations.append(entry["iteration"])
#         loss_mask_values.append(entry["loss_mask"])

# # Plot segm/AP against iterations
# plt.figure(figsize=(10, 6))
# plt.plot(iterations, loss_mask_values, label='loss_mask', color='blue')
# plt.title("loss_mask vs Iterations")
# plt.xlabel("Iterations")
# plt.ylabel("loss_mask")
# plt.grid(True)
# plt.legend()
# plt.tight_layout()

# # Save or show the plot
# # plt.savefig("segm_ap_vs_iterations.png")  # Optional: Save the plot
# plt.show()