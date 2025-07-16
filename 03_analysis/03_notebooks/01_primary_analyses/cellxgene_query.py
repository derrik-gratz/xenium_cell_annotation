"""
cellxgene_query.py

Demonstrates how to query datasets from the cellxgene census and load them as AnnData objects.
Sections are marked for interactive exploration or notebook conversion.
"""

import cellxgene_census
import anndata
import pandas as pd

# 1. List available metadata keys for a given organism
def list_available_metadata_keys(organism="Homo sapiens"):
    census = cellxgene_census.open_soma()
    keys = list(census["census_data"][organism.lower().replace(" ", "_")].obs.keys())
    print("Available cell metadata keys:")
    for k in keys:
        print(f"  - {k}")
    census.close()
    return keys

# 2. Show example values for a metadata key
def show_example_values(organism="Homo sapiens", key="cell_type", n=10):
    census = cellxgene_census.open_soma()
    obs = census["census_data"][organism.lower().replace(" ", "_")].obs.read(column_names=[key]).concat().to_pandas()
    print(f"Example values for '{key}':")
    print(obs[key].drop_duplicates().head(n))
    census.close()

# 3. Query and load AnnData
def query_and_load_anndata(
    organism="Homo sapiens",
    obs_value_filter=None,
    var_value_filter=None,
    obs_column_names=None,
    var_column_names=None
):
    census = cellxgene_census.open_soma()
    adata = cellxgene_census.get_anndata(
        census=census,
        organism=organism,
        obs_value_filter=obs_value_filter,
        var_value_filter=var_value_filter,
        obs_column_names=obs_column_names,
        var_column_names=var_column_names,
    )
    census.close()
    return adata

if __name__ == "__main__":
    print("\n=== 1. List available metadata keys ===")
    keys = list_available_metadata_keys("Homo sapiens")

    # For interactive use: let user pick a key to explore
    print("\n=== 2. Show example values for a metadata key ===")
    key_to_explore = "cell_type"  # Change as needed
    show_example_values("Homo sapiens", key=key_to_explore)

    # For interactive use: let user define a query
    print("\n=== 3. Query and load AnnData ===")
    # Example: Query for B cells in lung with COVID-19, only primary data
    obs_value_filter = (
        "cell_type == 'B cell' and tissue_general == 'lung' "
        "and disease == 'COVID-19' and is_primary_data == True"
    )
    obs_column_names = ["sex", "cell_type", "tissue_general", "disease", "is_primary_data"]
    print(f"Querying with filter: {obs_value_filter}")
    adata = query_and_load_anndata(
        organism="Homo sapiens",
        obs_value_filter=obs_value_filter,
        obs_column_names=obs_column_names
    )
    print("\nAnnData object summary:")
    print(adata)
    print("\nFirst few rows of adata.obs:")
    print(adata.obs.head())

    # For notebook: insert more interactive exploration here (e.g., adata.var, adata.X, plotting, etc.) 