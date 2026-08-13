document.querySelectorAll("[data-copy]").forEach((copyBtn) => {
  copyBtn.addEventListener("click", async () => {
    const box = copyBtn.closest(".install-box");
    const repoUrl = box ? box.querySelector(".repo-url") : null;
    if (!repoUrl) return;
    const text = repoUrl.textContent.trim();
    const setIcon = (done) => {
      copyBtn.innerHTML = done
        ? '<i class="fa-solid fa-check" aria-hidden="true"></i>'
        : '<i class="fa-regular fa-copy" aria-hidden="true"></i>';
      copyBtn.setAttribute("aria-label", done ? "コピーしました" : "コピー");
      copyBtn.classList.toggle("is-done", done);
    };
    try {
      await navigator.clipboard.writeText(text);
      setIcon(true);
      setTimeout(() => setIcon(false), 1600);
    } catch {
      const range = document.createRange();
      range.selectNodeContents(repoUrl);
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
    }
  });
});

document.querySelectorAll("[data-changelog-more]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const list = btn.closest(".changelog");
    if (!list) return;
    list.classList.add("is-expanded");
    btn.hidden = true;
  });
});

/* Click-to-expand preview for Markdown figures */
(() => {
  const thumbs = document.querySelectorAll(".md-figure img");
  if (!thumbs.length) return;

  const dialog = document.createElement("dialog");
  dialog.className = "img-lightbox";
  dialog.setAttribute("aria-label", "画像プレビュー");
  dialog.innerHTML =
    '<img class="img-lightbox-img" alt="" />' +
    '<button type="button" class="img-lightbox-close" aria-label="閉じる">×</button>';
  document.body.appendChild(dialog);

  const full = dialog.querySelector(".img-lightbox-img");
  const closeBtn = dialog.querySelector(".img-lightbox-close");

  const open = (img) => {
    full.src = img.currentSrc || img.src;
    full.alt = img.alt || "";
    if (typeof dialog.showModal === "function") {
      dialog.showModal();
    } else {
      dialog.setAttribute("open", "");
    }
  };

  const close = () => {
    if (typeof dialog.close === "function" && dialog.open) {
      dialog.close();
    } else {
      dialog.removeAttribute("open");
    }
    full.removeAttribute("src");
    full.alt = "";
  };

  thumbs.forEach((img) => {
    img.classList.add("is-zoomable");
    img.setAttribute("tabindex", "0");
    img.setAttribute("role", "button");
    if (!img.getAttribute("aria-label")) {
      img.setAttribute("aria-label", "画像を拡大表示");
    }
    img.addEventListener("click", () => open(img));
    img.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        open(img);
      }
    });
  });

  closeBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    close();
  });

  dialog.addEventListener("click", (e) => {
    if (e.target === dialog) close();
  });

  full.addEventListener("click", (e) => e.stopPropagation());

  dialog.addEventListener("cancel", (e) => {
    e.preventDefault();
    close();
  });
})();
