#!/usr/bin/env python3
import os
import shutil

# Make.fun entrypoint for news-image-20261124: 24 November World News Infographic
# Verified Tuesday 24 November 2026 Edition: 35 stories across 6 regions - COP31 overtime, Ukraine barrage, Bahrain radar
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    
    here = os.path.dirname(os.path.abspath(__file__))
    src_png = os.path.join(here, "entry.png")
    dst_png = os.path.join(out_dir, "entry.png")
    
    shutil.copyfile(src_png, dst_png)
    file_size = os.path.getsize(dst_png)
    print(f"Delivered 24 Nov 2026 world news infographic to {dst_png} ({file_size} bytes)")

if __name__ == "__main__":
    main()
