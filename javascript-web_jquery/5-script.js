<script>
  $(document).ready(function () {
    $("#add_item").click(function () {
      var newList = $("<li>Item</li>")
        $("UL.my_list").append(newList)
    })
  })
</script>
