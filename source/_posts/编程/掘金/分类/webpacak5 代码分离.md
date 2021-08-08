
---
title: 'webpacak5 代码分离'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb3243451ca649c8848f4e797d2eae41~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:58:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb3243451ca649c8848f4e797d2eae41~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>代码分离. 这一章的目的在于重用以及基本的缓存</p>
<p>首先第一部分在于提出公用的，比如都是 <code>loadsh</code> 是公用的部分。</p>
<p>如果正常发布的话，<code>index.js</code> 和 <code>another-module.js</code>. 都会打包 <code>loadsh</code>.</p>
<p><strong>index.js</strong></p>
<pre><code class="copyable">import _ from 'lodash';

console.log(_.join(['index','loaded'], ' '));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>another-module.js</strong></p>
<pre><code class="copyable">import _ from 'lodash';

console.log(_.join(['Another', 'module', 'loaded!'], ' '));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">01 代码分离的方法 主动选择分享哪些模块</h2>
<pre><code class="copyable">entry: &#123;
           index: &#123;
              import: './src/index.js',
              dependOn: 'shared',
            &#125;,
            another: &#123;
              import: './src/another-module.js',
              dependOn: 'shared',
            &#125;,
            shared: 'lodash'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>shared</code> 关键字可以例举出公共的模块。<br>
在具体的路径中 <code>dependOn</code> 选择 <code>shared</code>.</p>
<p>就可以选择哪些依赖。<code>shared</code> 也可以是数组。<br>
我想到另一种可能,我有多种 <code>shared</code> 模式有多种可能，于是我测试了一下。</p>
<pre><code class="copyable">entry: &#123;
        index: &#123;
            import: './src/index.js',
            dependOn: 'shared',
        &#125;,
        another: &#123;
            import: './src/another-module.js',
            dependOn: ['shared', 'shared1'],
        &#125;,
        shared: 'lodash',
        shared1: 'moment'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样也可以。</p>
<p>这样相对来说比较灵活。</p>
<p>只是文档中有一句我实在是不明白</p>
<blockquote>
<p>如果我们要在一个 HTML 页面上使用多个入口时，还需设置 <code>optimization.runtimeChunk: 'single'</code>，否则还会遇到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbundlers.tooling.report%2Fcode-splitting%2Fmulti-entry%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://bundlers.tooling.report/code-splitting/multi-entry/" ref="nofollow noopener noreferrer">这里</a>所述的麻烦。</p>
</blockquote>
<p>我查看了这个链接以后，理解了问题的意思。</p>
<p>就是不同的入口应该是重新实例化对象，来解决文章中文问题。</p>
<p>但是为什么加 <code>optimization.runtimeChunk: 'single'</code> 就能解决，我查了下含义</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fq%2F1010000014954264" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/q/1010000014954264" ref="nofollow noopener noreferrer">optimization.runtimeChunk 具体作用是什么？</a></p>
<p>其实就是解决缓存问题的，虽然我还没有做过实验，所以这里我并没有理解。</p>
<h2 data-id="heading-1">02 代码分离的方法 自动分离公共模块</h2>
<p>回到最初的入口方式</p>
<pre><code class="copyable">    entry: &#123;
      index: './src/index.js',
      another: './src/another-module.js',
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是有办法能够自动分离，而不用选择</p>
<pre><code class="copyable">optimization: &#123;
        splitChunks: &#123;
            chunks: 'all'
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就能自动将公共的模块分离出来，我查了下 <code>splitChunks</code></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fplugins%2Fsplit-chunks-plugin%2F%23optimization-splitchunks" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/plugins/split-chunks-plugin/#optimization-splitchunks" ref="nofollow noopener noreferrer">SplitChunksPlugin</a></p>
<pre><code class="copyable">    splitChunks: &#123;
      chunks: 'async',
      minSize: 20000,
      minRemainingSize: 0,
      minChunks: 1,
      maxAsyncRequests: 30,
      maxInitialRequests: 30,
      enforceSizeThreshold: 50000,
      cacheGroups: &#123;
        defaultVendors: &#123;
          test: /[\/]node_modules[\/]/,
          priority: -10,
          reuseExistingChunk: true,
        &#125;,
        default: &#123;
          minChunks: 2,
          priority: -20,
          reuseExistingChunk: true,
        &#125;,
      &#125;,
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我开始会担心，提取成一个公共 <code>chunk</code> 是否会太大，这些属性证明我想多了。</p>
<p>代码分离这件事，主要还是优化速度。你经常改变的是业务逻辑，公共组件其实很少变，提取出来，最大化利用浏览器缓存。</p>
<p>大概是这样子，具体属性可以等用到了再研究。</p>
<h2 data-id="heading-2">03 dynamic import</h2>
<p>动态导入这个东西队伍贫乏的 webpack 知识，以前似乎也有类似的方法，能够实现动态加载和拆分模块，使用 <code>jsonp</code> 去动态加载，只是语法似乎和这个不太一样。</p>
<p>说起来也简单，首先我引入 <code>moment</code> , 然后写个方法动态加载。</p>
<p>dynamic.js</p>
<pre><code class="copyable">export default async () => &#123;
    let &#123; default: m &#125; = await import("moment");
    let timeString = m().format('MMMM Do YYYY, h:mm:ss.SSS a');
    console.log("-----dynamicImport in test------");
    console.log(timeString);
    return timeString;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后外部引用后，直接编译。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb3243451ca649c8848f4e797d2eae41~tplv-k3u1fbpfcp-watermark.image" alt="2607814-6458a9a1bd93f38d.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>moment</code> 会有两个，一个语言包一个程序，一般正常是一个。</p>
