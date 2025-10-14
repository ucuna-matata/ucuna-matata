// Smooth scroll animation for scroll indicator
document.querySelector('.scroll-indicator')?.addEventListener('click', () => {
    document.querySelector('.about')?.scrollIntoView({ 
        behavior: 'smooth' 
    });
});

// Intersection Observer for scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Animate sections on scroll
document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.about-card, .team-member, .stat-card');

    sections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(50px)';
        section.style.transition = `all 0.6s ease ${index * 0.1}s`;
        observer.observe(section);
    });

    // Add parallax effect to gradient orbs
    document.addEventListener('mousemove', (e) => {
        const orbs = document.querySelectorAll('.gradient-orb');
        const mouseX = e.clientX / window.innerWidth;
        const mouseY = e.clientY / window.innerHeight;

        orbs.forEach((orb, index) => {
            const speed = (index + 1) * 20;
            const x = (mouseX - 0.5) * speed;
            const y = (mouseY - 0.5) * speed;
            
            orb.style.transform = `translate(${x}px, ${y}px)`;
        });
    });

    // Add typing effect to tagline
    const tagline = document.querySelector('.tagline');
    if (tagline) {
        const text = tagline.textContent;
        tagline.textContent = '';
        let i = 0;
        
        const typeWriter = () => {
            if (i < text.length) {
                tagline.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        };
        
        setTimeout(typeWriter, 500);
    }

    // Animated counter for stats
    animateStats();
});

// Add dynamic gradient to team name on mouse move
const teamName = document.querySelector('.team-name');
if (teamName) {
    teamName.addEventListener('mousemove', (e) => {
        const rect = teamName.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width) * 100;
        const y = ((e.clientY - rect.top) / rect.height) * 100;
        
        teamName.style.backgroundPosition = `${x}% ${y}%`;
        teamName.style.backgroundSize = '200% 200%';
    });
}

// Animated counter function
function animateStats() {
    const statNumbers = document.querySelectorAll('.stat-number');

    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.getAttribute('data-target'));
                const duration = 2000;
                const step = target / (duration / 16);
                let current = 0;

                const updateCounter = () => {
                    current += step;
                    if (current < target) {
                        entry.target.textContent = Math.floor(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        entry.target.textContent = target;
                    }
                };

                updateCounter();
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statNumbers.forEach(stat => statsObserver.observe(stat));
}

// Contact form handling with backend API
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formMessage = document.getElementById('form-message');
        const submitBtn = contactForm.querySelector('.submit-btn');
        const originalBtnText = submitBtn.textContent;

        // Get form data
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            message: document.getElementById('message').value
        };

        // Disable button and show loading
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';

        try {
            // Send to backend API
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (response.ok) {
                formMessage.className = 'form-message success';
                formMessage.textContent = result.message || 'Message sent successfully! We\'ll get back to you soon.';
                contactForm.reset();
            } else {
                throw new Error(result.error || 'Failed to send message');
            }
        } catch (error) {
            formMessage.className = 'form-message error';
            formMessage.textContent = error.message || 'Failed to send message. Please try again.';
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = originalBtnText;

            // Hide message after 5 seconds
            setTimeout(() => {
                formMessage.style.display = 'none';
            }, 5000);
        }
    });
}
