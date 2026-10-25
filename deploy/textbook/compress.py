"""Pack a Chromium PDF into object streams (tagged PDFs shrink by about 60%). Usage: compress.py in.pdf out.pdf"""
import sys, pikepdf
with pikepdf.open(sys.argv[1]) as p:
    p.docinfo["/Title"] = sys.argv[3] if len(sys.argv) > 3 else p.docinfo.get("/Title", "")
    p.save(sys.argv[2], compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate, recompress_flate=True)
