# Project Charter

## Mission

Build the open scientific infrastructure for AI-guided molecular sensing, beginning with condition-standardized fluorescent probe response.

## Initial benchmark

**FluoroGenome-ProbeResponse** evaluates whether models can predict and prioritize sensor response under realistic experimental conditions.

## Atomic object

The core object is not a molecule. It is an experiment:

- scientific question
- hypothesis
- sensor
- analyte
- interferents
- protocol
- measurement
- evidence
- next experiment

## What this project is not

- Not a generic fluorophore property predictor.
- Not a ChatGPT wrapper for chemistry.
- Not a claim of experimentally validated performance before data exist.
- Not a replacement for wet-lab judgment.

## What makes it defensible

The benchmark focuses on probe response, selectivity, matrix effects, raw spectra, uncertainty, and active learning. These are typically missing or under-standardized in fluorescence ML datasets.
