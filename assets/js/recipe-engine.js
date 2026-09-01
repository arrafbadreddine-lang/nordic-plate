/**
 * Svenska Recept - Interactive Recipe Engine
 * Features:
 * 1. Dynamic Portion Scaler with fractional display
 * 2. Interactive Ingredient & Step Checklists (persisted in localStorage)
 * 3. Heart / Favorite Bookmark system with Live Header Counter (persisted in localStorage)
 * 4. Digital Kitchen Timer with Sound/Visual alert
 * 5. Horizontal Carousel Smooth Arrow Navigation
 * 6. Social Share & One-Click Copy Link with Toast notification
 * 7. Interactive Review & Rating System with Star Picker (persisted in localStorage)
 * 8. "Hoppa till recept" smooth scroll
 */

document.addEventListener('DOMContentLoaded', () => {
  initFavoritesSystem();
  initPortionsScaler();
  initChecklists();
  initTimers();
  initCarousels();
  initMobileMenu();
  initSocialShare();
  initCommentsSystem();
  initJumpToRecipe();
});

/* ==========================================================================
   1. FAVORITES / HEART BOOKMARK SYSTEM
   ========================================================================== */

function getSavedFavorites() {
  try {
    return JSON.parse(localStorage.getItem('svenska_recept_favoriter')) || [];
  } catch (e) {
    return [];
  }
}

function saveFavorites(favs) {
  try {
    localStorage.setItem('svenska_recept_favoriter', JSON.stringify(favs));
    updateFavoritesBadgeCount();
  } catch (e) {}
}

function updateFavoritesBadgeCount() {
  const favs = getSavedFavorites();
  const badges = document.querySelectorAll('.favorites-badge-count');
  badges.forEach(b => {
    b.textContent = favs.length;
  });
}

function initFavoritesSystem() {
  updateFavoritesBadgeCount();
  const favs = getSavedFavorites();

  document.querySelectorAll('.card-heart-btn').forEach(btn => {
    const slug = btn.getAttribute('data-slug');
    if (favs.includes(slug)) {
      btn.classList.add('is-saved');
      btn.innerHTML = `<svg class="svg-icon" viewBox="0 0 24 24" fill="#C05621" stroke="#C05621" stroke-width="1.55"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>`;
    }

    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      let currentFavs = getSavedFavorites();
      if (currentFavs.includes(slug)) {
        currentFavs = currentFavs.filter(s => s !== slug);
        btn.classList.remove('is-saved');
        btn.innerHTML = `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>`;
        showToast("Recept borttaget från favoriter");
      } else {
        currentFavs.push(slug);
        btn.classList.add('is-saved');
        btn.innerHTML = `<svg class="svg-icon" viewBox="0 0 24 24" fill="#C05621" stroke="#C05621" stroke-width="1.55"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>`;
        showToast("Sparat i dina favoriter! ❤️");
      }
      saveFavorites(currentFavs);
    });
  });

  const pageHeartBtn = document.getElementById('save-recipe-btn');
  if (pageHeartBtn) {
    const slug = pageHeartBtn.getAttribute('data-slug');
    if (favs.includes(slug)) {
      pageHeartBtn.classList.add('is-saved');
      pageHeartBtn.textContent = '❤️ Sparad i favoriter';
    }
    pageHeartBtn.addEventListener('click', () => {
      let currentFavs = getSavedFavorites();
      if (currentFavs.includes(slug)) {
        currentFavs = currentFavs.filter(s => s !== slug);
        pageHeartBtn.classList.remove('is-saved');
        pageHeartBtn.textContent = 'Spara recept';
        showToast("Recept borttaget från favoriter");
      } else {
        currentFavs.push(slug);
        pageHeartBtn.classList.add('is-saved');
        pageHeartBtn.textContent = '❤️ Sparad i favoriter';
        showToast("Sparat i dina favoriter! ❤️");
      }
      saveFavorites(currentFavs);
    });
  }
}

/* ==========================================================================
   2. DYNAMIC PORTIONS SCALER
   ========================================================================== */

