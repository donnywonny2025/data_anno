try:
    await page.evaluate('''() => {
        // Deploy a tracking loop to build an indestructible shield over the native back button
        setInterval(() => {
            // Find Grok's native Back button visually by location (top left, SVG icon)
            let nativeBack = Array.from(document.querySelectorAll('button')).find(b => 
                b.innerHTML.includes('<svg') && 
                b.getBoundingClientRect().x < 100 && 
                b.getBoundingClientRect().y < 100 && 
                b.getBoundingClientRect().width > 0
            );
            
            if (nativeBack) {
                let rect = nativeBack.getBoundingClientRect();
                let shield = document.getElementById('god-mode-glass-breaker');
                
                // If shield doesn't exist, build it
                if (!shield) {
                    shield = document.createElement('div');
                    shield.id = 'god-mode-glass-breaker';
                    // The shield is pinned directly to the root body to immune it from React's stacking contexts
                    shield.style.position = 'fixed';
                    shield.style.zIndex = '2147483647';
                    shield.style.cursor = 'pointer';
                    shield.style.borderRadius = '50%'; // Match the circular UI
                    
                    shield.onclick = function(e) {
                        e.preventDefault();
                        e.stopPropagation();
                        // Instead of a synthetic DOM click, force the browser history to literally rewind
                        window.history.back();
                    };
                    document.body.appendChild(shield);
                }
                
                // Track the native button's physical pixels 5 times a second
                shield.style.left = rect.left + 'px';
                shield.style.top = rect.top + 'px';
                shield.style.width = rect.width + 'px';
                shield.style.height = rect.height + 'px';
                
            } else {
                // If the native back button despawns, purge the shield
                let shield = document.getElementById('god-mode-glass-breaker');
                if (shield) shield.remove();
            }
        }, 200);
    }''')
    print("✅ [GHOST FOX] Invisible shield tracker deployed over native Back button.")
except Exception as e:
    print(f"⚠️ {e}")