<p>原理可以看这里 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fwoai3c%2Fp%2F13669933.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/woai3c/p/13669933.html" ref="nofollow noopener noreferrer">深入了解 webpack 模块加载原理</a></p>
<p>就是 <code>jsonp</code> 加载。</p>
<p>那么这时候还有另外一种用法，就是写在按钮事件里或者其他延时加载的方法。</p>
<pre><code class="copyable">   dynamicImportBtn.innerHTML = 'dynamic import btn';
   dynamicImportBtn.onclick = async () => &#123;
        let &#123; default: m &#125; = await import("moment");
        let timeString = m().format('MMMM Do YYYY, h:mm:ss.SSS a');
        console.log("-----dynamicImport in test------");
        console.log(timeString);
    &#125;
    element.append(dynamicImportBtn);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>果然在点击按钮以后，才会加载对应 <code>js</code>.</p>
<h2 data-id="heading-3">04. 预加载</h2>
<blockquote>
<p>prefetch(预获取)：将来某些导航下可能需要的资源<br>
preload(预加载)：当前导航下可能需要资源</p>
</blockquote>
<pre><code class="copyable"><link rel="prefetch" as="script" href="http://127.0.0.1:5500/dist/762.bundle.js">
<link rel="prefetch" as="script" href="http://127.0.0.1:5500/dist/700.bundle.js">
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><link rel="prefetch" as="script" href="http://127.0.0.1:5500/dist/762.bundle.js">
<link rel="prefetch" as="script" href="http://127.0.0.1:5500/dist/700.bundle.js">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在代码中的应用就是, 你提前加入这一段注释，告诉 <strong>webpack</strong> 你需要对这段代码执行什么策略</p>
<pre><code class="copyable">let &#123; default: m &#125; = await import(/* webpackPreload: true */ "moment");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后会在<code>html</code>中生成, 但是需要注意的点是，前提你是通过 <strong>webpack</strong> 来生成 <code>html</code></p>
<p>开始我以为这个是 <strong>webpck</strong> 通过 <strong>js</strong> 实现的，原来是 <code>html</code> 标准。</p>
<p>可以参考这两篇文章</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.webhek.com%2Fpost%2Flink-prefetch.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.webhek.com/post/link-prefetch.html" ref="nofollow noopener noreferrer">www.webhek.com/post/link-p…</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fcangqinglang%2Fp%2F11308243.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/cangqinglang/p/11308243.html" ref="nofollow noopener noreferrer">www.cnblogs.com/cangqinglan…</a></p>
<p>总结来说就是</p>
<p><code>preload</code> 并行下载<br>
<code>prefetch</code> 闲时下载</p>
<p>自己估算好使用场景，选择预加载以及预加载的顺序</p>
<p>这里我不过多研究以及测试，后续需要用到之后在进行学习了测试</p>
<h2 data-id="heading-4">05. end</h2>
<p>这一章主要还是为了教会我们如何使用 <strong>webpack</strong> 对代码进行分割。</p>
<p>给出了几种方式</p>
<ol>
<li>提取公共代码，将公共代码单独提取，以便减小体积，也充分利用浏览器缓存。</li>
<li>拆分代码，不同逻辑的代码进行拆分，达到同样的效果</li>
<li>预加载，不管是图片也好，模块也好。预加载达到优化速度的请求</li>
</ol>
<p>最后文中给出了几种分析包的方式，插件。</p>
<p>后续有机会实验一下。</p></div>  
</div>
            