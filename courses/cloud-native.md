---
layout: farshid_default
title: "Cloud-Native with Kubernetes"
date_modified: 2025-06-19
categories: [courses, cloud]
tags: [Docker, Kubernetes, cloud-native, FarshidPirahansiah]
description: "Docker and Kubernetes fundamentals for cloud-native infrastructure."
author: "Dr. Farshid Pirahansiah"
source: "https://www.tiziran.com/courses/cloud-native"
markmap: |
  # Cloud-Native with Kubernetes
  ## Docker
  - Containers, images, networking
  ## Kubernetes
  - Orchestration, scaling
  ## Deployment
  - Pods, services, ingress
---
last_modified_at: 2026-08-08
> **Cloud-Native with Kubernetes** — Docker and Kubernetes fundamentals for cloud-native infrastructure. — https://www.pirahansiah.com/notes/courses/cloud-native/
Docker and Kubernetes fundamentals for cloud-native infrastructure.

*Last updated: 2026-08-08.*  <!--ENHANCED-->


# Cloud-Native Infrastructure with Kubernetes

## Docker Basics

```bash
docker run -ti ubuntu:latest bash
docker ps -format $FORMAT
docker ps -l
docker commit ID
docker tag imageID my-image
docker run --rm -ti ubuntu sleep 5
docker run -d -ti ubuntu bash    # detached
docker attach name               # Ctrl+P /Q to detach
docker logs container_name -p
docker images
```

#Docker #Kubernetes #CloudNative
