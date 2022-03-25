# Tracing Tokyo's air sources to identify Kawasaki Disease's etiological triggers

<img src="https://vasculitis2022.org/wp-content/uploads/2020/10/Vasculitis-2022.png" width="350" />

This document intends to expand, provide context and reproducible analysis code on the study presented in a [poster](https://github.com/helical-itn/anca2022-posters/raw/main/posters/ESR6.%20Alejandro%20Fontal/alejandro_poster_vasculitis_2022.pdf) for the [20th International Vasculitis and ANCA Workshop](https://vasculitis2022.org/), which takes place in Dublin, Ireland, from the 3rd to the 6th of April 2022.



## Background

**Kawasaki Disease (KD)** is a systemic vasculitis that mainly affects children **younger than 5 years old**. Although KD cases have been registered in over 60 countries across several continents, its incidence is **highest in East Easia**, particularly in **Japan**, where the highest annual incidence rate was recorded in 2018: **359 per 100 000 children aged 0-4 years** {cite}`AE202023`. After more than five decades since its discovery and active research, the etiology of KD is **yet to be elucidated**. Recent studies have analyzed the association between KD and diverse environmental factors, with some advances pointing towards a **relevant role of the atmospheric transport of a wind-borne agent triggering the disease** {cite}`rodo_association_2011, rodo_tropospheric_2014`. The specific nature of this agent(s) is still unknown, with biological (bacterial, fungal or viral) and chemical (pollution) elements being the strongest candidates to initiate the autoimmune cascade which leads to the disease.

One of the most striking features of the epidemiological dynamics of Kawasaki Disease is the defined **seasonal structure** across multiple countries, with broad coherence in fluctuations of cases across the Northern Hemisphere extra-tropical latitudes {cite}`burns_seasonality_2013`. 

In the case of Japan, the number of admissions has been recorded in the epidemiological records since 1970, and show the following pattern:

![KD Records Japan](images/kd_records_japan.png)

Three main features are notable:

+ The epidemic peaks of **1979**, **1982** and **1986** (and to a lesser degree, **1984**).
+ The **increasing trend** starting around **1995** until today.
+ The marked **seasonality** from **2000** onwards.

All of this prompts several questions towards the nature of the drivers of these changes in incidence for a disease that is non-communicable in nature.

In this work, we focus on the period from **2011 to 2018** for the prefecture of **Tokyo**, and try to associate the **seasonal maxima** and **minima** to **atmospheric transport patterns**.

## Methods


### Kawasaki Disease

#### Source

We collected data on **date of admission** and **reported date of symptoms onset** for a total of **13970 KD cases** in hospitals belonging to the **Tokyo** prefecture from **2011** to **2018**. This data was originally collected by the (22nd to 25th) nationwide epidemiological surveys of Kawasaki disease in Japan {cite}`makino2015descriptive, makino2018epidemiological, makino2019nationwide, AE202023`. 

#### Computation of KD maxima and minima

The data was aggregated to generate **daily counts** of hospital admissions and **registered onsets**. 

![Daily counts](images/daily_cases_tokyo.png)

The daily counts were then aggregated by week to obtain a weekly estimate of **case onsets per day** (that is, the daily average for each consecutive week in a year).  

To generate the **yearly maxima** and **minima**, we selected the **5 weeks** with the **most daily cases** and the **5 weeks** with the **least daily cases** for **each year**, respectively, and are shown in the following figure:

![Weekly counts](images/weekly_kd_tokyo.png)





### Trajectory Generation

To model **air mass back-trajectories**, we used the Hybrid Single Particle Lagrangian Integrated Trajectory (**HYSPLIT**) model version 5 {cite}`stein_noaas_2015`, which we operated programmatically via the Python package `PySPLIT` {cite}`warner_introduction_2018` to generate a high amount of trajectories. 



#### Meteorology data


### Differential Trajectory Analysis

## Results

## Limitations / Outlook

## References

```{bibliography}
:style: unsrt
```


