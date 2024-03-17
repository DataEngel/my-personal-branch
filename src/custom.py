<!DOCTYPE html>
<html>
<head>
    <title>Nav Menu</title>
    <style>
        /* Aquí va tu CSS para el menú de navegación */
    </style>
</head>
<body>
    <nav id="navbarSupportedContent">
        <!-- Contenido del menú de navegación -->
    </nav>
    <button class="custom_menu-btn">Toggle Menu</button>
    <div id="displayDate"></div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            var nav = $("#navbarSupportedContent");
            var btn = $(".custom_menu-btn");
            
            btn.click(function(e) {
                e.preventDefault();
                nav.toggleClass("lg_nav-toggle");
                $(".custom_menu-btn").toggleClass("menu_btn-style");
            });

            function getCurrentYear() {
                var d = new Date();
                var currentYear = d.getFullYear();
                $("#displayDate").html(currentYear);
            }

            getCurrentYear();
        });
    </script>
</body>
</html>
