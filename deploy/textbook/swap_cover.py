"""Replace page 1 of a volume with a footer-free cover (same page object, so outline and links stay valid).
Usage: python3 swap_cover.py volume.pdf cover.pdf   (volume.pdf is rewritten in place)"""
import sys, pikepdf
vol, cov = sys.argv[1], sys.argv[2]
with pikepdf.open(vol, allow_overwriting_input=True) as v, pikepdf.open(cov) as c:
    src = v.copy_foreign(c.pages[0].obj)
    page = v.pages[0].obj
    page.Contents = src.Contents
    page.Resources = src.Resources
    v.save(vol)
