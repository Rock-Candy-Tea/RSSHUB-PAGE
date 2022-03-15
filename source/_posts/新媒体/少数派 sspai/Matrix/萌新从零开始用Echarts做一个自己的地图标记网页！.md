
---
title: '萌新从零开始用Echarts做一个自己的地图标记网页！'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2022/03/12/article/37364a7641e904a8b51250823e068358?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Sat, 12 Mar 2022 03:49:49 GMT
thumbnail: 'https://cdn.sspai.com/2022/03/12/article/37364a7641e904a8b51250823e068358?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-0b37afcb><div class="update-wrap" data-v-0b37afcb></div><div class="content wangEditor-txt minHeight" data-v-0b37afcb><p>那是一个风和日丽的夜晚，我可爱的老婆大人突然跟我说她最近制作一份 PPT 的时候需要进行地图标记，但是原先她使用的网站失效了，问我有没有什么地图标记的好办法，最好能按照她的要求进行一定的定制。我想了想，要不直接再给我老婆做一个网页算了，虽然我已经很久没练过HTML，CSS和JavaScript了，但好歹之前接触过点皮毛，要不趁这次机会再试一次？</p><h2>准备工作</h2><p>说干就干，反正电脑上本身就装了<a href="https://code.visualstudio.com/">VSCode</a>，那么直接写个静态的HTML文件应该就能搞定。至于制作地图的方案么，想到前段时间分析数据的时候用过pyecharts进行制表，这次索性直接用Echarts进行做个试试。由于之前从来没用过Echarts，所以先上<a href="https://echarts.apache.org/zh/index.html">官网</a>看看<a href="https://echarts.apache.org/handbook/zh/get-started/">上手教程</a>和<a href="https://echarts.apache.org/examples/zh/editor.html?c=map-HK">地图案例</a>。</p><p>按照[上手教程](<a href="https://echarts.apache.org/handbook/zh/get-started/">Handbook - Apache ECharts</a>),先把<a href="https://www.jsdelivr.com/package/npm/echarts">echarts.js</a>文件下载下来，然后根据<a href="https://echarts.apache.org/examples/zh/editor.html?c=map-HK">地图案例</a>还需要下载<a href="https://www.jsdelivr.com/package/npm/jquery">jquery.js</a>。这两个依赖下载完成后就能开始编写HTML文件了。</p><h2>撸代码</h2><h3>创建空白模板</h3><p>在echarts.js和jquery.js文件的同目录下创建一个名为index.html的空白文件（反正需求简单，一个静态网页搞定一切）。VSCode编辑时，直接输入「！」</p><p>回车后，一个空白的HTML文件模板就完成了。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/12/article/37364a7641e904a8b51250823e068358?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/2022/03/12/article/37364a7641e904a8b51250823e068358" referrerpolicy="no-referrer"></figure><h3>引入外部js文件并创建视图容器</h3><p>在头部文件中添加echarts.js和jquery.js</p><pre class="language-htmlembedded"><code><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="echarts.min.js"></script>
    <script src="jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    <!--style中定义视图的长宽尺寸-->
    <div id="main" style="width: 1600px;height:1200px;"></div>
    <!--生成地图的主代码文件-->
    <script type="text/javascript">
        ……
        ……
        ……
    </script>
</body>
</html></code></pre><h3>参考案例画出中国地图</h3><p>根据官网上的<a href="https://echarts.apache.org/zh/option.html#title">文档</a>，及其他百度到的案例，利用阿里云的<a href="http://datav.aliyun.com/portal/school/atlas/area_selector">geoJson</a>作为绘制中国地图的数据源</p><pre class="language-htmlembedded"><code><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="echarts.min.js"></script>
    <script src="jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    <!--style中定义视图的长宽尺寸-->
    <div id="main" style="width: 1600px;height:1200px;"></div>
    <script type="text/javascript">
      // 初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));
      myChart.showLoading();
$.get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json', function (geoJson) 
      &#123;
       myChart.hideLoading();
       echarts.registerMap('china', geoJson);
       myChart.setOption(
         option = &#123;
             title: &#123;
             text: '中国地图'
             &#125;,
             geo: &#123;
                 name: '中国地图',
                 type: 'map',
                 map: 'china',
                &#125;
            &#125;
       )
    &#125;)
    </script>
