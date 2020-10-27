$(document).ready(function(){
      $('#submitbutton').attr("disabled", true);
      $("#fg2").hide();
      $("#fg3").hide();
      $("#fg4").hide();
      $("#fg5").hide();

      $("#itemtype").change(function(){
        $("#fg2").show();
        $('[name="source[]"]').prop("checked", false);
        $('#mainstat').val("");
        $('[name="offstat[]"]').prop("checked", false);
        $("#fg3").hide();
        $("#fg4").hide();
        $('#spec').val("");
        $("#fg5").hide();
        $('#submitbutton').attr("disabled", true);
        });

      $('[name="source[]"]').change(function(){

        if ($("#itemtype").val()=='Cloth' || $("#itemtype").val()=='Leather' || $("#itemtype").val()=='Mail'|| $("#itemtype").val()=='Plate')
          $("#fg3").show();
        if ($("#itemtype").val()=='Neck/Ring')
          $("#fg4").show();
        if ($("#itemtype").val()=='Trinket')
          $("#fg5").show();
        if (!$('#raid').is(":checked") && !$('#dungeon').is(":checked")){
          $('#mainstat').val("");
          $('[name="offstat[]"]').prop("checked", false);
          $("#fg3").hide();
          $("#fg4").hide();
          $("#fg5").hide();
          $('#submitbutton').attr("disabled", true);
        }
        });

      $("#mainstat").change(function(){
        $("#fg4").show();
        $("#fg5").hide();
        $('#submitbutton').attr("disabled", true);
        });

      $('[name="offstat[]"]').change(function(){
        var checkedBoxes = $("input[type=checkbox]:checked", "#fg4");
        var uncheckedBoxes = $("input[type=checkbox]:not(:checked)","#fg4")
        if (checkedBoxes.length==2){
          $('#submitbutton').attr("disabled", false);
          for ( var i = 0, l = uncheckedBoxes.length; i < l; i++ ) {
            uncheckedBoxes[i].disabled = true;
          }
        }else{
          $('#submitbutton').attr("disabled", true);
          for ( var i = 0, l = uncheckedBoxes.length; i < l; i++ ) {
            uncheckedBoxes[i].disabled = false;
          }
        }
        });

      $('#spec').change(function(){
        if ($("#spec").val()==''){
          $('#submitbutton').attr("disabled", true);
        }else{
          $('#submitbutton').attr("disabled", false);
        }
        });

  });