// Document ready function
document.addEventListener('DOMContentLoaded', function () {
    // Initialize animations
    initAnimations();

    // Initialize smooth scrolling
    initSmoothScroll();

    // Initialize department card hover effects
    initDepartmentCards();

    // Initialize contact form
    initContactForm();

    // Initialize sticky header
    initStickyHeader();

    // Initialize mobile menu
    initMobileMenu();

    // Initialize countdown timer
    initCountdownTimer();

    // Initialize image gallery
    initImageGallery();
});

// Function to initialize animations
function initAnimations() {
    const animatedElements = document.querySelectorAll('.highlight-card, .department-card, .timeline-item, .sponsor-placeholder');

    // Create intersection observer for fade-in animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    // Observe each element
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

// Function to initialize smooth scrolling
function initSmoothScroll() {
    const navLinks = document.querySelectorAll('nav a, .cta-button, .footer-links a');

    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            const href = this.getAttribute('href');

            // Check if the link is an anchor
            if (href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}

// Function to initialize department cards
function initDepartmentCards() {
    const departmentCards = document.querySelectorAll('.department-card');

    departmentCards.forEach(card => {
        card.addEventListener('click', function () {
            const link = this.querySelector('.department-link');
            if (link) {
                window.location.href = link.getAttribute('href');
            }
        });
    });
}

// Function to initialize contact form
function initContactForm() {
    const contactForm = document.querySelector('.contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(this);
            const formDataObj = {};
            formData.forEach((value, key) => {
                formDataObj[key] = value;
            });

            // Simulate form submission with a loading state
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            submitButton.textContent = 'Sending...';
            submitButton.disabled = true;

            // Simulate an API call with a timeout
            setTimeout(() => {
                // Reset the form
                contactForm.reset();

                // Show success message
                showNotification('Message sent successfully! We will get back to you soon.', 'success');

                // Reset button
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            }, 1500);
        });
    }
}

// Function to initialize sticky header
function initStickyHeader() {
    const header = document.querySelector('header');
    const hero = document.querySelector('.hero');
    let lastScrollPosition = 0;

    if (!header || !hero) return;

    window.addEventListener('scroll', () => {
        const currentScrollPosition = window.pageYOffset;

        // Add/remove sticky class based on scroll position
        if (currentScrollPosition > hero.offsetHeight) {
            header.classList.add('header-sticky');
        } else {
            header.classList.remove('header-sticky');
        }

        // Hide/show header based on scroll direction
        if (currentScrollPosition > lastScrollPosition && currentScrollPosition > header.offsetHeight) {
            header.style.transform = 'translateY(-100%)';
        } else {
            header.style.transform = 'translateY(0)';
        }

        lastScrollPosition = currentScrollPosition;
    });
}

// Function to show notifications
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;

    // Add notification to DOM
    document.body.appendChild(notification);

    // Add active class to trigger animation
    setTimeout(() => {
        notification.classList.add('active');
    }, 10);

    // Remove notification after 5 seconds
    setTimeout(() => {
        notification.classList.remove('active');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 5000);
}

// Function to handle countdown timer
function initCountdownTimer() {
    const daysEl = document.getElementById('days');
    const hoursEl = document.getElementById('hours');
    const minutesEl = document.getElementById('minutes');
    const secondsEl = document.getElementById('seconds');

    if (daysEl && hoursEl && minutesEl && secondsEl) {
        // Set event date (March 13, 2026)
        const eventDate = new Date('2026-03-13T09:00:00').getTime();

        const update = () => {
            const now = new Date().getTime();
            const distance = eventDate - now;

            if (distance < 0) {
                const countdownSection = document.querySelector('.countdown');
                if (countdownSection) {
                    countdownSection.innerHTML = '<div class="container"><h3>🎉 Event Has Started!</h3></div>';
                }
                return;
            }

            // Calculate days, hours, minutes, seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Update HTML
            daysEl.textContent = days;
            hoursEl.textContent = hours;
            minutesEl.textContent = minutes;
            secondsEl.textContent = seconds;
        };

        // Update every second
        setInterval(update, 1000);
        update(); // Run immediately
    }
}

// Function to handle image gallery
function initImageGallery() {
    const galleryItems = document.querySelectorAll('.gallery-item');

    if (galleryItems.length > 0) {
        galleryItems.forEach(item => {
            item.addEventListener('click', function () {
                const img = this.querySelector('img');
                if (!img) return;

                const imgSrc = img.getAttribute('src');
                const imgAlt = img.getAttribute('alt');

                // Create modal
                const modal = document.createElement('div');
                modal.className = 'gallery-modal';
                modal.innerHTML = `
                    <div class="gallery-modal-content">
                        <span class="gallery-modal-close">&times;</span>
                        <img src="${imgSrc}" alt="${imgAlt}">
                        <p>${imgAlt}</p>
                    </div>
                `;

                // Add modal to DOM
                document.body.appendChild(modal);

                // Prevent scrolling when modal is open
                document.body.style.overflow = 'hidden';

                // Close modal when clicking on close button
                modal.querySelector('.gallery-modal-close').addEventListener('click', () => {
                    document.body.removeChild(modal);
                    document.body.style.overflow = '';
                });

                // Close modal when clicking outside the image
                modal.addEventListener('click', (e) => {
                    if (e.target === modal) {
                        document.body.removeChild(modal);
                        document.body.style.overflow = '';
                    }
                });
            });
        });
    }
}

// Function to initialize mobile menu
function initMobileMenu() {
    const toggle = document.getElementById('mobile-nav-toggle');
    const nav = document.getElementById('main-nav');
    const navLinks = document.querySelectorAll('nav a');

    if (toggle && nav) {
        // Toggle menu on click
        toggle.addEventListener('click', (e) => {
            e.stopPropagation();
            nav.classList.toggle('active');
            const icon = toggle.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-bars');
                icon.classList.toggle('fa-times');
            }
        });

        // Close menu when clicking a link
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                nav.classList.remove('active');
                const icon = toggle.querySelector('i');
                if (icon) {
                    icon.classList.add('fa-bars');
                    icon.classList.remove('fa-times');
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!nav.contains(e.target) && !toggle.contains(e.target)) {
                nav.classList.remove('active');
                const icon = toggle.querySelector('i');
                if (icon) {
                    icon.classList.add('fa-bars');
                    icon.classList.remove('fa-times');
                }
            }
        });
    }
}
