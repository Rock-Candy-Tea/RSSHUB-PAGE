
---
title: '前端服务可维护性差？最低成本拆解EGG服务实践分享'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5150a2cdf39448ba94777d2f16fb2027~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 07:31:22 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5150a2cdf39448ba94777d2f16fb2027~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是曹俊_Eren。本文可能更适用于有多人协作开发的中大型项目，当然如果你的项目因为各种原因导致代码文件杂乱无章，也是适用。</p>
<p>Ryan Dahl自 2009 年创造出 nodejs 距今已经12年，业界已经有很多成熟的框架，比如express、koa、egg等。在编写服务端代码时，往往都会划分出<code>router</code>层、<code>controller</code>层和<code>service</code>层，当然也会有一些其他层，比如<code>model</code>层和<code>view</code>层。</p>
<ul>
<li>router: 监听页面的路由,并调用Controller层的路由处理函数</li>
<li>controller: 给Router层提供服务,调用Service层提供的数据处理</li>
<li>service: 实现具体的功能</li>
</ul>
<p><strong>router像是前台，根据顾客的需求指引进店；controller像是服务员，为顾客点菜下单是她的工作；service就是厨师，菜的味道好不好都由他决定。</strong></p>
<p>如上面所说的，笔者在服务端中建好router、controllr、service三个文件夹，将各个业务模块的代码分别存放到里面，这种方式简单快捷，很适合项目的快速起步。后来团队的开发者慢慢增多，接近有4～5个人开发这个项目。</p>
<p>一起来看下这个项目的整体结构</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5150a2cdf39448ba94777d2f16fb2027~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到应用app下有controller、service和router，是很典型的单体应用。然后展开controller目录可以看到</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69dda403e54f4b5c88ed84fc17d46b19~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现有很多不同的模块（抑或是功能？）聚合在里面。</p>
<p>我来简单概括下上图的问题：</p>
<p>首先，这个项目<strong>没有严格的模块划分</strong>，每个组员按照各自的理解创建目录和文件，久而久之架构混乱，已经嗅到腐烂的气息。一个模块的controller、service文件各自在一个大型的目录下，在开发一个模块时要跨越整个项目的多个目录，开发体验不好。</p>
<p>其次，<strong>没有区分公共代码和业务代码</strong>，开发者想查找、调用一些通用逻辑时比较困难，新人学习成本高。</p>
<p>每个开发者的工作习惯都不一样，对模块的划分理解不一样。新开发者可能没有意识到文件目录的命名规范，在编写工具类时也可能没有注意到公共内容和业务内容的分离。</p>
<p><strong>通过口口相传的规范无法彻底被执行</strong>，也就是我们所谓的“部落知识”（在一个组织里面独有的知识）。开发者造成混乱没有局限在一定范围的话，最后可能需要重构整个项目。</p>
<p>上述问题，归根到底在于<strong>系统架构不清晰</strong>，<strong>缺乏模块的划分或者模块划分不明确</strong>，聚度低、高耦合。</p>
<p>试想，如果我们将项目划分为多个模块，在开发某个模块时，在它的目录下就可以完成所有功能。如果出现的坏代码，只需要重构模块所在目录，而不需要重构整个项目，会不会更好呢？</p>
<h3 data-id="heading-0">好的设计</h3>
<p>微服务、领域驱动设计是很流行的话题，但前端服务的复杂度往往不高。如果拆分成多个服务，不仅需要<strong>投入大量人力成本</strong>，还可能会发现每个服务都比较“<strong>单薄</strong>”，很多时候稍庞大的前端服务都是“<strong>比上不足不下有余</strong>”。</p>
<p>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftech.meituan.com%2F2017%2F12%2F22%2Fddd-in-practice.html" target="_blank" rel="nofollow noopener noreferrer" title="https://tech.meituan.com/2017/12/22/ddd-in-practice.html" ref="nofollow noopener noreferrer">领域驱动设计在互联网业务开发中的实践</a>中详细讲解微服务是如何拆分的，里面提到的“分治”思想可能对前端服务提高可维护性有帮助。</p>
<blockquote>
<p><strong>分治</strong> 把问题空间分割为规模更小且易于处理的若干子问题。分割后的问题需要足够小，以便一个人单枪匹马就能够解决他们；其次，必须考虑如何将分割后的各个部分装配为整体。分割得越合理越易于理解，在装配成整体时，所需跟踪的细节也就越少。即更容易设计各部分的协作方式。评判什么是分治得好，即高内聚低耦合。</p>
</blockquote>
<p>因此根据业务需求，设计业务模块以及它们之间的关系非常重要。当系统越来越庞大，每一个模块会越发接近一个<strong>微型应用</strong>。多人协作时，每个人负责会有各自模块，如果每个模块都是一个微型应用，每个人可以在模块里面完成所有功能的开发，是一件很有趣的事情。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7db50afdffd6427881857ca19a388873~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果某个业务因为频繁变化而导致代码腐烂，也仅仅是重构这个模块即可，对其他模块没有影响。</p>
<h3 data-id="heading-1">egg框架</h3>
<p>笔者的项目使用的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Feggjs.org%2Fzh-cn%2Fintro%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://eggjs.org/zh-cn/intro/index.html" ref="nofollow noopener noreferrer">egg.js</a> 框架，这是它的设计原则之一</p>
<blockquote>
<p>按照约定进行开发，奉行『约定优于配置』</p>
</blockquote>
<p>egg 可以自动抓取 router 、controller、service、middleware 等目录下的文件，将方法挂载在特定上下文变量。</p>
<p>默认的目录结构是这样的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a83761f476c41ef8e197386bfc0b35a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是一种大单体应用的结构，不好划分模块。<strong>怎么样通过工程化手段，把单体应用划分成多个微型应用了？</strong></p>
<p><code>egg</code> 有一个很好的功能是可以定制上层框架，详情可以参考官网章节 <a href="https://link.juejin.cn/?target=https%3A%2F%2Feggjs.org%2Fzh-cn%2Fadvanced%2Fframework.html" target="_blank" rel="nofollow noopener noreferrer" title="https://eggjs.org/zh-cn/advanced/framework.html" ref="nofollow noopener noreferrer">框架开发</a> ，接下来深入了解一下</p>
<h3 data-id="heading-2">微应用的实现</h3>
<p>要实现单体应用划分成多个微型应用的需求，需要使用到egg提供的<strong>框架继承</strong>和<strong>自定义加载器</strong>的功能。</p>
<h4 data-id="heading-3">框架继承</h4>
<p>首先需要创建一个npm应用，项目包含下面文件和代码</p>
<pre><code class="copyable">// package.json
&#123;
  "name": "my-framework",
  "dependencies": &#123;
    "egg": "^2.0.0"
  &#125;
