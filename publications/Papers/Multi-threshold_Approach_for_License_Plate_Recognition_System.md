---
layout: farshid_default
author: Dr. Farshid Pirahansiah
categories: [conference-paper, license-plate-recognition, thresholding]
tags: [license-plate, multi-threshold, image-segmentation, thresholding, computer-vision, intelligent-transportation]
description: "Conference paper on a multi-threshold approach for license plate recognition systems."
excerpt: "Multi-threshold methods for improved license plate recognition in intelligent transportation systems."
seo_title: "Multi-threshold Approach for License Plate Recognition System"
seo_description: "Research on multi-threshold techniques for enhancing license plate recognition accuracy."
keywords: [license plate recognition, multi-threshold, image segmentation, thresholding, intelligent transportation]
title: "Multi-threshold Approach for License Plate Recognition System"
date: 2024-10-19
markmap: |
  # Multi-threshold LPR
  ## Adaptive Approach
  - MLP + Backpropagation
  - Peak Value Analysis
  ## Comparison Methods
  - Kittler/Illingworth
  - Potential Difference
  - Otsu's Method
  ## Recognition Process
  - Image Segmentation
  - Character Segmentation
  - Classification
  ## Future Work
  - Real-time Specifications
---


Multi-threshold_Approach_for_License_Plate_Recognition_System


https://www.pirahansiah.com/contents/publications/Papers/Multi-threshold_Approach_for_License_Plate_Recognition_System


[spotify]( https://podcasters.spotify.com/pod/show/pirahansiah/episodes/My-Conference-Paper-Multi-threshold-Approach-for-License-Plate-Recognition-System-e2ps2fe)

[PDF Download My Conference Paper]( http://waset.org/publications/3636 )


{% if page.extname == "Multi-threshold_Approach_for_License_Plate_Recognition_System.md" %}
  ![My Conference Paper  Multi-threshold Approach for License Plate Recognition System ](/contents/publications/Papers/Multi-threshold_Approach_for_License_Plate_Recognition_System.png)
{% else %}
  <img src="/contents/publications/Papers/Multi-threshold_Approach_for_License_Plate_Recognition_System.png" alt="My Conference Paper:  Multi-threshold Approach for License Plate Recognition System"  style="max-width: 100%; height: auto;">
{% endif %}


# Multi-threshold Approach for License Plate Recognition System

## 1. Introduction
   - **Objective**: Propose an adaptive multi-threshold approach for image segmentation, specifically in object detection.
   - **Application**: Malaysian License Plate Recognition (LPR) system.
   - **Challenge**: Different types of license plates require varied detection techniques depending on the country.

## 2. Adaptive Multi-threshold Approach
   - **Key Method**:
     - Multi Layer Perceptron (MLP) trained by backpropagation to optimize threshold values.
     - Finds optimum threshold values by analyzing the peak value from a graph of object count versus threshold ranges.
   - **Advantages**:
     - Adaptive to different types of license plates, including single-line and double-line plates with varying fonts.

## 3. Comparison with Other Threshold Methods
   - **Other Techniques**:
     - Kittler and Illingworth’s Threshold
     - Potential Difference
     - Otsu’s Method
   - **Performance**:
     - The adaptive multi-threshold approach improves overall performance compared to these existing methods.

## 4. License Plate Recognition Process
   - **Steps**:
     1. **Image Segmentation**: Applies multi-thresholding to separate the license plate and individual characters.
     2. **Character Segmentation**: Uses the threshold values to segment characters within the license plate region.
     3. **Recognition**: Classifies the segmented characters to extract the license plate number.

## 5. Conclusion and Future Work
   - **Key Findings**:
     - The proposed adaptive multi-threshold method enhances the performance of the LPR system.
   - **Future Work**:
     - Further improvements are underway to accommodate real-time system specifications.