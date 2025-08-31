const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    const mainContent = document.getElementById('mainContent');

    hamburger.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      mainContent.classList.toggle('expanded');
    });

    const slider = document.getElementById('slider');
    const slides = slider.querySelectorAll('img');
    const totalSlides = slides.length;
    
    let currentIndex = 0;
    let autoSlide = setInterval(nextSlide, 4000);
    
    // Show the current slide based on index
    function showSlide(index) {
      slider.style.transform = `translateX(-${index * 100}%)`;
    }
    
    // Go to the next slide
    function nextSlide() {
      currentIndex = (currentIndex + 1) % totalSlides;
      showSlide(currentIndex);
    }
    
    // Go to the previous slide
    function prevSlide() {
      currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
      showSlide(currentIndex);
    }
    
    // Reset auto play timer
    function resetAutoSlide() {
      clearInterval(autoSlide);
      autoSlide = setInterval(nextSlide, 500);
    }
    
    // Button Event Listeners
    document.getElementById('nextBtn').addEventListener('click', () => {
      nextSlide();
      resetAutoSlide();
    });
    
    document.getElementById('prevBtn').addEventListener('click', () => {
      prevSlide();
      resetAutoSlide();
    });
    
    // Pause on hover
    slider.addEventListener('mouseenter', () => clearInterval(autoSlide));
    slider.addEventListener('mouseleave', () => autoSlide = setInterval(nextSlide, 4000));
    function toggleMenu() {
      const menu = document.getElementById('menu');
      menu.classList.toggle('active');
    }
    function toggleMenu() {
      const menu = document.getElementById("menu");
      const content = document.querySelector(".content");
    
      menu.classList.toggle("active");
    
      if (menu.classList.contains("active")) {
        content.style.marginTop = "240px";
      } else {
        content.style.marginTop = "140px";
      }}
      const links = document.querySelectorAll('.property-list a');

    links.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent link navigation

        // Remove 'active' from all
        links.forEach(l => l.classList.remove('active'));

        // Add 'active' to the clicked link
        this.classList.add('active');
      });
    });

    

  
  // Initialize the map and set its view
  var map = L.map('map').setView([6.5244, 3.3792], 13); // Lagos coordinates

  // Add OpenStreetMap tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  // Add a marker
  L.marker([6.5244, 3.3792])
    .addTo(map)
    .bindPopup('Hello from Lagos!')
    .openPopup();
