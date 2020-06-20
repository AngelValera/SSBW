// modo nocturno
$(document).ready(function () {
    var dark = false;
    //--------------- Modo nocturno -----------------------------
    $("#tipolectura").css('cursor', 'pointer');
    $("#tipolectura").on('click', function (e) {
        if (!dark) {            
            $(this).find("i").removeClass("fa-moon-o").addClass("fa-sun-o");
            document.body.setAttribute("data-theme", "dark");
            $("[id*=visita_card]").each(function () {
                $(this).addClass("bg-light");
            });
            $(".list-group-item").each(function () {
                $(this).addClass("bg-light");
            });
            dark = true;
        } else {
            $(this).find("i").removeClass("fa-sun-o").addClass("fa-moon-o");
            document.body.removeAttribute("data-theme");
            $("[id*=visita_card]").each(function () {
                $(this).removeClass("bg-light");
            });
            $(".list-group-item").each(function () {
                $(this).addClass("bg-light");
            });
            dark = false;
        }
    });
});