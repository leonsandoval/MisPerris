var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
        "/",
        '/static/core/css/style.css',
        '/static/core/css/materialize.min.css',
        '/static/core/img/crowfunding.jpg',
        '/static/core/img/googleplus.png',
        '/static/core/img/logo.png',
        '/static/core/img/mail.png',
        '/static/core/img/rescate.jpg',
        '/static/core/img/social-inst.png',
        '/static/core/img/socialfacebook.png',
        '/static/core/js/materialize.min.js',
        '/static/core/js/script.js',
        'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});