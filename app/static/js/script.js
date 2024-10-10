// script2.js
document.querySelector('.search-bar button').addEventListener('click', function () {
    const query = document.querySelector('.search-bar input').value;
    alert('Searching for: ' + query);

});
// Show the first image initially
// JavaScript to handle image carousel transitions

let currentImageIndex = 0;
const images = document.querySelectorAll('.carousel-image');
const totalImages = images.length;

// Function to show the image
function showImage(index) {
    images.forEach((img, i) => {
        if (i === index) {
            img.classList.add('active');
        } else {
            img.classList.remove('active');
        }
    });
}

// Function to move to the next image
function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % totalImages;
    showImage(currentImageIndex);
}

// Show the first image initially
showImage(currentImageIndex);

// Set interval to change images automatically every 3 seconds
setInterval(nextImage, 3000);


    // Get the carousel indicators container
    const indicatorsContainer = document.getElementById('carousel-indicators');

    // Get the number of carousel items
    const carouselItems = document.querySelectorAll('.carousel-item');
    const itemCount = carouselItems.length;

    // Create the indicators dynamically
    for (let i = 0; i < itemCount; i++) {
    const indicator = document.createElement('button');
    indicator.type = 'button';
    indicator.dataset.bsTarget = '#demo';
    indicator.dataset.bsSlideTo = i.toString();
    indicator.classList.add('carousel-indicator');
    if (i === 0) {
    indicator.classList.add('active');
}
    indicatorsContainer.appendChild(indicator);
}

    // Start the automatic slide
    let currentIndex = 0;
    const interval = setInterval(() => {
    currentIndex++;
    if (currentIndex >= itemCount) {
    currentIndex = 0;
}
    const carousel = document.getElementById('demo');
    carousel.querySelector('.carousel-indicator.active').classList.remove('active');
    carousel.querySelectorAll('.carousel-indicator')[currentIndex].classList.add('active');
    carousel.querySelector('.carousel-inner .carousel-item.active').classList.remove('active');
    carousel.querySelectorAll('.carousel-inner .carousel-item')[currentIndex].classList.add('active');
}, 3000);


    document.addEventListener("DOMContentLoaded", function() {
    const avatar = document.getElementById('avatar');
    const dropdownMenu = document.getElementById('dropdown-menu');
    const themeToggle = document.getElementById('theme-toggle');
    let isDarkMode = false;

    // Toggle dropdown visibility when clicking on the avatar
    avatar.addEventListener('click', function() {
        dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
    });

    // Switch between dark and light modes
    themeToggle.addEventListener('click', function() {
        isDarkMode = !isDarkMode;
        document.body.classList.toggle('dark-mode', isDarkMode);
        document.body.classList.toggle('light-mode', !isDarkMode);

        // Update the button text based on the current theme
        themeToggle.textContent = isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode';
    });

    // Hide the dropdown if clicking outside of it
    document.addEventListener('click', function(event) {
        if (!avatar.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });
});
document.addEventListener("DOMContentLoaded", function() {
    const avatar = document.getElementById('avatar');
    const dropdownMenu = document.getElementById('dropdown-menu');
    const themeToggle = document.getElementById('theme-toggle');
    let isDarkMode = false;

    // Toggle dropdown visibility when clicking on the avatar
    avatar.addEventListener('click', function() {
        dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
    });

    // Switch between dark and light modes
    themeToggle.addEventListener('click', function() {
        isDarkMode = !isDarkMode;
        document.body.classList.toggle('dark-mode', isDarkMode);
        document.body.classList.toggle('light-mode', !isDarkMode);

        // Update the button text based on the current theme
        themeToggle.textContent = isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode';
    });

    // Hide the dropdown if clicking outside of it
    document.addEventListener('click', function(event) {
        if (!avatar.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });
});

// Add functionality for Add to Cart and Favorite buttons as needed