function initPortionsScaler() {
  const portionsDisplay = document.querySelector('.portions-display');
  const decreaseBtn = document.querySelector('.portion-btn.decrease');
  const increaseBtn = document.querySelector('.portion-btn.increase');
  const ingredients = document.querySelectorAll('.ingrediens-mangd');

  if (!portionsDisplay || !decreaseBtn || !increaseBtn) return;

  const basePortions = parseFloat(portionsDisplay.getAttribute('data-base-portioner')) || 4;
  const unitText = portionsDisplay.getAttribute('data-enhet-text') || 'portioner';
  let currentPortions = basePortions;

  function formatQuantity(val) {
    if (val === 0 || isNaN(val)) return '';
    const rounded = Math.round(val * 10) / 10;
    if (Math.abs(rounded - 0.25) < 0.05) return '¼';
    if (Math.abs(rounded - 0.5) < 0.05) return '½';
    if (Math.abs(rounded - 0.75) < 0.05) return '¾';
    if (Math.abs(rounded - 1.5) < 0.05) return '1 ½';
    if (Math.abs(rounded - 2.5) < 0.05) return '2 ½';
    if (rounded % 1 === 0) return rounded.toString();
    return rounded.toFixed(1).replace('.0', '');
  }

  function updateQuantities(newPortions) {
    if (newPortions < 1) newPortions = 1;
    if (newPortions > 40) newPortions = 40;
    currentPortions = newPortions;

    portionsDisplay.textContent = `${currentPortions} ${unitText}`;

    const factor = currentPortions / basePortions;
    ingredients.forEach(el => {
      const baseVal = parseFloat(el.getAttribute('data-base-mangd'));
      if (!isNaN(baseVal) && baseVal > 0) {
        const scaled = baseVal * factor;
        el.textContent = formatQuantity(scaled);
      }
    });
  }

  decreaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    updateQuantities(currentPortions - (currentPortions > 4 ? 2 : 1));
  });

  increaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    updateQuantities(currentPortions + (currentPortions >= 4 ? 2 : 1));
  });
}

/* ==========================================================================
   3. CHECKLISTS (INGREDIENSER & STEG)
   ========================================================================== */

function initChecklists() {
  const pageId = window.location.pathname.split('/').pop().replace('.html', '') || 'recipe';

  // Ingredient items
  document.querySelectorAll('.ingredient-item').forEach((item, idx) => {
    const cb = item.querySelector('.ingredient-checkbox');
    const storageKey = `ing_${pageId}_${idx}`;
    if (localStorage.getItem(storageKey) === '1') {
      if (cb) cb.checked = true;
      item.classList.add('checked');
    }

    item.addEventListener('click', (e) => {
      if (e.target !== cb) {
        if (cb) cb.checked = !cb.checked;
      }
      if (cb && cb.checked) {
        item.classList.add('checked');
        localStorage.setItem(storageKey, '1');
      } else {
        item.classList.remove('checked');
        localStorage.removeItem(storageKey);
      }
    });
  });

  // Instruction steps
  document.querySelectorAll('.instruction-step').forEach((step, idx) => {
    const storageKey = `step_${pageId}_${idx}`;
    if (localStorage.getItem(storageKey) === '1') {
      step.classList.add('completed');
    }

    step.addEventListener('click', (e) => {
      if (e.target.closest('.step-timer-knapp')) return;
      step.classList.toggle('completed');
      if (step.classList.contains('completed')) {
        localStorage.setItem(storageKey, '1');
      } else {
        localStorage.removeItem(storageKey);
      }
    });
  });
}

/* ==========================================================================
   4. DIGITAL KITCHEN TIMER
   ========================================================================== */

let activeTimerInterval = null;

function initTimers() {
  document.querySelectorAll('.step-timer-knapp').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const minutes = parseInt(btn.getAttribute('data-minuter'), 10) || 10;
      startKitchenTimer(minutes);
    });
  });
}

