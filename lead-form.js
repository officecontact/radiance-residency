/* =====================================================================
   Radiance Residency — Lead capture widget
   Self-contained, no dependencies. Auto-inits every form.js-lead-form.
   Delivery: (1) emails the lead via Web3Forms (when a key is set),
   (2) opens a pre-filled WhatsApp chat for instant contact, and
   (3) fires a GA4 `generate_lead` event so enquiries are measurable.
   Works on any page.
   ===================================================================== */
(function () {
    'use strict';

    // Web3Forms access key — get a free one in 60s at https://web3forms.com
    // (enter your email, copy the key it sends you). Until it is set, leads
    // still arrive instantly via WhatsApp; email simply stays off.
    var WEB3FORMS_ACCESS_KEY = '';
    var WA_NUMBER = '918770445161';

    function val(form, name) {
        var el = form.querySelector('[name="' + name + '"]');
        return el ? String(el.value || '').trim() : '';
    }

    function track(eventName, d) {
        // Report the lead to GA4 so enquiries become visible + markable as
        // key events. Safe no-op if gtag isn't loaded yet.
        try {
            if (typeof window.gtag === 'function') {
                window.gtag('event', eventName, {
                    college: d.college || '',
                    room_type: d.room || '',
                    enquiry_page: d.page || '',
                    value: 1
                });
            }
        } catch (e) {}
    }

    function openWhatsApp(d) {
        var lines = ['New Enquiry from Website', '', '*Name:* ' + d.name, '*Phone:* ' + d.phone];
        if (d.email) lines.push('*Email:* ' + d.email);
        if (d.college) lines.push('*College:* ' + d.college);
        if (d.room) lines.push('*Room Type:* ' + d.room);
        if (d.page) lines.push('*Page:* ' + d.page);
        window.open('https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(lines.join('\n')), '_blank');
    }

    function emailLead(d) {
        // Email the lead via Web3Forms. Skips cleanly until a key is set.
        if (!WEB3FORMS_ACCESS_KEY) { return Promise.resolve(); }
        return fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
            body: JSON.stringify({
                access_key: WEB3FORMS_ACCESS_KEY,
                subject: 'New Hostel Enquiry — ' + d.name + ' (' + (d.college || 'N/A') + ')',
                from_name: 'Radiance Residency Website',
                Name: d.name,
                Phone: d.phone,
                Email: d.email || 'Not provided',
                College: d.college || 'Not selected',
                'Room Type': d.room || 'Not selected',
                'Enquiry Page': d.page || ''
            })
        });
    }

    function showSuccess(form) {
        var done = form.querySelector('.lead-form-success');
        if (done) { done.style.display = 'block'; }
        var btn = form.querySelector('button[type="submit"]');
        if (btn) {
            btn.innerHTML = '<i class="fas fa-check-circle" aria-hidden="true"></i> <span>Enquiry Sent! We\'ll call you back.</span>';
            btn.style.background = '#27ae60';
        }
        setTimeout(function () { try { form.reset(); } catch (e) {} }, 400);
    }

    function init(form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            var d = {
                name: val(form, 'name'),
                phone: val(form, 'phone'),
                email: val(form, 'email'),
                college: val(form, 'college'),
                room: val(form, 'room'),
                page: (document.title || '').replace(' | Radiance Residency', '')
            };
            var nameEl = form.querySelector('[name="name"]');
            var phoneEl = form.querySelector('[name="phone"]');
            if (!d.name) { if (nameEl) nameEl.focus(); return; }
            if (!d.phone || d.phone.replace(/\D/g, '').length < 10) { if (phoneEl) phoneEl.focus(); return; }

            var btn = form.querySelector('button[type="submit"]');
            if (btn) { btn.disabled = true; btn.innerHTML = '<i class="fas fa-spinner fa-spin" aria-hidden="true"></i> <span>Sending...</span>'; }

            // Record the lead in GA4 (visible as the `generate_lead` event —
            // mark it as a Key Event in GA4 to count enquiries as conversions).
            track('generate_lead', d);

            // Fire email (best-effort) and ALWAYS open WhatsApp for instant contact.
            emailLead(d)["catch"](function () {}).then(function () { showSuccess(form); });
            openWhatsApp(d);
        });
    }

    function boot() {
        var forms = document.querySelectorAll('form.js-lead-form');
        for (var i = 0; i < forms.length; i++) { init(forms[i]); }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else { boot(); }
})();
