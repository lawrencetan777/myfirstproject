
from roboflow import Roboflow
rf = Roboflow(api_key="UirqjppkQ1iI56ScqxWu")
project = rf.workspace().project("cones-cjefi")
model = project.version(12).model

# infer on a local image
print(model.predict("python apps\PXL_20231109_032023569-NIGHT.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("python apps\PXL_20231109_032023569-NIGHT.jpg", confidence=40, overlap=30).save("prediction.jpg")

