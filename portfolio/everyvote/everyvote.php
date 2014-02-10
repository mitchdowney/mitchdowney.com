<?php

if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Home-Page") {
  require("2014-02-09-Home-Page.php");
}
if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-About-Page") {
  require("2014-02-09-About-Page.php");
}
if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Calendar-Page") {
  require("2014-02-09-Calendar-Page.php");
}
if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Debate-Page") {
  require("2014-02-09-Debate-Page.php");
}
if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Election-Page") {
  require("2014-02-09-Election-Page.php");
}
if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Groups-Page") {
  require("2014-02-09-Groups-Page.php");
}

?>

<div class="col-md-3 sidebar">
  
  <div class="sidebar-headline">
    Archive
  </div>
  
  <div class="sidebar-title">
    February 2014
  </div>
  
  <div class="sidebar-text">
    <ul>
      <li><a href="?portfolio=everyvote&item=2014-02-09-Home-Page"
        <?php
        if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Home-Page") {
            echo 'class="highlight"';
          }
        ?>
      >Home Page</a></li>
      <li><a href="?portfolio=everyvote&item=2014-02-09-About-Page"
        <?php
        if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-About-Page") {
            echo 'class="highlight"';
          }
        ?>
      >About Page</a></li>
      <li><a href="?portfolio=everyvote&item=2014-02-09-Calendar-Page"
        <?php
        if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Calendar-Page") {
            echo 'class="highlight"';
          }
        ?>
      >Calendar Page</a></li>
      <li><a href="?portfolio=everyvote&item=2014-02-09-Debate-Page"
        <?php
        if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Debate-Page") {
            echo 'class="highlight"';
          }
        ?>
      >Debate Page</a></li>
      <li><a href="?portfolio=everyvote&item=2014-02-09-Election-Page"
        <?php
        if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Election-Page") {
            echo 'class="highlight"';
        }
        ?>
      >Election Page</a></li>
      <li><a href="?portfolio=everyvote&item=2014-02-09-Groups-Page"
        <?php
        if ($_GET['portfolio'] == "everyvote" && $_GET['item'] == "2014-02-09-Groups-Page") {
            echo 'class="highlight"';
        }
        ?>
      >Groups Page</a></li>
    </ul>
  </div>

</div><!-- /.col-md-3 sidebar pull-left -->