(function () {
	var partialsCache = {};

	function fetchFile (path, callback) {
		var xhr = new XMLHttpRequest();
		// xhr.onload = function () {
		// 	callback(request.responseText);
		// }
		xhr.onreadystatechange = function () {
			if (xhr.readyState == 4 && xhr.status == 200) {
				callback(xhr.responseText);
			}
		}
		xhr.open("GET", path);
		xhr.setRequestHeader("Access-Control-Allow-Origin", "*")
		xhr.send(null);
	}

	function getContent (fragmentId, callback) {
		if (partialsCache[fragmentId]) {
			callback(partialsCache[fragmentId]);
		} else {
			fetchFile(fragmentId, function (content) {
				partialsCache[fragmentId] = content;

				callback(content);
			});
		}
	}

	function setActiveLink(fragmentId) {
		var el = document.getElementsByClassName("navbar")[0];
		var links = el.getElementsByTagName("a");

		for(var i=0,len=links.length; i<len; i++) {
			var link = links[i];
			var pageName = link.getAttribute("href").substr(1);
			console.log(pageName, fragmentId)
			if(pageName === fragmentId) {
				
				link.setAttribute("class", "active");
			} else {
				link.removeAttribute("class");
			}
		}
	}

	function navigate () {
		var app = document.getElementById("app");

		fragmentId = location.hash.substr(1)

		getContent(fragmentId, function (content) {
			app.innerHTML = content;
			setActiveLink(fragmentId);
		});
	}


	// Navigate once to the initial hash value.
	// navigate();


	window.addEventListener("hashchange", function () {
		// var app = document.getElementById("app");
		// app.innerHTML = location.hash;
		navigate();
	});

}());
