# from ....tools.normalize import log_cpm
from .....tools.decorators import method

from .....tools.utils import check_version
from scIB.integration import runSaucie
from scIB.preprocessing import hvg_batch, scale_batch, reduce_data


@method(
    method_name="Saucie",
    paper_name="Sc"
    paper_url="temp",
    paper_year=2020,
    code_url="",
    code_version=check_version("saucie"),
    # image="openproblems-template-image" # only if required
)
def saucie_embed_full_unscaled(adata):
    runSaucie(adata, "batch")
    reduce_data(adata, use_rep="X_emb")
    # Complete the result in-place
    return adata

def saucie_embed_hvg_unscaled(adata):
    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)    
    runSaucie(adata, "batch")
    reduce_data(adata, use_rep="X_emb")
    return adata

def saucie_embed_hvg_scaled(adata):
    adata = hvg_batch(adata, "batch", target_genes=2000, adataOut=True)    
    adata = scale_batch(adata, "batch")
    runSaucie(adata, "batch")
    reduce_data(adata, use_rep="X_emb")
    return adata

def saucie_embed_full_scaled(adata):
    adata = scale_batch(adata, "batch")
    runSaucie(adata, "batch")
    reduce_data(adata, use_rep="X_emb")
    return adata


