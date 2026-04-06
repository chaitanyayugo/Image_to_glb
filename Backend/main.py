from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from depth_model import get_depth_map
from mesh_generator import generate_glb
import shutil, uuid, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    # Save uploaded image
    uid = str(uuid.uuid4())
    img_path = f"temp/{uid}.png"
    os.makedirs("temp", exist_ok=True)

    with open(img_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Generate depth map
    depth_map = get_depth_map(img_path)

    # Generate .glb
    glb_path = f"temp/{uid}.glb"
    generate_glb(img_path, depth_map, glb_path)

    return FileResponse(glb_path, filename="output.glb")
