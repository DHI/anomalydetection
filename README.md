# anomalydetection: Anomaly Detection for time series data.
Sensors often provide faulty or missing observations. These anomalies must be detected automatically and replaced with more feasible values before feeding the data to numerical simulation engines as boundary conditions or real time decision systems.

This package aims to provide examples and algortihms for detecting anomalies in time series data specifically tailored to DHI users and the water domain. It is simple to install and deploy operationally and is accessible to everyone (open-source).

# Installation
pip install git+https://github.com/DHI/anomalydetection.git

# Definitons
Note that we distinguish between [two types of anomaly detection]: https://scikit-learn.org/stable/modules/outlier_detection.html

- Outlier detection (unsupervised anomaly detection)
The training data may contain outliers, i.e. observations far from most other observations. Outlier detectors try to conecntrate on the observations in the training data that similar and close togehter, and ignores observations further away.

- Novelty detection (semi-supervised anomaly detection)
The training data is considered "normal" and is not polluted by outliers. New test data observations can be categorized as an outlier and is in this context called a novelty.



