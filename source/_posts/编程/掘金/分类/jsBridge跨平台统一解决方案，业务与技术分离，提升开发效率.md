
---
title: 'jsBridge跨平台统一解决方案，业务与技术分离，提升开发效率'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7919'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 04:50:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=7919'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">概述</h3>
<p>在混合模式移动应用开发中，为了实现h5自身不具备的功能，不可避免的会产生h5与原生的交互。但是h5跟原生是不相通，他们之间的联系是通过一座桥来进行联系，这就是jsBridge。</p>
<p>至于jsBridge的实现原理，网上各种介绍的文章比比皆是，这里不再赘述，这也不是本文的重点。本文的重点是介绍jsBridge 在开发中的解决方案，怎样用最舒服的姿势来使用jsBridge。</p>
<h3 data-id="heading-1">插件</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40zebing%2Fjs-bridge" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@zebing/js-bridge" ref="nofollow noopener noreferrer">@zebing/js-bridge</a> 插件是适配多平台的jsBridge交互插件，目前已经在android，ios以及windows qt开发的应用中使用，效果显著。极大的解决了各平台之间的差异，以及本地开发原生接口不可调试的问题。</p>
<h3 data-id="heading-2">使用</h3>
<p><strong>1. 默认交互方案</strong></p>
<p>插件默认提供了无感使用的方案，只针对android和ios,只要h5跟native端遵循以下规则。</p>
<p>native端：</p>
<pre><code class="copyable">// android
// 将方法注入到 window.jsBridgeMethods 中

// ios
// 通过 messageHandlers 进行交互
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>android和ios两端方法接收到的参数是一个json字符串，格式如下：</p>
</blockquote>
<pre><code class="copyable">&#123;
    xxx: "参数1"，
    xxx: "参数2",
    ...
    callback?: "回调函数名称", // 通过window[callbackName] 进行回调
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>h5端：</strong></p>
<pre><code class="copyable">import jsBridge from '@zebing/js-bridge';

// test 为调用的方法名
jsBridge.test(&#123;
    xxx: '参数1'，
    xxx: '参数2',
    callback: function () &#123;&#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 自定义适配器交互方案</strong></p>
<p>如果默认交互方案不满足，可以自定义适配器进行交互。通过调用create 进行初始化。以安卓端为例，如下：</p>
<pre><code class="copyable">import &#123; create, register &#125; from '@zebing/js-bridge'
const JsBridge = create([&#123;
  platform () &#123;
    if (typeof window !== 'object') &#123;
      return false;
    &#125;

    const userAgent = window.navigator.userAgent;
    return userAgent.indexOf('Android') > -1 || userAgent.indexOf('Adr') > -1;
  &#125;,

  support (name) &#123;
    const apis = window['jsBridgeMethods'] || &#123;&#125;;
    const support = Object.prototype.toString.call(apis[name]) === '[object Function]';

    return support;
  &#125;,

  run (name, options) &#123;
    
    window.jsBridgeMethods[name](JSON.stringify(options));
  &#125;
&#125;]);

jsBridge.test(&#123;
  xxx: '参数1'，
  xxx: '参数2',
  callback: function () &#123;&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>create 接收一个数组，可传入多个适配器。一个平台只会使用一个符合条件的适配器。即使传入的适配器有多个符合，后面的会忽略。</p>
<p>适配器必须满足以下条件：</p>
<ol>
<li>platform 方法，用以判断是否适用当前平台。</li>
<li>support 方法， 用以判断要调用的方法是否可调用。</li>
<li>run 方法，用以执行调用原生方法进行交互。</li>
</ol>
<blockquote>
<p>用户与原生交互不能使用 platform, support, run 三个方法名</p>
</blockquote>
<h3 data-id="heading-3">3. 本地开发调试</h3>
<p>本地开发调试这也是本插件的一大特色。具体如下：
在根目录下新建文件js-bridge.methods.js文件</p>
<pre><code class="copyable">// js-bridge.methods.js 文件内容
module.exports = &#123;
  test (options) &#123;
    const &#123; id, callback &#125; = JSON.parse(options);
    window[callback](&#123; id, result: 'test ok' &#125;);
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后新建js-bridge.js文件通过create创建实例</p>
<pre><code class="copyable">import &#123; create &#125; from '@zebing/js-bridge';

const adapter = [];

// 本地开发模拟原生交互
if (process.env.BUILD_ENV === 'development') &#123;
  const bridgeMethods = require(`../../bridge.methods.js`);

  if (process.client) &#123;
    window.jsBridgeMethods = bridgeMethods;
    adapter.push(&#123;
      platform: () => true, 

      support: (name) => typeof (window.jsBridgeMethods || &#123;&#125;)[name] === 'function',

      run (name, options) &#123;
        window.jsBridgeMethods[name](JSON.stringify(options));
      &#125;
    &#125;)
  &#125;
&#125;

// 安卓jsBridge适配器，ios使用默认适配器
adapter.push(&#123;
  platform () &#123;
    if (typeof window !== 'object') &#123;
      return false;
    &#125;

    const userAgent = window.navigator.userAgent;
    return userAgent.indexOf('Android') > -1 || userAgent.indexOf('Adr') > -1;
  &#125;, 

  support: (name) => typeof (window.jsBridgeMethods || &#123;&#125;)[name] === 'function',

  run (name, options) &#123;
    window.jsBridgeMethods[name](JSON.stringify(options));
  &#125;
&#125;)

export default create(adapter);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后引入jsBridge进行调用</p>
<pre><code class="copyable">import jsBridge from 'js-bridge.js'

jsBridge.test(&#123;
  xxx: '参数1'，
  xxx: '参数2',
  callback: function () &#123;&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4. 使用Promise代替callback</h3>
<pre><code class="copyable">jsBridge.test(&#123;
  xxx: '参数1'，
  xxx: '参数2',
  callback: function () &#123;&#125;
&#125;)

可改为

jsBridge.test(&#123;
  xxx: '参数1'，
  xxx: '参数2',
  callback: true,
&#125;).then((result) => &#123;

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">5. 兼容安卓4.4 及以下低端机</h3>
<p>由于 <code>jsBridge.test</code> 调用方式采用了Proxy代理，因此会存在安卓4.4 及以下低端机不兼容的问题。但是提供了兼容的方案。如下：</p>
<pre><code class="copyable">// 将调用方式
jsBridge.test(&#123;
  xxx: '参数1'，
  xxx: '参数2',
  callback: function () &#123;&#125;
&#125;)

替换成
jsBridge.run('test', &#123;
  xxx: '参数1'，
  xxx: '参数2',
  callback: function () &#123;&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            