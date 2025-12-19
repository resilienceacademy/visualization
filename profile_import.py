"""
Detailed import profiling for leafmap.maplibregl

Run this in your Jupyter notebook cell to profile imports:

%run profile_import.py

Or copy-paste the code directly into a cell.
"""
import time
import sys

def profile_detailed():
    """Profile imports with detailed breakdown."""

    print("="*60)
    print("IMPORT PROFILING FOR leafmap.maplibregl")
    print("="*60)
    print()

    results = []

    # 1. NumPy
    print("Importing numpy...", end=" ", flush=True)
    start = time.perf_counter()
    import numpy
    elapsed = time.perf_counter() - start
    results.append(("numpy", elapsed))
    print(f"{elapsed:.3f}s")

    # 2. IPython/ipywidgets (for interactive widgets)
    print("Importing ipywidgets...", end=" ", flush=True)
    start = time.perf_counter()
    try:
        import ipywidgets
        elapsed = time.perf_counter() - start
        results.append(("ipywidgets", elapsed))
        print(f"{elapsed:.3f}s")
    except ImportError:
        print("not installed")

    # 3. Pandas (often used by geospatial libs)
    print("Importing pandas...", end=" ", flush=True)
    start = time.perf_counter()
    try:
        import pandas
        elapsed = time.perf_counter() - start
        results.append(("pandas", elapsed))
        print(f"{elapsed:.3f}s")
    except ImportError:
        print("not installed")

    # 4. GeoPandas
    print("Importing geopandas...", end=" ", flush=True)
    start = time.perf_counter()
    try:
        import geopandas
        elapsed = time.perf_counter() - start
        results.append(("geopandas", elapsed))
        print(f"{elapsed:.3f}s")
    except ImportError:
        print("not installed")

    # 5. Rasterio
    print("Importing rasterio...", end=" ", flush=True)
    start = time.perf_counter()
    try:
        import rasterio
        elapsed = time.perf_counter() - start
        results.append(("rasterio", elapsed))
        print(f"{elapsed:.3f}s")
    except ImportError:
        print("not installed")

    # 6. Base leafmap
    print("Importing leafmap (base)...", end=" ", flush=True)
    start = time.perf_counter()
    try:
        import leafmap
        elapsed = time.perf_counter() - start
        results.append(("leafmap (base)", elapsed))
        print(f"{elapsed:.3f}s")
    except ImportError as e:
        print(f"error: {e}")

    # 7. leafmap.maplibregl
    print("Importing leafmap.maplibregl...", end=" ", flush=True)
    start = time.perf_counter()
    try:
        import leafmap.maplibregl
        elapsed = time.perf_counter() - start
        results.append(("leafmap.maplibregl", elapsed))
        print(f"{elapsed:.3f}s")
    except ImportError as e:
        print(f"error: {e}")

    # Summary
    print()
    print("="*60)
    print("SUMMARY (sorted by time)")
    print("="*60)

    results.sort(key=lambda x: x[1], reverse=True)
    total = sum(t for _, t in results)

    for name, duration in results:
        pct = (duration / total) * 100 if total > 0 else 0
        bar = "█" * int(pct / 2)
        print(f"{name:25} {duration:6.3f}s ({pct:5.1f}%) {bar}")

    print("-"*60)
    print(f"{'TOTAL':25} {total:6.3f}s")
    print("="*60)

    # Recommendations
    print()
    print("RECOMMENDATIONS:")
    print("-"*60)

    slowest = results[0] if results else None
    if slowest:
        name, duration = slowest
        if duration > 2:
            print(f"⚠️  '{name}' is the slowest ({duration:.1f}s)")

            if "geopandas" in name:
                print("   → GeoPandas loads GDAL/GEOS - unavoidable overhead")
            elif "leafmap" in name:
                print("   → leafmap loads many geospatial dependencies")
            elif "rasterio" in name:
                print("   → Rasterio loads GDAL bindings")

    print()
    print("💡 Tips to speed up notebook startup:")
    print("   1. Run imports once at the start of your session")
    print("   2. Use `%load_ext autoreload` to avoid re-importing")
    print("   3. Consider `import leafmap` (folium backend) if you")
    print("      don't need MapLibre GL features")
    print("   4. Pre-warm your kernel before presentations")

if __name__ == "__main__":
    profile_detailed()
