// Radiance Residency PWA Service Worker
// Minimal offline-first cache for core assets
const CACHE_VERSION = "radiance-v1-2026-05-19";
const CORE_ASSETS = [
    "/",
    "/about",
    "/rooms",
    "/amenities",
    "/safety",
    "/contact",
    "/reviews",
    "/student-testimonials",
    "/style.min.css",
    "/script.min.js",
    "/favicon.svg",
    "/manifest.json"
];

self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open(CACHE_VERSION).then((cache) => cache.addAll(CORE_ASSETS).catch(() => {}))
    );
    self.skipWaiting();
});

self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((keys) =>
            Promise.all(
                keys.filter((k) => k !== CACHE_VERSION).map((k) => caches.delete(k))
            )
        )
    );
    self.clients.claim();
});

self.addEventListener("fetch", (event) => {
    const req = event.request;
    if (req.method !== "GET") return;
    // Network-first for HTML, cache-first for assets
    const isHTML = req.headers.get("accept") && req.headers.get("accept").includes("text/html");
    if (isHTML) {
        event.respondWith(
            fetch(req)
                .then((res) => {
                    const copy = res.clone();
                    caches.open(CACHE_VERSION).then((c) => c.put(req, copy));
                    return res;
                })
                .catch(() => caches.match(req).then((r) => r || caches.match("/")))
        );
    } else {
        event.respondWith(
            caches.match(req).then((cached) =>
                cached ||
                fetch(req).then((res) => {
                    const copy = res.clone();
                    if (res.ok) caches.open(CACHE_VERSION).then((c) => c.put(req, copy));
                    return res;
                }).catch(() => cached)
            )
        );
    }
});
