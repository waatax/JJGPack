import Alpine from 'alpinejs'
import './style.css'

window.Alpine = Alpine
Alpine.start()

// ===== SCROLL REVEAL =====
const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
                if (entry.isIntersecting) {
                        entry.target.classList.add('visible')
                        // Stagger children if they have [data-reveal-child]
                        const children = entry.target.querySelectorAll('[data-reveal-child]')
                        children.forEach((child, i) => {
                                child.style.transitionDelay = `${i * 0.1}s`
                                child.classList.add('visible')
                        })
                }
        })
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' })

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el))

// ===== COUNTER ANIMATION =====
function animateCounter(el) {
        const target = parseInt(el.getAttribute('data-count'))
        const suffix = el.getAttribute('data-suffix') || ''
        const prefix = el.getAttribute('data-prefix') || ''
        const duration = 2000
        const start = performance.now()

        function update(now) {
                const elapsed = now - start
                const progress = Math.min(elapsed / duration, 1)
                // Ease out cubic
                const eased = 1 - Math.pow(1 - progress, 3)
                const current = Math.round(target * eased)
                el.textContent = prefix + current + suffix
                if (progress < 1) requestAnimationFrame(update)
        }
        requestAnimationFrame(update)
}

const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.dataset.animated) {
                        entry.target.dataset.animated = 'true'
                        animateCounter(entry.target)
                }
        })
}, { threshold: 0.5 })

document.querySelectorAll('[data-count]').forEach(el => counterObserver.observe(el))

// ===== SMOOTH NAV SHADOW =====
const header = document.querySelector('header')
if (header) {
        let lastScroll = 0
        window.addEventListener('scroll', () => {
                const scrollY = window.scrollY
                if (scrollY > 20) {
                        header.classList.add('shadow-premium')
                } else {
                        header.classList.remove('shadow-premium')
                }
                lastScroll = scrollY
        }, { passive: true })
}
