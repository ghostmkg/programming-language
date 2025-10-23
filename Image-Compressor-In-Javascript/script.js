const fileInput = document.getElementById('file');
    const qualityEl = document.getElementById('quality');
    const maxWEl = document.getElementById('maxW');
    const maxHEl = document.getElementById('maxH');
    const compressBtn = document.getElementById('compress');
    const downloadBtn = document.getElementById('download');
    const resetBtn = document.getElementById('reset');
    const previewImg = document.getElementById('preview');
    const canvas = document.getElementById('canvas');
    const origMeta = document.getElementById('origMeta');
    const outMeta = document.getElementById('outMeta');

    let originalFile = null;
    let outBlob = null;

    function fmtBytes(b){
      if(!b && b!==0) return '—';
      const u=['B','KB','MB','GB']; let i=0;
      while(b>=1024 && i<u.length-1){b/=1024;i++}
      return b.toFixed(b<10&&i>0?2:0)+' '+u[i];
    }

    function loadImage(file){
      return new Promise((resolve,reject)=>{
        const url = URL.createObjectURL(file);
        const img = new Image();
        img.onload = () => { URL.revokeObjectURL(url); resolve(img); };
        img.onerror = reject;
        img.src = url;
      });
    }

    async function compress(){
      if(!originalFile){ alert('Please choose an image first.'); return; }
      const img = await loadImage(originalFile);
      const maxW = parseInt(maxWEl.value||1600,10);
      const maxH = parseInt(maxHEl.value||1600,10);
      let { width:w, height:h } = img;

      // Constrain to bounding box while keeping aspect ratio
      const ratio = Math.min(maxW / w, maxH / h, 1);
      const cw = Math.round(w * ratio), ch = Math.round(h * ratio);

      canvas.width = cw; canvas.height = ch;
      const ctx = canvas.getContext('2d');
      ctx.clearRect(0,0,cw,ch);
      ctx.drawImage(img, 0, 0, cw, ch);

      const q = parseFloat(qualityEl.value||0.7);
      // Prefer WebP when supported; fallback to JPEG
      const type = canvas.toDataURL('image/webp', q).startsWith('data:image/webp') ? 'image/webp' : 'image/jpeg';

      outBlob = await new Promise(res=>canvas.toBlob(res, type, q));
      canvas.classList.remove('muted');

      outMeta.textContent = `Size: ${fmtBytes(outBlob.size)} • Type: ${type.replace('image/','').toUpperCase()} • ${cw}×${ch}`;
      downloadBtn.disabled = false;
    }

    function reset(){
      originalFile = null; outBlob = null;
      previewImg.src = ''; canvas.width = canvas.height = 0;
      origMeta.textContent = 'No file.'; outMeta.textContent = '—';
      canvas.classList.add('muted'); downloadBtn.disabled = true;
      fileInput.value = ''; qualityEl.value = 0.7; maxWEl.value = 1600; maxHEl.value = 1600;
    }

    fileInput.addEventListener('change', async (e)=>{
      const f = e.target.files[0];
      if(!f) return;
      if(!f.type.startsWith('image/')){ alert('Please select an image file.'); reset(); return; }
      originalFile = f;
      previewImg.src = URL.createObjectURL(f);
      origMeta.textContent = `Size: ${fmtBytes(f.size)} • Type: ${f.type || 'image'} `;
      outMeta.textContent = '—'; canvas.classList.add('muted'); downloadBtn.disabled = true;
    });

    compressBtn.addEventListener('click', compress);

    downloadBtn.addEventListener('click', ()=>{
      if(!outBlob) return;
      const a = document.createElement('a');
      const name = (originalFile?.name || 'image').replace(/\.(\w+)$/,'');
      const ext = (outBlob.type.includes('webp') ? 'webp' : 'jpg');
      a.href = URL.createObjectURL(outBlob);
      a.download = `${name}.compressed.${ext}`;
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(()=>URL.revokeObjectURL(a.href), 1000);
    });

    resetBtn.addEventListener('click', reset);