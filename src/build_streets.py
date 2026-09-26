"""Build deduplicated street-name tables from the IBGE CNEFE file for Piracicaba."""

from __future__ import annotations

import io
import zipfile
from pathlib import Path
from urllib.request import urlopen

import pandas as pd

SOURCE_URL = (
    "https://ftp.ibge.gov.br/Cadastro_Nacional_de_Enderecos_para_Fins_Estatisticos/"
    "Censo_Demografico_2022/Arquivos_CNEFE/CSV/Municipio/35_SP/"
    "3538709_PIRACICABA.zip"
)

COLUMNS = [
    "DSC_LOCALIDADE",
    "NOM_TIPO_SEGLOGR",
    "NOM_TITULO_SEGLOGR",
    "NOM_SEGLOGR",
]


def download_zip(url: str = SOURCE_URL) -> bytes:
    with urlopen(url) as response:
        return response.read()


def load_cnefe(zip_bytes: bytes) -> pd.DataFrame:
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archive:
        csv_name = next(name for name in archive.namelist() if name.lower().endswith(".csv"))
        with archive.open(csv_name) as csv_file:
            df = pd.read_csv(csv_file, sep=";", dtype=str, low_memory=False)

    out = df[COLUMNS].copy()
    for col in COLUMNS:
        out[col] = out[col].fillna("").str.strip()

    out["FULL_STREET_NAME"] = (
        out[["NOM_TIPO_SEGLOGR", "NOM_TITULO_SEGLOGR", "NOM_SEGLOGR"]]
        .apply(lambda row: " ".join(part for part in row if part), axis=1)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )
    return out


def build_tables(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    street_cols = ["NOM_TIPO_SEGLOGR", "NOM_TITULO_SEGLOGR", "NOM_SEGLOGR"]
    locality_cols = ["DSC_LOCALIDADE", *street_cols]

    streets = (
        df[street_cols + ["FULL_STREET_NAME"]]
        .drop_duplicates(subset=street_cols)
        .sort_values(street_cols)
        .reset_index(drop=True)
    )

    locality_streets = (
        df[locality_cols + ["FULL_STREET_NAME"]]
        .drop_duplicates(subset=locality_cols)
        .sort_values(locality_cols)
        .reset_index(drop=True)
    )
    return streets, locality_streets


def main() -> None:
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_cnefe(download_zip())
    streets, locality_streets = build_tables(df)

    streets.to_csv(output_dir / "streets_unique.csv", index=False)
    locality_streets.to_csv(output_dir / "streets_by_locality.csv", index=False)

    print(f"Address records: {len(df):,}")
    print(f"Unique street denominations: {len(streets):,}")
    print(f"Locality-street combinations: {len(locality_streets):,}")


if __name__ == "__main__":
    main()
