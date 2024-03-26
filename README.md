# YOLOv8-pose-train-T-less-and-estimate-its-pose
This repo uses YOLOv8-pose to train the 14th object of the datastes of T-less,then predicts its key-points and estimates its pose with a deep camera.

Step1.
	Label the 14th object with keypoints by Labelme.
Step2.
	Transform the keypoints' informations to training of YOLOv8-pose.
Step3.
	Predict the key-points of 14th objects.
Step4.
	Estimate the object's pose by the keypoints with deep camera.
