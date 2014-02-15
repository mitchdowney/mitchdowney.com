<!DOCTYPE html>
<html>

<head>

  <title>mitchdowney.com</title>

  <meta charset=”utf-8”> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">
    
  <meta property="og:url" content="#" />
  <meta property="og:title" content="#" />
  <meta property="og:description" content="#" />
  <meta property="og:image" content="#" />
    
  <link href="css/bootstrap.css" type="text/css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="font-awesome-4.0.3/css/font-awesome.min.css">
  <link href="css/styles.css" type="text/css" rel="stylesheet">
  <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,400italic|Roboto+Slab:400,700' rel='stylesheet' type='text/css'>
  <script src="js/jquery-1.11.0.min.js"></script>
  <script src="js/bootstrap.js"></script>

</head>
  
<body>

<div class="md-container">

  <?php 
  
  include 'header.php'; 
  
  ?>

  <?php 
  
  error_reporting(E_ALL ^ E_NOTICE);
  
  if ($_GET['portfolio'] == "everyvote") {
    require("portfolio/everyvote/everyvote.php");
  }
  elseif ($_GET['portfolio'] == "partystarter") {
    require("portfolio/partystarter/partystarter.php");
  }
  elseif ($_GET['portfolio'] == "earthhq") {
    require("portfolio/earthhq/earthhq.php");
  }
  elseif ($_GET['portfolio'] == "advantage-act") {
    require("portfolio/advantage-act/advantage-act.php");
  }
  elseif ($_GET['portfolio'] == "top-video-timeline") {
    require("portfolio/top-video-timeline/top-video-timeline.php");
  }
  else {
  
  ?>

  <div class="col-md-9 main">
    <div class="main-project-first">
      <a href="?portfolio=everyvote&item=2014-02-09-Home-Page" class="color-text color-everyvote-hover">EveryVote <i class="fa fa-check-square-o main-project-icon"></i></a>
    </div>
    
    <div class="main-project color-partystarter-hover">
      PartyStarter <i class="fa fa-group main-project-icon"></i> 
    </div>
    
    <div class="main-project color-earthhq-hover">
      EarthHQ <i class="fa fa-globe main-project-icon"></i>
    </div>
    
    <div class="main-project color-advantage-act-hover">
      Advantage ACT <i class="fa fa-book main-project-icon"></i>
    </div>
    
    <div class="main-project color-top-video-timeline-hover">
      Top Video Timeline <i class="fa fa-film main-project-icon"></i>
    </div>
    
    <div class="clearfix">
    </div>
    
  </div><!-- /.col-md-9 main  -->

  <div class="col-md-3 sidebar"><br />
    
    <div class="sidebar-title">
      <span style="color:#B56400">UX Design</span>
    </div>
    
    <div class="sidebar-text">
      Axure, Fireworks, Illustrator, Prototypes, Wireframes, HCI, Competitive Analysis, Site Maps, Personas, Usability Testing, Responsive Design, Mobile Design
    </div><br />
    
    <div class="sidebar-title">
      <span style="color:#006B8E;">Web Development</span>
    </div>
    
    <div class="sidebar-text">
      HTML/CSS, Javascript, jQuery, Bootstrap, Python, Django, PHP, MySQL, Git
    </div><br />
    
    <div class="sidebar-title">
      <span style="color:#D54040;">Education</span>
    </div>
    
    <div class="sidebar-text">
      Northern Illinois University
    </div>
    
    <div class="sidebar-subtext">
      M.S.Ed. Instructional Technology
    </div>
    
    <div class="sidebar-text">
      University of Illinois
    </div>
    
    <div class="sidebar-subtext">
      B.A. English & Philosophy
    </div><br />
    
    <div class="sidebar-title">
      <span style="color:#6C9F20;">Specialities</span>
    </div>
    
    <div class="sidebar-text">
      Educational Software<br />
      Free/Open Source Software<br />
      Productivity Software<br />
      Social Networks
    </div><br />
      
  </div><!-- /.col-md-3 side-bar -->
  
  <?php
  
  }

  ?>

  <?php include 'footer.php'; ?>
  
</div><!-- /.container -->

</body>