(function() {
  var indexMeta = {
    url: './json/index.json',
  };
  var columnMeta = {
    url: './column-defines.json',
  };
  var dataGridDiv = document.querySelector('#data-grid');
  var dataId = document.querySelector('#data-id');
  var gridOptions;

  function loadMeta(meta) {
    return new Promise(function(resolve) {
      var request = new XMLHttpRequest();
      request.open('GET', meta.url);
      request.responseType = 'json';
      request.onload = function() {
        if (request.status === 200) {
          meta.json = request.response;
          resolve();
        }
      };
      request.send();
    });
  }

  var getIndex = loadMeta(indexMeta);
  var getColDefs = loadMeta(columnMeta);

  Promise.all([getIndex, getColDefs]).then(function() {
    indexMeta.json.sort().reverse();
    initPage();
  });

  function initPage() {
    console.log('init table.');
    gridOptions = {
      defaultColDef: {
        resizable: true,
        rowSelection: 'single',
        editable: true,
      },
      animateRows: true,
      columnDefs: columnMeta.json,
    };
    new agGrid.Grid(dataGridDiv, gridOptions);
    updateTable(indexMeta.json[0]);
  }

  function updateTable(name) {
    fetch(toDataURL(name))
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        gridOptions.api.setRowData(data);
        dataId.innerHTML = name;
      });
  }

  function toDataURL(name) {
    return './json/' + name + '.json';
  }
})();
