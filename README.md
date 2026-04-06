# 🖼️ Image to 3D GLB Generator

A web-based tool that converts 2D images into 3D `.glb` files using AI-powered depth estimation.

> MCA Final Year Project — [Your Name] | [Your College]

## 🚀 Features
- Upload any image and get a 3D `.glb` file
- Real-time 3D preview in browser (Three.js)
- Powered by Depth Anything V2 (free & accurate)
- Download generated `.glb` file

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript, Three.js |
| Backend | FastAPI (Python) |
| AI Model | Depth Anything V2 |
| 3D Processing | Open3D, Trimesh |

## ⚙️ Installation

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
