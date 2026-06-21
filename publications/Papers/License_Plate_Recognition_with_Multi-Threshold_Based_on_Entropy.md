---
layout: farshid_default
author: Dr. Farshid Pirahansiah
categories: [conference-paper, license-plate-recognition, entropy]
tags: [license-plate, entropy, multi-threshold, image-segmentation, computer-vision, intelligent-transportation]
description: "Conference paper on license plate recognition using multi-threshold methods based on entropy analysis."
excerpt: "Multi-threshold approach for license plate recognition using entropy-based image segmentation techniques."
seo_title: "License Plate Recognition with Multi-Threshold Based on Entropy"
seo_description: "Research on entropy-based multi-threshold methods for accurate license plate recognition systems."
keywords: [license plate recognition, entropy, multi-threshold, image segmentation, computer vision]
title: "License Plate Recognition with Multi-Threshold Based on Entropy"
date: 2024-10-19
---

License_Plate_Recognition_with_Multi-Threshold_Based_on_Entropy



https://www.pirahansiah.com/contents/publications/Papers/License_Plate_Recognition_with_Multi-Threshold_Based_on_Entropy


[spotify]( https://podcasters.spotify.com/pod/show/pirahansiah/episodes/License-Plate-Recognition-with-Multi-threshold-based-on-Entropy-e2ps290)

[PDF Download My Conference Paper]( https://doi.org/10.1109/ICEEI.2011.6021627 )


{% if page.extname == "License_Plate_Recognition_with_Multi-Threshold_Based_on_Entropy.md" %}
  ![My Conference Paper License Plate Recognition with Multi-Threshold Based on Entropy  ](/contents/publications/Papers/License_Plate_Recognition_with_Multi-Threshold_Based_on_Entropy.png)
{% else %}
  <img src="/contents/publications/Papers/License_Plate_Recognition_with_Multi-Threshold_Based_on_Entropy.png" alt="My Conference Paper: License Plate Recognition with Multi-Threshold Based on Entropy "  style="max-width: 100%; height: auto;">
{% endif %}


# License Plate Recognition with Multi-threshold based on Entropy

## 1. Introduction
   - **Objective**: Propose a multi-thresholding method for license plate recognition.
   - **Importance of Thresholding**:
     - Simplifies image segmentation
     - Ensures robustness and accuracy in recognizing license plate characters.
   - **Challenges**:
     - Selecting the correct threshold values for better segmentation results.

## 2. Entropy-based Thresholding
   - **Method**:
     - Based on maximizing the cross entropy between the original image and the segmented image.
     - Entropy is treated as a probability distribution of the image histogram.
   - **Historical Background**:
     - Originally proposed by Pun and later improved by Kapur for image segmentation.
     - Entropy-based thresholding is widely used for bi-level and multi-level thresholding.

## 3. Proposed Method
   - **Multi-thresholding Based on Maximum Entropy**:
     - Selects several threshold values by maximizing the entropy.
     - Integrates partial ranges of the image histogram to achieve better segmentation.
   - **Comparison with Other Methods**:
     - Compared to single-thresholding techniques based on maximum entropy.
     - Evaluates how multi-thresholding enhances the recognition accuracy.

## 4. License Plate Recognition Process
   - **Steps**:
     1. **Image Segmentation**: Separates the license plate region using multi-thresholding.
     2. **Character Segmentation**: Applies the selected thresholds to segment individual characters.
     3. **Recognition**: Recognizes the segmented characters to produce the license plate number.

## 5. Results and Discussion
   - **Performance**:
     - The proposed multi-threshold method outperforms single-thresholding techniques.
     - Shows improved segmentation results for varying lighting and environmental conditions.

## 6. Conclusion
   - **Key Findings**:
     - Multi-thresholding based on entropy enhances the accuracy of license plate recognition.
   - **Implications**:
     - Can be applied in real-world license plate recognition systems with better robustness.