function startKitchenTimer(minutes) {
  if (activeTimerInterval) clearInterval(activeTimerInterval);

  let existingModal = document.querySelector('.timer-modal');
  if (existingModal) existingModal.remove();

  let totalSeconds = minutes * 60;

  const modal = document.createElement('div');
  modal.className = 'timer-modal';
  modal.innerHTML = `
    <div style="background: #18283E; color: #FFFFFF; padding: 1.25rem 1.5rem; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); display: flex; align-items: center; gap: 1.25rem; font-family: var(--font-body);">
      <div>
        <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #94A3B8; font-weight: 700;">Kökstimer</div>
        <div id="timer-display" style="font-size: 1.8rem; font-weight: 800; font-variant-numeric: tabular-nums; color: #F59E0B;">${formatTimerTime(totalSeconds)}</div>
      </div>
      <button id="close-timer-btn" style="background: rgba(255,255,255,0.15); border: none; color: #FFFFFF; padding: 0.5rem 0.85rem; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 0.85rem;">Stäng</button>
    </div>
  `;
  document.body.appendChild(modal);

  const display = document.getElementById('timer-display');
  const closeBtn = document.getElementById('close-timer-btn');

  closeBtn.addEventListener('click', () => {
    clearInterval(activeTimerInterval);
    modal.remove();
  });

  activeTimerInterval = setInterval(() => {
    totalSeconds--;
    if (totalSeconds <= 0) {
      clearInterval(activeTimerInterval);
      display.textContent = "KLART! 🔔";
      display.style.color = "#4ADE80";
      showToast("Tiden är ute! Maten är klar! 🔔");
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        osc.connect(audioCtx.destination);
        osc.frequency.value = 880;
        osc.start();
        setTimeout(() => osc.stop(), 500);
      } catch (err) {}
    } else {
      display.textContent = formatTimerTime(totalSeconds);
    }
  }, 1000);
}

function formatTimerTime(seconds) {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

/* ==========================================================================
   5. SMOOTH CAROUSEL ARROWS
   ========================================================================== */

function initCarousels() {
  document.querySelectorAll('.carousel-section').forEach(section => {
    const track = section.querySelector('.recipe-carousel');
    const prevBtn = section.querySelector('.carousel-prev');
    const nextBtn = section.querySelector('.carousel-next');

    if (!track || !prevBtn || !nextBtn) return;

    prevBtn.addEventListener('click', () => {
      track.scrollBy({ left: -320, behavior: 'smooth' });
    });

    nextBtn.addEventListener('click', () => {
      track.scrollBy({ left: 320, behavior: 'smooth' });
    });
  });
}

/* ==========================================================================
   6. SOCIAL SHARING & COPY LINK
   ========================================================================== */

function initSocialShare() {
  const currentUrl = encodeURIComponent(window.location.href);
  const title = encodeURIComponent(document.title);

  document.querySelectorAll('.share-btn-facebook').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.open(`https://www.facebook.com/sharer/sharer.php?u=${currentUrl}`, '_blank', 'width=600,height=400');
    });
  });

  document.querySelectorAll('.share-btn-pinterest').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const heroImg = document.querySelector('.recipe-hero-fullwidth img');
      const media = heroImg ? encodeURIComponent(heroImg.src) : '';
      window.open(`https://pinterest.com/pin/create/button/?url=${currentUrl}&media=${media}&description=${title}`, '_blank', 'width=750,height=500');
    });
  });

  document.querySelectorAll('.share-btn-whatsapp').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.open(`https://api.whatsapp.com/send?text=${title}%20${currentUrl}`, '_blank');
    });
  });

  document.querySelectorAll('.share-btn-copy').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (navigator.clipboard) {
        navigator.clipboard.writeText(window.location.href).then(() => {
          showToast("Länk kopierad till urklipp! 📋");
        }).catch(() => {
          fallbackCopy();
        });
      } else {
        fallbackCopy();
      }
    });
  });

  function fallbackCopy() {
    const tempInput = document.createElement('input');
    tempInput.value = window.location.href;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    showToast("Länk kopierad till urklipp! 📋");
  }
}

