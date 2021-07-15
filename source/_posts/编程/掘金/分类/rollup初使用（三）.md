
---
title: 'rollup初使用（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b16b05cfbc1d4551b52efa426be5e975~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 14:31:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b16b05cfbc1d4551b52efa426be5e975~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>概要：本文主要介绍在rollup中，如何使用rollup编译打包vue组件。</p>
<h2 data-id="heading-0">新建test.vue的一个vue组件</h2>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"msg"</span>></span>&#123;&#123;msg&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>:<span class="hljs-string">'TestComponent'</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> msg = <span class="hljs-string">'hello world!这是我的自定义组件库！'</span>;
    <span class="hljs-keyword">return</span> &#123;
      msg
    &#125;

  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span>></span><span class="css">
  <span class="hljs-selector-class">.msg</span> &#123;
    <span class="hljs-attribute">color</span>: red;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">index.js入口文件中引入test.vue组件</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> test <span class="hljs-keyword">from</span> <span class="hljs-string">'./test.vue'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.component(test.name, test);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">rollup编译打包vue组件需要使用的npm包依赖</h2>
<ul>
<li>rollup-plugin-vue@next是用来编译vue代码的。支持vue3</li>
<li>@vue/compiler-sfc是rollup-plugin-vue@next插件需要的一个依赖</li>
<li>rollup-plugin-postcss sass 主要是因为在vue组件库中用到的样式，用的是sass所以安装sass</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">npm i rollup-plugin-vue@next -D
npm i  @vue/compiler-sfc -D
npm i rollup-plugin-postcss -D
npm i sass -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">配置打包配置文件</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vue = <span class="hljs-built_in">require</span>(<span class="hljs-string">'rollup-plugin-vue'</span>);
<span class="hljs-keyword">const</span> postcss = <span class="hljs-built_in">require</span>(<span class="hljs-string">'rollup-plugin-postcss'</span>);
  plugins: [
    vue(),
    postcss(),
  ],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时执行 npm run dev 顺利打包！但是会有警告</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b16b05cfbc1d4551b52efa426be5e975~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个警告说输出文件中缺少一个在浏览器window中设置globals的变量，这个名词跟我们设置的external modoule需要设置成一样的。
在配置文件的output中设置一下即可：</p>
<pre><code class="hljs language-js copyable" lang="js">  output: [&#123;
      <span class="hljs-attr">file</span>: outputPath,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'umd'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'datavTest'</span>,
      <span class="hljs-attr">globals</span>: &#123;<span class="hljs-attr">vue</span>: <span class="hljs-string">'Vue'</span>&#125;
    &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后打包会发现组件库是成功的！</p>
<h2 data-id="heading-4">编写example/index.html</h2>
<p>引入vue3的global库cdn,编写一个简单的vue3实例，引入自定义的vue插件之前需要use一下，这里的use(datavTest)对应的是配置文件中output配置的name属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="https://cdn.jsdelivr.net/npm/vue@3.1.0-beta.7/dist/vue.global.js"></script>
  <script src="../dist/datav.umd.js"></script>
</head>
<body>
  <div id="app">&#123;&#123;msg&#125;&#125;
    <data-test-component></data-test-component>
  </div>
  
</body>
<script>
  Vue.createApp(&#123;
    setup() &#123;
      var msg = 'hello my Vue component!';
      return &#123; msg &#125;;
    &#125;
  &#125;).use(datavTest).mount('#app');
</script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是当打开index.html的时候会在浏览器中报错说：
页面报错Cannot read property 'openBlock' of undefined</p>
<p>是因为打包后代码编译的Vue引用不到而引起的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/206476a80a5d470599d70bce7fc517fc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如上图，在编译后的datav.umd.js文件中找到render函数，将里面的vue改成配置时候设置的Vue即可。再打开页面发现组件显示成功！
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acd4bc0b8249439ea83f293baf150736~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">踩坑记录</h2>
<ul>
<li>错误1：[!](plugin vue) TypeError: Cannot read property 'refSugar' of undefined</li>
</ul>
<p><strong>解决办法是</strong></p>
<pre><code class="hljs language-js copyable" lang="js">rm -rf node_modules
rm package-lock.json
npm cache clear --force
npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>错误2 [!](plugin commonjs) SyntaxError: Unexpected token (2:2) in D:\noteDemo.. src\test.vue?vue&type=template&id=0f72a62a&lang.js (2:2)</li>
</ul>
<p><strong>解决办法是</strong>将vue插件放在最上面既可
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ea5fb09668d4a83bfa83e5bd4bf3e61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>错误3 rollup-plugin-postcss ( PostCSS plugin postcss-noop-plugin requires PostCSS 8. Migration guide for end-users:)</li>
</ul>
<p><strong>解决办法是</strong> 安装 <a href="https://link.juejin.cn/?target=mailto%3Aautoprefixer%408.0.0" target="_blank" title="mailto:autoprefixer@8.0.0" ref="nofollow noopener noreferrer">autoprefixer@8.0.0</a>然后修改配置</p>
<pre><code class="hljs language-js copyable" lang="js">    postcss(&#123;
      <span class="hljs-comment">// 把 css 插入到 style 中</span>
      <span class="hljs-comment">// inject: true,</span>
      <span class="hljs-comment">// 把 css 放到和js同一目录</span>
      <span class="hljs-attr">extract</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">plugins</span>: [
         <span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>)(&#123; <span class="hljs-attr">overrideBrowserslist</span>: [<span class="hljs-string">'> 0.15% in CN'</span>] &#125;) <span class="hljs-comment">// 自动添加css前缀</span>
      ]
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>错误4：[!] TypeError: keypath.split is not a function是因为配置globals的时候没有带引号</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63554735f7064c51bf64148b5ae993ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>错误5：datav.umd.js:17 Uncaught TypeError: Cannot read property 'withScopeId' of undefined，是因为rollUp不支持css 的scoped，去掉了test.vue中的scoped</li>
<li>错误6：index.html页面报错Cannot read property 'openBlock' of undefined,是因为打包后代码编译的Vue引用不到而引起的</li>
</ul>
<p>解决办法：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/206476a80a5d470599d70bce7fc517fc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            