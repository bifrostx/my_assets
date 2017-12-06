jQuery(function(){
    var counter = 1;
    jQuery('#add-token').click(function(event){
        event.preventDefault();

        var newRow = jQuery('<label for="id_tokenname">货币名称:</label><input type="text" name="name" class="form-control" id="id_tokenname"/><label for="id_tokenamount">数量:</label><input type="text" name="amount" class="form-control" id="id_tokenamount"/><button type="submit" class="btn btn-primary" name="submit">添加</button>');
            counter++;
        jQuery('#token_form').append(newRow);
    });
});