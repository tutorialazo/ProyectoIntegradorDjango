"use strict";

$(document).ready(function () {
  var slideWidth = $('.slide').width(); // Ancho de cada slide

  var totalSlides = $('.slide').length; // Número total de slides

  var currentIndex = 0; // Índice del slide actual

  function moveToSlide(index) {
    if (index < 0 || index >= totalSlides) return; // Verifica límites

    var offset = -index * slideWidth; // Calcula el desplazamiento

    $('.slider-container').css('transform', 'translateX(' + offset + 'px)');
    currentIndex = index;
  } // Cambio automático cada 3 segundos


  setInterval(function () {
    moveToSlide(currentIndex + 1);
  }, 3000);
}); // script.js

$(document).ready(function () {
  var currentIndex = 0;
  var slides = $('.slide');
  var dots = $('.dot');

  function showSlide(index) {
    slides.removeClass('active');
    dots.removeClass('active');
    slides.eq(index).addClass('active');
    dots.eq(index).addClass('active');
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    showSlide(currentIndex);
  }

  $('.next').on('click', nextSlide);
  $('.prev').on('click', prevSlide);
  dots.on('click', function () {
    var index = $(this).index();
    showSlide(index);
  });
  setInterval(nextSlide, 3000); // Cambio automático cada 3 segundos
}); // JavaScript para hacer que el carrusel se desplace automáticamente

document.addEventListener('DOMContentLoaded', function () {
  var carousel = document.querySelector('.image-carousel');
  var images = document.querySelectorAll('.carousel-image');
  var index = 0;
  var totalImages = images.length;
  var interval = 2000; // Tiempo en milisegundos entre desplazamientos

  function moveCarousel() {
    index++;

    if (index >= totalImages) {
      index = 0;
    }

    var offset = -index * 210; // 210 es el ancho de la imagen + margen (200 + 10)

    carousel.style.transform = "translateX(".concat(offset, "px)");
  }

  setInterval(moveCarousel, interval);
}); // JavaScript para hacer que el carrusel se desplace automáticamente

document.addEventListener('DOMContentLoaded', function () {
  var carousel = document.querySelector('.image-carousel');
  var isPaused = false;
  carousel.addEventListener('mouseover', function () {
    return isPaused = true;
  });
  carousel.addEventListener('mouseout', function () {
    return isPaused = false;
  });

  function scrollCarousel() {
    if (!isPaused) {
      var firstImage = carousel.querySelector('.carousel-image:first-child');
      carousel.appendChild(firstImage.cloneNode(true));
      firstImage.remove();
    }
  }

  setInterval(scrollCarousel, 3000); // Tiempo en milisegundos entre desplazamientos
});
//# sourceMappingURL=slider.dev.js.map
