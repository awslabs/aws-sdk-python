/**
 * Keep the active client highlighted and its nav section expanded across all
 * of its API reference pages (/clients/<name>/...).
 *
 * Zensical already auto-expands "Available Clients" and highlights the active
 * client on that client's own index page, but not on its nested symbol pages
 * (operations/, enums/, structures/, unions/, errors/). This restores that
 * orientation so the sidebar stays anchored while browsing a client's API.
 */
function highlightActiveClient() {
  // Match ".../clients/<name>/..." and capture the client segment.
  var match = location.pathname.match(/\/clients\/([^/]+)\//);
  if (!match) return;

  // Reconstruct the client's index path, e.g. "/clients/polly/", preserving
  // any site base path (the docs are served under a sub-path in production).
  var clientRoot =
    location.pathname.slice(0, match.index) + "/clients/" + match[1] + "/";

  // Scope to the primary sidebar only. The secondary "On this page" TOC uses
  // the same link classes, and its same-page anchors would otherwise all match
  // clientRoot on a client's index page and get highlighted.
  var sidebar = document.querySelector(".md-nav--primary");
  if (!sidebar) return;

  // The client appears exactly once in the sidebar, so find it and stop —
  // avoids scanning the rest of the nav (hundreds of links once many clients
  // exist).
  var links = sidebar.querySelectorAll(".md-nav__link[href]");
  var link = null;
  for (var i = 0; i < links.length; i++) {
    if (links[i].pathname === clientRoot && !links[i].hash) {
      link = links[i];
      break;
    }
  }
  if (!link) return;

  // Highlight the client whose pages we're currently viewing.
  link.classList.add("md-nav__link--active");

  // Expand every collapsible ancestor (incl. "Available Clients") so the
  // highlighted link is visible. Expansion is driven by the toggle checkbox.
  var item = link.closest(".md-nav__item--nested");
  while (item) {
    var toggle = item.querySelector(":scope > .md-nav__toggle");
    if (toggle) toggle.checked = true;
    var parent = item.parentElement;
    item = parent && parent.closest(".md-nav__item--nested");
  }
}

// Re-run on every instant-navigation page load; fall back to a one-time run if
// the document$ observable isn't available.
if (typeof document$ !== "undefined" && document$.subscribe) {
  document$.subscribe(highlightActiveClient);
} else {
  highlightActiveClient();
}
