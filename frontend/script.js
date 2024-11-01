function showFileName() {
    const input = document.getElementById('file-upload');
    const fileName = input.files[0]?.name || "envie um vídeo";
    document.getElementById('file-name').textContent = fileName;
}