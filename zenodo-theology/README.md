# zenodo-theology

Curated, publication-ready theology articles deposited to **Zenodo** for DOI minting and citation.

**Scope:** non-designism theological work. Designism research is a separate program and is deposited into the [`scientific-designism`](https://zenodo.org/communities/scientific-designism) Zenodo community; keeping the two streams distinct protects the framing of each. Articles here are deposited at the **account level (no community attached)** by default, which still yields full DOIs and discoverability. They can be grouped into a theology/Christian community later without changing any DOI.

This folder is also the explicit "published set" — if an article has a folder here with a `RECORD.md`, it has a DOI.

## Layout

Each article is a self-contained folder:

```
zenodo-theology/
  <article-slug>/
    article.md      # single source of truth (Markdown)
    metadata.json   # Zenodo deposit metadata — see _template/metadata.json
    article.pdf     # built from article.md; this is the deposited artifact
    RECORD.md       # written back AFTER publishing: DOI, record URL, version
```

**Single-source rule:** `article.md` is canonical. The deposited `article.pdf` and any public (GitHub Pages) HTML must be *built* from it, never authored separately, so the citable record and the reading view cannot drift.

## Workflow

1. Drop the finished article as `<slug>/article.md`.
2. Fill in `<slug>/metadata.json` from `_template/metadata.json`.
3. Build `article.pdf` from `article.md`.
4. **Draft** deposit (review before publishing):
   ```bash
   python /media/jdlongmire/Macro-Drive-1TB/GitHub_Repos/ologos-repos/zenodo-publisher/zenodo_publisher.py \
     "<slug>/article.pdf" --metadata "<slug>/metadata.json" \
     --env /media/jdlongmire/Macro-Drive-1TB/GitHub_Repos/ologos-repos/zenodo-publisher/.env
   ```
   Review the draft on Zenodo.
5. **Publish** (only when approved) by adding `--publish` to the command above.
6. Record the minted DOI + record URL in `<slug>/RECORD.md`.

> Token: the publisher uses `ZENODO_ACCESS_TOKEN` (production, publish-capable). The credential lives in the central store; it is not committed here.

## Conventions

- **Slug:** lowercase, hyphenated, stable, descriptive (it becomes the folder name and should not change after publish).
- **License:** default `cc-by-4.0` unless a piece sets otherwise in its `metadata.json`.
- **Corrections:** publish an erratum as a *new version* of the existing Zenodo record (the concept DOI preserves the lineage); do not delete the prior version.
