
---
title: 'Google Map API 的基础使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6647'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 19:39:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=6647'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<p>因为公司业务由国内市场到国际市场，有一些国际性业务的项目需要用到Google Map。项目完成后，把一些常用的方法写出来，供大家参考。</p>
<h3 data-id="heading-0">一、自定义信息窗口、自定义图标以及自定义控件</h3>
<pre><code class="copyable">// 自定义Marker标记点
var marker = new google.maps.Marker(&#123;
     position:  myLatLng,
     icon: '../car.png',  // 如果为空则显示默认的图标
     map: map
&#125;);
 
// 自定义InfoWindow信息窗口
htmlWindow = "<div class='wrapBox'>\
                   <div>IMEI: " + imei + "</div>\
                   <div>Address：<span id='map-address'>" + pointToAddress(myCenter.lat, myCenter.lng) + "</span>" + info + "</div>\
                   <div>Speed：" + speed + " km/h</div>\
                   <div>Time：" + toDate(2018-12-17 16:12:50) + "</div>\
               </div>";
 
var infowindow= new google.maps.InfoWindow(&#123;
     content: htmlWindow,
     disableAutoPan:true //设置为true时可禁用自动平移功能
&#125;);
 
//打开信息窗体
infowindow.open(map, marker);
 
//marker点事件，点击关闭信息窗体
marker.addListener('click', function() &#123;
    infowindow.close();
&#125;);
 
//监听X关闭按钮事件
google.maps.event.addListener(infowindow,"closeclick", function()&#123;
    infowindow.close();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义标记和自定义信息窗口比较简单，效果如上图（中）。如果我们要改变地图默认的控件位置或需要自定义控件怎么办？接着往下看。<br>
googl map默认开启的控件有：<br>
mapTypeControl   // 地图类型控件<br>
zoomControl      //地图缩小放大控件<br>
streetViewControl   //小黄人街景控件<br>
fullscreenControl   //全屏控件<br>
默认没有开启的还有panControl、scaleControl、overviewMapControl、rotateControl:true等</p>
<pre><code class="copyable">// 关闭地图类型控件，打开缩小放大控件并设置其位置为坐下方
var myOptions2 = &#123;
    zoom: 15,
    center: myLatLng,
    mapTypeControl: false,
    zoomControl: true,
    zoomControlOptions: &#123;
        style:google.maps.ZoomControlStyle.SMALL,
        position:google.maps.ControlPosition.LEFT_BOTTOM
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，所有控件都有position属性，代表控件的位置，包括的选项有：OTTOM、BOTTOM_CENTER、BOTTOM_LEFT、BOTTOM_RIGHT、CENTER、LEFT、LEFT_BOTTOM、LEFT_CENTER、LEFT_TOP、RIGHT、RIGHT_BOTTOM、RIGHT_CENTER、RIGHT_TOP、TOP、TOP_CENTER、TOP_LEFT、TOP_RIGHT。记不住没有关系，你不妨console.log(google.maps.ControlPosition)试试。</p>
<p>而只有部分控件有style属性，而且各不相同。</p>
<h3 data-id="heading-1">地址解析</h3>
<pre><code class="copyable">// 地址解析方法
function pointToAddress(lat, lng, backcall) &#123;
    // 实例化Geocoder服务用于解析地址
    var geocoder = new google.maps.Geocoder();
    // 地理反解析过程
    // 请求数据GeocoderRequest为location,值类型为LatLng因此我们要实例化经纬度
    geocoder.geocode(&#123; location: new google.maps.LatLng(lat, lng) &#125;, function geoResults(results, status) &#123;
       if (status == google.maps.GeocoderStatus.OK) &#123;
             backcall(results[0].formatted_address);
        &#125; else &#123;
             console.log("：error " + status);
        &#125;
    &#125;);
&#125;
 
// 在需要解析的地方调用方法
pointToAddress(myCenter.lat, myCenter.lng, function (address) &#123;
    // 获得地址
    console.log(address);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到地图上控件名称显示的是中文，如果用户手机系统是英文，地图也会自动切换为英文。暂时更新到这里，关于google map实现轨迹回放请前往博主的另外一篇文章。</p></div>  
</div>
            