# SUMMARY

This dataset provides global 10K most populous locations from Sentinel1/2 and Landsat missions. The dataset was collated from [SSL4EO-L](https://huggingface.co/datasets/torchgeo/ssl4eo_l) and [SSL4EO-S12](https://huggingface.co/datasets/wangyi111/SSL4EO-S12). Apart from original metadata from the geotifs, it contains an additional context file which contains information extracted from filenames and geotif metadata for ease of access. Data has been preprocessed save Normalization for quick access when developing ML products.


ssl4eo-s12-landsat-combined

## About
This dataset combines SSL4EO-L and SSL4EO-S12 to form a combined multiview dataset. The combined dataset has 66800 locations with view from atleast 5 sensors.
The sensors available are:

```bash
- s1_grd
- s2_l1c
- s2_l2a
- ssl4eo_l_oli_sr
- ssl4eo_l_tirs_toa
- ssl4eo_l_etm_sr
- ssl4eo_l_etm_toa
- ssl4eo_l_tm_toa
```

The data has been very kindly hosted in AWS Open Data Registry, in ```ssl4eo-s12-landsat-combined``` bucket. 


## Data
Each of the above folders has atleast 8 files and at max 12 files. All folders have original image data as .h5 format, along with context for four seasons. In most cases, there might be additional metadata file which contains details about the original satellite metadata. The file details are as given below:

```bash
- <datestr>.h5 -> contains all bands fom the relevant satellite and product 
- context_<datestr>.json -> contains releavant context for the corresponding datestr.h5
- meta_<datestr>.json -> Additional metadata if available for the corresponding datestr.h5
```

All input files are of shape 224, 224. Additionally, Lee-filtering based speckle fltering has been done for Sentinel1 products have been and Sentinel2 products have been scaled according to information provided [here](https://forum.sentinel-hub.com/t/normalization-of-sentinel-data-for-ml-downstream/5459/2). Sentinel data has additionally been scaled to be between 0 and 255. Landsat data is already in between that range. No normalization has been applied to the input data.

## Data Access
ssl4eo-s12-landsat-combined

## Data Tutorial
Please find the attached python scripts for visualizing and accessing the data.

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
