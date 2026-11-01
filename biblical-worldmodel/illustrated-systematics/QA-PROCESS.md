# Illustrated Systematics: Visual QA Process

**Status:** Adopted 2026-11-01 (JD directive, after a missed defect on BWM-IS-05 panel 1). Applies to every plate in this program before ingestion, and to any plate already ingested when this process is invoked retroactively.

## Why this process exists

A full-plate read at delivery size is not proofreading. On BWM-IS-05, a full-size read passed a plate whose generator had systematically rendered "Genesis" as "Genessis" in five of seven Genesis references, and a caption word ("else") whose letterforms were too tightly kerned to read cleanly. Both were found only by magnified, element-by-element inspection. The process below makes that inspection mandatory and recorded.

## The element checklist

Every plate is decomposed into text elements, and every element is verified. The checklist for a standard ten-panel plate:

- Header: main title, subtitle, framing box, book stack (each spine), volume marker.
- Each panel 1 to 9: panel title, quotation bubble text, quotation reference, caption (every line).
- Closing panel: title, each checklist line, closing quotation and its reference.
- Footer: oddXian.com pointer and volume ID.

## Verification standard

1. Each element is read from a magnified crop of that panel (minimum 2x, references and other short lines at 4x or more), never from the full-plate view alone.
2. The crop reading is compared letter by letter against the PANEL-SCRIPT.md text for that element. Proper names and Scripture references are spelled out in the check (G-e-n-e-s-i-s), not skimmed.
3. Pass/fail is judged at reading scale: lettering that is technically present but does not read cleanly at delivery size is a defect. (The "else" rule, from BWM-IS-05 panel 1.)
4. Known generator habits are standing checklist items: doubled letters in repeated words (Genesis rendered "Genessis"), stray letters at line breaks, garbled suffixes on repeated small-type lines, and dropped words in long captions. Each new systematic habit found is added to this list in the QA log.
5. A second pass re-reads every crop after any repair, including the elements adjacent to a repair (a patch must not damage its neighbors, its panel border, or the lines above and below it).

## Repairs

- Repairs are programmatic and minimal: only the defective element is covered and re-lettered, matched in height to the element's own ink box (located by pixel measurement, not estimated), with the fill sampled from the element's own background.
- Every repair is disclosed in the volume's TRANSCRIPTION.md production note and in QA-LOG.md, with the original defect named. A repaired plate is a repaired derivative of the raw generation and is never described as a clean generation.
- If a repair fails verification twice, stop patching that element and escalate: regenerate the plate or take the defect to JD.

## Records

- The completed element checklist for each plate is recorded in QA-LOG.md (elements checked, defects found, repairs made, verification result) before or with ingestion.
- No plate is ingested without a completed checklist. Statuses stay honest: a plate with an open checklist is a draft, whatever it looks like at full size.

Human-Curated, AI-Enabled (HCAE)
