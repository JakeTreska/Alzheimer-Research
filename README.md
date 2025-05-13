🧠 MRI-Based Alzheimer's Disease Classification

This project applies deep learning to classify MRI brain scans into three cognitive states: Cognitively Normal (CN), Mild Cognitive Impairment (MCI), and Alzheimer’s Disease (AD). Using data from the ADNI dataset and advanced image preprocessing, we built and evaluated state-of-the-art neural networks to identify biomarkers of Alzheimer's with high accuracy.

🔍 Overview

Dataset: 1,716 MRI scans (~84,000+ images) from ADNI
MRI Plane: Axial PD/T2 FSE, selected for clarity of Lateral Ventricles
Preprocessing:
DICOM to JPEG conversion
Reorganized dataset
Focused on middle 4 slices per MRI scan using custom CNN to detect “butterfly” shape of Lateral Ventricles
Applied gamma correction and adaptive thresholding


Model Architectures

1. CRNN (Convolutional Recurrent Neural Network)
CNN for spatial feature extraction
LSTM layers to capture temporal relationships across 4 selected slices
Fully Connected layers for final classification
Accuracy: 75%
2. InceptionV3
Inception-based CNN with parallel convolutions for deeper feature representation
Outperformed CRNN on individual predictions
Accuracy: 81.7%
🔁 Ensembled Model
Combined predictions from CRNN and InceptionV3
Final Accuracy: 82%
Evaluated using Precision, Recall, and F1-score


Results

Model	Accuracy	Parameters
CRNN	75.0%	~2.5M
InceptionV3	81.7%	~22M
Ensemble	82.0%	


📈 Future Directions

Incorporate additional datasets (e.g., OASIS-1, OASIS-2)
Use tools like Freesurfer for advanced brain segmentation
Integrate genetic and proteomic biomarkers (e.g., APOE ε4, Tau, Beta-Amyloid)
Analyze more than 4 slices per scan using 3D CNNs or attention mechanisms


🙏 Acknowledgements

This work was conducted under the mentorship of Dr. Juhao Wu at SLAC National Accelerator Laboratory. Huge thanks to the SLAC team and all collaborators who made this possible.
