
---
title: 'vite hmr基本原理及vue3的update前后关系'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1823d9bdcc2d499fb56a828a453ec625~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 22:07:00 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1823d9bdcc2d499fb56a828a453ec625~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这篇文章暂时只分析vite的基本和重点分析一下hmr的vue reload基本原理，其他部分暂时还没看。。</p>
<p>我们知道vite是不需要打包的，这是依赖了浏览器的esm模块化的功能，例如如果我们如果在html中这样写</p>
<pre><code class="copyable"><script type='module' src="/src/main.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么浏览器就会发出一个http://..../src/main.js的一个请求给倒vite的service，这个service是koa写的，这样我们就给它fs.read我们项目中的html，但是vite也有一个client端的代码，用于接受热更新的通知，所以我们同时还要把这个东西给注入进去，这样浏览器端就有了client.js，</p>
<p>然后接下来浏览器就通过这两个插入的script标签继续请求.js，我们的koa接受到之后，再去fs.read文件返回即可,我这里暂时还放的是vue2的，因为公司用的还是vue2的，但是后面分析流程还是会讲vue3，</p>
<p>这是main.js的原文件</p>
<p><code>import Vue from 'vue'</code></p>
<p><code>import App from './components/App.vue'</code></p>
<p><code>let app = new Vue(&#123;</code></p>
<p><code>render: h => h(App) //当h接受obj时候会走createComponent</code></p>
<p><code>&#125;).$mount('#app')</code></p>
<p>main.js会请求一个vue第三方库，对于第三方库我们都知道需要把前缀改为/@module/vue，这样，不然浏览器会报错，这样改完我们分析url带@module，就知道去node_modules里面去取了，对于第三方库的依赖我们也要去reWriteImport，</p>
<p>如果我们自己的App.vue，那么就去src底下读，这没有任何问题，因为浏览器会自动根据当前路径拼接./components/App.vue</p>
<p><code>const vue = fs.readFileSync(p, 'utf-8')</code></p>
<p><code>cacheEntry.set(url, vue)</code></p>
<p><code>const ast = compilerSFC.parse(vue)</code></p>
<p>当然vue不能fs之后直接传，我们要用compilerSFC分析之后得到一个ast对象，把东西拼一下再翻回去，这里主要是对template的处理，需要再单独发一个请求url带上?template后缀</p>
<p><code>res = ` import &#123;render as _render&#125; from '$&#123;url&#125;?type=template' $&#123;rewriteImport(aa)&#125; let compVm _script.render = _render ....` </code></p>
<p><code>这样_script.render就是的返回值也是个js，这个当然也需要另外处理</code></p>
<h2 data-id="heading-0">hmr:（配合vue3）</h2>
<p>这时候重点来了，当我们去改变文件的时候，我们需要使用第三方库chokidar来监听文件的变化，这里要分几种情况，如果是vue文件或者style文件，暂时先看vue，</p>
<p>cacheEntry是我们在第一次读文件的时候做的一个缓存</p>
<pre><code class="copyable">  chokidar.watch('./src').on('change', (fpath) => &#123;    if (fpath.endsWith('vue')) &#123;      let vueFile = fpath.replace(path.dirname(fpath), "")      let cache = cacheEntry.get(vueFile)      if (isTemplateBlocksEqual(vueFile, cache)) &#123;           //todo      &#125; else &#123;      &#125;      ws.send(vueFile.slice(1));    &#125; else &#123;      //todo    &#125;  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把它从缓存中拿出来和新的文件做一次比较，从而得出到底是文件的哪里发生了变化，</p>
<p>如果是template变化了，那么就只发一个vue-rerender,意思是把tempalte重新请求一次运行一下，如果不是，那么就是文件里script的东西变了，那么就发vue-reload，我们来看一下这种情况，当client收到之后</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1823d9bdcc2d499fb56a828a453ec625~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到调用_VUE_HMR_RUNTIME_.reaload,然后重新import把新的m.default传入，进入这个函数可以看到我们把新的newComp给extend到老的record.component上去了,</p>
<p>record的数据结构长这样&#123;component:&#123;&#125;,instances:[]&#125;，一个是数据，一个是所有的组件的实例instances</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67000dbc3df54580bdf2b7fc152ac7b9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们这里的改动component其实是会影响到所有的实例上的instance.type，因为他们是引用关系，具体什么流程后面会说到，然后对于每一个改变的组件**，都会去从父亲开始update**，我觉得也许是跟slot有关系，但是也不确定。。。。然后用一个queueJob去防止parent多次重复upate，注释也写的很明白，</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ab749a87c714455a724cd7b99b28f7b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后看一下update里面，</p>
<p><code>instance.update = effect(function componentEffect() &#123;</code></p>
<p><code>if (!instance.isMounted) &#123; // ... &#125;</code></p>
<p><code>else &#123; //... const nextTree = renderComponentRoot(instance);</code></p>
<p><code>const prevTree = instance.subTree;</code></p>
<p><code>instance.subTree = nextTree;</code></p>
<p><code>if ((process.env.NODE_ENV !== 'production')) &#123;</code></p>
<p><code>startMeasure(instance, `patch`);</code></p>
<p><code>&#125;</code></p>
<p><code>patch(prevTree, nextTree, // parent may have changed if it's in a teleport</code></p>
<p><code>next.el = nextTree.el; //...</code></p>
<p><code>&#125;</code></p>
<p>这里用effect包裹了一下，应该也是为了收集依赖，</p>
<p>renderComponentRoot里面帮我们拿到了新的vnode，拿的方式就是normalizeVnode（render.call()）<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6704da8a7e4346beac3c13627454171d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就进入了pactch的过程</p>
<p>暂时先写到这里，后面会附上github代码地址</p></div>  
</div>
            