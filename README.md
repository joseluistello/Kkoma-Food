# Kkoma
### High Level Design

### Full Stack Web Application for Instant Grocery and Retail Delivery. Build with Django Rest Framework, Vue.js, Bulma and Stripe.

[Kkoma](https://user-images.githubusercontent.com/65988061/147229494-358b6e27-7e50-4088-9c10-4e011f6d8ae1.mp4)

[1. First Part](#1-first-part)

&nbsp;&nbsp;[1.1 Abstract](#11-description)

&nbsp;&nbsp;[1.2 Acronyms](#12-acronyms)

&nbsp;&nbsp;[1.3 Goals](#13-goals)

&nbsp;&nbsp;[1.4 Stakeholders](#14-stakeholders)

&nbsp;&nbsp;[1.5 Assumptions](#15-assumptions)

&nbsp;&nbsp;[1.6 Limitations & Unknowns](#16-limitations-and-unknowns)

&nbsp;&nbsp;[1.7 Supported use-cases](#17-supported-use-cases)

&nbsp;&nbsp;[1.8 Out of Scope](#18-out-of-scope)


[2. Proposal](#2-Proposal)

&nbsp;&nbsp;[2.0 Architecture](#20-architecture)

&nbsp;&nbsp;[2.1 Architecture Diagram](#21-architecture-diagram)

[3. How to run](#3-How-to-run)

&nbsp;&nbsp;[3.1 Installation](#31-installation)

--- 

## 1. First Part

### 1.1 Abstract

This project aims to replicate the functionality of startups such as Justo or JOKR. It is a platform I created to learn how to develop full-stack projects.

### 1.2 Acronyms

- DRF: Django Rest Framework
- DB: Database
- API: Application Programming Interface 

### 1.3 Goals

Provide a system architecture that allows users to make online grocery purchases. Additionally, this project targets the open-source software development community

### 1.4 Stakeholders
- Project Owner: [Jose Luis Tello](https://joseluistello.live/fijacion-de-precios)
- Open-source community: Anyone interested in copying, manipulating and reproducing this software for learning purposes.

### 1.5 Assumptions
- Products are separated by category 
- Each category represents a set of related products 
- Django Rest Framework was chosen to create the Rest API used in the backend
- Continuous integration with Stripe

### 1.6 Limitations & Unknowns
- The currency selected is USD
- Stripe Support

### 1.7 Supported use-cases
- Users can find products through a search engine
- Users can view their purchase history
- Users can buy an unlimited number of products 
- System is able to send notifications at any part of the purchasing process

### 1.8 Out of Scope
- Real-time GPS
- Reviews

## 2. Proposal

### 2.1 Architecture

### 2.2 Architecture diagram