&#125;

// index.js
module.exports = require('./lib/framework.js');

// lib/framework.js
const path = require('path');
const egg = require('egg');
const EGG_PATH = Symbol.for('egg#eggPath');

class Application extends egg.Application &#123;
  get [EGG_PATH]() &#123;
    // 返回 framework 路径
    return path.dirname(__dirname);
  &#125;
&#125;

// 覆盖了 Egg 的 Application
module.exports = Object.assign(egg, &#123;
  Application,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在我们的服务应用中，通过<strong>package.json</strong>引入</p>
<pre><code class="copyable">// package.json
&#123;
  "scripts": &#123;
    "dev": "egg-bin dev"
  &#125;,
  "egg": &#123;
    "framework": "my-framework"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以实现一个框架的继承，但依旧没有实现我们需要的功能。我们可以利用继承的特性，<strong>重写</strong>现有egg提供的功能。</p>
<h4 data-id="heading-4">自定义加载器</h4>
<p>egg之所以可以自动抓取目录下的文件，是因为它的<strong>加载器(Loader)</strong>。如果想要自动抓取模块下的目录，就需要定制egg的文件加载功能。</p>
<p>可以通过继承 <strong>Loader</strong> 类，重写它的方法，进而实现<strong>自定义文件加载</strong>。</p>
<pre><code class="copyable">// lib/framework.js
const path = require('path');
const egg = require('egg');
const EGG_PATH = Symbol.for('egg#eggPath');

+ class MyAppWorkerLoader extends egg.AppWorkerLoader &#123; // AppWorkerLoader 是什么呢?
+   load() &#123;
+     super.load();
+     // 自己扩展
+   &#125;
+ &#125;

class Application extends egg.Application &#123;
  get [EGG_PATH]() &#123;
    // 返回 framework 路径
    return path.dirname(__dirname);
  &#125;
  // 覆盖 Egg 的 Loader，启动时使用这个 Loader
  get [EGG_LOADER]() &#123;
    return YadanAppWorkerLoader;
  &#125;
&#125;

// 覆盖了 Egg 的 Application
module.exports = Object.assign(egg, &#123;
  Application,
+   // 自定义的 Loader 也需要 export，上层框架需要基于这个扩展
+   AppWorkerLoader: MyAppWorkerLoader,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中的 <strong>AppWorkerLoader</strong> 继承于 <strong>Loader</strong> 基类，在官网的<a href="https://link.juejin.cn/?target=https%3A%2F%2Feggjs.org%2Fzh-cn%2Fadvanced%2Floader.html%23%25E6%2589%25A9%25E5%25B1%2595-loader" target="_blank" rel="nofollow noopener noreferrer" title="https://eggjs.org/zh-cn/advanced/loader.html#%E6%89%A9%E5%B1%95-loader" ref="nofollow noopener noreferrer">加载器</a>章节中说到 <strong>Loader</strong> 有下面方法：</p>
<ul>
<li>loadPlugin()：加载插件</li>
<li>loadConfig()：加载配置</li>
<li>loadAgentExtend()：加载agent对象的extend对象</li>
<li>loadApplicationExtend()：加载app对象的extend对象</li>
<li>loadRequestExtend(): 加载request对象</li>
<li>loadResponseExtend()：加载response对象</li>
<li>loadContextExtend(): 加载context对象</li>
<li>loadHelperExtend(): 加载工具方法</li>
<li>loadCustomAgent(): 加载定义的agent对象</li>
<li>loadCustomApp(): 加载定义的app对象</li>
<li>loadService(): 加载service</li>
<li>loadMiddleware(): 加载中间件</li>
<li>loadController(): 加载controller</li>
<li>loadRouter(): 加载路由文件</li>
</ul>
<p>从继承关系 <strong>MyAppWorkerLoader -> AppWorkerLoader -> Loader</strong> 看来，我们完全可以在 <strong>MyAppWorkerLoader</strong> 中定制上面所有的方法</p>
<h4 data-id="heading-5">定制 controller 的加载</h4>
<p>Loader 类的 <strong>loadController</strong> 方法实现了controller目录的抓取，在 <strong>egg-core</strong> 包可以找到它。</p>
<pre><code class="copyable">// egg-core/lib/loader/mixin/controller.js
const path = require('path');
const is = require('is-type-of');

module.exports = &#123;
  /**
   * Load app/controller
   * @param &#123;Object&#125; opt - LoaderOptions
   * @since 1.0.0
   */
  loadController(opt) &#123;
    opt = Object.assign(&#123;
      caseStyle: 'lower', // 转换文件名的首字母
      directory: path.join(this.options.baseDir, 'app/controller'), // controller所在位置
      initializer: (obj, opt) => &#123; // 对每个文件 export 出来的值进行处理
        if (is.function(obj) && !is.generatorFunction(obj) && !is.class(obj) && !is.asyncFunction(obj)) &#123; // 判断controller是不是函数
          obj = obj(this.app); // 传入app对象到controller函数中
        &#125;
        if (is.class(obj)) &#123; // 判断controller是不是类
          obj.prototype.pathName = opt.pathName;
          obj.prototype.fullPath = opt.path;
          return wrapClass(obj);  // 主要是定义执行在controller前面的middleware
        &#125;
        if (is.object(obj)) &#123;
          return wrapObject(obj, opt.path); // 主要是定义执行在controller前面的middleware
        &#125;
        // support generatorFunction for forward compatbility
        if (is.generatorFunction(obj) || is.asyncFunction(obj)) &#123;
          return wrapObject(&#123; 'module.exports': obj &#125;, opt.path)['module.exports']; // 主要是定义执行在controller前面的middleware
        &#125;
        return obj;
      &#125;,
    &#125;, opt);
    const controllerBase = opt.directory;

    this.loadToApp(controllerBase, 'controller', opt); // 将controller导出的对象挂在在app上下文对象中
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码可见，通过传入参数<code>opt.directory</code>可以定义controller的所在目录</p>
<pre><code class="copyable">// lib/framework.js
const path = require('path');
const egg = require('egg');
const EGG_PATH = Symbol.for('egg#eggPath');

class MyAppWorkerLoader extends egg.AppWorkerLoader &#123;
+  loadController(opt) &#123;
+    super.loadController(Object.assign(&#123; // 调用父类的loadController方法
+      directory: [
+        ...['your/controller/path'],  // 自定义的controller路径
+        path.resolve(process.cwd(), 'app/controller'),  // egg的controller默认路径 
+      ],
+      override: false, // 遇到已经存在的文件时是直接覆盖还是抛出异常
+    &#125;, opt));
+  &#125;

class Application extends egg.Application &#123;
  get [EGG_PATH]() &#123;
    // 返回 framework 路径
    return path.dirname(__dirname);
  &#125;
  // 覆盖 Egg 的 Loader，启动时使用这个 Loader
  get [EGG_LOADER]() &#123;
    return YadanAppWorkerLoader;
  &#125;
&#125;

// 覆盖了 Egg 的 Application
module.exports = Object.assign(egg, &#123;
  Application,
   // 自定义的 Loader 也需要 export，上层框架需要基于这个扩展
   AppWorkerLoader: MyAppWorkerLoader,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上代码就可以实现controller目录的扩展。</p>
<p>此外，我们还可以扩展 <strong>router、service、middleware、extend</strong> 目录，想要了解具体实现的同学，可以参考封装好的npm包 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ferencoding%2Fegg-micro-app" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/erencoding/egg-micro-app" ref="nofollow noopener noreferrer">egg-micro-app</a> 。核心内容在文件lib/framework.js中，代码不到100行非常简单。</p>
<p>这样便可以实现将大型项目拆解为多个独立模块，每一个模块都是一个微应用，大家可以按照自己的想法将业务模块和通用文件安放到不同的位置，完结撒花。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7db50afdffd6427881857ca19a388873~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            