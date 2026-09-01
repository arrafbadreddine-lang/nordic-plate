/**
 * Svenska Recept - Sök- och Filtreringsmotor
 * Hanterar sökning i realtid, filter-chips och URL-parametrar.
 */

document.addEventListener('DOMContentLoaded', () => {
  initSokOchFilter();
});

function initSokOchFilter() {
  const searchInput = document.getElementById('recipe-search-input');
  const filterChips = document.querySelectorAll('.filter-chip');
  const quickChips = document.querySelectorAll('.quick-chip');
  const recipeCards = document.querySelectorAll('.recipe-card');
  const resultsCounter = document.getElementById('search-results-count');
  const noResultsEl = document.getElementById('no-results-msg');

  let currentCategory = 'all';
  let currentSearchQuery = '';

  // Snabb-chips (klickbara etiketter)
  quickChips.forEach(chip => {
    chip.addEventListener('click', (e) => {
      e.preventDefault();
      const term = (chip.dataset.search || chip.textContent.trim()).toLowerCase();
      
      // Kontrollera om termen motsvarar ett fördefinierat filter
      if (['under-30', 'vegetariskt', 'husmanskost', 'fika', 'smorgasbord'].includes(term)) {
        valjKategori(term);
        if (searchInput) searchInput.value = '';
        currentSearchQuery = '';
      } else {
        if (searchInput) {
          searchInput.value = chip.textContent.trim();
          currentSearchQuery = term;
        } else {
          window.location.href = `recept.html?q=${encodeURIComponent(chip.textContent.trim())}`;
          return;
        }
      }
      appliceraFilter();
    });
  });

  // Filterknappar (chips)
  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const cat = chip.dataset.category || 'all';
      valjKategori(cat);
      appliceraFilter();
    });
  });

  function valjKategori(cat) {
    currentCategory = cat;
    filterChips.forEach(c => {
      if (c.dataset.category === cat) {
        c.classList.add('active');
      } else {
        c.classList.remove('active');
      }
    });
  }

  // Sökfält input
  if (searchInput) {
    // Förhindra oavsiktlig form-submit vid tryck på Enter
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
      }
    });

    searchInput.addEventListener('input', (e) => {
      currentSearchQuery = e.target.value.toLowerCase().trim();
      appliceraFilter();
    });

    // Tolka URL-parametrar (t.ex. recept.html?q=under-30 eller recept.html?q=kladdkaka)
    const urlParams = new URLSearchParams(window.location.search);
    const qParam = urlParams.get('q');
    const catParam = urlParams.get('category');

    if (catParam) {
      valjKategori(catParam.toLowerCase());
    } else if (qParam) {
      const lowerQ = qParam.toLowerCase().trim();
      if (['under-30', 'vegetariskt', 'husmanskost', 'fika', 'smorgasbord'].includes(lowerQ)) {
        valjKategori(lowerQ);
      } else {
        searchInput.value = qParam;
        currentSearchQuery = lowerQ;
      }
    }
  }

  function appliceraFilter() {
    if (!recipeCards.length) return;
    let synliga = 0;

    recipeCards.forEach(card => {
      const cardCategory = (card.dataset.category || '').toLowerCase();
      const cardDiet = (card.dataset.diet || '').toLowerCase();
      const cardTime = parseInt(card.dataset.time || '999', 10);
      const cardTitle = (card.querySelector('.recipe-card-title')?.textContent || '').toLowerCase();
      const cardDesc = (card.querySelector('.recipe-card-desc')?.textContent || '').toLowerCase();
      const cardIngredients = (card.dataset.ingredients || '').toLowerCase();

      // Kategorimatchning
      let categoryMatch = false;
      if (currentCategory === 'all' || currentCategory === 'alla') {
        categoryMatch = true;
      } else if (currentCategory === 'under-30') {
        categoryMatch = cardTime <= 30;
      } else if (currentCategory === 'vegetariskt') {
        categoryMatch = cardDiet.includes('vegetariskt') || cardDiet.includes('vegan');
      } else {
        categoryMatch = (cardCategory === currentCategory);
      }

      // Sökordsmatchning
      const searchMatch = !currentSearchQuery ||
        cardTitle.includes(currentSearchQuery) ||
        cardDesc.includes(currentSearchQuery) ||
        cardIngredients.includes(currentSearchQuery);

      if (categoryMatch && searchMatch) {
        card.style.display = 'flex';
        synliga++;
      } else {
        card.style.display = 'none';
      }
    });

    if (resultsCounter) {
      resultsCounter.textContent = `Visar ${synliga} recept`;
    }

    if (noResultsEl) {
      noResultsEl.style.display = (synliga === 0) ? 'block' : 'none';
    }
  }

  appliceraFilter();
}