</body>
</html></code></pre><p>这样一个最简单的中国地图网页就已经完成了，而且在鼠标移动到不同区域的时候能够高亮并显示省名。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/12/article/74a43fb78919254452e9d6e570b7f4e7?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/2022/03/12/article/74a43fb78919254452e9d6e570b7f4e7" referrerpolicy="no-referrer"></figure><h3>定制属于自己的地图标记</h3><p>查阅了很多他人写的案例，但最终发现只有<a href="https://echarts.apache.org/zh/option.html#title">官方文档</a>最有用。因为Echarts就像是一件功能丰富的工具，而官方的文档就是这件工具具体的使用手册，涵盖了这个工具所有的功能。只要你像查字典一样学会了查询官方文档，那么就能将地图按你心目中想象地样子进行定制。</p><p>比如想用鼠标可以选中多个中国地图中的区域，而不是只能置于其上时高亮。那么就需要先看看geo这个类有哪些方法可以被使用。</p><p>在文档中搜索geo后，下图中红框圈出的就是geo具有属性和方法</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/12/article/5af5fbfabc4aa96246956b2dbf9ec800?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/2022/03/12/article/5af5fbfabc4aa96246956b2dbf9ec800" referrerpolicy="no-referrer"></figure><p>而我们需要的就是「selectMode」这个方法，根据查询到的手册，这一栏我们可以填写布尔值或是'single','multiple'的。那么我们只要将「selectMode」添加到「geo」类中，并输入'multiple'，就能开启鼠标选中地图中的区域的功能。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/12/article/8b28242b56f1d55d448d54a81c0119d2?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/2022/03/12/article/8b28242b56f1d55d448d54a81c0119d2" referrerpolicy="no-referrer"></figure><pre class="language-htmlembedded"><code>    <script type="text/javascript">
      // 初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));
      myChart.showLoading();
$.get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json', function (geoJson) 
      &#123;
       ……
             geo: &#123;
                 name: '中国地图',
                 type: 'map',
                 map: 'china',
                 selectedMode: 'multiple',
                &#125;
        ……
    &#125;)
    </script></code></pre><p>同理，如果我们想要添加标记的散点，那么除了绘制geo地图外，还要在此图层上添加一层散点图。我们查看一下「setOption」中「series」属性具有的选项。在这些选项中，很快我们就能发现「scatter」就是我们要的散点。于是和「geo」一样，我们将「scatter」添加进「setOption」中，并采用「geo」的坐标系。</p><pre class="language-htmlembedded"><code>    <script type="text/javascript">
      // 初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));
      myChart.showLoading();
$.get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json', function (geoJson) 
      &#123;
       ……
             geo: &#123;
                 name: '中国地图',
                 type: 'map',
                 map: 'china',
                 selectedMode: 'multiple',
              &#125;,
              series: &#123;
                  name: '标记点',
                  type: 'scatter',
                  coordinateSystem: 'geo',
              &#125;
        ……
    &#125;)
    </script></code></pre><p>完成到这里，打开index.html文件，你会发现地图上并没有任何标记点。这当然是因为——你没告诉它点在哪里，那它当然就啥也不给你标出来！所以和上面的步骤一样，我们查询官方文档中scatter.data，并在散点图上给一个标记点。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/12/article/047bdd7962e0bae1dcbcf5e2edf46dfb?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/2022/03/12/article/047bdd7962e0bae1dcbcf5e2edf46dfb" referrerpolicy="no-referrer"></figure><p>既然是中国地图，那么以广东省广州市为例，我们查询一下广州市的经纬坐标值，将数据填写进scatter，并将「label」的「show」属性设置为 true ，格式化「label」的显示格式和放在标记点左边显示（都是查官方文档查的），这样再次打开地图就能看到标记点了。</p><pre class="language-htmlembedded"><code>    <script type="text/javascript">
      // 初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));
      myChart.showLoading();
$.get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json', function (geoJson) 
      &#123;
       ……
             geo: &#123;
                 name: '中国地图',
                 type: 'map',
                 map: 'china',
                 selectedMode: 'multiple',
              &#125;,
              series: &#123;
                  name: '标记点',
                  type: 'scatter',
                  coordinateSystem: 'geo',
                  data: &#123;name: 'Guangzhou', value:[113.23333,23.16667]&#125;,
                  label:&#123;
                    formatter: '&#123;b&#125;',
                    show: true,
                    position: 'right',
                  &#125;,
              &#125;
        ……
    &#125;)
    </script></code></pre><h2>总结</h2><p>“授人以鱼不如授人以渔”。只要按照上面「根据需求」->「<a href="https://echarts.apache.org/zh/option.html#title">查官方文档</a>」->「将查到属性或方法放入加进源代码」的逻辑，那么就能完全定制出自己想要的一个地图标记网页。如果你也是个爱折腾的人，不妨也试试看做一个属于自己的地图标记网页。（最后把这篇文章做的示例放在结尾，并且把echarts.js和jquery.js改成从网站获取，有需要的人可以拷走直接看成果）</p><pre class="language-htmlembedded"><code><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.3.1/dist/echarts.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
    <title>地图Demo</title>
</head>
<body>
    <!--style中定义视图的长宽尺寸-->
    <div id="main" style="width: 1600px;height:1200px;"></div>
    <script type="text/javascript">
      // 初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));
      myChart.showLoading();
