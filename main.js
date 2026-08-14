import Alpine from 'alpinejs'
import './style.css'

window.Alpine = Alpine
Alpine.start()

// ============================================================
// SCROLL PROGRESS BAR
// ============================================================
const progressBar = document.createElement('div')
progressBar.className = 'scroll-progress-bar'
progressBar.style.width = '0%'
document.body.prepend(progressBar)

function updateProgress() {
	const scrollTop = window.scrollY
	const docHeight = document.documentElement.scrollHeight - window.innerHeight
	const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0
	progressBar.style.width = `${Math.min(progress, 100)}%`
}

// ============================================================
// SCROLL REVEAL (Enhanced with multiple directions)
// ============================================================
const revealObserver = new IntersectionObserver((entries) => {
	entries.forEach(entry => {
		if (entry.isIntersecting) {
			entry.target.classList.add('visible')
			const children = entry.target.querySelectorAll('[data-reveal-child]')
			children.forEach((child, i) => {
				child.style.transitionDelay = `${i * 0.1}s`
				child.classList.add('visible')
			})
		}
	})
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' })

document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale').forEach(el => revealObserver.observe(el))

// ============================================================
// COUNTER ANIMATION (Enhanced with formatting)
// ============================================================
function animateCounter(el) {
	const target = parseInt(el.getAttribute('data-count'))
	const suffix = el.getAttribute('data-suffix') || ''
	const prefix = el.getAttribute('data-prefix') || ''
	const useCommas = el.getAttribute('data-commas') === 'true'
	const duration = 2200
	const start = performance.now()

	function formatNumber(num) {
		if (useCommas) return num.toLocaleString()
		return num.toString()
	}

	function update(now) {
		const elapsed = now - start
		const progress = Math.min(elapsed / duration, 1)
		// Ease out quart for smoother deceleration
		const eased = 1 - Math.pow(1 - progress, 4)
		const current = Math.round(target * eased)
		el.textContent = prefix + formatNumber(current) + suffix
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

// ============================================================
// SMART STICKY HEADER (Auto-hide on scroll down, show on up)
// ============================================================
const header = document.querySelector('header')
if (header) {
	let lastScroll = 0
	let headerHidden = false

	window.addEventListener('scroll', () => {
		const scrollY = window.scrollY

		// Add shadow after scrolling
		if (scrollY > 20) {
			header.classList.add('shadow-premium')
		} else {
			header.classList.remove('shadow-premium')
		}

		// Auto-hide/show behavior (only on long pages after hero)
		if (scrollY > 400) {
			if (scrollY > lastScroll && !headerHidden && scrollY - lastScroll > 10) {
				header.style.transform = 'translateY(-100%)'
				header.style.transition = 'transform 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94)'
				headerHidden = true
			} else if (scrollY < lastScroll && headerHidden) {
				header.style.transform = 'translateY(0)'
				headerHidden = false
			}
		} else {
			header.style.transform = 'translateY(0)'
			headerHidden = false
		}

		lastScroll = scrollY
	}, { passive: true })
}

// ============================================================
// BACK TO TOP BUTTON
// ============================================================
const backToTopBtn = document.querySelector('.back-to-top')
if (backToTopBtn) {
	window.addEventListener('scroll', () => {
		if (window.scrollY > 600) {
			backToTopBtn.classList.add('visible')
		} else {
			backToTopBtn.classList.remove('visible')
		}
	}, { passive: true })

	backToTopBtn.addEventListener('click', () => {
		window.scrollTo({ top: 0, behavior: 'smooth' })
	})
}

// ============================================================
// 3D TILT EFFECT ON CARDS
// ============================================================
document.querySelectorAll('.card-3d').forEach(card => {
	card.addEventListener('mousemove', (e) => {
		const rect = card.getBoundingClientRect()
		const x = e.clientX - rect.left
		const y = e.clientY - rect.top
		const centerX = rect.width / 2
		const centerY = rect.height / 2
		const rotateX = ((y - centerY) / centerY) * -5
		const rotateY = ((x - centerX) / centerX) * 5

		card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`
	})

	card.addEventListener('mouseleave', () => {
		card.style.transform = ''
	})
})

// ============================================================
// PARALLAX SCROLL ELEMENTS
// ============================================================
function updateParallax() {
	const scrollY = window.scrollY
	document.querySelectorAll('[data-parallax]').forEach(el => {
		const speed = parseFloat(el.getAttribute('data-parallax')) || 0.3
		const rect = el.getBoundingClientRect()
		if (rect.top < window.innerHeight && rect.bottom > 0) {
			const offset = (scrollY - el.offsetTop + window.innerHeight) * speed
			el.style.transform = `translateY(${offset}px)`
		}
	})
}

// ============================================================
// TEXT SPLIT ANIMATION (Character reveal on scroll)
// ============================================================
function setupTextReveal() {
	document.querySelectorAll('[data-text-reveal]').forEach(el => {
		if (el.dataset.textRevealSetup) return
		el.dataset.textRevealSetup = 'true'
		const text = el.textContent
		el.textContent = ''
		el.style.visibility = 'visible'
		const words = text.trim().split(/\s+/)
		words.forEach((word, i) => {
			const span = document.createElement('span')
			span.textContent = word + ' '
			span.style.opacity = '0'
			span.style.transform = 'translateY(20px)'
			span.style.display = 'inline-block'
			span.style.transition = `all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) ${i * 0.05}s`
			el.appendChild(span)
		})

		const observer = new IntersectionObserver((entries) => {
			entries.forEach(entry => {
				if (entry.isIntersecting) {
					el.querySelectorAll('span').forEach(span => {
						span.style.opacity = '1'
						span.style.transform = 'translateY(0)'
					})
					observer.unobserve(el)
				}
			})
		}, { threshold: 0.3 })
		observer.observe(el)
	})
}

// ============================================================
// TYPING ANIMATION
// ============================================================
function setupTyping() {
	document.querySelectorAll('[data-typing]').forEach(el => {
		if (el.dataset.typingSetup) return
		el.dataset.typingSetup = 'true'
		const phrases = el.getAttribute('data-typing').split('|')
		let phraseIndex = 0
		let charIndex = 0
		let isDeleting = false
		let typeSpeed = 60

		function type() {
			const current = phrases[phraseIndex]
			if (isDeleting) {
				el.textContent = current.substring(0, charIndex - 1)
				charIndex--
				typeSpeed = 30
			} else {
				el.textContent = current.substring(0, charIndex + 1)
				charIndex++
				typeSpeed = 60
			}

			if (!isDeleting && charIndex === current.length) {
				typeSpeed = 2500
				isDeleting = true
			} else if (isDeleting && charIndex === 0) {
				isDeleting = false
				phraseIndex = (phraseIndex + 1) % phrases.length
				typeSpeed = 400
			}

			setTimeout(type, typeSpeed)
		}

		const observer = new IntersectionObserver((entries) => {
			if (entries[0].isIntersecting) {
				type()
				observer.unobserve(el)
			}
		})
		observer.observe(el)
	})
}

// ============================================================
// LAZY IMAGE LOADING WITH BLUR-UP
// ============================================================
function setupLazyImages() {
	document.querySelectorAll('img[data-src]').forEach(img => {
		img.style.filter = 'blur(10px)'
		img.style.transition = 'filter 0.5s ease'

		const observer = new IntersectionObserver((entries) => {
			entries.forEach(entry => {
				if (entry.isIntersecting) {
					const realSrc = img.getAttribute('data-src')
					img.src = realSrc
					img.onload = () => {
						img.style.filter = 'blur(0)'
					}
					observer.unobserve(img)
				}
			})
		}, { rootMargin: '200px' })
		observer.observe(img)
	})
}

// ============================================================
// SMOOTH ANCHOR SCROLL WITH OFFSET
// ============================================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
	anchor.addEventListener('click', (e) => {
		const targetId = anchor.getAttribute('href')
		if (targetId === '#') return
		const target = document.querySelector(targetId)
		if (target) {
			e.preventDefault()
			const headerHeight = header ? header.offsetHeight : 0
			const targetPos = target.getBoundingClientRect().top + window.scrollY - headerHeight - 20
			window.scrollTo({ top: targetPos, behavior: 'smooth' })
		}
	})
})

// ============================================================
// MAGNETIC BUTTON EFFECT
// ============================================================
document.querySelectorAll('.btn-glow, .floating-cta-btn').forEach(btn => {
	btn.addEventListener('mousemove', (e) => {
		const rect = btn.getBoundingClientRect()
		const x = e.clientX - rect.left - rect.width / 2
		const y = e.clientY - rect.top - rect.height / 2
		btn.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`
	})

	btn.addEventListener('mouseleave', () => {
		btn.style.transform = ''
	})
})

// ============================================================
// UNIFIED SCROLL HANDLER (Performance optimized)
// ============================================================
let ticking = false
window.addEventListener('scroll', () => {
	if (!ticking) {
		requestAnimationFrame(() => {
			updateProgress()
			updateParallax()
			ticking = false
		})
		ticking = true
	}
}, { passive: true })

// ============================================================
// INIT ON DOM READY
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
	setupTextReveal()
	setupTyping()
	setupLazyImages()
	updateProgress()
})

// Also run on window load for dynamically loaded content
window.addEventListener('load', () => {
	setupTextReveal()
	setupTyping()
	setupLazyImages()
})
