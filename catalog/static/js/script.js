function goToHotel(hotelId){
window.location.href = "/room/" + hotelId +"/";
}

function goToHotel(hotelId){
window.location.href = "/room/" + hotelId +"/";
}

function toggleCheckboxes(checkbox) {
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  var hiddenField = document.getElementById('room');

  checkboxes.forEach(function(cb) {
    if (cb !== checkbox) {
      cb.checked = false;
    } else {
      hiddenField.value = checkbox.id;
    }
  });
}