$.get('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json', function (geoJson) 
      &#123;
       myChart.hideLoading();
       echarts.registerMap('china', geoJson);
       myChart.setOption(
         option = &#123;
             title: &#123;
             text: '中国地图'
             &#125;,
             geo: &#123;
                 name: '中国地图',
                 type: 'map',
                 map: 'china',
                 selectedMode: 'multiple',
                &#125;,
             series: &#123;
                  name: '标记点',
                  type: 'scatter',
                  coordinateSystem: 'geo',
                  data: [&#123;name: 'Guangzhou', value:[113.23333,23.16667]&#125;],
                  label:&#123;
                    formatter: '&#123;b&#125;',
                    show:true,
                    position: 'right',
                  &#125;,
             &#125;
            &#125;
       )
    &#125;)
    </script>
</body>
</html></code></pre><p>PS：很高兴老婆大人对我最后的成品非常满意，嘿嘿嘿~</p></div><div class="update-details-wrap" data-v-0b37afcb></div><!----></div><div style="border:1px solid transparent;" data-v-0b37afcb></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-0b37afcb><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>4</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-1032" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E8%90%8C%E6%96%B0%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E7%94%A8Echarts%E5%81%9A%E4%B8%80%E4%B8%AA%E8%87%AA%E5%B7%B1%E7%9A%84%E5%9C%B0%E5%9B%BE%E6%A0%87%E8%AE%B0%E7%BD%91%E9%A1%B5%EF%BC%81%E3%80%91%E9%82%A3%E6%98%AF%E4%B8%80%E4%B8%AA%E9%A3%8E%E5%92%8C%E6%97%A5%E4%B8%BD%E7%9A%84%E5%A4%9C%E6%99%9A%EF%BC%8C%E6%88%91%E5%8F%AF%E7%88%B1%E7%9A%84%E8%80%81%E5%A9%86%E5%A4%A7%E4%BA%BA%E7%AA%81%E7%84%B6%E8%B7%9F%E6%88%91%E8%AF%B4%E5%A5%B9%E6%9C%80%E8%BF%91%E5%88%B6%E4%BD%9C%E4%B8%80%E4%BB%BDPPT%E7%9A%84%E6%97%B6%E5%80%99%E9%9C%80%E8%A6%81%E8%BF%9B%E8%A1%8C%E5%9C%B0%E5%9B%BE%E6%A0%87%E8%AE%B0%EF%BC%8C%E4%BD%86%E6%98%AF%E5%8E%9F%E5%85%88%E5%A5%B9%E4%BD%BF%E7%94%A8%E7%9A%84%E7%BD%91%E7%AB%99%E5%A4%B1%E6%95%88%E4%BA%86%EF%BC%8C%E9%97%AE%E6%88%91%E6%9C%89%E6%B2%A1%E6%9C%89%E4%BB%80%E4%B9%88%E5%9C%B0%E5%9B%BE%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2022%2F03%2F12%2Fda3881e9fa48aee66fb41b7e21a33aca.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-5413" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E8%90%8C%E6%96%B0%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E7%94%A8Echarts%E5%81%9A%E4%B8%80%E4%B8%AA%E8%87%AA%E5%B7%B1%E7%9A%84%E5%9C%B0%E5%9B%BE%E6%A0%87%E8%AE%B0%E7%BD%91%E9%A1%B5%EF%BC%81%E3%80%91%E9%82%A3%E6%98%AF%E4%B8%80%E4%B8%AA%E9%A3%8E%E5%92%8C%E6%97%A5%E4%B8%BD%E7%9A%84%E5%A4%9C%E6%99%9A%EF%BC%8C%E6%88%91%E5%8F%AF%E7%88%B1%E7%9A%84%E8%80%81%E5%A9%86%E5%A4%A7%E4%BA%BA%E7%AA%81%E7%84%B6%E8%B7%9F%E6%88%91%E8%AF%B4%E5%A5%B9%E6%9C%80%E8%BF%91%E5%88%B6%E4%BD%9C%E4%B8%80%E4%BB%BDPPT%E7%9A%84%E6%97%B6%E5%80%99%E9%9C%80%E8%A6%81%E8%BF%9B%E8%A1%8C%E5%9C%B0%E5%9B%BE%E6%A0%87%E8%AE%B0%EF%BC%8C%E4%BD%86%E6%98%AF%E5%8E%9F%E5%85%88%E5%A5%B9%E4%BD%BF%E7%94%A8%E7%9A%84%E7%BD%91%E7%AB%99%E5%A4%B1%E6%95%88%E4%BA%86%EF%BC%8C%E9%97%AE%E6%88%91%E6%9C%89%E6%B2%A1%E6%9C%89%E4%BB%80%E4%B9%88%E5%9C%B0%E5%9B%BE%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            