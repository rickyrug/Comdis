console.log("any")
$(document).ready(function(){

    $("#productsList").DataTable({
        "dom": '<"toolbar"><"top"f>rt<"bottom"lpi><"clear">', // ordena los elementos de la tabla y se agrega un div Toolbar para agregar un boton.
        "processing": true,
        data : dataset,
        select: true,
        "columns":[
            {
                "title":"Actions",
                "render":function(data,type,row,meta)
                {
                    
                    data =   '<a href="'+url_upsert+'/'+row.pk+'" class="mr-1">Edit</a>'
                           + '<a href="'+url_delete+'/'+row.pk+'">Delete</a>' 
                    return data;
                }

            },
            { 
                "title":"Id",
                "data": "pk" 
            
            },
            { 
                "title":"Name",
                "data": "fields.Name" 
            
            },
            { 
                "title":"Created",
                "data": "fields.Created" 
            
            },
            { 
                "title":"Created By",
                "data": "fields.CreatedBy" 
            
            },
            { 
                "title":"Updated",
                "data": "fields.Created" 
            
            },
            { 
                "title":"Created By",
                "data": "fields.CreatedBy" 
            
            },
        ]

    });

    $("div.toolbar").html('<a href="'+url_upsert+'" class="btn btn-primary" id="btnAddProduct">+</a>');  //se agrega boton de ++



});