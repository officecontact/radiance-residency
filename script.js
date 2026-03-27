/* ========================================
   Radiance Residency - Main JavaScript
   Production-Ready | Vanilla JS | No Dependencies
   ======================================== */

document.addEventListener('DOMContentLoaded', function () {

    /* ===========================================
       1. LANGUAGE TOGGLE (EN / HI)
       Single button #langToggle that swaps between languages
       =========================================== */
    var langToggle = document.getElementById('langToggle');
    var savedLang = localStorage.getItem('lang') || 'en';

    function setLanguage(lang) {
        // Update all translatable elements
        var elements = document.querySelectorAll('[data-en][data-hi]');
        elements.forEach(function (el) {
            var val = el.getAttribute('data-' + lang);
            // Use innerHTML if value contains HTML tags, textContent otherwise
            if (val && val.indexOf('<') !== -1) {
                el.innerHTML = val;
            } else {
                el.textContent = val;
            }
        });

        // Update placeholder translations
        var placeholderEls = document.querySelectorAll('[data-en-placeholder][data-hi-placeholder]');
        placeholderEls.forEach(function (el) {
            el.placeholder = el.getAttribute('data-' + lang + '-placeholder');
        });

        // Update toggle button state
        if (langToggle) {
            langToggle.setAttribute('data-lang', lang);
            var textSpans = langToggle.querySelectorAll('.lang-toggle-text');
            textSpans.forEach(function (span) {
                var spanText = span.textContent.trim().toLowerCase();
                if ((spanText === 'en' && lang === 'en') || (spanText === 'hi' && lang === 'hi')) {
                    span.style.fontWeight = '700';
                    span.style.opacity = '1';
                } else {
                    span.style.fontWeight = '400';
                    span.style.opacity = '0.6';
                }
            });
        }

        // Update document lang attribute
        document.documentElement.lang = lang === 'hi' ? 'hi' : 'en';

        localStorage.setItem('lang', lang);
    }

    if (langToggle) {
        langToggle.addEventListener('click', function () {
            var currentLang = langToggle.getAttribute('data-lang') || 'en';
            var newLang = currentLang === 'en' ? 'hi' : 'en';
            setLanguage(newLang);
        });
    }

    // Apply saved language on load
    setLanguage(savedLang);


    /* ===========================================
       2. MOBILE MENU TOGGLE
       #mobileMenuToggle toggles #headerNav with .active
       =========================================== */
    var mobileMenuToggle = document.getElementById('mobileMenuToggle');
    var headerNav = document.getElementById('headerNav');

    if (mobileMenuToggle && headerNav) {
        mobileMenuToggle.addEventListener('click', function () {
            headerNav.classList.toggle('active');
            mobileMenuToggle.classList.toggle('active');

            var expanded = mobileMenuToggle.getAttribute('aria-expanded') === 'true';
            mobileMenuToggle.setAttribute('aria-expanded', expanded ? 'false' : 'true');
        });

        // Close menu when a nav link is clicked
        headerNav.querySelectorAll('.nav-link').forEach(function (link) {
            link.addEventListener('click', function () {
                headerNav.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
            });
        });

        // Close menu on click outside
        document.addEventListener('click', function (e) {
            if (!headerNav.contains(e.target) && !mobileMenuToggle.contains(e.target)) {
                headerNav.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }


    /* ===========================================
       3. HEADER SCROLL EFFECT
       #header gets .scrolled when scrollY > 50
       =========================================== */
    var header = document.getElementById('header');

    function handleHeaderScroll() {
        if (!header) return;
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', handleHeaderScroll, { passive: true });
    handleHeaderScroll();


    /* ===========================================
       4. ANIMATED COUNTERS
       .hero-stat-number elements with numeric content
       Ease-out cubic, triggered by IntersectionObserver
       =========================================== */
    function parseStatValue(text) {
        // Extract the leading number from text like "64+", "112+", "4.8"
        var match = text.match(/^([\d.]+)/);
        return match ? parseFloat(match[1]) : null;
    }

    function animateCounters() {
        var counters = document.querySelectorAll('.hero-stat-number');
        counters.forEach(function (counter) {
            if (counter.dataset.animated) return;

            var originalText = counter.textContent.trim();
            var targetVal = parseStatValue(originalText);
            if (targetVal === null) return;

            counter.dataset.animated = 'true';

            // Determine suffix (everything after the number)
            var suffix = originalText.replace(/^[\d.]+/, '');
            var isFloat = originalText.indexOf('.') !== -1;
            var duration = 2000;
            var startTime = null;

            // Preserve any child elements (like star icon)
            var childHTML = '';
            var childNodes = counter.querySelectorAll('i, svg');
            childNodes.forEach(function (child) {
                childHTML += child.outerHTML;
            });

            function step(timestamp) {
                if (!startTime) startTime = timestamp;
                var progress = Math.min((timestamp - startTime) / duration, 1);
                // Ease-out cubic: 1 - (1 - t)^3
                var eased = 1 - Math.pow(1 - progress, 3);
                var current = eased * targetVal;

                if (isFloat) {
                    counter.innerHTML = current.toFixed(1) + childHTML + suffix.replace(/<[^>]*>/g, '');
                } else {
                    counter.innerHTML = Math.floor(current) + suffix;
                }

                if (progress < 1) {
                    requestAnimationFrame(step);
                } else {
                    // Restore original content exactly
                    counter.innerHTML = targetVal + (isFloat ? '' : '') + suffix;
                    if (childHTML) {
                        // Re-check: if suffix didn't include the icon, re-append
                        if (!counter.querySelector('i') && childHTML) {
                            counter.innerHTML = (isFloat ? targetVal.toFixed(1) : targetVal) + childHTML + suffix.replace(/<[^>]*>/g, '');
                        }
                    }
                }
            }

            // Store original HTML for final restoration
            var origHTML = counter.innerHTML;
            requestAnimationFrame(step);
        });
    }

    // Trigger counters when .hero-stats enters viewport
    var statsSection = document.querySelector('.hero-stats');
    if (statsSection) {
        var statsObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    animateCounters();
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2, rootMargin: '0px 0px -50px 0px' });
        statsObserver.observe(statsSection);
    }


    /* ===========================================
       5. SCROLL REVEAL ANIMATIONS
       .reveal, .reveal-left, .reveal-right, .reveal-scale
       get .visible on viewport entry with stagger
       =========================================== */
    var revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');

    // Auto-apply stagger classes to sibling reveal elements
    revealElements.forEach(function (el) {
        var children = el.parentElement ? el.parentElement.children : [];
        var revealSiblings = [];

        for (var i = 0; i < children.length; i++) {
            var child = children[i];
            if (
                child.classList.contains('reveal') ||
                child.classList.contains('reveal-left') ||
                child.classList.contains('reveal-right') ||
                child.classList.contains('reveal-scale')
            ) {
                revealSiblings.push(child);
            }
        }

        if (revealSiblings.length > 1) {
            revealSiblings.forEach(function (sibling, idx) {
                var staggerIndex = Math.min(idx + 1, 8);
                if (!sibling.className.match(/stagger-\d/)) {
                    sibling.classList.add('stagger-' + staggerIndex);
                }
            });
        }
    });

    if (revealElements.length > 0) {
        var revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        revealElements.forEach(function (el) {
            revealObserver.observe(el);
        });
    }


    /* ===========================================
       6. 3D TILT EFFECT ON CARDS
       .tilt-card gets subtle rotateX/rotateY on mousemove
       Max 5 degrees
       =========================================== */
    var tiltCards = document.querySelectorAll('.tilt-card');

    tiltCards.forEach(function (card) {
        card.style.transformStyle = 'preserve-3d';
        card.style.transition = 'transform 0.15s ease-out';

        card.addEventListener('mousemove', function (e) {
            var rect = card.getBoundingClientRect();
            var centerX = rect.left + rect.width / 2;
            var centerY = rect.top + rect.height / 2;
            var mouseX = e.clientX - centerX;
            var mouseY = e.clientY - centerY;

            var normalX = mouseX / (rect.width / 2);
            var normalY = mouseY / (rect.height / 2);

            var rotateY = normalX * 5;
            var rotateX = -normalY * 5;

            card.style.transform = 'perspective(800px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg)';
        });

        card.addEventListener('mouseleave', function () {
            card.style.transition = 'transform 0.4s ease-out';
            card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg)';

            setTimeout(function () {
                card.style.transition = 'transform 0.15s ease-out';
            }, 400);
        });
    });


    /* ===========================================
       7. PARALLAX EFFECT
       .parallax-bg elements
       =========================================== */
    var parallaxElements = document.querySelectorAll('.parallax-bg');

    function handleParallax() {
        parallaxElements.forEach(function (el) {
            var rect = el.getBoundingClientRect();
            var elementCenter = rect.top + rect.height / 2;
            var viewportCenter = window.innerHeight / 2;
            var offset = (elementCenter - viewportCenter) * 0.15;

            el.style.transform = 'translateY(' + offset + 'px)';
        });
    }

    if (parallaxElements.length > 0) {
        window.addEventListener('scroll', handleParallax, { passive: true });
        handleParallax();
    }


    /* ===========================================
       8. CONTACT FORM -> EMAILJS + WHATSAPP
       Sends email via EmailJS AND opens WhatsApp
       =========================================== */

    // ========== EMAILJS CONFIG ==========
    // REPLACE these with your actual EmailJS values:
    var EMAILJS_PUBLIC_KEY = 't8itVSQVr8oJ6wy-X';
    var EMAILJS_SERVICE_ID = 'service_4tenaxt';
    var EMAILJS_TEMPLATE_ID = 'template_47jf68k';
    // ====================================

    // Initialize EmailJS
    if (typeof emailjs !== 'undefined' && EMAILJS_PUBLIC_KEY !== 'YOUR_PUBLIC_KEY') {
        emailjs.init(EMAILJS_PUBLIC_KEY);
    }

    var form = document.getElementById('contactForm');

    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            var nameField = document.getElementById('contactName');
            var phoneField = document.getElementById('contactPhone');
            var emailField = document.getElementById('contactEmail');
            var collegeField = document.getElementById('contactCollege');
            var roomField = document.getElementById('contactRoom');
            var messageField = document.getElementById('contactMessage');

            var name = nameField ? nameField.value.trim() : '';
            var phone = phoneField ? phoneField.value.trim() : '';
            var email = emailField ? emailField.value.trim() : '';
            var college = collegeField ? collegeField.value : '';
            var room = roomField ? roomField.value : '';
            var message = messageField ? messageField.value.trim() : '';

            // Validate required fields
            if (!name) { if (nameField) nameField.focus(); return; }
            if (!phone) { if (phoneField) phoneField.focus(); return; }

            var btn = form.querySelector('button[type="submit"]');
            var originalHTML = btn ? btn.innerHTML : '';

            // Show loading state
            if (btn) {
                btn.innerHTML = '<i class="fas fa-spinner fa-spin" aria-hidden="true"></i> <span>Sending...</span>';
                btn.disabled = true;
            }

            // === SEND VIA EMAILJS ===
            var emailSent = false;
            if (typeof emailjs !== 'undefined' && EMAILJS_PUBLIC_KEY !== 'YOUR_PUBLIC_KEY') {
                var templateParams = {
                    from_name: name,
                    phone: phone,
                    email: email || 'Not provided',
                    college: college || 'Not selected',
                    room_type: room || 'Not selected',
                    message: message || 'No message'
                };

                emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, templateParams)
                    .then(function () {
                        emailSent = true;
                        showSuccess(btn, originalHTML);
                    })
                    .catch(function () {
                        // Email failed, WhatsApp is the fallback
                        sendWhatsApp(name, phone, email, college, room, message);
                        showSuccess(btn, originalHTML);
                    });
            } else {
                // EmailJS not configured, use WhatsApp only
                sendWhatsApp(name, phone, email, college, room, message);
                showSuccess(btn, originalHTML);
            }

            // === ALSO SEND WHATSAPP (always, as backup + instant notification) ===
            sendWhatsApp(name, phone, email, college, room, message);
        });
    }

    function sendWhatsApp(name, phone, email, college, room, message) {
        var lines = [
            'New Enquiry from Website',
            '',
            '*Name:* ' + name,
            '*Phone:* ' + phone
        ];
        if (email) lines.push('*Email:* ' + email);
        if (college) lines.push('*College:* ' + college);
        if (room) lines.push('*Room Type:* ' + room);
        if (message) lines.push('*Message:* ' + message);

        var waMsg = encodeURIComponent(lines.join('\n'));
        window.open('https://wa.me/918770445161?text=' + waMsg, '_blank');
    }

    function showSuccess(btn, originalHTML) {
        if (!btn) return;
        btn.innerHTML = '<i class="fas fa-check-circle" aria-hidden="true"></i> <span>Enquiry Sent!</span>';
        btn.style.background = '#27ae60';
        setTimeout(function () {
            btn.innerHTML = originalHTML;
            btn.style.background = '';
            btn.disabled = false;
            var form = document.getElementById('contactForm');
            if (form) form.reset();
        }, 3000);
    }


    /* ===========================================
       9. AI CHATBOT
       #chatbotToggle, .chatbot-window, #chatbotClose,
       #chatbotInput, #chatbotSend, #chatbotMessages,
       .chatbot-quick-reply buttons
       =========================================== */
    var chatbotToggle = document.getElementById('chatbotToggle');
    var chatbotWindow = document.getElementById('chatbotWindow');
    var chatbotClose = document.getElementById('chatbotClose');
    var chatInput = document.getElementById('chatbotInput');
    var chatSend = document.getElementById('chatbotSend');
    var chatMessages = document.getElementById('chatbotMessages');

    // Knowledge base with keyword matching
    var chatKnowledge = {
        pricing: {
            keywords: ['price', 'pricing', 'cost', 'fee', 'fees', 'rent', 'charge', 'kitna', 'paisa', 'rupee', 'rs', '\u20B9', 'rate', 'affordable', 'cheap', 'budget', 'monthly', 'per month'],
            answer: 'Our pricing:\n\n\u2022 Double Bed Non-AC: starts \u20B97,000/month (including meals)\n\u2022 Double Bed AC: starts \u20B99,000/month (including meals)\n\nBoth options include home-style meals, Wi-Fi, housekeeping, and all amenities. We offer the best value for premium hostel accommodation near Medicaps University. Would you like to book a room?'
        },
        amenities: {
            keywords: ['amenity', 'amenities', 'facility', 'facilities', 'wifi', 'internet', 'laundry', 'washing', 'parking', 'ac', 'air condition', 'ro', 'water', 'study', 'gym', 'cctv', 'guard', 'housekeeping', 'cleaning'],
            answer: 'We offer premium amenities including: High-Speed Wi-Fi, 24/7 CCTV Security, AC & Non-AC Rooms, Home-Style Meals, RO Purified Water, Vehicle Parking, Daily Housekeeping, Laundry Service, Dedicated Study Areas, Private Bathrooms, and Rooftop Lounge. All maintenance issues resolved within 24\u201348 hours!'
        },
        location: {
            keywords: ['location', 'address', 'where', 'map', 'direction', 'kahan', 'distance', 'far', 'near', 'close', 'walk', 'rau', 'pigdamber'],
            answer: 'We are located directly in front of Medicaps University, Pigdamber, Rau, Indore, MP 453331. Just a 2-minute walk from the campus gate! We are also near SD Bansal College, IPS Academy, IIST, and IIM Indore.'
        },
        booking: {
            keywords: ['book', 'booking', 'reserve', 'join', 'admission', 'available', 'vacancy', 'room available', 'register', 'enroll', 'seat', 'apply', 'visit'],
            answer: 'Great choice! To book your room at Radiance Residency, you can:\n\n1) Fill our enquiry form on the website\n2) WhatsApp us at +91 8770-445-161\n3) Call us directly\n\nLimited rooms available \u2014 book early!'
        },
        food: {
            keywords: ['food', 'meal', 'meals', 'breakfast', 'lunch', 'dinner', 'tiffin', 'khana', 'mess', 'canteen', 'dining', 'veg', 'non-veg', 'cook', 'nutrition', 'diet'],
            answer: 'Yes! We provide home-style meals included in your hostel fee (Double bed Non-AC from \u20B97,000/month, AC from \u20B99,000/month). Our dining serves nutritious, freshly prepared food that tastes just like home cooking. Your mom would approve!'
        },
        safety: {
            keywords: ['safe', 'safety', 'secure', 'security', 'cctv', 'guard', 'camera', 'protection', 'warden'],
            answer: 'Safety is our top priority! We have 24/7 CCTV surveillance, security guards, and controlled entry/exit. Over 112 students and their parents trust us. Your safety is guaranteed at Radiance Residency.'
        },
        colleges: {
            keywords: ['college', 'university', 'medicaps', 'ips', 'iist', 'iim', 'bansal', 'sd bansal', 'campus', 'institute'],
            answer: 'Radiance Residency is near multiple top colleges: Medicaps University (2 min walk!), SD Bansal College, IPS Academy, IIST, and IIM Indore. Students from all these colleges stay with us.'
        },
        contact: {
            keywords: ['contact', 'phone', 'call', 'number', 'whatsapp', 'email', 'reach', 'talk', 'helpline'],
            answer: 'You can reach us at:\n\n\u2022 Phone/WhatsApp: +91 8770-445-161\n\u2022 Email: info@radianceresidency.com\n\u2022 Visit: In front of Medicaps University, Pigdamber, Rau, Indore\n\nWe are available 24/7!'
        },
        rooms: {
            keywords: ['room', 'single', 'double', 'sharing', 'bed', 'furnished', 'bathroom', 'attached', 'occupancy'],
            answer: 'We offer fully furnished rooms with private attached bathrooms.\n\n\u2022 Double Bed Non-AC: from \u20B97,000/month\n\u2022 Double Bed AC: from \u20B99,000/month\n\nBoth options include meals, Wi-Fi, housekeeping, and all amenities!'
        }
    };

    function getBotResponse(userMsg) {
        var msg = userMsg.toLowerCase().trim();

        // Check for greetings
        if (/^(hi|hello|hey|hii|hlo|namaste|namaskar|good morning|good evening|good afternoon|sup)/.test(msg)) {
            return 'Hello! Welcome to Radiance Residency \u2014 the best boys hostel near Medicaps University, Indore. How can I help you today? You can ask about rooms, pricing, amenities, or booking!';
        }

        // Check for thanks
        if (/\b(thank|thanks|thankyou|thank you|dhanyawad|shukriya|thnx|thx)\b/.test(msg)) {
            return 'You\'re welcome! Feel free to ask anything else. You can also WhatsApp us at +91 8770-445-161 for instant assistance!';
        }

        // Search knowledge base with keyword scoring
        var bestMatch = null;
        var bestScore = 0;

        for (var topic in chatKnowledge) {
            if (!chatKnowledge.hasOwnProperty(topic)) continue;
            var score = 0;
            chatKnowledge[topic].keywords.forEach(function (kw) {
                if (msg.indexOf(kw) !== -1) score++;
            });
            if (score > bestScore) {
                bestScore = score;
                bestMatch = topic;
            }
        }

        if (bestMatch && bestScore > 0) {
            return chatKnowledge[bestMatch].answer;
        }

        // Default fallback
        return 'Thank you for your interest in Radiance Residency! For detailed information, please WhatsApp us at +91 8770-445-161 or call us directly. You can also ask me about our rooms, pricing, amenities, location, or booking process!';
    }

    function addChatMessage(text, sender) {
        if (!chatMessages) return;
        var div = document.createElement('div');
        div.className = 'chatbot-message chatbot-message-' + sender;
        var p = document.createElement('p');
        p.textContent = text;
        div.appendChild(p);
        chatMessages.appendChild(div);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function handleUserMessage() {
        if (!chatInput) return;
        var msg = chatInput.value.trim();
        if (!msg) return;

        addChatMessage(msg, 'user');
        chatInput.value = '';

        // Simulate typing delay
        setTimeout(function () {
            var response = getBotResponse(msg);
            addChatMessage(response, 'bot');
        }, 500);
    }

    // Toggle chatbot window
    if (chatbotToggle && chatbotWindow) {
        chatbotToggle.addEventListener('click', function () {
            var isOpen = chatbotWindow.style.display !== 'none';
            if (isOpen) {
                chatbotWindow.style.display = 'none';
                chatbotToggle.setAttribute('aria-expanded', 'false');
                // Show open icon, hide close icon
                var openIcon = chatbotToggle.querySelector('.chatbot-toggle-icon-open');
                var closeIcon = chatbotToggle.querySelector('.chatbot-toggle-icon-close');
                if (openIcon) openIcon.style.display = '';
                if (closeIcon) closeIcon.style.display = 'none';
            } else {
                chatbotWindow.style.display = '';
                chatbotToggle.setAttribute('aria-expanded', 'true');
                // Show close icon, hide open icon
                var openIcon2 = chatbotToggle.querySelector('.chatbot-toggle-icon-open');
                var closeIcon2 = chatbotToggle.querySelector('.chatbot-toggle-icon-close');
                if (openIcon2) openIcon2.style.display = 'none';
                if (closeIcon2) closeIcon2.style.display = '';
                if (chatInput) chatInput.focus();
            }
        });
    }

    // Close chatbot
    if (chatbotClose) {
        chatbotClose.addEventListener('click', function () {
            if (chatbotWindow) chatbotWindow.style.display = 'none';
            if (chatbotToggle) {
                chatbotToggle.setAttribute('aria-expanded', 'false');
                var openIcon = chatbotToggle.querySelector('.chatbot-toggle-icon-open');
                var closeIcon = chatbotToggle.querySelector('.chatbot-toggle-icon-close');
                if (openIcon) openIcon.style.display = '';
                if (closeIcon) closeIcon.style.display = 'none';
            }
        });
    }

    // Send message on button click
    if (chatSend) {
        chatSend.addEventListener('click', handleUserMessage);
    }

    // Send message on Enter key
    if (chatInput) {
        chatInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                handleUserMessage();
            }
        });
    }

    // Quick reply buttons (.chatbot-quick-reply with data-en/data-hi text)
    var quickReplies = document.querySelectorAll('.chatbot-quick-reply');
    quickReplies.forEach(function (btn) {
        btn.addEventListener('click', function () {
            var questionText = btn.textContent.trim();

            addChatMessage(questionText, 'user');

            setTimeout(function () {
                var response = getBotResponse(questionText);
                addChatMessage(response, 'bot');
            }, 500);
        });
    });


    /* ===========================================
       10. SMOOTH SCROLL FOR ANCHOR LINKS
       =========================================== */
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            var href = this.getAttribute('href');
            if (href === '#' || href.length < 2) return;

            var target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                var headerHeight = header ? header.offsetHeight : 0;
                var targetPosition = target.getBoundingClientRect().top + window.scrollY - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });


    /* ===========================================
       11. ACTIVE NAV LINK HIGHLIGHTING
       .nav-link inside .nav-list inside #headerNav
       =========================================== */
    function highlightActiveNav() {
        var allNavLinks = document.querySelectorAll('#headerNav .nav-list .nav-link');

        function norm(p) {
            return p.replace(/\/index\.html$/, '/').replace(/\/$/, '') || '/';
        }

        var curNorm = norm(window.location.pathname);
        var bestMatch = null;
        var bestLen = -1;

        allNavLinks.forEach(function (link) {
            link.classList.remove('active');
            var href = link.getAttribute('href');
            if (!href || href.charAt(0) === '#') return;

            var a = document.createElement('a');
            a.href = href;
            var linkNorm = norm(a.pathname);

            if (curNorm === linkNorm) {
                if (linkNorm.length > bestLen) { bestMatch = link; bestLen = linkNorm.length; }
            } else if (linkNorm !== '/' && curNorm.indexOf(linkNorm + '/') === 0) {
                if (linkNorm.length > bestLen) { bestMatch = link; bestLen = linkNorm.length; }
            }
        });

        if (bestMatch) bestMatch.classList.add('active');
    }

    highlightActiveNav();
    window.addEventListener('hashchange', highlightActiveNav);


    /* ===========================================
       12. CURSOR GLOW EFFECT (Desktop Only)
       Follows cursor over hero section
       =========================================== */
    var heroSection = document.querySelector('.hero, #hero, [class*="hero-section"]');

    if (heroSection && window.matchMedia('(pointer: fine)').matches) {
        var glowCursor = document.createElement('div');
        glowCursor.className = 'cursor-glow';
        glowCursor.style.cssText = [
            'position: fixed',
            'width: 250px',
            'height: 250px',
            'border-radius: 50%',
            'background: radial-gradient(circle, rgba(212, 175, 55, 0.15) 0%, rgba(212, 175, 55, 0.05) 40%, transparent 70%)',
            'pointer-events: none',
            'z-index: 9999',
            'transform: translate(-50%, -50%)',
            'opacity: 0',
            'transition: opacity 0.3s ease',
            'will-change: transform'
        ].join(';');

        document.body.appendChild(glowCursor);

        var glowX = 0;
        var glowY = 0;
        var currentGlowX = 0;
        var currentGlowY = 0;
        var glowVisible = false;
        var glowAnimating = false;

        function animateGlow() {
            if (!glowVisible) {
                glowAnimating = false;
                return;
            }

            currentGlowX += (glowX - currentGlowX) * 0.15;
            currentGlowY += (glowY - currentGlowY) * 0.15;

            glowCursor.style.left = currentGlowX + 'px';
            glowCursor.style.top = currentGlowY + 'px';

            requestAnimationFrame(animateGlow);
        }

        heroSection.addEventListener('mousemove', function (e) {
            glowX = e.clientX;
            glowY = e.clientY;

            if (!glowVisible) {
                glowVisible = true;
                glowCursor.style.opacity = '1';
            }

            if (!glowAnimating) {
                glowAnimating = true;
                currentGlowX = glowX;
                currentGlowY = glowY;
                requestAnimationFrame(animateGlow);
            }
        });

        heroSection.addEventListener('mouseleave', function () {
            glowVisible = false;
            glowCursor.style.opacity = '0';
        });
    }


    /* ===========================================
       13. INTERACTIVE NUMBER COUNTER HOVER EFFECT
       Pulse/glow on .hero-stat when hovered
       =========================================== */
    var statItems = document.querySelectorAll('.hero-stat');

    statItems.forEach(function (stat) {
        stat.addEventListener('mouseenter', function () {
            stat.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
            stat.style.transform = 'scale(1.08)';
            stat.style.boxShadow = '0 0 20px rgba(201, 168, 76, 0.3)';

            var numEl = stat.querySelector('.hero-stat-number');
            if (numEl) {
                numEl.style.transition = 'text-shadow 0.3s ease, transform 0.3s ease';
                numEl.style.textShadow = '0 0 12px rgba(201, 168, 76, 0.5)';
                numEl.style.transform = 'scale(1.05)';
            }
        });

        stat.addEventListener('mouseleave', function () {
            stat.style.transform = 'scale(1)';
            stat.style.boxShadow = 'none';

            var numEl = stat.querySelector('.hero-stat-number');
            if (numEl) {
                numEl.style.textShadow = 'none';
                numEl.style.transform = 'scale(1)';
            }
        });
    });


    /* ===========================================
       14. IMAGE FADE-IN ON SCROLL
       Images fade in gently when scrolled into view
       =========================================== */
    var galleryImages = document.querySelectorAll('.gallery-item');
    if (galleryImages.length > 0) {
        galleryImages.forEach(function (item, idx) {
            item.style.opacity = '0';
            item.style.transform = 'translateY(20px)';
            item.style.transition = 'opacity 0.6s ease ' + (idx * 0.08) + 's, transform 0.6s ease ' + (idx * 0.08) + 's';
        });

        var galleryObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var items = entry.target.querySelectorAll('.gallery-item');
                    items.forEach(function (item) {
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0)';
                    });
                    galleryObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        var galleryGrid = document.querySelector('.gallery-grid');
        if (galleryGrid) galleryObserver.observe(galleryGrid);
    }


    /* ===========================================
       15. MAGNETIC BUTTON EFFECT
       .btn-primary buttons pull toward cursor on hover
       =========================================== */
    if (window.matchMedia('(pointer: fine)').matches) {
        var magneticButtons = document.querySelectorAll('.btn-primary');

        magneticButtons.forEach(function (btn) {
            btn.style.transition = 'transform 0.2s ease-out';

            btn.addEventListener('mousemove', function (e) {
                var rect = btn.getBoundingClientRect();
                var centerX = rect.left + rect.width / 2;
                var centerY = rect.top + rect.height / 2;
                var deltaX = e.clientX - centerX;
                var deltaY = e.clientY - centerY;

                // Subtle pull: max ~6px displacement
                var pullX = deltaX * 0.15;
                var pullY = deltaY * 0.15;

                btn.style.transform = 'translate(' + pullX + 'px, ' + pullY + 'px)';
            });

            btn.addEventListener('mouseleave', function () {
                btn.style.transition = 'transform 0.35s ease-out';
                btn.style.transform = 'translate(0, 0)';

                setTimeout(function () {
                    btn.style.transition = 'transform 0.2s ease-out';
                }, 350);
            });
        });
    }


    /* ===========================================
       16. TEXT SCRAMBLE EFFECT
       Hero badge text scrambles briefly on page load
       =========================================== */
    var heroBadge = document.querySelector('.hero-badge');

    if (heroBadge) {
        var finalText = heroBadge.textContent;
        var scrambleChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#@$%&*';
        var scrambleDuration = 1200; // total ms
        var startDelay = 300; // delay before starting
        var framesPerChar = 3; // randomize each char N times before settling

        function scrambleText(element, target) {
            var length = target.length;
            var totalFrames = length * framesPerChar;
            var frame = 0;
            var interval = scrambleDuration / totalFrames;

            function tick() {
                if (frame >= totalFrames) {
                    element.textContent = target;
                    return;
                }

                var settledCount = Math.floor(frame / framesPerChar);
                var result = '';

                for (var i = 0; i < length; i++) {
                    if (target[i] === ' ') {
                        result += ' ';
                    } else if (i < settledCount) {
                        result += target[i];
                    } else {
                        result += scrambleChars[Math.floor(Math.random() * scrambleChars.length)];
                    }
                }

                element.textContent = result;
                frame++;
                setTimeout(tick, interval);
            }

            tick();
        }

        setTimeout(function () {
            scrambleText(heroBadge, finalText);
        }, startDelay);
    }


    /* ===========================================
       17. SMOOTH PAGE TRANSITIONS
       Fade-out before navigating to other pages
       =========================================== */
    // Create transition overlay
    var transitionOverlay = document.createElement('div');
    transitionOverlay.className = 'page-transition-overlay';
    transitionOverlay.style.cssText = [
        'position: fixed',
        'top: 0',
        'left: 0',
        'width: 100%',
        'height: 100%',
        'background: #0a1628',
        'z-index: 99999',
        'opacity: 0',
        'pointer-events: none',
        'transition: opacity 0.35s ease'
    ].join(';');
    document.body.appendChild(transitionOverlay);

    // Fade-in on page load (reverse the overlay)
    window.addEventListener('pageshow', function () {
        transitionOverlay.style.opacity = '0';
        transitionOverlay.style.pointerEvents = 'none';
    });

    // Intercept nav link clicks for smooth transition
    var internalLinks = document.querySelectorAll('a[href$=".html"], #headerNav .nav-list .nav-link');

    internalLinks.forEach(function (link) {
        link.addEventListener('click', function (e) {
            var href = link.getAttribute('href');
            if (!href) return;

            // Skip anchors, external links, and mailto/tel
            if (href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel') || href.startsWith('javascript')) return;

            // Skip if modifier keys are held (new tab)
            if (e.ctrlKey || e.metaKey || e.shiftKey) return;

            e.preventDefault();

            transitionOverlay.style.opacity = '1';
            transitionOverlay.style.pointerEvents = 'all';

            setTimeout(function () {
                window.location.href = href;
            }, 350);
        });
    });

});
