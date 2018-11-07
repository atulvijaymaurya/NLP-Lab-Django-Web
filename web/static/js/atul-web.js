function loadHeader()
{
    document.getElementById('header').innerHTML = `<div class="head">
    <img src="static/images/logo2.png" height="100" width="100" style="margin-left: auto;margin-top: 15px;">
    <div style="margin-right:auto;">
      <h1>Text Analytics & NLP Lab</h1>
      <h2>@ CA Dept, NIT Trichy</h2>
    </div>
  </div>
    <div class="topnav">
      <a id="nav_home" href="/">Home</a>
      <a id="nav_people" href="/people">People</a>
      <a id="nav_publications" href="/publications">Publications</a>
      <a id="nav_projects" href="/projects">Projects</a>
      <a id="nav_demos" href="/demos">Demos</a>
      <a id="nav_gallery" href="/gallery">Gallery</a>
      <!--<a href="/blog">Blog</a>-->
      <a id="nav_contactus" href="/contactus">Contact Us</a>
    </div>`
}