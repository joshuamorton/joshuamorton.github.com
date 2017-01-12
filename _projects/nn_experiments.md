---
layout: page
title: Neural Network Experiments
priority: 150
logo: line-chart
summary: |
    Research project on how neural networks interact with time-series data.
---

In Fall 2016, I was able to work with Professor Lance Fortnow on an independent
study/undergraduate research project. The goal of this project was to explore a
question of mutual interest: in systems like the stock market, where there can
be abrupt changes in the underlying assumptions about the system as a whole
(say, following the financial crisis, or following September 11th), is there a
way to have a pretrained model converge to the new understanding more quickly
than it would normally, and more quickly than training a new model from scratch
would converge?

While not conclusive, the answer seemed to be that with normal networks there
was nothing that was effective, however recurrent neural networks were
incredibly effective as long as the data could be formed as a time series (which
was almost always possible with data where this kind of problem could arise).

The code for this project is a number of dirty and hacky tensorflow models that
will soon be availible here.
