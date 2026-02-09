javascript.document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission
        console.log('Form submitted!'); // Log a message to the console
    });
});
        let scrolling = true;
        const scrollSpeed = 0.37;
        const introHero = document.querySelector('.intro-hero');
        let scrollPos = 0;
        
        function autoScroll() {
            if (!scrolling) return;
            
            const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
            const percentage = scrollPos / maxScroll;
            
            // Opacity
            if (percentage > 0.8) {
                introHero.style.opacity = Math.max(0, 1 - (percentage - 0.8) / 0.2);
            } else {
                introHero.style.opacity = 1;
            }
            
            // Dynamische Geschwindigkeit
            let speed = scrollSpeed;
            if (percentage < 0.1) speed = scrollSpeed * 1.3;
            else if (percentage > 0.4 && percentage < 0.7) speed = scrollSpeed * 1.15;
            else if (percentage > 0.8) speed = scrollSpeed * 0.7;
            
            scrollPos += speed;
            window.scrollTo(0, scrollPos);
            
            // Check ob Ende erreicht
            if (scrollPos >= maxScroll) {
                scrolling = false;
                setTimeout(() => {
                    scrolling = true;
                    scrollPos = 0;
                    window.scrollTo(0, 0);
                    autoScroll();
                }, 3000);
            } else {
                requestAnimationFrame(autoScroll);
            }
        }
        
        // Starten wenn Seite geladen ist
        window.addEventListener('load', () => {
            autoScroll();
        });
        
        // Stoppen bei Nutzer-Interaktion
        document.addEventListener('wheel', (e) => {
            scrolling = false;
            scrollPos = window.scrollY || document.documentElement.scrollTop;
        }, true);
        
        document.addEventListener('touchmove', () => {
            scrolling = false;
        }, true);