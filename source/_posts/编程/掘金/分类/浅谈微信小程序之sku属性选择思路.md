
---
title: '浅谈微信小程序之sku属性选择思路'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/603930eea6734edea6649992ffa35f6f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 05 May 2021 18:56:09 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/603930eea6734edea6649992ffa35f6f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><h2 data-id="heading-0">写在前面</h2>
<p>  在电商平台，sku属性选择是产品模块中的一个常见问题。其实，解决这个问题并不难，关键是要理清自己的思路，将这个大问题拆分成几个小问题，再逐一击破就好了。写这篇文章一来是对前段时间的小程序sku属性选择做个总结，二来是希望放在网上能帮助到大家。掘金上的内容都系本人原创，如需转载请注明出处，感谢！</p>
<h2 data-id="heading-1">需求分析及解决思路</h2>
<p>  其实我个人更倾向于将这个问题拆分为如下三个小问题：</p>
<h3 data-id="heading-2">需求1：sku页面的渲染</h3>
<p>  在商品列表页，点击不同的产品，会根据不同的产品id请求产品详情接口，跳转到对应的产品详情页面。在产品详情页面，点击加入购物车按钮，会弹出产品的sku页面。</p>
<p>  某个产品的产品详情请求结果如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;<span class="hljs-attr">data</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">246</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"Sling Cosmetic Bags dsfsad测试"</span>,…&#125;&#125;
<span class="hljs-attr">data</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">246</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"Sling Cosmetic Bags dsfsad测试"</span>,…&#125;
<span class="hljs-attr">color_image</span>: <span class="hljs-string">"https://assets.forucdn.com/basics/DD-W/j5tB2xyie4maeMWKboYDuOseOgz2Jar8kIZQE1u1.jpeg"</span>
<span class="hljs-attr">description</span>: <span class="hljs-string">"<p>* EVA Flexibility&nbsp;soles with&nbsp;cross&nbsp;&nbsp;performance&nbsp;design&nbsp;for sneaker shoes&nbsp;&nbsp;</p><p>* Mesh&nbsp;-knit fabric&nbsp;upper lining construction with EVA padded insoles</p><p>* Complete with 4 eyelets and a lace up closure for a classic look</p><p>* Perfect for every season, wear them all year round</p>"</span>
<span class="hljs-attr">id</span>: <span class="hljs-number">246</span>
<span class="hljs-attr">images</span>: [<span class="hljs-string">"https://appfiles.forucdn.com/samples/1/0/Z8-1-20210428091333-X41yFkML.jpg"</span>,…]
<span class="hljs-attr">lowest_price</span>: <span class="hljs-string">"9.99"</span>
<span class="hljs-attr">merchant</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">code</span>: <span class="hljs-string">"HCFW"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"迪摩信息有限公司"</span>, <span class="hljs-attr">address</span>: <span class="hljs-string">"拉萨西峰区"</span>,…&#125;
<span class="hljs-attr">address</span>: <span class="hljs-string">"拉萨西峰区"</span>
<span class="hljs-attr">code</span>: <span class="hljs-string">"HCFW"</span>
<span class="hljs-attr">id</span>: <span class="hljs-number">1</span>
<span class="hljs-attr">name</span>: <span class="hljs-string">"迪摩信息有限公司"</span>
<span class="hljs-attr">thumb</span>: <span class="hljs-string">"https://appfiles.forucdn.com/avatars/5/20210426151158-T6UCoTjYJ6.jpeg"</span>
<span class="hljs-attr">name</span>: <span class="hljs-string">"Sling Cosmetic Bags dsfsad测试"</span>
<span class="hljs-attr">size_image</span>: <span class="hljs-string">"https://appfiles.forucdn.com/testing/admin/basics/Z8/OyrsoiMFpUNYeP8eWhZdHfCsQqPsKYDHGtYi2KYb.jpg"</span>
<span class="hljs-attr">status</span>: <span class="hljs-string">"active"</span>
<span class="hljs-attr">type</span>: <span class="hljs-string">"public"</span>
<span class="hljs-attr">variants</span>: [&#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3795</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"9.99"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"白色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-均码"</span>&#125;,…]
<span class="hljs-number">0</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3795</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"9.99"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"白色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-均码"</span>&#125;
<span class="hljs-number">1</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3796</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"66.66"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"富贵色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"男士"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"男士-38"</span>&#125;
<span class="hljs-number">2</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3797</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"34.56"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"黄色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-41"</span>&#125;
<span class="hljs-number">3</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3798</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"34.56"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"黄色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-42"</span>&#125;
<span class="hljs-number">4</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3799</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"34.56"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"绿色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-41"</span>&#125;
<span class="hljs-number">5</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3800</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"34.56"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"绿色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-42"</span>&#125;
<span class="hljs-number">6</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3801</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"12.34"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"测试色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-测试均码"</span>&#125;
<span class="hljs-number">7</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3802</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"100.00"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"黑色"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"男士"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"男士-37"</span>&#125;
<span class="hljs-number">8</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3803</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"31.23"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"dsad"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"男士"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"男士-323"</span>&#125;
<span class="hljs-number">9</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3804</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"99.99"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"测试"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-41"</span>&#125;
<span class="hljs-number">10</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3805</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"99.99"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"测试"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-42"</span>&#125;
<span class="hljs-number">11</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">3806</span>, <span class="hljs-attr">price</span>: <span class="hljs-string">"99.99"</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"测试"</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">"通用"</span>, <span class="hljs-attr">size</span>: <span class="hljs-string">"通用-43"</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  下图是对应产品的详情页面：</p>
<p>         <img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/603930eea6734edea6649992ffa35f6f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  下图是根据产品详情接口的请求结果，渲染出的对应产品的sku页面：</p>
<p>          <img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a8b0d7972934e58b0e4ec3c994b0dbd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>解决思路：</strong></p>
<ul>
<li>
<p><strong>技术选型：</strong> 原生微信小程序MINA框架 + Vant Weapp</p>
</li>
<li>
<p><strong>组件化的开发思想：</strong></p>
</li>
</ul>
<p>  1. 产品详情页分为两个组件： 产品详情组件和底部导航组件。其中，底部导航组件又分为底部导航工具组件以及产品sku组件；</p>
<p>  2. 在底部导航组件中，为加入购物车按钮添加点击事件，使用有赞提供的Popup弹出层组件编写产品sku组件，并使用一个变量用于控制弹出层的显示与隐藏。同时可以在弹出层组件的关闭回调中做一些初始化操作，在后续的需求中会具体提到需要处理的初始化操作。</p>
<ul>
<li><strong>产品sku组件的渲染：</strong></li>
</ul>
<p>  1. 根据产品详情接口的请求结果，使用万能的flex和有赞提供的步进器组件布局。</p>
<p>  2.<code>需要特别注意颜色和尺码分类下的按钮渲染</code>。观察详情接口返回的<code>variants</code>数据不难发现，<strong>返回的颜色和尺寸数据有一部分是重合的。所以，不能直接对返回的数据进行循环渲染。需要对返回的数据做去重处理，否则显示在颜色和尺寸分类下的部分数据会存在数据重叠的情况，这显然是不合理的。</strong> 比如，<code>variants</code>的第10到第12条数据，测试这个颜色就重复了两次。<code>variants</code>的第4、6、11条数据，通用-42这个尺码就重复了两次。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"attribute-warp"</span>></span>
    颜色
<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex-button-warp stepper-warp"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">van-button</span>  
        <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;colors&#125;&#125;"</span>
        <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"id"</span> 
        <span class="hljs-attr">custom-class</span>=<span class="hljs-string">"color &#123;&#123;selectedColorId === item.id ? 'selected' : '' &#125;&#125;"</span>
        <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"handleColorClicked"</span>
        <span class="hljs-attr">data-color</span>=<span class="hljs-string">"&#123;&#123;item&#125;&#125;"</span>
        <span class="hljs-attr">disabled</span> = <span class="hljs-string">"&#123;&#123;!m1.hasTag(availableColorArray, item.color)&#125;&#125;"</span>
    ></span>
        &#123;&#123;item.color&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">van-button</span>></span>       
<span class="hljs-tag"></<span class="hljs-name">view</span>></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//监听传入的product数据，如果详情接口请求成功，且能够拿到详情数据，则使用集合过滤重复的颜色分类属性</span>
  <span class="hljs-attr">properties</span>: &#123;
    <span class="hljs-attr">product</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">observer</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Object</span>.keys(data).length > <span class="hljs-number">0</span>) &#123;
          <span class="hljs-built_in">this</span>.onClose()
          <span class="hljs-keyword">const</span> colors = <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">this</span>.data.product.variants.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.color))).map(<span class="hljs-function">(<span class="hljs-params">color, index</span>) =></span> (&#123;
            color,
            <span class="hljs-attr">id</span>: index
          &#125;))
          <span class="hljs-built_in">this</span>.setData(&#123;
            colors
          &#125;)
        &#125;
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">需求2：显示已选产品的属性</h3>
<p>  这个小需求其实由三部分组成，都是在点击时触发：</p>
<p>  1. <strong>显示已选产品的分类属性（点击时触发）：</strong></p>
<p>  如果没有选择产品的分类属性，提示语为请选择产品属性；如果选择了产品的分类属性，则将选择的产品分类属性在产品sku组件中显示出来。</p>
<p>          <img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3721a266b4f4cb3acecca35c75468b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>          <img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0920444c557f424db2186ac8b00a30a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  <strong>解决思路：</strong></p>
<p>  既然是分不同条件显示已选产品的分类属性，最容易想到的自然是MINA框架里面的<code>wx:if</code>和<code>wx:else</code>。于是可以设定判断条件，只要两个分类属性都没有被选中，就提示请选择产品属性，否则显示已选产品的分类属性。那么如何获取按钮里面的值呢？其实只需要在产品分类属性的点击事件中，通过自定义属性传入当前点击的对象，再获取里面的值显示到产品sku上就可以了。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"message"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; selectedColor === '' && selectedSize === ''&#125;&#125;"</span>></span>请选择产品属性<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">wx:else</span>></span>已选属性： &#123;&#123;selectedColor&#125;&#125; &#123;&#123;selectedSize&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  2. <strong>显示已选产品的价格属性（点击时触发）：</strong></p>
<p>  如果没有选择产品的分类属性或者选择的分类属性只有颜色属性或者尺码属性，显示的产品价格为返回的产品详情接口中的<code>lowest_price</code>字段；如果选中的分类属性包含了颜色属性和尺码属性，则会在返回的产品详情接口中的<code>variants</code>对象数组中去查找对应分类属性。如果能够找到对应分类属性的价格，则返回相应的价格，否则会报<code>价格字段不存在</code>的错误。因此需要做点击分类属性的属性关联，这个会在需求3中解决。</p>
<p>  <strong>解决思路：</strong></p>
<p>  逻辑是这样的：监听传入的<code>product</code>数据，只要接收到了这个数据或者弹出层被关闭的时候，就立刻初始化<code>currentPrice </code>的值，并将<code>product.lowest_price</code>的值赋给<code>currentPrice </code>。在产品分类属性的点击事件中，判断产品颜色分类属性和尺寸分类属性是否都有被选中。如果没有，则显示返回的产品详情接口中的<code>lowest_price</code>字段；如果都有被选中，则在<code>variants</code>中去查找选中分类属性对应的价格，如果找不到就会报<code>价格字段不存在</code>的错误。因此需要做点击分类属性的属性关联，这个会在需求3中解决。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"product-price-warp"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span>></span>￥<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"product-price"</span>></span>&#123;&#123; currentPrice &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  3. <strong>切换不同分类属性的逻辑（点击时触发）：</strong></p>
<p>  拿点击颜色分类属性举栗子。点击颜色分类属性之前，其实可以分为三种情况（最后有两种情况结果一样，可以归并为一类）：</p>
<ul>
<li>还没有任何颜色分类属性被选中，此时点击会直接激活选中颜色分类属性的样式；</li>
</ul>
<p>          <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8018d63a8baa4489bd311d5bebb6dc24~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>有颜色分类属性被选中且选中的颜色分类属性和要点击的颜色分类属性一致，此时点击会取消激活的颜色分类属性样式；</li>
</ul>
<p>          <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7b104ad2fc3417b9abe51766634aa8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>有颜色分类属性被选中且选中的颜色分类属性和要点击的颜色分类属性不一致，此时点击会取消之前激活的颜色分类属性样式，并激活当前选中颜色分类属性的样式。</li>
</ul>
<p>          <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/207cdf3e4a5f4c348443631d2750ee96~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  <strong>解决思路：</strong> 举选择颜色分类属性的栗子来说，可以使用一个变量判断当前颜色分类属性是否被选中，以及当前选中的颜色分类属性对应的id。这样就可以和当前点击的对象的id做比较，从而处理不同的判断逻辑。这也是为什么在需求1中重构详情接口返回的数据时，除了取分类属性名外，还要为它们分配id的原因。当然，在最后关闭弹出层的回调中，需要重置所选颜色分类属性的文字和id、所选尺码分类属性的文字和id。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">handleColorClicked</span>(<span class="hljs-params">e</span>)</span> &#123;
  <span class="hljs-comment">//此处如果不使用if条件判断，按钮依然可以点击</span>
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.data.availableColorArray.includes(e.currentTarget.dataset.color.color)) <span class="hljs-keyword">return</span>
  <span class="hljs-comment">//比较当前选中对象的id和当前点击对象的id</span>
  <span class="hljs-comment">//1.如果selectedSizeId === -1，则表明当前没有颜色分类属性被选中。此时点击需要将当前点击对象的id和值传过去，传id是为了进行下一次比较，传值是为了显示已选产品的分类属性。</span>
  <span class="hljs-comment">//2.如果选中的颜色分类属性id和当前点击对象的id不一致。此时点击除了会取消选中的颜色分类属性，还会激活当前选中颜色分类的样式（第一种情况和第二种情况是一样的）。</span>
  <span class="hljs-comment">//3.如果选中颜色分类属性的id和当前点击对象的id一致。此时点击会取消选中的颜色分类属性，相当于清空选中的颜色分类属性。</span>
  <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data.selectedColorId.length === <span class="hljs-number">0</span> || <span class="hljs-built_in">this</span>.data.selectedColorId !== e.currentTarget.dataset.color.id) &#123;
    <span class="hljs-keyword">const</span> availableSizeArray = <span class="hljs-built_in">this</span>.data.product.variants.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.color === e.currentTarget.dataset.color.color).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.size)
    <span class="hljs-built_in">this</span>.setData(&#123;
      <span class="hljs-attr">selectedColorId</span>: e.currentTarget.dataset.color.id,
      <span class="hljs-attr">selectedColor</span>: e.currentTarget.dataset.color.color,
      availableSizeArray
    &#125;)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data.selectedColorId === e.currentTarget.dataset.color.id) &#123;
    <span class="hljs-keyword">const</span> availableSizeArray = <span class="hljs-built_in">this</span>.data.sizes.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.size)
    <span class="hljs-built_in">this</span>.setData(&#123;
      <span class="hljs-attr">selectedColorId</span>: -<span class="hljs-number">1</span>,
      <span class="hljs-attr">selectedColor</span>: <span class="hljs-string">''</span>,
      availableSizeArray
    &#125;)
  &#125;
  <span class="hljs-built_in">this</span>.setSelectedPrice()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">需求3：处理点击不同分类按钮的属性关联问题</h3>
<p>  点击产品的颜色分类属性，会筛选产品的尺码分类属性，可用的显示，禁用的灰显且不可点击；取消选择对应的颜色分类属性后，产品的尺码分类属性会全部恢复为可用状态。点击产品的尺寸分类属性也是同样一个道理，所以需要为点击不同的分类按钮做属性关联。</p>
<p>  <strong>解决思路：</strong></p>
<p>  以点击颜色分类属性举例，聊一聊产品尺码分类属性的筛选原则。点击颜色分类属性后， 需要在产品的<code>variants</code>数据中，找到包含当前颜色分类属性的<code>variant</code>的<code>size</code>。这一个或多个size就是点击颜色分类属性后当前可用的<code>size</code>属性集，取反就是禁用的<code>size</code>属性集。因为在需求2中已经粘贴了点击事件的代码逻辑，此处就不再粘贴。</p>
<p>  这里有两处地方需要特别注意：1.使用<code>van-button</code>循环遍历分类数据后，<code>disabled</code>属性的禁用原则是先筛选出可用的属性集然后取反。如果先对当前点击的<code>color</code>属性取反，再通过可用的<code>color</code>属性集选取禁用的<code>size</code>属性集，可能会造成禁用的<code>size</code>属性集中包含当前点击的<code>color</code>属性对应的可用的<code>size</code>属性集；2.由于微信小程序不支持在函数中传参，因此在禁用条件中需要使用<code>wxs</code>语言来判断，不能使用<code>!availableColorArray.includes(item.color)</code>判断。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// wxs不支持es6语法</span>
<span class="hljs-comment">//使用两个逗号的原因是在于可能会有名字包含测试和测试色(一个颜色包含另外一个颜色的名称)这类情况</span>
<span class="hljs-comment">//可以对数组循环遍历，判断名字是否一样，如果一样，就返回true</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasTag</span>(<span class="hljs-params">tags, name</span>) </span>&#123;
  <span class="hljs-keyword">var</span> testStr = <span class="hljs-string">','</span> + tags.join(<span class="hljs-string">','</span>) + <span class="hljs-string">','</span> 
  <span class="hljs-keyword">return</span> testStr.indexOf(<span class="hljs-string">','</span> + name + <span class="hljs-string">','</span>) != -<span class="hljs-number">1</span>
&#125;

<span class="hljs-comment">// 导出</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">hasTag</span>: hasTag
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"attribute-warp"</span>></span>
    颜色
<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex-button-warp stepper-warp"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">van-button</span>  
        <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;colors&#125;&#125;"</span>
        <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"id"</span> 
        <span class="hljs-attr">custom-class</span>=<span class="hljs-string">"color &#123;&#123;selectedColorId === item.id ? 'selected' : '' &#125;&#125;"</span>
        <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"handleColorClicked"</span>
        <span class="hljs-attr">data-color</span>=<span class="hljs-string">"&#123;&#123;item&#125;&#125;"</span>
        <span class="hljs-attr">disabled</span> = <span class="hljs-string">"&#123;&#123;!m1.hasTag(availableColorArray, item.color)&#125;&#125;"</span>
    ></span>
        &#123;&#123;item.color&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">van-button</span>></span>       
<span class="hljs-tag"></<span class="hljs-name">view</span>></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">代码整合</h3>
<p> utils\helper.wxs:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 不支持es6语法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasTag</span>(<span class="hljs-params">tags, name</span>) </span>&#123;
  <span class="hljs-keyword">var</span> testStr = <span class="hljs-string">','</span> + tags.join(<span class="hljs-string">','</span>) + <span class="hljs-string">','</span> 
  <span class="hljs-keyword">return</span> testStr.indexOf(<span class="hljs-string">','</span> + name + <span class="hljs-string">','</span>) != -<span class="hljs-number">1</span>
&#125;

<span class="hljs-comment">// 导出</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">hasTag</span>: hasTag
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> components\common\popup\index.wxml:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">wxs</span>
  <span class="hljs-attr">src</span>=<span class="hljs-string">"../../../utils/helper.wxs"</span>
  <span class="hljs-attr">module</span>=<span class="hljs-string">"m1"</span>
/></span>
<span class="hljs-tag"><<span class="hljs-name">van-popup</span>
  <span class="hljs-attr">closeable</span>
  <span class="hljs-attr">show</span>=<span class="hljs-string">"&#123;&#123; visible &#125;&#125;"</span>
  <span class="hljs-attr">position</span>=<span class="hljs-string">"bottom"</span>
  <span class="hljs-attr">custom-class</span>=<span class="hljs-string">"popup"</span>
  <span class="hljs-attr">bind:close</span>=<span class="hljs-string">"onClose"</span>
></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex-warp"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"product-picture"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">base-image</span>
                <span class="hljs-attr">width</span>=<span class="hljs-string">"182rpx"</span>
                <span class="hljs-attr">height</span>=<span class="hljs-string">"182rpx"</span>
                <span class="hljs-attr">class</span>=<span class="hljs-string">"product-image"</span>
                <span class="hljs-attr">src</span>=<span class="hljs-string">"&#123;&#123;product.images[0]&#125;&#125;"</span>
            /></span> 
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"product-explain"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"product-price-warp"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">view</span>></span>￥<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"product-price"</span>></span>&#123;&#123; currentPrice &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"message"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; selectedColor === '' && selectedSize === ''&#125;&#125;"</span>></span>请选择产品属性<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">wx:else</span>></span>已选属性： &#123;&#123;selectedColor&#125;&#125; &#123;&#123;selectedSize&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>    
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"attribute-warp"</span>></span>
        颜色
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex-button-warp stepper-warp"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">van-button</span>  
            <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;colors&#125;&#125;"</span>
            <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"id"</span> 
            <span class="hljs-attr">custom-class</span>=<span class="hljs-string">"color &#123;&#123;selectedColorId === item.id ? 'selected' : '' &#125;&#125;"</span>
            <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"handleColorClicked"</span>
            <span class="hljs-attr">data-color</span>=<span class="hljs-string">"&#123;&#123;item&#125;&#125;"</span>
            <span class="hljs-attr">disabled</span> = <span class="hljs-string">"&#123;&#123;!m1.hasTag(availableColorArray, item.color)&#125;&#125;"</span>
        ></span>
            &#123;&#123;item.color&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">van-button</span>></span>       
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"attribute-warp"</span>></span>
        尺码
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex-button-warp stepper-warp"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">van-button</span>  
            <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;sizes&#125;&#125;"</span>
            <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"id"</span> 
            <span class="hljs-attr">custom-class</span>=<span class="hljs-string">"color &#123;&#123;selectedSizeId === item.id ? 'selected' : '' &#125;&#125;"</span>
            <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"handleSizeClicked"</span>
            <span class="hljs-attr">data-size</span>=<span class="hljs-string">"&#123;&#123;item&#125;&#125;"</span>
            <span class="hljs-attr">disabled</span> = <span class="hljs-string">"&#123;&#123;!m1.hasTag(availableSizeArray, item.size)&#125;&#125;"</span>
        ></span>
            &#123;&#123;item.size&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">van-button</span>></span>    
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"attribute-warp"</span>></span>
        数量
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"stepper-warp"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">van-stepper</span> 
            <span class="hljs-attr">max</span>=<span class="hljs-string">"10000"</span>
            <span class="hljs-attr">value</span>=<span class="hljs-string">"&#123;&#123; value &#125;&#125;"</span> 
            <span class="hljs-attr">async-change</span> 
            <span class="hljs-attr">bind:change</span>=<span class="hljs-string">"onChange"</span> 
            <span class="hljs-attr">input-class</span>=<span class="hljs-string">"stepper-input"</span>
            <span class="hljs-attr">plus-class</span>=<span class="hljs-string">"stepper-operation"</span>
            <span class="hljs-attr">minus-class</span>=<span class="hljs-string">"stepper-operation"</span>
        /></span>
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"handleConfirmed"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"confirm-button"</span>></span>确定<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="hljs-tag"></<span class="hljs-name">van-popup</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p> components\common\popup\index.wxss:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.popup</span> &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#FFFFFF</span>;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0px</span> -<span class="hljs-number">4px</span> <span class="hljs-number">8px</span> <span class="hljs-number">0px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.06</span>);
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">20px</span> <span class="hljs-number">20px</span> <span class="hljs-number">0px</span> <span class="hljs-number">0px</span>;
&#125;

<span class="hljs-selector-class">.flex-warp</span> &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">41</span>rpx <span class="hljs-number">17</span>rpx <span class="hljs-number">51</span>rpx <span class="hljs-number">32</span>rpx;
    <span class="hljs-attribute">display</span>: flex;
&#125;

<span class="hljs-selector-class">.product-expalin</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">flex-direction</span>: column;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">17</span>rpx;
&#125;
<span class="hljs-selector-class">.product-price-warp</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">39</span>rpx;
    <span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">36</span>rpx;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">34</span>rpx;
    <span class="hljs-attribute">font-weight</span>: bold;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#FA5151</span>;
&#125;
<span class="hljs-selector-class">.message</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30</span>rpx;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#7A7A7A</span>;
&#125;
<span class="hljs-selector-class">.attribute-warp</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30</span>rpx;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#181818</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">47</span>rpx <span class="hljs-number">0</span> <span class="hljs-number">20</span>rpx <span class="hljs-number">33</span>rpx;
&#125;
<span class="hljs-selector-class">.confirm-button</span> &#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">62</span>rpx;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">80</span>rpx;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">80</span>rpx;
    <span class="hljs-attribute">text-align</span>: center;
    <span class="hljs-attribute">font-size</span>:<span class="hljs-number">30</span>rpx;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#FA5151</span>;
&#125;
<span class="hljs-selector-class">.stepper-input</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">166</span>rpx;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">80</span>rpx;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30</span>rpx;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#181818</span>;
&#125;
<span class="hljs-selector-class">.stepper-operation</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">87</span>rpx;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">80</span>rpx;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#F2F2F2</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">10</span>rpx;
&#125;
<span class="hljs-selector-class">.stepper-warp</span> &#123;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">30</span>rpx;
&#125;
<span class="hljs-selector-class">.flex-button-warp</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">flex-wrap</span>: wrap;
&#125;
<span class="hljs-selector-class">.color</span> &#123;
    <span class="hljs-attribute">min-width</span>: <span class="hljs-number">200</span>rpx;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">80</span>rpx;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#F2F2F2</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">40</span>rpx;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30</span>rpx;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#181818</span>;
    <span class="hljs-attribute">text-align</span>: center;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">80</span>rpx;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">20</span>rpx <span class="hljs-number">10</span>rpx <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-class">.product-explain</span> &#123;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">17</span>rpx;
&#125;
<span class="hljs-selector-class">.selected</span> &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#FFFFFF</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">2</span>rpx solid <span class="hljs-number">#181818</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> components\common\popup\index.js:</p>
<pre><code class="hljs language-js copyable" lang="js">Component(&#123;
  <span class="hljs-comment">/**
   * 组件的属性列表
   */</span>
  <span class="hljs-attr">properties</span>: &#123;
    <span class="hljs-attr">product</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">observer</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Object</span>.keys(data).length > <span class="hljs-number">0</span>) &#123;
          <span class="hljs-built_in">this</span>.onClose()
          <span class="hljs-keyword">const</span> colors = <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">this</span>.data.product.variants.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.color))).map(<span class="hljs-function">(<span class="hljs-params">color, index</span>) =></span> (&#123;
            color,
            <span class="hljs-attr">id</span>: index
          &#125;))
          <span class="hljs-keyword">const</span> sizes = <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">this</span>.data.product.variants.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.size))).map(<span class="hljs-function">(<span class="hljs-params">size, index</span>) =></span> (&#123;
            size,
            <span class="hljs-attr">id</span>: index
          &#125;))
          <span class="hljs-built_in">this</span>.setData(&#123;
            colors,
            sizes
          &#125;)
        &#125;
      &#125;
    &#125;,
    <span class="hljs-attr">visible</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>
    &#125;
  &#125;,
  <span class="hljs-comment">/**
   * 组件的初始数据
   */</span>
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">selectedColor</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">selectedSize</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">currentPrice</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">colors</span>: &#123;&#125;,
    <span class="hljs-attr">sizes</span>: &#123;&#125;,
    <span class="hljs-attr">selectedColorId</span>: -<span class="hljs-number">1</span>,
    <span class="hljs-attr">selectedSizeId</span>: -<span class="hljs-number">1</span>,
    <span class="hljs-attr">availableSizeArray</span>: [],
    <span class="hljs-attr">availableColorArray</span>: []
  &#125;,
  <span class="hljs-comment">/**
   * 组件的方法列表
   */</span>
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">handleConfirmed</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.setData(&#123;
        <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>
      &#125;)     
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data.selectedColor !== <span class="hljs-string">''</span> && <span class="hljs-built_in">this</span>.data.selectedSize !== <span class="hljs-string">''</span>) &#123;
        <span class="hljs-comment">//全部选中且校验成功时调用</span>
        <span class="hljs-built_in">this</span>.onClose()
        wx.showToast(&#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'加入购物车成功'</span>,
          <span class="hljs-attr">icon</span>: <span class="hljs-string">'success'</span>,
          <span class="hljs-attr">duration</span>: <span class="hljs-number">2000</span>
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//未全部选中时调用</span>
        wx.showToast(&#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'请选择商品属性'</span>,
          <span class="hljs-attr">icon</span>: <span class="hljs-string">'none'</span>,
          <span class="hljs-attr">duration</span>: <span class="hljs-number">2000</span>
        &#125;); 
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">onChange</span>(<span class="hljs-params">event</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.setData(&#123;
        <span class="hljs-attr">value</span>: event.detail
      &#125;)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">onClose</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> availableSizeArray = <span class="hljs-built_in">this</span>.data.product.variants.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.size)
      <span class="hljs-keyword">const</span> availableColorArray = <span class="hljs-built_in">this</span>.data.product.variants.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.color)
      <span class="hljs-built_in">this</span>.setData(&#123;
        <span class="hljs-attr">currentPrice</span>: <span class="hljs-built_in">this</span>.data.product.lowest_price,
        <span class="hljs-attr">visible</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">selectedColor</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">selectedSize</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">selectedColorId</span>: -<span class="hljs-number">1</span>,
        <span class="hljs-attr">selectedSizeId</span>: -<span class="hljs-number">1</span>,
        availableSizeArray,
        availableColorArray
      &#125;)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">setSelectedPrice</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> currentPrice
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data.selectedColor !== <span class="hljs-string">''</span> && <span class="hljs-built_in">this</span>.data.selectedSize !== <span class="hljs-string">''</span>) &#123;
        currentPrice = <span class="hljs-built_in">this</span>.data.product.variants.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.size === <span class="hljs-built_in">this</span>.data.selectedSize && item.color === <span class="hljs-built_in">this</span>.data.selectedColor).price
      &#125; <span class="hljs-keyword">else</span> &#123;
        currentPrice = <span class="hljs-built_in">this</span>.data.product.lowest_price
      &#125;
      <span class="hljs-built_in">this</span>.setData(&#123;
        currentPrice
      &#125;) 
    &#125;,
    <span class="hljs-function"><span class="hljs-title">handleSizeClicked</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-comment">//此处如果不使用if条件判断，按钮依然可以点击</span>
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.data.availableSizeArray.includes(e.currentTarget.dataset.size.size)) <span class="hljs-keyword">return</span>
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data.selectedSizeId === -<span class="hljs-number">1</span> || <span class="hljs-built_in">this</span>.data.selectedSizeId !== e.currentTarget.dataset.size.id) &#123;
        <span class="hljs-keyword">const</span> availableColorArray = <span class="hljs-built_in">this</span>.data.product.variants.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.size === e.currentTarget.dataset.size.size).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.color)
        <span class="hljs-built_in">this</span>.setData(&#123;
          <span class="hljs-attr">selectedSizeId</span>: e.currentTarget.dataset.size.id,
          <span class="hljs-attr">selectedSize</span>: e.currentTarget.dataset.size.size,
          availableColorArray
        &#125;)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data.selectedSizeId === e.currentTarget.dataset.size.id) &#123;
        <span class="hljs-keyword">const</span> availableColorArray = <span class="hljs-built_in">this</span>.data.colors.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.color)
        <span class="hljs-built_in">this</span>.setData(&#123;
          <span class="hljs-attr">selectedSizeId</span>: -<span class="hljs-number">1</span>,
          <span class="hljs-attr">selectedSize</span>: <span class="hljs-string">''</span>,
          availableColorArray
        &#125;)
      &#125;
      <span class="hljs-built_in">this</span>.setSelectedPrice()
    &#125;,
    <span class="hljs-comment">//禁用存在一对多的问题，不能直接使用该禁用的，只能使用未禁用的，然后再对未禁用的进行取反</span>
    <span class="hljs-function"><span class="hljs-title">handleColorClicked</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-comment">//此处如果不使用if条件判断，按钮依然可以点击</span>
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.data.availableColorArray.includes(e.currentTarget.dataset.color.color)) <span class="hljs-keyword">return</span>
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data.selectedColorId.length === <span class="hljs-number">0</span> || <span class="hljs-built_in">this</span>.data.selectedColorId !== e.currentTarget.dataset.color.id) &#123;
        <span class="hljs-keyword">const</span> availableSizeArray = <span class="hljs-built_in">this</span>.data.product.variants.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.color === e.currentTarget.dataset.color.color).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.size)
        <span class="hljs-built_in">this</span>.setData(&#123;
          <span class="hljs-attr">selectedColorId</span>: e.currentTarget.dataset.color.id,
          <span class="hljs-attr">selectedColor</span>: e.currentTarget.dataset.color.color,
          availableSizeArray
        &#125;)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.data.selectedColorId === e.currentTarget.dataset.color.id) &#123;
        <span class="hljs-keyword">const</span> availableSizeArray = <span class="hljs-built_in">this</span>.data.sizes.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.size)
        <span class="hljs-built_in">this</span>.setData(&#123;
          <span class="hljs-attr">selectedColorId</span>: -<span class="hljs-number">1</span>,
          <span class="hljs-attr">selectedColor</span>: <span class="hljs-string">''</span>,
          availableSizeArray
        &#125;)
      &#125;
      <span class="hljs-built_in">this</span>.setSelectedPrice()
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p> components\common\popup\index.json:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"component"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"usingComponents"</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">写在最后</h2>
<p>  由于代码写得比较仓促，本文的代码逻辑还是比较复杂，而且存在大量的重复代码，有时间和兴趣的小伙伴可以使用组件化的思想重新编写代码。年少轻狂，总以为天下事，无可不为，岁月蹉跎，终感到天下人力有尽头。单纯无知，总认为目光内，皆为好人，时间流转，终叹息社会人笑里藏刀。社会很大，人心很复杂，一路走来，背最黑的铁锅，闹最大的笑话。塞翁失马，焉知非福，惋惜之余也庆幸自己遇到了这么好的妈，希望自己能保持本心，不被社会改变。</p>
<hr>
<p>                              <strong>学习&总结</strong></p>
<hr></div>  
</div>
            