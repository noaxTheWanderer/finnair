$( document ).ready(function() {
	return;
    list_trips();
});

function list_trips() {
	$.ajax({
		url: "/api",
		data: {"query": "trips"},
		success: update_listing,
		dataType: "json"
	});
}

function showMore(event){
	var footer = $(event.target).parent().find(".card-footer");
	console.log(footer);
	footer.css("display", "block");
	console.log("triggered");
}

function update_listing(data){
	var container = $(".row")[0];
	var html = "";
	for (var i = 0; i < data.length; i++) {
		var item = data[i];
		html = html +"<div class='col-lg-4 col-sm-6 portfolio-item'><div class='card h-100'><a href='#'><img class='card-img-top' src='"+ item["image"] +"'></a>";
		html = html + '<div class="card-body"><h4 class="card-title"><a href="#">'+item["name"]+'</a></h4><h5>'+ item["tagline"] +'</h5>';
		html = html + "<p>" + item["flight-time"]+ "</p>";
		html = html + '<button type="button" onclick="showMore(event)" class="btn btn-secondary">...</button><button type="button" class="btn btn-success">From '+ item["price"]+'</button>';
		html = html + '<div class="card-footer text-muted" style="display: none;">' + item["description"] + "</div>";
		html = html + "</div></div></div>";
		
	}
	$(container).html(html);
	console.log(data);
}