
---
title: '从Exifjs的原理入手，搞定js二进制数据的操作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8faa01ba1c284c9187cb9224c92e5efe~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 15 May 2021 09:10:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8faa01ba1c284c9187cb9224c92e5efe~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a name="user-content-wL1sd" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-0">前言</h1>
<p>上一章我们大概了解如何通过js库来获取Exif信息。那么这些库是怎么实现的呢。我们用比较流行的Exifjs来做分析和学习。<br>通过学习Exifjs，我们大概可以发现，我们需要了解以下知识：<br>1、Exif标识<br>2、base64的由来和作用，以及常用api<br>3、js如何操作二进制流，这也是js实现读取exif信息的核心
<a name="user-content-7OxuZ" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-1">知识点梳理</h1>
<p><a name="user-content-cnL2P" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-2">1、Exif信息标识</h2>
<p>当照片拍摄的时候，会把Exif参数信息存放到jpeg格式文件的原始数据内部。<br>通过查看Exifjs源码，会发现它有一个映射关系，如下图：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8faa01ba1c284c9187cb9224c92e5efe~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>那么这个映射关系是如何来的呢，通过查看Exif官方标准，发现exifjs的映射表与下图的tagId、tagName的映射关系相同。<br>知道这些关系以后，后面我们会根据tagId来进行exif信息的操作。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d9726e50ecc42679f2239df9638c644~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-uD0Uc" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-3">2、base64相关</h2>
<p>base64大家可能比较熟悉，其实它不算Exif信息获取的一个核心功能，在实现中的作用也只是为了兼容图片数据格式。这里我们单独罗列出来是因为它与我们前端开发有着紧密的联系。那么了解了它的由来、作用以及相关的api对我们日常的工作还是会有一定作用的。<br>对于base64的由来、作用，建议大家去看看<a href="http://www.ruanyifeng.com/blog/2008/06/base64.html" target="_blank" rel="nofollow noopener noreferrer">base64笔记</a>，这里阮一峰老师做了专业、详细的讲解。<br>我这里主要说一下相关api的应用：<br>1、window.atob和window.btoa，用法很简单，作用也很简单就是有关base64的解码和编码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> str = <span class="hljs-string">"Man"</span>;
<span class="hljs-keyword">const</span> base64 = <span class="hljs-built_in">window</span>.btoa(str); <span class="hljs-comment">// 字符串编码成base64</span>
<span class="hljs-keyword">const</span> result = <span class="hljs-built_in">window</span>.atob(base64) <span class="hljs-comment">// base64解码成字符串</span>
<span class="hljs-built_in">console</span>.log(base64) <span class="hljs-comment">//TWFu</span>
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// Man</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-n9ubN" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-4">3、js中有关二进制数据的操作</h2>
<p>js中关于二进制的操作主要有两大块，blob和ArrayBuffer。
<a name="user-content-t8Hb6" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-5">3.1 Blob</h3>
<p>Blob是一个大类，我们常用的File对象，继承自Blob对象并扩展支持用户上传。所以Blob具有的功能，基本上File都会具有。
<a name="user-content-klLbY" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-6">3.1.1Blob构造函数Blob( array, options )</h4>
<p>array，数组里面的元素共同组合成Blob的数据源。<br>options 可能会指定如下两个属性：</p>
<ul>
<li>type，默认值为 ""，它代表了将会被放入到blob中的数组内容的MIME类型。</li>
<li>endings，默认值为"transparent"，用于指定包含行结束符\n的字符串如何被写入。 它是以下两个值中的一个： "native"，代表行结束符会被更改为适合宿主操作系统文件系统的换行符，或者 "transparent"，代表会保持blob中保存的结束符不变。</li>
</ul>
<p>下面我们对于不同类型的数据调用一下Blob，来看看都会返回什么。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> data1 = <span class="hljs-number">1</span>;
<span class="hljs-keyword">var</span> data2 = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> data3 = <span class="hljs-string">'a'</span>;
<span class="hljs-keyword">var</span> data4 = [<span class="hljs-number">1</span>];
<span class="hljs-keyword">var</span> data5 = &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">"test"</span> &#125;;
<span class="hljs-keyword">var</span> blob1 = <span class="hljs-keyword">new</span> Blob([data1]);
<span class="hljs-keyword">var</span> blob2 = <span class="hljs-keyword">new</span> Blob([data2])
<span class="hljs-keyword">var</span> blob3 = <span class="hljs-keyword">new</span> Blob([data3])
<span class="hljs-keyword">var</span> blob4 = <span class="hljs-keyword">new</span> Blob([data4])
<span class="hljs-keyword">var</span> blob5 = <span class="hljs-keyword">new</span> Blob([data5])
<span class="hljs-keyword">var</span> blob6 = <span class="hljs-keyword">new</span> Blob([data1, data3])
<span class="hljs-keyword">var</span> blob7 = <span class="hljs-keyword">new</span> Blob([<span class="hljs-built_in">JSON</span>.stringify(data5)])
<span class="hljs-keyword">var</span> blob8 = <span class="hljs-keyword">new</span> Blob([<span class="hljs-built_in">JSON</span>.stringify(data5)], &#123;<span class="hljs-attr">type</span> : <span class="hljs-string">'application/json'</span>&#125;)
<span class="hljs-keyword">var</span> blob9 = <span class="hljs-keyword">new</span> Blob([data5],&#123;<span class="hljs-attr">type</span> : <span class="hljs-string">'application/json'</span>&#125;)
<span class="hljs-built_in">console</span>.log(blob1, <span class="hljs-string">'data1'</span>)
<span class="hljs-built_in">console</span>.log(blob2, <span class="hljs-string">'data2'</span>)
<span class="hljs-built_in">console</span>.log(blob3, <span class="hljs-string">'data3'</span>)
<span class="hljs-built_in">console</span>.log(blob4, <span class="hljs-string">'data4'</span>)
<span class="hljs-built_in">console</span>.log(blob5, <span class="hljs-string">'data5'</span>)
<span class="hljs-built_in">console</span>.log(blob6, <span class="hljs-string">'data6(data1,data3)'</span>)
<span class="hljs-built_in">console</span>.log(blob7, <span class="hljs-string">'data7(data5)'</span>)
<span class="hljs-built_in">console</span>.log(blob8, <span class="hljs-string">'data8(data5)'</span>)
<span class="hljs-built_in">console</span>.log(blob9, <span class="hljs-string">'data9(data5)'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1-9对应的数据返回如下：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eb2309deece43b89b54218e45bcd4c3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<br>可见Blob有两个属性 size表示包含数据的字节大小，type的值刚才所讲的options.type。<br><strong>需要注意的一点</strong>是 data5， data7这两个创建Blob以后size不一样。而区别就在于是否进行了JSON.stringify。<br>data5.toString()是[object Object]，length 正好是15。JSON.stringify(data5).length是16。看来是跟toString有关系。<br>我们创建一个新的data10来验证一下。</p>
<p>data10.toString()是test，length正好是4，JSON.stringify(data10).length是2。<br>这是因为在创建Blob的时候，会调用传入数据的toString方法。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03de43ba50ce4cbeb762c5151c964c3f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-vB4vd" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-7">3.1.2 slice方法</h4>
<p>这个方法返回一个新的 Blob 对象，包含了源 Blob 对象中指定范围内的数据。用法跟数组的是一样的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> sliceData = <span class="hljs-string">'abcdef123'</span>;
<span class="hljs-keyword">var</span> dataBlob = <span class="hljs-keyword">new</span> Blob([sliceData]);
<span class="hljs-keyword">var</span> dataBlob1 = dataBlob.slice(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>);
<span class="hljs-built_in">console</span>.log(dataBlob, dataBlob1) <span class="hljs-comment">// Blob &#123;size: 9, type: ""&#125; Blob &#123;size: 1, type: ""&#125;</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTextFromBlob</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> result1 = <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> Response(dataBlob).text(); <span class="hljs-comment">// 以字符串的方式提取blob的内容</span>
  <span class="hljs-keyword">var</span> result2 = <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> Response(dataBlob1).text();
  <span class="hljs-built_in">console</span>.log(result1, result2) <span class="hljs-comment">//abcdef123 a</span>
&#125;
getTextFromBlob();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-4DOlF" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-8">3.1.3 window.URL.createObjectURL</h4>
<p>这个方法可以把blob转换成一个Blob URL，我们常用的就是在用户上传的时候把File转换成一个Blob URL进行访问。Blob URL的优点就是比base64生成的图片要短小。但是缺点就是它并没有保存图片信息，而是浏览器根据一定的规则生成一个标识来指向真实资源的。所以它是强依于赖浏览器的。当创建Blob URL的环境销毁的时候（比如调用createObjectURL的页签关闭、刷新）这个Blob URL也就无法访问了。
<a name="user-content-TplyG" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-9">3.2 ArrayBuffer相关</h3>
<p>ArrayBuffer 对象用来表示通用的、固定长度的原始二进制数据缓冲区。ArrayBuffer不能直接操作，需要通过类型数组对象或者DataView进行操作。
<a name="user-content-jdZPI" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-10">3.2.1 ArrayBuffer</h4>
<p>ArrayBuffer只有一个参数，那就是要创建内存的大小，也就是字节数。创建出来的ArrayBuffer内容初始化是0。<br>具有的属性有byteLength，为字节大小，不可改变。<br>具有isView静态方法，判断参数是否为ArrayBuffer视图；还有slice方法类似数组的用法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> buffer = <span class="hljs-keyword">new</span> <span class="hljs-built_in">ArrayBuffer</span>(<span class="hljs-number">10</span>)
<span class="hljs-built_in">console</span>.log(buffer.byteLength); <span class="hljs-comment">// 10</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">ArrayBuffer</span>.isView(buffer)); <span class="hljs-comment">// false</span>
<span class="hljs-keyword">const</span> view = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(<span class="hljs-number">10</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">ArrayBuffer</span>.isView(view)); <span class="hljs-comment">// true</span>
<span class="hljs-keyword">const</span> buffer1 = buffer.slice(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>);
<span class="hljs-built_in">console</span>.log(buffer, buffer1) 
<span class="hljs-comment">/**
ArrayBuffer &#123;
  [Uint8Contents]: <00 00 00 00 00 00 00 00 00 00>,
  byteLength: 10
&#125;
ArrayBuffer &#123; [Uint8Contents]: <00>, byteLength: 1 &#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-UiUK0" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-11">3.2.2 类型数组对象TypedArray</h4>
<p>TypedArray是一个<strong>类数组</strong>视图，用于操作ArrayBuffer创造的二进制缓冲区的数据，包括9个视图Int8Array、Uint8Array等（每位占用的字节数不同）。TypedArray使用方法类似于普通的数组，但是还是有一些差异：<br>1、TypeArray是视图不是一种数据存储结构，它要操作的数据是ArrayBuffer中的数据。而Array本身就是用来存储数据的。<br>2、TypedArray中所有成员的类型是一样的，数组对成员的类型没有限制。<br>3、TypedArray初始值是0，数组是empty</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">const</span> view1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(<span class="hljs-number">10</span>);<span class="hljs-comment">// 在内存中生成一个缓冲区</span>
 <span class="hljs-keyword">const</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">10</span>);
 <span class="hljs-built_in">console</span>.log(view1, arr)
<span class="hljs-comment">/*
Int8Array(10) [
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0
] 
[ <10 empty items> ]
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、typedArray不同视图单个元素对应容纳的数值会有范围，比如int8Array是有符号的8位二进制数值范围[-128 ，127]<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/516716df6f69424487480c4babad0504~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>TypedArray实例化<br>有四种传参方式分别是：length，TypedArray、object，buffer(byteOffet,length)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> buffer = <span class="hljs-keyword">new</span> <span class="hljs-built_in">ArrayBuffer</span>(<span class="hljs-number">10</span>);
<span class="hljs-keyword">const</span> view1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(buffer);  <span class="hljs-comment">// buffer , 可选byteoffset，length未传</span>
<span class="hljs-keyword">const</span> view2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(<span class="hljs-number">5</span>);
<span class="hljs-keyword">const</span> buffer1 = view2.map(<span class="hljs-function">(<span class="hljs-params">v, i</span>) =></span> i)
<span class="hljs-keyword">const</span> view3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(buffer1.buffer, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>); <span class="hljs-comment">// buffer, byteoffset偏移坐标，length视图长度</span>
<span class="hljs-keyword">const</span> view4 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(view2) <span class="hljs-comment">// typedArray</span>
<span class="hljs-keyword">const</span> view5 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(&#123; <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">3</span> &#125;) <span class="hljs-comment">// object的时候会调用typedArray.from方法创建一个新的类数组</span>
<span class="hljs-keyword">const</span> view6 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]) <span class="hljs-comment">// object</span>
<span class="hljs-keyword">const</span> view7 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int16Array</span>(buffer)  <span class="hljs-comment">// int16 每位占用两个字节，所以10个字节的ArrayBuffer的视图长度为5,也就是分成了5段</span>
<span class="hljs-built_in">console</span>.log(view1, view2, view3, view4, view5)
<span class="hljs-comment">/**
view1:
Int8Array(10) [
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0
]
view2:
Int8Array(5) [ 0, 0, 0, 0, 0 ] 
view3:
Int8Array(2) [ 1, 2 ] 
view4:
Int8Array(5) [ 0, 0, 0, 0, 0 ] 
view5:
Int8Array(3) [ 0, 0, 0 ]
view6: 
Int8Array(4) [ 1, 2, 3, 4 ]
view7:
Int16Array(5) [ 0, 0, 0, 0, 0 ]
**/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-rIht1" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-12">3.2.3 DateView视图</h3>
<p>DataView 视图是一个可以从ArrayBuffer对象中读写多种数值类型的底层接口，使用它时，不用考虑不同平台的字节序问题。字节序此处就不展开了，有兴趣的同学可以传送了解<a href="https://developer.mozilla.org/zh-CN/docs/Glossary/Endianness" target="_blank" rel="nofollow noopener noreferrer">字节序</a>。大部分的计算机（所有英特尔处理器）都采用小字节序。<br>DateView的构造函数接受参数new DataView(buffer [, byteOffset [, byteLength]])，类似于我们上面讲的TypedArray中的buffer传参模式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> buffer = <span class="hljs-keyword">new</span> <span class="hljs-built_in">ArrayBuffer</span>(<span class="hljs-number">10</span>);
<span class="hljs-keyword">const</span> view1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(buffer);
view1[<span class="hljs-number">1</span>] = <span class="hljs-number">2</span>;
<span class="hljs-keyword">const</span> view = <span class="hljs-keyword">new</span> <span class="hljs-built_in">DataView</span>(buffer, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="hljs-built_in">console</span>.log(view)
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">0</span>))
<span class="hljs-built_in">console</span>.log(view.getInt16(<span class="hljs-number">0</span>)) <span class="hljs-comment">//一次获取两个字节</span>
<span class="hljs-built_in">console</span>.log(view.getInt16(<span class="hljs-number">1</span>)) <span class="hljs-comment">//Offset is outside the bounds of the DataView</span>
<span class="hljs-comment">/**
view:
DataView &#123;
  byteLength: 2,
  byteOffset: 1,
  buffer: ArrayBuffer &#123;
    [Uint8Contents]: <00 02 00 00 00 00 00 00 00 00>,
    byteLength: 10
  &#125;
&#125;
view.getInt8(0)
2
view.getInt16(0)
512
view.getInt16(1)
Offset is outside the bounds of the DataView
**/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DateView不用考虑平台的字节序，指的是它制定字节序。两个字节及以上的getXXX存在两个参数“偏移量和字节序”，字节序默认是高字节序。getInt8只有一个参数，getInt16有两个参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> buffer = <span class="hljs-keyword">new</span> <span class="hljs-built_in">ArrayBuffer</span>(<span class="hljs-number">10</span>);
<span class="hljs-keyword">const</span> view1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(buffer);
view1[<span class="hljs-number">1</span>] = <span class="hljs-number">2</span>;
<span class="hljs-keyword">const</span> view = <span class="hljs-keyword">new</span> <span class="hljs-built_in">DataView</span>(buffer, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">0</span>)) <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">1</span>)) <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(view.getInt16(<span class="hljs-number">0</span>)) <span class="hljs-comment">// 512</span>
<span class="hljs-built_in">console</span>.log(view.getInt16(<span class="hljs-number">0</span>, <span class="hljs-literal">true</span>)) <span class="hljs-comment">// 2 字节序为true代表小字节序</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是写入字节，超过两个字节也涉及到字节位的问题，同以上的get获取类似。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> buffer = <span class="hljs-keyword">new</span> <span class="hljs-built_in">ArrayBuffer</span>(<span class="hljs-number">10</span>);
<span class="hljs-keyword">const</span> view1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Int8Array</span>(buffer);
view1[<span class="hljs-number">1</span>] = <span class="hljs-number">2</span>;
<span class="hljs-keyword">const</span> view = <span class="hljs-keyword">new</span> <span class="hljs-built_in">DataView</span>(buffer, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">0</span>)) <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">1</span>)) <span class="hljs-comment">// 0</span>
view.setInt8(<span class="hljs-number">1</span>, <span class="hljs-number">5</span>)
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">0</span>)) <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">1</span>)) <span class="hljs-comment">// 5</span>
view.setInt16(<span class="hljs-number">0</span>, <span class="hljs-number">5</span>)
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">0</span>)) <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">1</span>)) <span class="hljs-comment">// 5</span>
view.setInt16(<span class="hljs-number">0</span>, <span class="hljs-number">5</span>, <span class="hljs-literal">true</span>)
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">0</span>)) <span class="hljs-comment">// 5</span>
<span class="hljs-built_in">console</span>.log(view.getInt8(<span class="hljs-number">1</span>)) <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-doJRj" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-13">4、获取Exif信息</h2>
<p>主要思想就是，通过JPEG的格式和标志来判断信息。<br>关于Exif信息的含义，参考资料为文章：“<a href="https://blog.csdn.net/weixin_44350337/article/details/109558492" target="_blank" rel="nofollow noopener noreferrer">EXIF信息及含义</a>”。<br>1、JPEG文件都是以十六进制 '0xFFD8’开始，以’0xFFD9’结束。在JPEG数据中有像’0xFF**'这样的数据，这些被称为“标志”，它表示JPEG信息数据段。0xFFD8 表示SOI（Start of image 图像开始），0xFFD9表示EOI（End of image 图像结束）。这两个特殊的标志没有附加的数据，而其他的标志在标志后都带有附加的数据。<br>2、从0xFFE0 ~ 0xFFEF 的标志是“应用程序标志”，Exif使用0xFFE1标志Exif信息，Exif数据是从ASCII字符"Exif"和2个字节的0x00开始，后面就是Exif的数据了。<br>3、TIFF头指的是TIFF格式的前8个字节。前两个字节定义了TIFF数据采用何种字节顺序。如果是0x4949 ，表示采用"Intel"的小字节序，如果为0x4d4d ，表示采用高字节序。<br>4、TIFF头的最后4个字节是第一个IFD(Image File Directory, described in next chapter 图像文件目录，描述下一个字符)的偏移量。在TIFF格式中所有的偏移量都是从TIFF头的第一个字节（0x4949或者0x4d4d）开始计算的到所在位置的字节数目，这个偏移量也不例外。通常第一个IFD是紧跟在TIFF头后面的，所以它的偏移量为’0x00000008’。<br>5、接着TIFF头的是第一个IFD。它包含了图像信息数据。在下表中，开始的两个字节（‘EEEE’）表示这个IFD所包含的目录实体数量。然后紧跟着就是实体对象（每个实体12个字节）。在最后一个目录实体后面有一个4字节大小的数据（表中的是’LLLLLLLL’），它表示下一个IFD的偏移量。如果这个偏移量的值是’0x00000000’，就表示这个IFD是最后一个IFD。<br>完整代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyExif</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">image</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getImageExif(image)
    &#125;
    <span class="hljs-function"><span class="hljs-title">getImageExif</span>(<span class="hljs-params">image</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(image.src) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.domImageExif(image.src)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(image <span class="hljs-keyword">instanceof</span> Blob)&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.blobImageExif(image)
        &#125;
    &#125;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">blobImageExif</span>(<span class="hljs-params">file</span>)</span> &#123;
        <span class="hljs-keyword">var</span> _t = <span class="hljs-built_in">this</span>
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            <span class="hljs-keyword">var</span> fileReader = <span class="hljs-keyword">new</span> FileReader();
            fileReader.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
                res(_t.findExifInJPEG(e.target.result));
            &#125;;
            fileReader.readAsArrayBuffer(file);
        &#125;)
    &#125;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">domImageExif</span>(<span class="hljs-params">src</span>)</span>&#123;
        <span class="hljs-keyword">let</span> result;
        <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^data\:/i</span>.test(src)) &#123; <span class="hljs-comment">// Data URI</span>
            result = <span class="hljs-built_in">this</span>.base64Url(src);
        &#125; <span class="hljs-keyword">else</span> &#123;
            result = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.blobUrl(src);
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(result)
    &#125;
    <span class="hljs-function"><span class="hljs-title">base64Url</span>(<span class="hljs-params">base64</span>)</span>&#123;
        base64 = base64.replace(<span class="hljs-regexp">/^data\:([^\;]+)\;base64,/gmi</span>, <span class="hljs-string">''</span>);
        <span class="hljs-keyword">const</span> binary = atob(base64);
        <span class="hljs-keyword">const</span> len = binary.length;
        <span class="hljs-keyword">const</span> buffer = <span class="hljs-keyword">new</span> <span class="hljs-built_in">ArrayBuffer</span>(len); <span class="hljs-comment">// 根据长度创建二进制缓冲区</span>
        <span class="hljs-keyword">const</span> view = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(buffer); <span class="hljs-comment">// 创建视图操作</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
            view[i] = binary.charCodeAt(i); <span class="hljs-comment">//获取字符串的Unicode </span>
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.findExifInJPEG(buffer)
    &#125;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">blobUrl</span>(<span class="hljs-params">src</span>)</span>&#123;
        <span class="hljs-keyword">const</span> buffer = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.httpToBlob(src);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.findExifInJPEG(buffer)
    &#125;
    <span class="hljs-function"><span class="hljs-title">httpToBlob</span>(<span class="hljs-params">url</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            <span class="hljs-keyword">var</span> http = <span class="hljs-keyword">new</span> XMLHttpRequest();
            http.open(<span class="hljs-string">"GET"</span>, url, <span class="hljs-literal">true</span>);
            http.responseType = <span class="hljs-string">"arraybuffer"</span>;
            http.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status == <span class="hljs-number">200</span> || <span class="hljs-built_in">this</span>.status === <span class="hljs-number">0</span>) &#123;
                    res(<span class="hljs-built_in">this</span>.response);
                &#125;
            &#125;;
            http.send();
        &#125;)
        
    &#125;
    <span class="hljs-function"><span class="hljs-title">findExifInJPEG</span>(<span class="hljs-params">buffer</span>)</span>&#123;
        <span class="hljs-keyword">var</span> dataView = <span class="hljs-keyword">new</span> <span class="hljs-built_in">DataView</span>(buffer);
        <span class="hljs-comment">// JPEG文件都是以十六进制 '0xFFD8’开始</span>
        <span class="hljs-keyword">if</span> ((dataView.getUint16(<span class="hljs-number">0</span>) != <span class="hljs-number">0xFFD8</span>)) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Not a valid JPEG"</span>);
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; <span class="hljs-comment">// not a valid jpeg</span>
        &#125;
        
        <span class="hljs-keyword">let</span> length = buffer.byteLength;
        <span class="hljs-keyword">let</span> exifStartIndex = <span class="hljs-built_in">this</span>.getExifPosition(dataView, length);
        <span class="hljs-keyword">if</span>(exifStartIndex) &#123;
            <span class="hljs-comment">// 根据上一次获取的索引，然后根据索引后4位判断后续是否是Exif信息</span>
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.getStringFromDB(dataView, exifStartIndex, <span class="hljs-number">4</span>) !== <span class="hljs-string">'Exif'</span>) &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Not valid EXIF data!'</span>);
                <span class="hljs-keyword">return</span> ;
            &#125;
            <span class="hljs-comment">// 这里exifStartIndex + 6的原因是Exif数据是从ASCII字符"Exif"和2个字节的0x00开始，后面就是Exif的数据了。EXif+2个字节 正好是6</span>
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getTIFFInfo(dataView, exifStartIndex + <span class="hljs-number">6</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>
        &#125;
        
    &#125;
    <span class="hljs-function"><span class="hljs-title">getExifPosition</span>(<span class="hljs-params">dataView, byteLength</span>)</span> &#123;
        <span class="hljs-keyword">let</span> offset = <span class="hljs-number">2</span>; <span class="hljs-comment">//因为前两位是0xFFD8，ArrayBuffer 使用的视图是Uint8Array所以从2（0xFFD8是两位）开始遍历</span>
        <span class="hljs-keyword">while</span>(offset < byteLength) &#123;
            <span class="hljs-comment">// Exif使用APP1（0xFFE1）标志</span>
            <span class="hljs-keyword">if</span>(dataView.getUint8(offset) === <span class="hljs-number">0xFF</span> && dataView.getUint8(offset + <span class="hljs-number">1</span>) === <span class="hljs-number">0xE1</span>) &#123;
                <span class="hljs-comment">//APP1的数据从"SSSS"后开始 所以加4</span>
                <span class="hljs-keyword">return</span> offset + <span class="hljs-number">4</span>;
            &#125;
            offset++;
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">getStringFromDB</span>(<span class="hljs-params">dataView, start, length</span>)</span>&#123;
        <span class="hljs-keyword">let</span> max = start + length;
        <span class="hljs-keyword">let</span> result = <span class="hljs-string">""</span>;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = start; i < max; i++) &#123;
            result += <span class="hljs-built_in">String</span>.fromCharCode(dataView.getUint8(i))
        &#125;
        <span class="hljs-keyword">return</span> result;
    &#125;
    <span class="hljs-function"><span class="hljs-title">getTIFFInfo</span>(<span class="hljs-params">dataView, tiffOffset</span>)</span> &#123;
        <span class="hljs-comment">//前两个字节定义了TIFF数据采用何种字节顺序</span>
        <span class="hljs-keyword">let</span> bigEndian = dataView.getUint16(tiffOffset) === <span class="hljs-number">0x4D4D</span>;
        <span class="hljs-comment">// 然后的两个字节总是2个字节长度的0x002A</span>
        <span class="hljs-keyword">if</span> (dataView.getUint16(tiffOffset + <span class="hljs-number">2</span>, !bigEndian) != <span class="hljs-number">0x002A</span>) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Not valid TIFF data! (no 0x002A)"</span>);
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;
        <span class="hljs-comment">//TIFF头的最后4个字节是第一个IFD的偏移量。</span>
        <span class="hljs-keyword">const</span> firstIFDOffset = dataView.getUint32(tiffOffset + <span class="hljs-number">4</span>, !bigEndian);
        <span class="hljs-comment">//通常第一个IFD是紧跟在TIFF头后面的，所以它的偏移量为’0x00000008’</span>
        <span class="hljs-keyword">if</span> (firstIFDOffset < <span class="hljs-number">0x00000008</span>) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Not valid TIFF data! (First offset less than 8)"</span>, dataView.getUint32(tiffOffset+<span class="hljs-number">4</span>, !bigEndian));
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;
        <span class="hljs-comment">// 0x0112 代表Orientation </span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getTag(dataView, tiffOffset + firstIFDOffset, bigEndian, <span class="hljs-number">0x0112</span>)
    &#125;
    <span class="hljs-function"><span class="hljs-title">getTag</span>(<span class="hljs-params">dataView, dirStart, bigEndian, tag</span>)</span>&#123;
        <span class="hljs-keyword">const</span> length = dataView.getUint16(dirStart, !bigEndian);
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
            <span class="hljs-comment">//开始的两个字节（‘EEEE’）表示这个IFD所包含的目录实体数量。然后紧跟着就是实体对象（每个实体12个字节）</span>
            <span class="hljs-keyword">let</span> offset = dirStart + i * <span class="hljs-number">12</span> + <span class="hljs-number">2</span>;
            <span class="hljs-keyword">if</span>(dataView.getUint16(offset, !bigEndian) === tag) &#123;
                <span class="hljs-comment">// 此处只获取Orientation的值，需要偏移8位</span>
                offset += <span class="hljs-number">8</span>;
                <span class="hljs-keyword">return</span> dataView.getUint16(offset, !bigEndian);
            &#125;

        &#125;

    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-ihsKI" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-14">5、最后</h2>
<p>1、js二进制操作的主要场景有：文件的切割、下载、内容获取，内容处理等。<br>2、blob相对于ArrayBuffer的可操作性还是比较小的。<br>3、base64、blob、ArrayBuffer的互相转换。<br>遇见好几次exif相关的问题了一直用exifjs。想着深究一下原理，没想到Exif标准真烧脑。。。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b31c64bfe534a7686441992dfd35efa~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br></p></div>  
</div>
            