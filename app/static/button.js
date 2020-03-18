dates = []
currentIndex = 0

function parse_url(s) {
    a = s.split("/")
    return "/data/" + a[0] + "-" + a[1]
}

window.onload = function () {
    for (i = 0; i < dates.length; i++) {
        render_map(parse_url(dates[i]), "container" + i)
    }
    document.getElementById("container" + currentIndex).style.display = "block"

    document.getElementById("prev").onclick = function () {
        if (currentIndex == 0) {
            return
        }

        document.getElementById("container" + currentIndex).style.display = "none"
        currentIndex--
        document.getElementById("date").innerText = dates[currentIndex]
        document.getElementById("container" + currentIndex).style.display = "block"
    }

    document.getElementById("next").onclick = function () {
        if (currentIndex == dates.length - 1) {
            return
        }

        document.getElementById("container" + currentIndex).style.display = "none"
        currentIndex++
        document.getElementById("date").innerText = dates[currentIndex]
        document.getElementById("container" + currentIndex).style.display = "block"
    }
}

