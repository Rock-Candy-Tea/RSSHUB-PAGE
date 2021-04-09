
---
title: 'Cesium加载大量Label实体时卡顿的一种解决方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df17ee2471bf4f60bab722ab2d65c7c2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 18:48:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df17ee2471bf4f60bab722ab2d65c7c2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>笔者接触CesiumJS是由于公司项目需要，直接边学边开发，两三个月来都挺顺风顺水的。直到数据量越来越大，地图上的实体越来越多，首屏加载的时候经常会卡顿，客户那边的机器性能太差，有时候卡顿的同时还出现浏览器无响应问题。测试把这个问题归为BUG，要求必须解决，搞得我头大。</p>
<h2 data-id="heading-1">加载成百上千实体时出现的问题</h2>
<p>让我们先来看下加载Label实体出现了什么问题？</p>
<pre><code class="copyable">function addBillboard(bsm, name, buildingType, position) &#123;
    this.viewer.entities.add(&#123;
        id: bsm,
        name,
        position: Cartesian3.fromDegrees(position[0], position[1], position[2]),
        label: &#123;
          text: name,
          font: style == 1 ? '500 40px Microsoft YaHei' : '500 30px Helvetica', // 15pt monospace
          outlineColor: Color.WHITE, // 边框颜色
          outlineWidth: 1, // 边框宽度
          scale: 0.5,
          style: style == 1 ? LabelStyle.FILL_AND_OUTLINE : LabelStyle.FILL,
          fillColor: style == 1 ? Color.BLACK : Color.WHITE,
          pixelOffset: new Cartesian2(110, -70), // 偏移量
          showBackground: true,
          backgroundColor: backColor,
          distanceDisplayCondition: new DistanceDisplayCondition(10.0, 8000.0),
          disableDepthTestDistance: 100.0,
          scaleByDistance: new NearFarScalar(500, 1, 1400, 0.0),
          translucencyByDistance: new NearFarScalar(500, 1, 1400, 0.0)
        &#125;,
        billboard: &#123;
          image: buildingTypeImage,
          width: 300,
          height: 140,
          pixelOffset: new Cartesian2(90, -25), // 偏移量
          distanceDisplayCondition: new DistanceDisplayCondition(10.0, 2000.0),
          disableDepthTestDistance: 100.0,
          scaleByDistance: new NearFarScalar(500, 1, 1400, 0.0),
          translucencyByDistance: new NearFarScalar(500, 1, 1400, 0.0)
        &#125;,
        properties: &#123;
          poiType: 'buildingPOI',
          name,
          buildingType,
          bsm,
          position
        &#125;
      &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我需要创建400多个上面这样的实体时，页面总会卡顿一段时间。于是我上网查找相关资料，可能我表述有问题，一直没找到我想要的答案。所以我进行了浏览器DevTools。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df17ee2471bf4f60bab722ab2d65c7c2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在加载地图的时候，js执行了4.75秒。。。。，公司电脑配置如下：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c2f0aa00bda4afa82a3ffd0d56ec98d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
性能不算差吧<br>
继续看Performance分析吧</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d8f8879b14f4003b68bd8a05b1361f7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这个getImageData怎么执行了2秒多，我当时想难道我传进去的图片Cesium要做其他的处理？
于是我把实体的<code>billboard</code>属性剔除掉了。</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/958b693721594965938891549e942206~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
少了20%的时间，噢，不对我已经没传图片进去了，<code>Cesium</code>依然调了<code>getImageData</code>，这就奇怪了，难道这是<code>Cesium</code>在生成图片，<code>entitie</code>属性只剩下label/position/properties/id/name了，除了label，其他都是纯数据的。难道label不是文本？<br></p>
<p>带着这个问题，我把实体的<code>label</code>属性也剔除掉了。进行了一次<code>Performance</code>。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b49295d6b596470abed634558ad531f4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<code>getImageData</code>方法没有调用。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f58e6b4e535d45038d16cbd9d74eda75~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
至此，我断定<code>Cesium</code>在创建含有label的<code>entitie</code>时，会动态生成对应label.name值的图片。</p>
<h2 data-id="heading-2">解决方案——自行动态生成图片</h2>
<p>找到问题，接下来就好办了，自己尝试构造这个label，不要用到Cesium的<code>Label</code>。原本项目中实体的<code>billboard</code>是一张<code>png</code>格式的底图。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/202fb47c3a8448e09e781007274a5a38~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
<strong>思路: 使用Canvas绘制一张带有文本的图片，再将base64码给<code>entitie</code>的<code>billboard</code></strong><br></p>
<pre><code class="copyable">const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');
const image = new Image();
image.style.width = '400px';
const name = '韭年';
image.onload = () => &#123;
    canvas.width = image.width;
    canvas.height = image.height;
    ctx.drawImage(image, 0, 0, image.width, image.height);
    ctx.font = 'bold 20px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'bottom';
    ctx.fillStyle = '#FFF';
    ctx.fillText(name, 220, 70);
    this.imageUrl = canvas.toDataURL('image/png');
  &#125;;
image.src = Iurl;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>图片生成完成，把生成的图片加到<code>billboard</code>中，再进行一次<code>Performance</code>看看：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c37acac30bcb4375903cf1411d63ad0c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
页面秒开了，没有卡顿！！</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea1df7b43b264edd964840e7fb103dd7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
标注也正常显示。</p>
<h2 data-id="heading-3">新的问题</h2>
<p>考虑到客户的电脑性能不好，每次开启页面都要动态生成几百张图片，也挺浪费性能的。那就做存储吧。<br>
存后端Or前端？
由于这些点位信息是动态配置的，有专门的页面进行管理，所以这些文本和底图会有改变的可能。这种情况把图片存在后端只能手动去控制生成图片。<br></p>
<h3 data-id="heading-4">IndexedDB存储</h3>
<p>大量图片，体积是很大的，<code>Storage</code>存不了这么多，只能放到<code>WebSQL</code>或<code>IndexedDB</code>,<code>WebSQL</code>已经不维护了，那就放在<code>IndexedDB</code>吧。</p>
<pre><code class="copyable">// 项目入口文件中创建并连接IndexedDB
//FILE -> main.js

const indexedDB = window.indexedDB || window.webkitIndexedDB || window.mozIndexedDB;
DBOpenRequest.onupgradeneeded = (e) => &#123;
  console.info('DB upgradeneeded')
  const db = e.target.result;
  if (!db.objectStoreNames.contains('buildingImage')) &#123;
    db.createObjectStore('buildingImage', &#123; keyPath: 'bsm' &#125;);
  &#125;
&#125;
DBOpenRequest.onsuccess = (e) => &#123;
  console.info('DB链接成功')
  const db = e.target.result;
  Vue.prototype.$DB = db;

  new Vue(&#123;
    router,
    store,
    beforeDestroy() &#123;
      DBOpenRequest.result.close();
    &#125;,
    render: h => h(App)
  &#125;).$mount('#app');
&#125;
DBOpenRequest.onerror = (e) => &#123;
  console.ERROR('Can not open indexedDB', e);

  new Vue(&#123;
    router,
    store,
    beforeDestroy() &#123;
      DBOpenRequest.result.close();
    &#125;,
    render: h => h(AppWith404)
  &#125;).$mount('#app');
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后： 在添加<code>entitie</code>的时候先查询库里对应的bsm存不存在，若存在，判断各类信息是否一致，一致的话使用存储的base64图片作为<code>billboard</code>的<code>image</code>；若不存在或者各类信息不一致，重新生成图片并存入库，再作为<code>billboard</code>的<code>image</code>。</p>
<h2 data-id="heading-5">结语</h2>
<p>至此，Cesium加载大量entitie卡顿的问题基本解决，进入页面也能达到秒开的速度。<br>
国内对<code>CesiumJS</code>的知识的分享过少，有时候遇到问题，网上找不到答案；并且<code>CesiumJS</code>的API超级多，很难在短时间内找到想要的功能API。若有想一起学习探讨的大佬，请私信！！！
本人对<code>CesiumJS</code>的认知就像学前端的时候刚学<code>JS</code>一样，一脸懵逼，文章中若有错误或讲得不对的，请批评指出。谢谢(●'◡'●)。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            