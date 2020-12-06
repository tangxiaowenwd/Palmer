

$('#tb_departments').bootstrapTable({
  url: '/dataAjax/2',
  type:'json',
  pagination:true,
  search:true,
  columns: [{
    field: 'ts_code',
    title: 'Ts_code'
  }, {
    field: 'name',
    title: 'Name'
  }, {
    field: 'price',
    title: 'Price'
  }],
});



// var hidde = ['due_date', 'list_date', 'issue_date', 'delist_date','exp_return', 'status',  'trustee', 'purc_startdate', 'redm_startdate', 'market'];
//
// // for (var i in hidde){
// // 	var bodys = document.getElementsByClassName(i);
// // 	for (var s in bodys.length){
// // 		console.log(bodys[s]);
// // 		bodys[s].setAttribute("style", "block:none");
// // 	}
// //
// // }
//
// function Mores(num) {
// 	$.ajax({
// 		type: 'post',                            // 传数据的方式
// 		url: '/dataAjax/'+num,
// 		error: function (xhr, err) {
// 			alert(err);
// 		},
// 		success: function (data) {    // success对应的回调函数的第一个参数，是服务器返回的数据
// 			if (data) {
// 				data = eval('(' + data + ')');
// 				for (var i in data) {
// 					var para = document.createElement("tr");
// 					for (var s in data[i]){
// 						var pard = document.createElement("td");
// 						pard.className = s;
// 						var node = document.createTextNode(data[i][s]);
// 						pard.appendChild(node);
// 						para.appendChild(pard);
// 					}
// 					var tobly = document.getElementsByClassName("zeng")[0];
// 					tobly.appendChild(para);
// 				}
//
// 			}
// 		}
// 	})
// }
//
// var totalHeight = $(document).height(); //整个文档高度
// var seeHeight = $(window).height(); //浏览器可视窗口高度
// var scrollTop = $(window).scrollTop(); //浏览器可视窗口顶端距离网页顶端的高度
//
//
// //添加滚动事件
// $(window).scroll(function() {
// 	scrollTop = $(window).scrollTop();
// 	totalHeight = $(document).height();
// 	var counts = document.getElementById("zeng").childElementCount;
// 	var num = counts/20;
// 	// console.log(scrollTop, seeHeight, totalHeight);
// 	//滚动条+可视高度+50，距离文档高度差50的时候就要加载数据了
// 	if(scrollTop + seeHeight + 50 > totalHeight) {
// 		Mores(num);
// 		for (var i in hidde){
// 			console.log(typeof(i));
// 			console.log(hidde[i]);
// 		}
// 	}
// });
