// Mobile menu functionality
const mobileMenuBtn = document.querySelector('.mobile-menu');
const navLinks = document.querySelector('.nav-links');
const authButtons = document.querySelector('.auth-buttons');

mobileMenuBtn?.addEventListener('click', () => {
    navLinks?.classList.toggle('show');
    authButtons?.classList.toggle('show');
});

// Form handling
const contactForm = document.getElementById('contactForm');
const signinForm = document.getElementById('signinForm');
const signupForm = document.getElementById('signupForm');

contactForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    // Add contact form submission logic here
    alert('Message sent successfully!');
    contactForm.reset();
});

signinForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    // Add sign in logic here
    alert('Sign in successful!');
});

signupForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }

    // Add sign up logic here
    alert('Sign up successful!');
});

// Password validation
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirmPassword');

confirmPasswordInput?.addEventListener('input', () => {
    if (passwordInput.value !== confirmPasswordInput.value) {
        confirmPasswordInput.setCustomValidity('Passwords do not match');
    } else {
        confirmPasswordInput.setCustomValidity('');
    }
});