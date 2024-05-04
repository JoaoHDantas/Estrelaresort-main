document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector(".carousel");
    const prevButton = document.querySelector(".prev");
    const nextButton = document.querySelector(".next");
    const slides = document.querySelectorAll(".slide");

    let currentIndex = 0;

    nextButton.addEventListener("click", () => {
        if (currentIndex < slides.length - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        updateCarousel();
    });

    prevButton.addEventListener("click", () => {
        if (currentIndex > 0) {
            currentIndex--;
        } else {
            currentIndex = slides.length - 1;
        }
        updateCarousel();
    });

    function updateCarousel() {
        const slideWidth = slides[0].clientWidth;
        carousel.style.transform = `translateX(${-slideWidth * currentIndex}px)`;
    }
});