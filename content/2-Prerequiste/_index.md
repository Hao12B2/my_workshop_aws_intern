---
title : "Preparation"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 2. </b> "
---
### Prerequisites
- An AWS account (mandatory)
- Basic understanding of AWS services like S3, Glu and Athena

### AWS Services Used
- **AmazonS3**: Forstoring raw and processed data.
- **AWSGlue**: Forbuilding and managing ETL pipelines.
- **AWSAthena**: Forquerying data using SQL-like syntax.

### Data Source
The data used in this workshop is sourced from the [Spotify Dataset 2023](https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023) available on Kaggle. The dataset, created by Tony Gordon Jr., includes detailed information about Spotify albums, artists, tracks, and various audio features like danceability, energy, loudness, and more. The dataset is available in CSV format and has been pre-processed for use in this project.

### Data Description
- Albums: Contains details of all the albums, including album ID, name, popularity, and release date.
- Artists: Contains information about the artists, including their names, number of
followers, and genres.
- Tracks: Contains track-level data, including track ID, popularity, and other features like
danceability and energy.
- Spotify Features: Contains various audio features like loudness, mode, speechiness, and
valence.

> Nguyen Van Hao

{{% notice info %}}

{{% /notice %}}