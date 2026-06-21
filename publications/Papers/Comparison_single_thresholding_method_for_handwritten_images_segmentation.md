---
layout: default
author: Dr. Farshid Pirahansiah
categories: [conference-paper, image-processing, thresholding]
tags: [thresholding, handwritten-images, segmentation, image-processing, binarization, computer-vision]
description: "Conference paper comparing single thresholding methods for handwritten image segmentation."
excerpt: "Comparison of thresholding techniques for segmenting handwritten images in document analysis applications."
seo_title: "Comparison of Single Thresholding Methods for Handwritten Image Segmentation"
seo_description: "Research comparing thresholding approaches for handwritten image segmentation in document processing."
keywords: [thresholding, handwritten images, segmentation, image processing, document analysis]
title: "Comparison Single Thresholding Method for Handwritten Images Segmentation"
date: 2024-10-19
---


Comparison_single_thresholding_method_for_handwritten_images_segmentation


https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Comparison_single_thresholding_method_for_handwritten_images_segmentation


[spotify](https://podcasters.spotify.com/pod/show/pirahansiah/episodes/My-Conference-Paper-Comparison-single-thresholding-method-for-handwritten-images-segmentation-e2ps22i )

[PDF Download My Conference Paper](https://doi.org/10.1109/ICPAIR.2011.5976918  )


{% if page.extname == "Comparison_single_thresholding_method_for_handwritten_images_segmentation.md" %}
  ![My Conference Paper  Comparison single thresholding method for handwritten images segmentation ](/farshid/portfolio/publications/Papers/Comparison_single_thresholding_method_for_handwritten_images_segmentation.png)
{% else %}
  <img src="/farshid/portfolio/publications/Papers/Comparison_single_thresholding_method_for_handwritten_images_segmentation.png" alt="My Conference Paper: Comparison single thresholding method for handwritten images segmentation "  style="max-width: 100%; height: auto;">
{% endif %}


# Comparison Single Thresholding Method for Handwritten Images Segmentation

## 1. Introduction
   - **Objective**: Propose and compare single thresholding methods for handwritten image segmentation.
   - **Key Concepts**:
     - Thresholding separates objects from the background in images.
     - Peak Signal-to-Noise Ratio (PSNR) is used to measure image quality.
   - **Importance**:
     - Handwritten recognition has various applications in mobile devices and OCR systems.

## 2. State of the Art
   - **Otsu’s Method**:
     - An unsupervised, nonparametric method for automatic threshold selection.
     - Uses bounding boxes of fragments and calculates global thresholds by maximizing class variance.
   - **Thresholding Techniques**:
     - **Single Thresholding**: Applies a single threshold value to the entire image.
     - **Multi-Level Thresholding**: Uses multiple threshold values for segmenting complex images.

## 3. Proposed Method
   - **PSNR-Based Thresholding**:
     - Uses PSNR to determine the quality of image segmentation.
     - Measures the effectiveness of separating objects (characters) from the background in handwritten images.
   - **Advantages**:
     - Optimized for average-quality handwritten images.
     - Improves segmentation performance compared to other methods.

## 4. Experimental Results
   - **Method Comparison**:
     - The proposed PSNR-based method is compared with Otsu's method and other techniques.
   - **Performance**:
     - The proposed method shows better PSNR values, indicating superior image segmentation quality.
     - Optimized for real-world handwritten images where object-background separation is crucial.

## 5. Conclusion
   - **Key Findings**:
     - PSNR-based single thresholding outperforms traditional methods like Otsu's in segmenting handwritten images.
   - **Implications**:
     - Suitable for OCR systems and mobile applications involving handwritten text recognition.