
---
title: 'WijmoJS 前端开发工具包发布更新，加入可视化地图组件'
categories: 
 - 编程
 - 开源中国
 - — 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-44771bb11b71747c85ec7ccb688102044a3.png'
author: 开源中国
comments: false
date: Tue, 23 Mar 2021 11:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-44771bb11b71747c85ec7ccb688102044a3.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align: justify;">WijmoJS 是葡萄城推出的一款前端开发工具包，由 80 多款基于 HTML5、支持跨平台的高性能 UI 组件（如表格组件、图表组件、数据分析组件、导航组件和金融图表组件等）构成，完美兼容原生 JavaScript，支持 Angular、React、Vue 等前端框架，用于企业级 Web 应用程序的快速开发和构建。</p> 
<p style="text-align:justify">近日，WijmoJS V2021.0 Update1正式发布，本次更新加入了一款同时兼容Angular、React和Vue的可视化地图组件，以及用于绑定REST API 的数据管理组件RestCollectionView。</p> 
<p style="text-align:justify">在为您列举 WijmoJS的更新内容之前，请前往<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.grapecity.com.cn%2Fdeveloper%2Fwijmojs" target="_blank">WijmoJS产品官网</a>下载安装包，以便同步体验。</p> 
<p style="text-align:justify"> </p> 
<p style="text-align:justify">前端开发工具包 WijmoJS V2021.0 Update1 新特性一览：</p> 
<h2 style="text-align:justify">加入同时兼容Angular、React和Vue的可视化地图组件</h2> 
<p style="text-align:justify">WijmoJS 在本次更新中，加入了一款用于地理数据可视化展示的地图组件FlexMap，该组件可以使您的地理数据栩栩如生，并变得更易于分析。目前， FlexMap组件还处于测试阶段，后续会持续优化并添加一些地图包（区域地图文件）。</p> 
<p style="text-align:justify">FlexMap组件功能支持渲染色度和为地图添加标注点，如散点图和气泡图，组件使用GeoJSON绑定地理要素图层和点图层（建议将NaturalEarthData用作GeoJSON数据的源，并根据需要自定义MapShaper）。</p> 
<p style="text-align:justify"> </p> 
<p style="text-align:justify">如下是FlexMap组件的部分使用场景：</p> 
<h3 style="text-align:justify">1. 在JavaScript、Angular、React和Vue中创建分级统计地图</h3> 
<p style="text-align:justify">借助FlexMap，只需几行代码就可以轻松创建分级统计地图。分级统计地图用于显示地理区域的统计值，每个区域都会根据其表示的数据进行着色。</p> 
<p style="text-align:justify"><img height="395" src="https://oscimg.oschina.net/oscnet/up-44771bb11b71747c85ec7ccb688102044a3.png" width="595" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:justify">2. 在JavaScript、Angular、React和Vue中创建散点图</h3> 
<p style="text-align:justify">FlexMap支持为地图添加兴趣点，以及创建散点图。散点图用于显示地图上特定坐标处的兴趣点。</p> 
<p style="text-align:justify"><img height="380" src="https://oscimg.oschina.net/oscnet/up-b6972939a2305191481179e7a9f99f96293.png" width="587" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:justify">3. 在JavaScript、Angular、React和Vue中创建气泡地图</h3> 
<p style="text-align:justify">FlexMap可用于创建气泡地图。气泡图在地图上显示的气泡大小取决于数据的值（较大的值=较大的气泡）。</p> 
<p style="text-align:justify"><img height="393" src="https://oscimg.oschina.net/oscnet/up-eef7e2ec597df7b96bd5c36340edc7ec70c.png" width="590" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:justify">新的图表动态调色板</h2> 
<p style="text-align:justify">WijmoJS 的第二个新功能是图表动态调色板，用于在地图和图表中创建漂亮的分级统计地图。</p> 
<p style="text-align:justify"><img height="413" src="https://oscimg.oschina.net/oscnet/up-7115c953698df6d12966aa24056b79d8a05.png" width="692" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify">调色板的配色方案参考了专业配色网站，包括以下几种：</p> 
<ul> 
 <li style="text-align:justify"><strong>顺序（</strong><strong>SequentialSingle和SequentialMulti）</strong> ：按颜色深浅显示数据从低到高的顺序，从低值到高值依次以深色到浅色表示。</li> 
 <li style="text-align:justify"><strong>发散</strong>：两端为深色，中端为浅色，浅色表示中间值，深色代表极低值和极高值。</li> 
 <li style="text-align:justify"><strong>定性</strong>：最适合显示名义或分类数据。颜色不表示值的差异。</li> 
</ul> 
<p style="text-align:justify">利用这些新的调色板可以创建非常美观的图表。</p> 
<p style="text-align:justify"><img height="444" src="https://oscimg.oschina.net/oscnet/up-20babb293ad4446d1b14b087dc773b3a7a6.png" width="820" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify"> </p> 
<h2 style="text-align:justify">用于绑定REST API的RestCollectionView组件</h2> 
<p style="text-align:justify">WijmoJS 的第三个新功能是一款RestCollectionView组件，该组件用于绑定REST API。</p> 
<p style="text-align:justify">在默认情况下，排序、分页和筛选是在服务器上完成的，但是借助WijmoJS ，便可以在客户端上更改其中的任何设置，将自定义的RestCollectionView绑定到WijmoJS组件中，便可自动调用服务器以执行CRUD操作。</p> 
<p style="text-align:justify"> </p> 
<p style="text-align:justify"><img height="293" src="https://oscimg.oschina.net/oscnet/up-8261bff27afb671bbe2a37d6c5e5ad10567.png" width="619" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify">要使用这个组件，您只需创建一个扩展RestCollectionView并重写以下方法：</p> 
<ul> 
 <li style="text-align:justify"><strong>getItems</strong>：从服务器获取项目列表。该列表可以被排序，过滤和分页。</li> 
 <li style="text-align:justify"><strong>addItem</strong>：将一个项目添加到服务器上的集合中。</li> 
 <li style="text-align:justify"><strong>patchItem</strong>：在服务器上编辑集合中的项目。</li> 
 <li style="text-align:justify"><strong>deleteItem</strong>：从服务器上的集合中删除一个项目。</li> 
</ul> 
<p style="text-align:justify"> </p> 
<h2 style="text-align:justify">可用于Angular、React和Vue的MultiRow单元格模板</h2> 
<p style="text-align:justify">WijmoJS 的最后一个新功能是可用于Angular、React和Vue的单元格模板，使用该模板来标记定义MultiRow单元格中的自定义内容。单元格模板支持绑定语法、嵌套组件、自定义HTML和条件逻辑。</p> 
<p style="text-align:justify"><img height="359" src="https://oscimg.oschina.net/oscnet/up-a41846b303393204be3362ee26c8ec07ed0.png" width="607" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify"> </p> 
<p style="text-align:justify"><span style="background-color:white"><span style="color:#555555">以上就是</span></span>前端开发工具包 WijmoJS V2021.0 Update1<span style="background-color:white"><span style="color:#555555">的更新内容，如需了解详细信息，欢迎访问</span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.grapecity.com.cn%2Fdeveloper%2Fwijmojs" target="_blank"><span style="background-color:white"><span style="color:#2676c0">WijmoJS  产品官网</span></span></a><span style="background-color:white"><span style="color:#555555">。</span></span></p>
                                        </div>
                                      
</div>
            