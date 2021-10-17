let map;

      function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
          center: new google.maps.LatLng(19.178868, 72.9584198),
          zoom: 17,
        });
        const iconBase =
          "assets/img/icons/";
        const icons = {
          important: {
            icon: iconBase + "important.png",
          },
          active: {
            icon: iconBase + "active.png",
          },
          homebase: {
            icon: iconBase + "homebase.png",
          },
        };
        const features = [
          {
            position: new google.maps.LatLng(19.178868, 72.9584198),
            type: "active",
          },
          {
            position: new google.maps.LatLng(19.180145, 72.960469),
            type: "active",
          },
          {
            position: new google.maps.LatLng(19.177486, 72.957403),
            type: "homebase",
          },
          {
            position: new google.maps.LatLng(19.177952, 72.954753),
            type: "important",
          },
          {
            position: new google.maps.LatLng(19.176077, 72.957253),
            type: "important",
          },
          {
            position: new google.maps.LatLng(19.180293, 72.956931),
            type: "active",
          },
          {
            position: new google.maps.LatLng(19.178783, 72.962467),
            type: "important",
          },
        ];

        // Create markers.
        for (let i = 0; i < features.length; i++) {
          const marker = new google.maps.Marker({
            position: features[i].position,
            icon: icons[features[i].type].icon,
            map: map,
          });
        }
      }

//   Hide and show div
$(document).ready(function () {
  $("#flip").click(function () {
    $("#panel").slideToggle("slow");
  });
});

// Search
  $(document).ready(function(){
            var submitIcon = $('.searchbox-icon');
            var inputBox = $('.searchbox-input');
            var searchBox = $('.searchbox');
            var isOpen = false;
            submitIcon.click(function(){
                if(isOpen == false){
                    searchBox.addClass('searchbox-open');
                    inputBox.focus();
                    isOpen = true;
                } else {
                    searchBox.removeClass('searchbox-open');
                    inputBox.focusout();
                    isOpen = false;
                }
            });  
             submitIcon.mouseup(function(){
                    return false;
                });
            searchBox.mouseup(function(){
                    return false;
                });
            $(document).mouseup(function(){
                    if(isOpen == true){
                        $('.searchbox-icon').css('display','block');
                        submitIcon.click();
                    }
                });
        });
            function buttonUp(){
                var inputVal = $('.searchbox-input').val();
                inputVal = $.trim(inputVal).length;
                if( inputVal !== 0){
                    $('.searchbox-icon').css('display','none');
                } else {
                    $('.searchbox-input').val('');
                    $('.searchbox-icon').css('display','block');
                }
            }