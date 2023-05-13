const nav = document.querySelector('nav');

document.addEventListener('scroll', () => {
    if (scrollY > 100) {


        nav.classList.add('bg-[#222222]');
    
    }

    else {

        nav.classList.remove('bg-[#222222]');

    }

})


