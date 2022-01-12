//nested burger type menu code, although in stead of hamburger menu
//the menu text is a word
let nestburgers = document.getElementsByClassName("nestburger");
for (let nestburger of nestburgers) {
    nestburger.addEventListener("click", (evt) => {
        toggleNest(evt.target)
    });
}

function toggleNest(burger) {
    let siblings = burger.parentElement.children;
    for (let sibling of siblings) {
        if (sibling === burger) {
            //alert("found self!");
        } else {
            if (sibling.style.display === "none") {
                sibling.style.display = "inherit";
            } else {
                sibling.style.display = "none";
            }
        }
    }
}

function closeNest(burger) {
    let siblings = burger.parentElement.children;
    for (let sibling of siblings) {
        if (sibling === burger) {
            //alert("found self!");
        } else {
            sibling.style.display = "none";
        }
    }

}

function closeAll() {
    for (let nestburger of nestburgers) {
        closeNest(nestburger);
    };
}

function openSelectedInitialNests() {
    for (let nestburger of nestburgers) {
        if (nestburger.classList.contains("initial-open")) {
            toggleNest(nestburger);
        }
    }
}

closeAll();
openSelectedInitialNests();