
---
title: '微信小程序地图如何显示附近厕所WC步行路线'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6a4b0c2b884165b314b3b9f7476541~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 18:15:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6a4b0c2b884165b314b3b9f7476541~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>第一次使用腾讯位置服务也算是挺早的，当时是在web端使用。后来，个人慢慢接触到小程序，有一次的需求是能够展示附近的各类店铺，方便自己快速定位周围有什么好吃好逛的地方。再后来每次到一个地方旅游，我们必不可少的一个需求就是需要上WC，当时就在想如何通过一个地图来实现快速定位周边WC的位置以及步行路线，现在好了，有腾讯位置服务功能可以直接在小程序上面直接使用，借助巨人的力量可以好好发挥去实现需求功能了。</p>
<p>因此，写这篇文章，也是希望能够总结对接腾讯位置服务功能步骤和知识点，方便开发同行快速上手和使用。</p>
<h2 data-id="heading-1">申请Key</h2>
<p>创建用于自己某一业务或某一场景的Key密钥，拥有这把钥匙，就可以开始地图功能体验啦！直接微信扫码授权登录即可，腾讯列表功能使用微信扫码登录方便好多，省去了古老需要密码登录的好方式。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6a4b0c2b884165b314b3b9f7476541~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">后台点击菜单：key与配额 ->key管理，具体开发者密钥申请信息填写如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc996be5395940c9b310ef6e7b78c277~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">设置域名</h2>
<p>小程序管理后台 -> 开发 -> 开发管理 -> 开发设置 -> “服务器域名” 中设置request合法域名，添加<a href="https://link.juejin.cn/?target=https%3A%2F%2Fapis.map.qq.com" target="_blank" rel="nofollow noopener noreferrer" title="https://apis.map.qq.com" ref="nofollow noopener noreferrer">apis.map.qq.com</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b02c9707b8fd490ea55e12927082663c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">引入js</h2>
<p>点击官网的开发文档中的微信小程序JavaScript SDK进行下载</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd56f609b13f46c991bd9cb8cc3ec179~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 引入SDK核心类，js文件根据自己业务，位置可自行放置</span>
<span class="hljs-keyword">var</span> QQMapWX = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../../libs/qqmap-wx-jssdk.js'</span>);
<span class="hljs-keyword">var</span> qqmapsdk;
Page(&#123;
    <span class="hljs-attr">data</span>:&#123;
      <span class="hljs-attr">longitude</span>:<span class="hljs-string">'113.390451'</span>,
      <span class="hljs-attr">latitude</span>:<span class="hljs-string">'23.048914'</span>
    &#125;,
    <span class="hljs-attr">onLoad</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 实例化API核心类</span>
        qqmapsdk = <span class="hljs-keyword">new</span> QQMapWX(&#123;
            <span class="hljs-attr">key</span>: <span class="hljs-string">'xxxx-xxxx，你自己申请到的key'</span>
        &#125;);
    &#125;,
    <span class="hljs-attr">onShow</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 调用接口</span>
      qqmapsdk.search(&#123;
          <span class="hljs-attr">keyword</span>: <span class="hljs-string">'广州大学城'</span>,
          <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-comment">//console.log(res);</span>
          &#125;,
          <span class="hljs-attr">fail</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-comment">//console.log(res);</span>
          &#125;,
          <span class="hljs-attr">complete</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-built_in">console</span>.log(res);
          &#125;
      &#125;);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">使用地图</h2>
<p>使用地图map组件，具体参数可登录微信官方文档进行查看
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32e09b8aeed14d3d9da59acb969035c1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5709cf60e30e48409cc65724f3a43d5f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>温馨提示：小程序界面默认顶部是白色背景固定高度的标题栏，如果需要隐藏顶部标题栏的方法，那么需要在app.json配置里的window里加"navigationStyle": "custom",</p>
</blockquote>
<h3 data-id="heading-5">默认效果图</h3>
<p>地图组件参数什么也没设置的情况下，默认如下效果图
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54106ec07de44ff9a6d43abe78dbca4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">view代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><view <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">'view'</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">map</span> <span class="hljs-attr">longitude</span>=<span class="hljs-string">"&#123;&#123;longitude&#125;&#125;"</span> <span class="hljs-attr">latitude</span>=<span class="hljs-string">"&#123;&#123;latitude&#125;&#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">map</span>></span></span>
</view>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">显示标注</h2>
<p>给默认坐标加个标注，标注可以是数组，坐标点数组值，这样在地图的效果就是多个标注点</p>
<p>marker：标记点用于在地图上显示标记的位置</p>
<p>关键代码：markers:[&#123;longitude:'113.390451',latitude:'23.048914'&#125;]
多个标注：markers:[&#123;longitude:'113.390451',latitude:'23.048914'&#125;,&#123;longitude:'113.390451',latitude:'23.048914'&#125;]</p>
<ul>
<li>bindmarkertap：点击标记点时触发</li>
<li>bindlabeltap：点击标记点label时触发</li>
<li>bindcallouttap：点击标记点对应的气泡时触发</li>
</ul>
<h3 data-id="heading-8">默认标注效果</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd7d865ca56d4235913ff57ce93dc485~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">js代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 引入SDK核心类，js文件根据自己业务，位置可自行放置</span>
<span class="hljs-keyword">var</span> QQMapWX = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../../libs/qqmap-wx-jssdk.js'</span>);
<span class="hljs-keyword">var</span> qqmapsdk;
Page(&#123;
    <span class="hljs-attr">data</span>:&#123;
      <span class="hljs-attr">longitude</span>:<span class="hljs-string">'113.390451'</span>,
      <span class="hljs-attr">latitude</span>:<span class="hljs-string">'23.048914'</span>,
      <span class="hljs-attr">markers</span>:[&#123;<span class="hljs-attr">longitude</span>:<span class="hljs-string">'113.390451'</span>,<span class="hljs-attr">latitude</span>:<span class="hljs-string">'23.048914'</span>&#125;]
    &#125;,
    <span class="hljs-attr">onLoad</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 实例化API核心类</span>
        qqmapsdk = <span class="hljs-keyword">new</span> QQMapWX(&#123;
            <span class="hljs-attr">key</span>: <span class="hljs-string">'xxxx-xxxx，你自己申请到的key'</span>
        &#125;);
    &#125;,
    <span class="hljs-attr">onShow</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 调用接口</span>
      qqmapsdk.search(&#123;
          <span class="hljs-attr">keyword</span>: <span class="hljs-string">'广州大学城'</span>,
          <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-comment">//console.log(res);</span>
          &#125;,
          <span class="hljs-attr">fail</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-comment">//console.log(res);</span>
          &#125;,
          <span class="hljs-attr">complete</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-built_in">console</span>.log(res);
          &#125;
      &#125;);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">view代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><view <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">'view'</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">map</span> <span class="hljs-attr">longitude</span>=<span class="hljs-string">"&#123;&#123;longitude&#125;&#125;"</span> <span class="hljs-attr">latitude</span>=<span class="hljs-string">"&#123;&#123;latitude&#125;&#125;"</span> <span class="hljs-attr">markers</span>=<span class="hljs-string">"&#123;&#123;markers&#125;&#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">map</span>></span></span>
</view>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">标注显示文本</h2>
<h3 data-id="heading-12">js代码效果</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a26c64c4f3824cc0920dced6d1ef2d6b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">js代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//关键代码</span>
<span class="hljs-comment">//markers属性下还有属性成员-&#123;label:&#123;content:'广州番禺大学城'&#125;</span>
<span class="hljs-attr">data</span>:&#123;
    <span class="hljs-attr">markers</span>:[&#123;<span class="hljs-attr">label</span>:&#123;<span class="hljs-attr">content</span>:<span class="hljs-string">'广州番禺大学城'</span>&#125;,<span class="hljs-attr">longitude</span>:<span class="hljs-string">'113.390451'</span>,<span class="hljs-attr">latitude</span>:<span class="hljs-string">'23.048914'</span>&#125;]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">WC路线规划</h3>
<p>下面的还有做样式设置，比如：箭头、和线路颜色，以及起点和终点的文本显示等等，纯属默认参数
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f24fdef61da1432a8af9d440c0039bb8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">js代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 引入SDK核心类，js文件根据自己业务，位置可自行放置</span>
<span class="hljs-keyword">var</span> QQMapWX = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../../libs/qqmap-wx-jssdk.js'</span>);
<span class="hljs-keyword">var</span> qqmapsdk;
Page(&#123;
    <span class="hljs-attr">data</span>:&#123;
      <span class="hljs-attr">longitude</span>:<span class="hljs-string">'113.390451'</span>,
      <span class="hljs-attr">latitude</span>:<span class="hljs-string">'23.048914'</span>,
      <span class="hljs-attr">markers</span>:[&#123;<span class="hljs-attr">label</span>:&#123;<span class="hljs-attr">content</span>:<span class="hljs-string">'广州番禺大学城'</span>&#125;,<span class="hljs-attr">longitude</span>:<span class="hljs-string">'113.390451'</span>,<span class="hljs-attr">latitude</span>:<span class="hljs-string">'23.048914'</span>&#125;]
    &#125;,
    <span class="hljs-attr">onLoad</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 实例化API核心类</span>
        qqmapsdk = <span class="hljs-keyword">new</span> QQMapWX(&#123;
            <span class="hljs-attr">key</span>: <span class="hljs-string">'xxxx-xxxx，你自己申请到的key'</span>
        &#125;);
    &#125;,
    <span class="hljs-attr">onShow</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 调用接口</span>
      qqmapsdk.search(&#123;
          <span class="hljs-attr">keyword</span>: <span class="hljs-string">'GoGo厕所'</span>,
          <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-comment">//console.log(res);</span>
          &#125;,
          <span class="hljs-attr">fail</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-comment">//console.log(res);</span>
          &#125;,
          <span class="hljs-attr">complete</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
              <span class="hljs-built_in">console</span>.log(res);
          &#125;
      &#125;);
  &#125;,
  <span class="hljs-comment">//触发表单提交事件，调用接口</span>
  <span class="hljs-function"><span class="hljs-title">formSubmit</span>(<span class="hljs-params">e</span>)</span> &#123;
    <span class="hljs-comment">//起点坐标：23.048914,113.390451 </span>
    <span class="hljs-comment">//终点坐标：23.061793,113.392056</span>
 
    <span class="hljs-comment">//23.061793,113.392056</span>
    <span class="hljs-comment">//23.063073,113.391762</span>
 
    <span class="hljs-keyword">var</span> _this = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">//调用距离计算接口</span>
    qqmapsdk.direction(&#123;
      <span class="hljs-attr">mode</span>: <span class="hljs-string">'driving'</span>,<span class="hljs-comment">//可选值：'driving'（驾车）、'walking'（步行）、'bicycling'（骑行），不填默认：'driving',可不填</span>
      <span class="hljs-comment">//from参数不填默认当前地址</span>
      <span class="hljs-attr">from</span>: e.detail.value.start,
      <span class="hljs-attr">to</span>: e.detail.value.dest, 
      <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res);
        <span class="hljs-keyword">var</span> ret = res;
        <span class="hljs-keyword">var</span> coors = ret.result.routes[<span class="hljs-number">0</span>].polyline, pl = [];
        <span class="hljs-comment">//坐标解压（返回的点串坐标，通过前向差分进行压缩）</span>
        <span class="hljs-keyword">var</span> kr = <span class="hljs-number">1000000</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">2</span>; i < coors.length; i++) &#123;
          coors[i] = <span class="hljs-built_in">Number</span>(coors[i - <span class="hljs-number">2</span>]) + <span class="hljs-built_in">Number</span>(coors[i]) / kr;
        &#125;
        <span class="hljs-comment">//将解压后的坐标放入点串数组pl中</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < coors.length; i += <span class="hljs-number">2</span>) &#123;
          pl.push(&#123; <span class="hljs-attr">latitude</span>: coors[i], <span class="hljs-attr">longitude</span>: coors[i + <span class="hljs-number">1</span>] &#125;)
        &#125;
        <span class="hljs-built_in">console</span>.log(pl)
        <span class="hljs-comment">//设置polyline属性，将路线显示出来,将解压坐标第一个数据作为起点</span>
        _this.setData(&#123;
          <span class="hljs-attr">latitude</span>:pl[<span class="hljs-number">0</span>].latitude,
          <span class="hljs-attr">longitude</span>:pl[<span class="hljs-number">0</span>].longitude,
          <span class="hljs-attr">polyline</span>: [&#123;
            <span class="hljs-attr">points</span>: pl,
            <span class="hljs-attr">color</span>: <span class="hljs-string">'#FF0000DD'</span>,
            <span class="hljs-attr">width</span>: <span class="hljs-number">4</span>
          &#125;]
        &#125;)
      &#125;,
      <span class="hljs-attr">fail</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(error);
      &#125;,
      <span class="hljs-attr">complete</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res);
      &#125;
    &#125;);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">view代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!--地图容器-->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">map</span>
<span class="hljs-attr">id</span>=<span class="hljs-string">"myMap"</span>
<span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%; height: 300px;"</span>
<span class="hljs-attr">longitude</span>=<span class="hljs-string">"&#123;&#123;longitude&#125;&#125;"</span> <span class="hljs-attr">latitude</span>=<span class="hljs-string">"&#123;&#123;latitude&#125;&#125;"</span>
<span class="hljs-attr">scale</span>=<span class="hljs-string">'16'</span>
<span class="hljs-attr">polyline</span>=<span class="hljs-string">"&#123;&#123;polyline&#125;&#125;"</span>
<span class="hljs-attr">show-location</span>
></span>
<span class="hljs-tag"></<span class="hljs-name">map</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">bindsubmit</span>=<span class="hljs-string">"formSubmit"</span>></span>
    <span class="hljs-comment"><!--输入起点和目的地经纬度坐标，格式为string格式--></span>
    <span class="hljs-comment"><!--起点输入框,同终点，不填默认当前位置--></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span>></span>起点坐标：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border:1px solid #000;"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"start"</span>></span><span class="hljs-tag"></<span class="hljs-name">input</span>></span><span class="hljs-tag"></<span class="hljs-name">label</span>></span>
    <span class="hljs-comment"><!--终点输入框,例：39.984060,116.307520--></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span>></span>终点坐标：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border:1px solid #000;"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"dest"</span>></span><span class="hljs-tag"></<span class="hljs-name">input</span>></span><span class="hljs-tag"></<span class="hljs-name">label</span>></span> 
    <span class="hljs-comment"><!--提交表单数据--></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">form-type</span>=<span class="hljs-string">"submit"</span>></span>路线规划<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">开启个性化腾讯地图</h3>
<p>微信扫码绑定，微信会判断当前小程序是否注册腾讯位置服务，如果提示未注册，那么可以输入已注册的账号，一般是手机号码登录，完成小程序和腾讯位置服务账号的绑定。</p>
<p>有些插件还要另外申请appid
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aead2cb7cf54da499f3b1fc8f938dc4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>原文作者：小5聊 <br>
原文链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Flmy_520%2Farticle%2Fdetails%2F112677899" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/lmy_520/article/details/112677899" ref="nofollow noopener noreferrer">blog.csdn.net/lmy_520/art…</a></p>
</blockquote></div>  
</div>
            