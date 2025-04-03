document.addEventListener("DOMContentLoaded", function() {
    new Swiper(".mySwiper", {
        loop: true,
        autoplay: { delay: 5000 }, // Auto-slide every 5 seconds
        navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
        pagination: { el: ".swiper-pagination", clickable: true },
    });
});
