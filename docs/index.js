(function() {
  function showTable() {
    console.log("show table.");
    // specify the columns
    var columnDefs = [
      { headerName: "序號", field: "序號", sortable: true },
      { headerName: "國別地區", field: "國別地區", sortable: true },
      { headerName: "中文片名", field: "中文片名" },
      { headerName: "上映日期", field: "上映日期", sortable: true },
      { headerName: "申請人", field: "申請人", sortable: true },
      { headerName: "出品", field: "出品", sortable: true },
      { headerName: "上映院數", field: "上映院數", sortable: true },
      { headerName: "銷售票數", field: "銷售票數", sortable: true },
      { headerName: "銷售金額", field: "銷售金額", sortable: true },
      { headerName: "累計銷售票數", field: "累計銷售票數", sortable: true },
      { headerName: "累計銷售金額", field: "累計銷售金額", sortable: true }
    ];

    // let the grid know which columns to use
    var gridOptions = {
      columnDefs: columnDefs
    };

    // lookup the container we want the Grid to use
    var eGridDiv = document.querySelector("#myGrid");

    // create the grid passing in the div to use together with the columns & data we want to use
    new agGrid.Grid(eGridDiv, gridOptions);

    fetch(
      "https://phate334.github.io/box-office-tw/json/20180730-20180805.json"
    )
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        gridOptions.api.setRowData(data);
      });
  }

  showTable();
})();
