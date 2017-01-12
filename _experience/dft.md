---
layout: page
title: DecisionFirst Technologies
priority: 900
logo: assets/images/decisionfirst.jpg
summary: |
    I worked as a Business Intelligence intern, building integrations for some
    of DFTs clients, as well as developer tools for other DFT devs.
---

During the summer of 2015 I interned with [Decision First
Technologies](http://www.decisionfirst.com/), a small Atlanta-based SAP parter
for business intelligence consulting. I worked on three major projects. In
    addition to the three projects, I helped to design and build client
    dashboards.

The first project was to create an end-user installer for a
[Salesforce-BusinessObjects integration
tool](http://www.decisionfirst.com/offerings/salesforce-connect-for-sap-analytics/).
This involved building a Java-based GUI and command line application to gather
information from an existing BusinessObjects installation and use it to
automatically configure a server. Additionally, we improved the process to
create a specific salesforce installation.

The second was to build a specialized set of internal tooling for
BusinessObjects dashboards. Specifically, a common client request was for
dashboards to contain a table of database-bound key performance indicators along
with summary analytics for them. The tool I created was a javascript extension
to an existing BusinessObjects component that would allow the streamlined
creation of KPI tables and the included charts (such as bulletcharts,
sparklines, and other KPI indicators). The tool was built in javascript using
[d3](http://d3js.org/) for visualizations.

The final project was an exploratory implementation of an alternate
BusinessObjects backend. Instead of a Java and tomcat-based system, the interns
suggested we design a python-based system built on Flask and SQLAlchemy because
it would be both faster and easier to use. The system we designed was both,
however it was difficult to impossible to deploy on client systems. We did use
it to streamline the process of building and testing dashboards and
visualizations.
