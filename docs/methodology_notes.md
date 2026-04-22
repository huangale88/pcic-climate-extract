# Climate Data Methodology Notes

## 1. Background

Mine water balance models require robust estimates of precipitation and temperature inputs over long temporal periods to characterize average conditions and interannual variability. In many remote regions, local meteorological station coverage is sparse, discontinuous, or unavailable.

Gridded observational climate datasets provide spatially continuous representations of meteorological variables derived from quality-controlled station data combined with interpolation techniques. These datasets are commonly used in mine water balance studies where on-site observational data are limited.

---

## 2. Gridded Dataset Description

This project uses the **PCIC‑Blend Gridded Observations Dataset**, which combines several well-established climate products to improve spatial realism and statistical performance across western Canada:

- **PNWNAmet**  
  Provides daily gridded precipitation, maximum temperature, and minimum temperature with strong performance in representing orographic precipitation patterns.

- **NRCANmet Version 2**  
  An updated temperature dataset based on adjusted and homogenized Canadian climate station data.

- **NRCANmet‑Adjusted**  
  A precipitation dataset derived from adjusted daily rainfall and snowfall observations from Environment and Climate Change Canada.

The datasets are blended within a transition region east of the Rocky Mountains using a sigmoidal weighting function, leveraging the relative strengths of each product.

**Temporal coverage:** 1950–2012  
**Spatial resolution:** approximately 10 km  
**Temporal resolution:** daily  

All station observations used in the gridding process were subject to quality control prior to interpolation.

---

## 3. Intended Application

The PCIC‑Blend dataset is used in this project as a **baseline climatology** for mine water balance modeling. The data are aggregated to monthly statistics appropriate for long-term planning, design evaluation, and uncertainty characterization.

This dataset is not relied upon for detailed analysis of short-duration extreme events or operational forecasting.

---

## 4. Site-Specific Climate Extraction

Climate data are extracted for the mine site by selecting the nearest grid cell based on geographic coordinates (latitude and longitude). This approach assumes that the selected grid cell provides a reasonable representation of site-scale average climatic conditions.

Daily time series are retained during early processing stages to preserve inherent temporal variability prior to aggregation.

---

## 5. Temporal Aggregation and Statistics

Daily climate data are aggregated to monthly statistics according to the following methods:

- **Precipitation**  
  Daily precipitation values are summed to monthly totals.

- **Temperature**  
  Daily mean temperature is calculated as the average of daily minimum and maximum temperatures, then averaged to monthly means.

For each calendar month (January through December), long-term climatological statistics are calculated over the full available period:

- Monthly mean
- Monthly standard deviation

These statistics form the primary deterministic and probabilistic climate inputs used in the mine water balance model.

---

## 6. Validation Against Station Data

Where available, gridded climate data are compared against observations from the nearest meteorological station or airport. Validation focuses on:

- Bias in monthly mean precipitation and temperature
- Agreement in seasonal patterns
- Relative representation of variability

If systematic biases are identified, simple adjustment methods may be applied:
- Multiplicative factors for precipitation
- Additive offsets for temperature

All validation results and adjustments are documented to maintain transparency.

---

## 7. Treatment of Climate Variability and Uncertainty

Monthly variability derived from historical observations is used as a proxy for climate uncertainty in the water balance. Uncertainty may be propagated through the water balance using:

- ±1 standard deviation envelopes
- Monte Carlo simulation approaches implemented within Excel

The uncertainty framework reflects historical climate variability and does not explicitly include future climate change projections.

---

## 8. Key Assumptions and Limitations

The methodology described herein is subject to the following limitations:

- Grid-cell averaging may underrepresent localized precipitation extremes and convective storm impacts
- Climate statistics are based on historical observations from 1950 to 2012
- Climatic stationarity is assumed for baseline water balance analysis

These limitations should be considered when interpreting water balance results and communicating findings.