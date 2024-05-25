# SUMMARY

This dataset provides global 10K most populous locations from Sentinel1/2 and Landsat missions. The dataset was collated from [SSL4EO-L](https://huggingface.co/datasets/torchgeo/ssl4eo_l) and [SSL4EO-S12](https://huggingface.co/datasets/wangyi111/SSL4EO-S12). Apart from original metadata from the geotifs, it contains an additional context file which contains information extracted from filenames and geotif metadata for ease of access. Data has been preprocessed save Normalization for quick access when developing ML products.

## About
This dataset combines SSL4EO-L and SSL4EO-S12 to form a combined multiview dataset. The combined dataset has 605904 locations with following views:

```python
{
    1 view: 157782,
    2 views: 85611,
    3 views: 119746,
    4 views: 88205,
    5 views: 49629,
    6 views: 35564,
    7 views: 43726,
    8 views: 25641
}
```

Views here represents data collected from different missions. The dataset includes all bands for OLI-SR, TM-TOA, S2L2A, OLI-TIRS-TOA, ETM-SR and B1, B9 and B10 from s2_L1C for top of atmosphere data. It also includes VV and VH bands for S1-GRD. Additionally, the following provides more details about combinations of different product types:

```python
ssl4eo_l_tirs_toa: 77088
ssl4eo_l_tm_toa: 55293
ssl4eo_l_oli_sr: 25401
ssl4eo_l_oli_sr, ssl4eo_l_tirs_toa: 9130
ssl4eo_l_etm_sr, ssl4eo_l_etm_toa: 28812
ssl4eo_l_oli_sr, ssl4eo_l_tm_toa: 4795
ssl4eo_l_tirs_toa, ssl4eo_l_tm_toa: 42874
s1_grd, s2_l1c, s2_l2a: 67823
s1_grd, s2_l1c, s2_l2a, ssl4eo_l_oli_sr: 41030
ssl4eo_l_etm_sr, ssl4eo_l_etm_toa, ssl4eo_l_oli_sr: 14616
ssl4eo_l_etm_sr, ssl4eo_l_etm_toa, ssl4eo_l_tirs_toa: 13011
ssl4eo_l_etm_sr, ssl4eo_l_etm_toa, ssl4eo_l_tm_toa: 21450
s1_grd, s2_l1c, s2_l2a, ssl4eo_l_oli_sr, ssl4eo_l_tirs_toa: 13222
s1_grd, s2_l1c, s2_l2a, ssl4eo_l_etm_sr, ssl4eo_l_etm_toa: 12173
s1_grd, s2_l1c, s2_l2a, ssl4eo_l_tm_toa: 3597
s1_grd, s2_l1c, s2_l2a, ssl4eo_l_oli_sr, ssl4eo_l_tm_toa: 8303
ssl4eo_l_oli_sr, ssl4eo_l_tirs_toa, ssl4eo_l_tm_toa: 2846
(
  s1_grd,
  s2_l1c,
  s2_l2a,
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_oli_sr,
  ssl4eo_l_tirs_toa
): 16906
(
  s1_grd,
  s2_l1c,
  s2_l2a,
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_oli_sr,
  ssl4eo_l_tirs_toa,
  ssl4eo_l_tm_toa
): 25641
(
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_oli_sr,
  ssl4eo_l_tirs_toa,
  ssl4eo_l_tm_toa
): 15931
(
  s1_grd,
  s2_l1c,
  s2_l2a,
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_oli_sr
): 24755
(
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_tirs_toa,
  ssl4eo_l_tm_toa
): 16912
(
  s1_grd,
  s2_l1c,
  s2_l2a,
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_oli_sr,
  ssl4eo_l_tm_toa
): 26820
(
  s1_grd,
  s2_l1c,
  s2_l2a,
  ssl4eo_l_oli_sr,
  ssl4eo_l_tirs_toa,
  ssl4eo_l_tm_toa
): 4502
(
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_oli_sr,
  ssl4eo_l_tm_toa
): 14729
(
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_oli_sr,
  ssl4eo_l_tirs_toa): 11937
(
  s1_grd,
  s2_l1c,
  s2_l2a,
  ssl4eo_l_etm_sr,
  ssl4eo_l_etm_toa,
  ssl4eo_l_tm_toa
): 6307
```

Additionally we have 251079 parallel views for S1-GRD, S2-L1C and S2-L2A. ETM-SR, ETM-TOA have 250000 parallel views. 

## Data
Each of the above folders has atleast 8 files. In most cases, there might be additional metadata file which contains details about the original satellite metadata. The file details are as given below:

```bash
- <datestr>.h5 -> contains all bands fom the relevant satellite and product 
- context_<datestr>.json -> contains releavant context for the corresponding datestr.h5
- meta_<datestr>.json -> Additional metadata if available for the corresponding datestr.h5
```

All input files are of shape 224, 224. Additionally, Lee-filtering based speckle fltering has been done for Sentinel1 products have been and Sentinel2 products have been scaled according to information provided [here](https://forum.sentinel-hub.com/t/normalization-of-sentinel-data-for-ml-downstream/5459/2). Sentinel data has additionally been scaled to be between 0 and 255. Landsat data is already in between that range. No normalization has been applied to the input data.

## Data Access

## Data Tutorial

## License

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Citations

```
@article{wang2022ssl4eo,
  title={SSL4EO-S12: A Large-Scale Multi-Modal, Multi-Temporal Dataset for Self-Supervised Learning in Earth Observation},
  author={Wang, Yi and Braham, Nassim Ait Ali and Xiong, Zhitong and Liu, Chenying and Albrecht, Conrad M and Zhu, Xiao Xiang},
  journal={arXiv preprint arXiv:2211.07044},
  year={2022}
}

@misc{stewart2023ssl4eol,
    title={SSL4EO-L: Datasets and Foundation Models for Landsat Imagery}, 
    author={Adam J. Stewart and Nils Lehmann and Isaac A. Corley and Yi Wang and Yi-Chia Chang and Nassim Ait Ali Braham and Shradha Sehgal and Caleb Robinson and Arindam Banerjee},
    year={2023},
    eprint={2306.09424},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```