function showToast(message) {
  let toast = document.querySelector('.toast-notification');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast-notification';
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 2500);
}

/* ==========================================================================
   7. INTERACTIVE COMMENTS & REVIEW SYSTEM
   ========================================================================== */

function initCommentsSystem() {
  const commentForm = document.getElementById('recipe-comment-form');
  const commentsList = document.getElementById('comments-list-container');
  const starButtons = document.querySelectorAll('.star-picker-btn');
  const ratingInput = document.getElementById('selected-rating-val');

  if (!commentForm || !commentsList) return;

  const pageSlug = window.location.pathname.split('/').pop().replace('.html', '') || 'general';

  // Star Rating Picker
  let selectedRating = 5;
  starButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      selectedRating = parseInt(btn.getAttribute('data-rating'), 10);
      if (ratingInput) ratingInput.value = selectedRating;
      updateStarPickerVisuals(selectedRating);
    });
  });

  function updateStarPickerVisuals(rating) {
    starButtons.forEach(b => {
      const r = parseInt(b.getAttribute('data-rating'), 10);
      if (r <= rating) {
        b.style.color = '#F59E0B';
      } else {
        b.style.color = '#CBD5E1';
      }
    });
  }

  // Load saved local comments
  try {
    const savedLocalComments = JSON.parse(localStorage.getItem(`comments_${pageSlug}`)) || [];
    savedLocalComments.forEach(c => {
      appendCommentToDOM(c, false);
    });
  } catch (e) {}

  // Handle new comment submission
  commentForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const nameInput = document.getElementById('comment-author-name');
    const textInput = document.getElementById('comment-text-content');

    const name = nameInput ? nameInput.value.trim() : 'Matälskare';
    const text = textInput ? textInput.value.trim() : '';

    if (!text) return;

    const newComment = {
      name: name,
      date: 'Just nu',
      rating: selectedRating,
      comment: text,
      verified: true
    };

    appendCommentToDOM(newComment, true);

    // Save to localStorage
    try {
      const current = JSON.parse(localStorage.getItem(`comments_${pageSlug}`)) || [];
      current.unshift(newComment);
      localStorage.setItem(`comments_${pageSlug}`, JSON.stringify(current));
    } catch (err) {}

    // Reset form
    if (textInput) textInput.value = '';
    showToast("Tack för ditt betyg och din kommentar! ⭐");
  });

  function appendCommentToDOM(c, prepend = false) {
    const card = document.createElement('div');
    card.className = 'comment-card';
    const starsHtml = '★'.repeat(c.rating) + '☆'.repeat(5 - c.rating);

    card.innerHTML = `
      <div class="comment-meta">
        <span class="comment-author">
          ${c.name}
          ${c.verified ? '<span class="comment-verified-badge">✓ Verifierad provlagare</span>' : ''}
        </span>
        <span>${c.date}</span>
      </div>
      <div style="color: #F59E0B; font-size: 1rem; margin-bottom: 0.4rem; letter-spacing: 0.1em;">${starsHtml}</div>
      <p class="comment-text">${c.comment}</p>
    `;

    if (prepend && commentsList.firstChild) {
      commentsList.insertBefore(card, commentsList.firstChild);
    } else {
      commentsList.appendChild(card);
    }
  }
}

/* ==========================================================================
   8. "HOPPA TILL RECEPT" SMOOTH SCROLL
   ========================================================================== */

function initJumpToRecipe() {
  const jumpBtn = document.querySelector('.btn-jump-to-recipe');
  if (jumpBtn) {
    jumpBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector('.recipe-body-grid');
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }
}

/* ==========================================================================
   9. MOBILE MENU
   ========================================================================== */

function initMobileMenu() {
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const siteNav = document.querySelector('.site-nav');
  if (menuBtn && siteNav) {
    menuBtn.addEventListener('click', () => {
      siteNav.classList.toggle('open');
    });
  }
}
