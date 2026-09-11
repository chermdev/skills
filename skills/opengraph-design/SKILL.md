---
name: opengraph-design
description: Design or improve Open Graph and social preview images that match a website's visual quality and brand, then integrate and verify their metadata. Use for share-card composition, typography, imagery, cropping, or localized image variants; general search ranking and indexing audits are outside this skill's scope.
---

# Open Graph Design

Treat the card as a small piece of the website's art direction. Its job is to make the brand and page's value recognizable before someone opens the link.

## 1. Ground the design in the existing site

Inspect the current card, actual hero, logo variants, typography, palette, and available image assets. Follow imports as well as public asset directories: the useful hero image may live in a source-assets folder. Read the page's visible copy and identify its audience and offer.

Preserve the supplied logo's geometry and identity. A request to improve a social card authorizes redesigning its composition, not inventing a new logo or turning the mark into a sculpture. Start with an existing hero image, product view, or relevant project asset; generate supporting artwork only when existing material cannot serve the brief.

When the user supplies inspiration, inspect the actual images. Extract a compositional principle, such as strong type beside a cropped product view, rather than copying another brand's identity. If the gallery cannot be viewed, disclose that limitation instead of claiming to have inspected it.

Finish this step with a concrete subject, a usable asset, and a short statement of the proposed hierarchy. Infer routine choices from the brief and continue without a mandatory approval round.

## 2. Compose for a thumbnail

Use a compact hierarchy: recognizable brand, one short headline, one supporting thought, and one main visual when useful. A centered wordmark alone rarely communicates enough about the page; a full webpage screenshot usually communicates too much at an unreadable size.

- **Type:** Choose deliberate line breaks and comfortable leading. Tighten display tracking without making letters collide. Use the site's fonts when they suit the composition; verify that the export renderer actually loads the intended face and weight. Keep the headline legible when the card is roughly 400 pixels wide.
- **Copy:** The headline expresses one idea; the subtext explains the offering or benefit. Use the page's real language. Let the metadata description carry details that would overload the image.
- **Color:** Preserve the brand's base palette. For a monochrome brand, a photograph's sky, a product detail, or one emphasized phrase can provide color when the brief allows it. Color is optional; avoid inventing an accent merely to make the card look modern.
- **Space:** Give text its own quiet area. Align the logo, headline, and subtext optically. Keep essential content away from edges and leave enough room for localized copy.
- **Image:** Choose a focal point before cropping. Show enough context to connect the card to the site, with sufficient contrast behind any overlaid text. Deliberately crop imagery rather than logos or essential copy.

For an Apple-inspired brief, translate the request into restraint: clear hierarchy, precise sans-serif typography, generous space, restrained material treatment, and a single strong image. This is a visual interpretation, not a requirement to use Apple logos, devices, fonts, or platform UI.

### Optional composition: an image extending beyond the frame

Useful when the site has a strong hero image and the user wants a minimal composition with depth. Place the text on a solid field and the image in a large rounded rectangle on the opposite side. Let that rectangle continue beyond the card's right or bottom edge, retaining a visible rounded corner that makes the crop feel intentional.

For example, on a 1200 × 630 canvas, start text around 64 pixels from the left and place an 820 × 570 image container around `(620, 134)` with a 36-pixel radius. These are exploration values, not a fixed template. Adjust the crop so the important subject survives the visible portion. A subtle edge or shadow can separate the image; add one only if separation needs it.

Other briefs may be better served by a full-bleed photograph, a product detail, or typography alone. Choose from the content rather than repeating this composition everywhere.

## 3. Build an editable, reproducible asset

Use the project's existing rendering pipeline when practical. SVG or HTML/CSS templates work well for precise text, original vector logos, and image placement. Use image-generation tools for artwork that benefits from synthesis, while keeping typography and approved branding deterministic where possible. Follow the active tool rules for image editing.

Retain an editable source and the final raster output inside the project. A common starting canvas is 1200 × 630; verify destination-specific requirements when needed. Export a widely supported PNG or JPEG and check the actual dimensions and file size. Avoid relying on an SVG as the crawler-facing image.

For SVG rendering, embed required images or resolve them explicitly in the generator; escape inserted text as XML. For HTML rendering, wait for fonts and images before capture. Use portable font assets or document the rendering dependency so a different machine does not silently substitute a font.

When the site has localized pages, use matching image text and alt text if the card contains language-specific copy. Reuse the composition, then inspect each language for overflow and awkward wrapping. Keep the regeneration command and source locations discoverable in the project's existing documentation.

## 4. Integrate at the correct URL

Inspect the rendered HTML before assuming Open Graph is absent. Distinguish a poor card from a missing image, an old cached preview, or a domain that still serves a hosting placeholder.

If integration is part of the request, verify `og:image`, its dimensions and alt text, and the corresponding large-image Twitter card. Keep structured image references consistent when present. Use absolute public image URLs that return the image without authentication. Add `og:image:secure_url` only for an HTTPS resource.

Separate image availability from canonical URL policy. Static HTML fixes absolute URLs at build time; reading a framework's request-URL helper during prerendering does not make the published file adapt to each incoming host. Use the host's deployment environment or an explicit site-origin setting for static builds. Per-request host adaptation requires server rendering or response rewriting. A protected deployment URL may be inaccessible to social crawlers. Preserve the intended production canonical unless changing that policy is within scope.

## 5. Verify the exported result

Inspect the actual raster at full size and at a representative thumbnail size. Check that the brand and headline read immediately, subtext remains useful, the image's focal point survives the crop, and the visible corner or edge treatment looks intentional. Compare against the website and the user's reference, then fix concrete visual weaknesses.

After building, inspect the generated HTML for every affected locale and confirm that each referenced image exists with the advertised dimensions and format. Check public retrieval when a deployment is available; distinguish local validation from deployed verification. Run checks appropriate to modified code, without adding a broad test suite for a visual asset change.

Deliver the finished preview inline, name the editable source, and report any remaining deployment or cache limitation. A generated concept alone is not completion when the user requested integration into the site.

## References

- Use the [OpenGraph inspiration gallery](https://www.opengraph.xyz/inspiration) for visual research when references would help.
- Consult the [Open Graph protocol](https://ogp.me/) when implementing or checking property semantics.
