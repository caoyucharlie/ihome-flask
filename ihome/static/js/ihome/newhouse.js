function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
   $.get('/house/areafacility', function (data) {
       var area_html_list = ''
       for (var i=0; i<data.area_list.length; i++){
           var area_html = '<option value="' +data.area_list[i].id +'">' + data.area_list[i].name + '</option>'

           area_html_list += area_html

       }

       $('#area-id').html(area_html_list)



       var facility_html_list = ''
       for (var i=0; i<data.facility_list.length; i++){
           var facility_html = '<li><div class="checkbox"><label>'
           facility_html += '<input type="checkbox" name="facility" value="' + data.facility_list[i].id + '">' + data.facility_list[i].name +'</label>'
           facility_html += '</div></li>'
           facility_html_list += facility_html
       }
       $('.house-facility-list').html(facility_html_list)
   })
})


