const MODEL_URL = "https://justadudewhohacks.github.io/face-api.js/models/";

async function loadModels() {
  await faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL);
  await faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL);
  await faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL);
}

async function startCamera(video) {
  const stream = await navigator.mediaDevices.getUserMedia({ video: true });
  video.srcObject = stream;
  await video.play();
}

async function getDescriptor(video) {
  if (typeof faceapi === "undefined") {
    console.error("face-api not loaded");
    return null;
  }

  const detection = await faceapi
    .detectSingleFace(video, new faceapi.TinyFaceDetectorOptions())
    .withFaceLandmarks()
    .withFaceDescriptor();

  return detection ? detection.descriptor : null;
}