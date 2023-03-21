const nav = document.querySelector('nav');

document.addEventListener('scroll', () => {

    if (scrollY > 100) {

        if (scrollY > window.innerHeight) {

            nav.classList.add('invisible');

        } else {

            nav.classList.add('bg-[#222222]');
            nav.classList.remove('invisible');

        }



    } else {

        nav.classList.remove('invisible');
        nav.classList.remove('bg-[#222222]');

    }

})