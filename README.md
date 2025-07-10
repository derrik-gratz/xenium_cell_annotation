# Analysis project template

The structure is inspired by the [gin-tonic](https://gin-tonic.netlify.app/standard/) project and the file naming conventions of [The Turing Way](https://book.the-turing-way.org/reproducible-research/rdm/rdm-storage#rr-rdm-storage-organisation).


```
01_documentation                # Documentation relevant to the project
│ project-notebook.txt
│ project-details.txt
02_data                         # Data generated as *inputs* to analysis
└─── 01_raw-data                # Symlinks, copies, or directions for retrieving raw data
└─── 02_data-processing         # Code or receipts from data processing
└─── 03_processed-data          # processed data (include instructions for retrieval)
03_analysis
└─── 01_config                  # Project level definitions that affect multiple scripts.
└─── 02_src                     # Source files for helper code/functions
└─── 03_notebooks               # Data exploration and manipulation experiments
│   └─── 01_primary-analyses    # Main workflow notebooks
│       │   01_first-script.rmd/ipynb/etc
│       │   02...
│   └─── 02_secondary-analyses  # Separate lines of inquiry that may not continue
│       │   02.1_spinoff.rmd/ipynb/etc                           
└─── 04_checkpoints             # Saved objects reflecting a checkpoint after computationally expensive portions of an analysis
│
04_results                      # Tables, models, etc that represent outputs of an analysis for dissemination
└─── tables
└─── figures
│   qc_pics.svg
│   └─── figure-scripts         # Isolated script to iterate on figures for publication
│       │   qc_pics.R
│   └─── figure-data            # Tables of values to accomapny generated figures, for reference & publication
│       │   qc_pics.txt
05_disseminations               # More comprehensive outputs. Reports, slides, tweets, manuscripts, etc.
```
