import sus

if not sus.is_installed("rembg"):
    sus.run_pip("install rembg==2.0.38 --no-deps", "rembg")

for dep in ['onnxruntime', 'pymatting', 'pooch']:
    if not sus.is_installed(dep):
        sus.run_pip(f"install {dep}", f"{dep} for REMBG extension")
