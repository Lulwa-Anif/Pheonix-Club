const navbarItems = document.querySelectorAll('#navbar-items li a');
        const sliderBar = document.getElementById('slider-bar');
        const sections = document.querySelectorAll('section');

        function setSliderPosition() {
            const currentScroll = window.scrollY + window.innerHeight / 2;

            sections.forEach((section, index) => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;

                if (currentScroll >= sectionTop && currentScroll < sectionTop + sectionHeight) {
                    const link = navbarItems[index];
                    const linkRect = link.getBoundingClientRect();

                    sliderBar.style.left = `${linkRect.left}px`;
                    sliderBar.style.width = `${linkRect.width}px`;
                }
            });
        }

        window.addEventListener('scroll', setSliderPosition);
        window.addEventListener('load', setSliderPosition);
   