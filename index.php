
<!-- Force page not to cache. -->
<!--<META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">-->
<!--<META HTTP-EQUIV="EXPIRES" CONTENT="Mon, 22 Jul 2002 11:12:01 GMT">-->

<!DOCTYPE HTML>
<html>
	<head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-PXBGMQDG5F"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-PXBGMQDG5F');
        </script>

		<title>Fraser Parlane, Ph.D.</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
        <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab&display=swap" rel="stylesheet">
    </head>
    <body class="is-preload" id="body">

        <!-- Header -->
        <header id="header">
            <?php include 'php/header.php'; ?>
        </header>

        <!-- Main -->
        <div id="main">
            <section>

                <?php include 'php/intro.php'; ?>
                <?php include 'php/highlights.php'; ?>

                <h1 id="projects">Projects</h1>
                <?php include 'php/projects.php'; ?>

                <h1 id="education">Education</h1>
                <?php include 'php/education.php'; ?>

                <h1 id="awards">Awards</h1>
                <?php include 'php/awards.php'; ?>

                <h1 id="publications">Publications</h1>
                <?php include 'php/publications.php'; ?>

                <h1 id="presentations">Presentations</h1>
                <?php include 'php/presentations.php'; ?>

                <h1 id="development">Development</h1>
                <?php include 'php/development.php'; ?>

                <h1 id="press">Press</h1>
                <?php include 'php/press.php'; ?>

            </section>
        </div>

        <!-- Footer -->
        <footer id="footer">
            <div class="inner">
                <ul class="copyright">
                    <li class="copyright-slug">&copy; Fraser Parlane</li>
                </ul>
            </div>
        </footer>

        <!-- Scripts -->
        <script src="assets/js/jquery.min.js"></script>
        <script src="assets/js/jquery.poptrox.min.js"></script>
        <script src="assets/js/browser.min.js"></script>
        <script src="assets/js/breakpoints.min.js"></script>
        <script src="assets/js/util.js"></script>
        <script src="assets/js/main.js"></script>

	</body>
</html>