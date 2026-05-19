---
layout: page
permalink: /research/
title: research
description:
nav: true
nav_order: 1
---

** I focus on understanding how galaxies grow, evolve, and build-up their stellar mass across cosmic time.
I use spatially-resolved observations from JWST to connect the physical processes driving star formation to the structural properties we observe. **

---

## **Size growth of star formation at high redshift**

We explore how galaxies build-up their stellar mass spatially at $z \sim 4-5$. With multi-wavelength size measurements probing tracers of different star formation timescales over a large sample of galaxies, we can explore population trends in the spatial extent of stellar populations. We use the morphological fitting tool [Forcepho](https://github.com/bd-j/forcepho) to fit rest-frame optical, UV, and $H\alpha$ (tracing decreasing timescales of star formation) sizes of >100 galaxies at $z \sim 4-5$. Our sample extends down to stellar masses $<10^7 M_\odot$, probing the regime of galaxies susceptible to bursty star formation in the high-redshift universe. This regime has important implications to star formation and galaxy assembly in the early universe, and our measured size differences across stellar populations contribute constraints to understanding the physical mechanisms driving bursty growth.

{% include figure.liquid path="assets/img/forcepho_example.png"
   caption="Example Forcepho morphological fits for a $z \sim 4-5$ galaxy.
   The rest-optical continuum morphology is used to continuum-subtract and isolate H$\alpha$ emission."
   class="img-fluid rounded" 
   width="60%" %}

---

## **Spatially-resolved star formation across cosmic time**

The structure of a galaxy encodes the physical processes driving its growth, but measuring spatially-resolved properties across large samples has historically been computationally challenging. We address this with a machine learning algorithm that performs SED fitting per-pixel (following the work in [P. Iglesias-Navarro, incl. N. Villanueva](https://www.aanda.org/articles/aa/full_html/2025/11/aa55810-25/aa55810-25.html)), which fits SED galaxy properties in fractions of a second per-pixel, and scales to entire photometric catalogs. 

From pixel-by-pixel maps of star formation properties (specifically specific star formation rate, sSFR) for a pilot sample of hundreds of massive galaxies over cosmic time, we construct radial sSFR profiles stacked across bins of stellar mass, star formation activity, and redshift. These large-scale population trends constrain the timescales and physical processes driving different regimes of galaxy growth, and which frameworks for the assembly of stellar mass dominate different types of galaxies at different epochs of cosmic time.

{% include figure.liquid path="assets/img/ssfrmap_examples.png"
   caption="Pixel-by-pixel sSFR maps for two example galaxies from our JWST sample,
   at z=0.94 (top) and z=4.86 (bottom), derived from SED fitting with BAGPIPES."
   class="img-fluid rounded" 
   width="60%" %}
