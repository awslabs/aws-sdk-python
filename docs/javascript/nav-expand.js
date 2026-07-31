/**
 * Keep API Reference nav expanded on /clients/ pages and highlight active client.
 * Uses Material for MkDocs document$ observable for instant navigation compatibility.
 */
function expandClientsNav() {
  if (!location.pathname.includes("/clients/")) return;
  document.querySelectorAll(".md-nav__item--nested").forEach(function (item) {
    var link = item.querySelector(":scope > .md-nav__link");
    if (link && link.textContent.trim().includes("Available Clients")) {
      // Expand "All Available Clients" drop down
      var toggle = item.querySelector(":scope > .md-nav__toggle");
      if (toggle) toggle.checked = true;
      item.setAttribute("data-md-state", "expanded");
      
      // Highlight active client
      var navItems = item.querySelectorAll(".md-nav__item .md-nav__link");
      navItems.forEach(function (navLink) {
        if (navLink.href && location.pathname.includes(navLink.pathname)) {
          navLink.classList.add("md-nav__link--active");
        }
      });
    }
  });
}

// Subscribe to Material's document$ observable for instant navigation support
document$.subscribe(expandClientsNav);
// Also run on initial page load
expandClientsNav();
