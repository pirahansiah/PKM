---
layout: default
author: Dr. Farshid Pirahansiah
categories: [conference-paper, character-recognition, feature-extraction]
tags: [character-recognition, global-feature, OCR, pattern-recognition, image-processing, computer-vision]
description: "Conference paper on character recognition using global feature extraction methods."
excerpt: "Methods for character recognition based on global feature extraction techniques for optical character recognition tasks."
seo_title: "Character Recognition Based on Global Feature Extraction"
seo_description: "Research on character recognition approaches using global feature extraction for OCR applications."
keywords: [character recognition, global feature, OCR, pattern recognition, image processing]
title: "Character Recognition Based on Global Feature"
date: 2024-10-19
---

Character_Recognition_Based_on_Global_Feature



https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Character_Recognition_Based_on_Global_Feature


[spotify]( https://podcasters.spotify.com/pod/show/pirahansiah/episodes/My-Conference-Paper-Character-Recognition-Based-on-Global-Feature-e2ps1tp)

[PDF Download My Conference Paper]( https://doi.org/10.1109/ICEEI.2011.6021649 )


{% if page.extname == "Character_Recognition_Based_on_Global_Feature.md" %}
  ![My Conference Paper  Character Recognition Based on Global Feature ](/farshid/portfolio/publications/Papers/Character_Recognition_Based_on_Global_Feature.png)
{% else %}
  <img src="/farshid/portfolio/publications/Papers/Character_Recognition_Based_on_Global_Feature.png" alt="My Conference Paper: Character Recognition Based on Global Feature "  style="max-width: 100%; height: auto;">
{% endif %}


# Character Recognition Based on Global Feature Extraction

## 1. Introduction
   - **Objective**: Propose a combination of two feature extraction techniques for character recognition.
   - **Key Techniques**:
     - Gray Level Co-occurrence Matrix (GLCM)
     - Edge Direction Matrix (EDMS)
   - **Challenges**:
     - Selecting the best feature extraction technique for various character recognition tasks.

## 2. Feature Extraction Techniques
   - **Gray Level Co-occurrence Matrix (GLCM)**:
     - Focuses on texture and pixel relationships in the image.
     - Extracts texture features for character recognition.
   - **Edge Direction Matrix (EDMS)**:
     - Emphasizes edges and directions in character images.
     - Extracts shape features.

## 3. Proposed Method
   - **Combination of GLCM and EDMS**:
     - A hybrid approach that leverages both texture and edge features.
     - Aims to improve accuracy over using either GLCM or EDMS alone.

## 4. Classification Techniques
   - **Classifiers Used**:
     - Neural Networks (NN)
     - Bayesian Networks (BN)
     - Decision Tree Classifiers
   - **Objective**: Find the best classifier to complement the hybrid feature extraction method.

## 5. Experimental Results
   - **Datasets**:
     - Binary character images of different sizes used for testing.
   - **Performance**:
     - The hybrid method (GLCM + EDMS) outperforms individual feature extraction techniques.
     - Results show improved accuracy in character recognition tasks.

## 6. Conclusion
   - **Key Findings**:
     - The combination of GLCM and EDMS provides better recognition performance than using either technique alone.
   - **Implications**:
     - More reliable character recognition systems for real-world applications.