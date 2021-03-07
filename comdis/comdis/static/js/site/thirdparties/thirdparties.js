$(document).ready(function(){

    $("#clientsList").DataTable({
        "dom": '<"toolbarCli"><"top"f>rt<"bottom"lpi><"clear">', // ordena los elementos de la tabla y se agrega un div Toolbar para agregar un boton.
        "processing": true,
        data : datasetClients,
        select: true,
        "columns":[
            {
                "title":"Actions",
                "render":function(data,type,row,meta)
                {
                    
                    data =   '<a href="'+url_upsertClient+'/'+row.pk+'" class="mr-1">Edit</a>'
                           + '<a href="'+url_deleteClient+'/'+row.pk+'">Delete</a>' 
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

    $("#suppliersList").DataTable({
        "dom": '<"toolbarSup"><"top"f>rt<"bottom"lpi><"clear">', // ordena los elementos de la tabla y se agrega un div Toolbar para agregar un boton.
        "processing": true,
        data : datasetSuppliers,
        select: true,
        "columns":[
            {
                "title":"Actions",
                "render":function(data,type,row,meta)
                {
                    
                    data =   '<a href="'+url_upsertSupplier+'/'+row.pk+'" class="mr-1">Edit</a>'
                           + '<a href="'+url_deleteSupplier+'/'+row.pk+'">Delete</a>' 
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

    $("div.toolbarCli").html('<a href="'+url_upsertClient+'" class="btn btn-primary" id="btnAddProduct">+</a>');  //se agrega boton del cliente ++
    $("div.toolbarSup").html('<a href="'+url_upsertSupplier+'" class="btn btn-primary" id="btnAddProduct">+</a>');  //se agrega boton del del proveedor ++

});