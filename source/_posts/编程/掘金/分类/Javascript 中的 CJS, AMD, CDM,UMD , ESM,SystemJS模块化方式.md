
---
title: 'Javascript 中的 CJS, AMD, CDM,UMD , ESM,SystemJS模块化方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b4ace2f8f44041b15eff53da2f2dd2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 04:47:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b4ace2f8f44041b15eff53da2f2dd2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">CJS</h1>
<p>commonJS的主要实现者是Node.js。通过exports和require</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b4ace2f8f44041b15eff53da2f2dd2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>commonJS模块的加载不适合网络加载，依赖的模块未加载会出现错误</strong></p>
<h1 data-id="heading-1">AMD（Asynchronous Module Definition-异步模块定义）</h1>
<p>定义模块define(id?, dependencies?, factory)</p>
<p>主要实现者：requireJS</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9113651a1fa048f9a8446d6f2c28fb3c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">CMD（Common Module Definition - 通用模块定义）</h1>
<p>实现：SeaJS</p>
<p>AMD的优化版</p>
<ul>
<li>AMD是依赖前置，提前加载依赖；CMD依赖后置，使用时才加载</li>
<li>require.js已经提供来延迟加载功能</li>
</ul>
<h1 data-id="heading-3">UMD（Universal Module Definition - 通用模块定义）</h1>
<p>CommonJS侧重服务器，而AMD侧重于浏览器，两者的模块不能共享</p>
<p>UMD的思想很简单</p>
<p>判断是AMD则使用AMD方式</p>
<p>是commonJS则使用CommonJS方式</p>
<p>都不是则将模块公开给全局（window或global）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcc0b8509f904b918c3587894d84f968~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">ESM</h1>
<p><code>ESM</code> 代表 <code>ES</code> 模块。这是 <code>Javascript</code> 提出的实现一个标准模块系统的方案。
如下：</p>
<pre><code class="copyable">import vue from 'vue';
import &#123;foo, bar&#125; from './myLib';
...

export default function() &#123;
  // your Function
&#125;;
export const function1() &#123;...&#125;;
export const function2() &#123;...&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">SystemJS</h1>
<p>SystemJS是一个通用的模块加载器，它能在浏览器或者NodeJS上动态加载模块</p>
<p>并且支持CommonJS、AMD、全局模块对象和ES6模块。通过使用插件，它不仅可以加载Js，还可以加载CoffeeScript和TypeScript。</p>
<p>SystemJS的另一个优点是，它建立在ES6模块加载器之上，所以它的语法和API在将来很可能是语言的一部分，这会让我们的代码更不会过时。</p>
<p>AngularJS里面就会使用</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d870a9b19f144428453f7c81fae6060~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">相关图片</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89750a25862a480486759799f74fa159~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/208c6020e2364b09829b1b6c1a9880b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>参考资料：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1at411q7Rk%3Ffrom%3Dsearch%26seid%3D888451372670607979" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1at411q7Rk?from=search&seid=888451372670607979" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1at…</a></li>
<li><a href="https://juejin.cn/post/6935973925004247077#heading-1" target="_blank" title="https://juejin.cn/post/6935973925004247077#heading-1">juejin.cn/post/693597…</a></li>
<li><a href="https://juejin.cn/post/6844903983987834888" target="_blank" title="https://juejin.cn/post/6844903983987834888">juejin.cn/post/684490…</a></li>
<li><a href="https://juejin.cn/post/6844904066233925639" target="_blank" title="https://juejin.cn/post/6844904066233925639">juejin.cn/post/684490…</a></li>
</ul></div>  
</div>
            