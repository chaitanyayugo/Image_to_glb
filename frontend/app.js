const imageInput = document.getElementById('imageInput');
const preview = document.getElementById('preview');
const generateBtn = document.getElementById('generateBtn');
const downloadBtn = document.getElementById('downloadBtn');
const loader = document.getElementById('loader');
const viewer = document.getElementById('viewer');

let glbBlob = null;

// Preview uploaded image
imageInput.addEventListener('change', (e) => {
    const file = e.target.files;
    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.hidden = false;
        generateBtn.disabled = false;
    }
});

// Generate GLB
generateBtn.addEventListener('click', async () => {
    const file = imageInput.files;
    if (!file) return;

    loader.hidden = false;
    generateBtn.disabled = true;
    downloadBtn.hidden = true;

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:8000/generate', {
            method: 'POST',
            body: formData
        });

        glbBlob = await response.blob();
        const url = URL.createObjectURL(glbBlob);

        downloadBtn.hidden = false;
        loadGLBViewer(url);
    } catch (err) {
        alert('Error generating model. Is the backend running?');
    } finally {
        loader.hidden = true;
        generateBtn.disabled = false;
    }
});

// Download GLB
downloadBtn.addEventListener('click', () => {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(glbBlob);
    a.download = 'output.glb';
    a.click();
});

// Three.js GLB Viewer
function loadGLBViewer(url) {
    viewer.innerHTML = '';

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x1a1a2e);

    const camera = new THREE.PerspectiveCamera(75, viewer.clientWidth / viewer.clientHeight, 0.1, 1000);
    camera.position.set(0, 0, 2);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(viewer.clientWidth, viewer.clientHeight);
    viewer.appendChild(renderer.domElement);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;

    const light = new THREE.AmbientLight(0xffffff, 1.5);
    scene.add(light);

    const loader3D = new THREE.GLTFLoader();
    loader3D.load(url, (gltf) => {
        scene.add(gltf.scene);
    });

    function animate() {
        requestAnimationFrame(animate);
        controls.update();
        renderer.render(scene, camera);
    }
    animate();
}

