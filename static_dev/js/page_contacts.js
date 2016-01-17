var ContactPage = function () {

    return {
        
    	//Basic Map
        initMap: function () {
			var map;
			$(document).ready(function(){
			  map = new GMaps({
				div: '#map',
				scrollwheel: false,				
				lat: 37.562256,
				lng: 126.935244
			  });
			  
			  var marker = map.addMarker({
				lat: 37.562256,
				lng: 126.935244,
	            title: 'EEL'
		       });
			});
        },

        //Panorama Map
  //       initPanorama: function () {
		//     var panorama;
		//     $(document).ready(function(){
		//       panorama = GMaps.createPanorama({
		//         el: '#panorama',
		//         lat : 40.748866,
		//         lng : -73.988366
		//       });
		//     });
		// }        

    };
}();