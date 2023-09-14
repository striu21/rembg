import fall

if not fall.is_installed("rembg"):
    fall.run_pip("install rembg==2.0.38 --no-deps", "rembg")

for dep in ['onnxruntime', 'pymatting', 'pooch']:
    if not fall.is_installed(dep):
        fall.run_pip(f"install {dep}", f"{dep} for REMBG extension")
