
---
title: 'vue cli中的env详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5754'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 16:48:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=5754'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>相信使用过 vueCli 开发项目的小伙伴有点郁闷，正常开发时会有三个接口环境（开发，测试，正式），但是 vueCli 只提供了两种 development,production(不包含 test-单测)模式。其实这是小伙伴们没有理解 vueCli 文档所导致的。</p>
<p>vueCli 命令中 <code>--mode</code> 对应的 <code>.env.[mode]</code>，而不是 <code>NODE_ENV</code></p>
<p>::: tip 注意
除了 VUE_APP_ 变量之外。<br>
还有两个特殊的变量：<br>
NODE_ENV： 是 <code>development</code>、<code>production</code>、<code>test</code> 中的一个。其值取决于应用运行的模式。<br>
BASE_URL： 和 vue.config.js 中的 <code>publicPath</code> 选项相符，即你的应用会部署到的基础路径。
:::</p>
<h2 data-id="heading-1">简介-官方</h2>
<p>mode 是 Vue CLI 项目中一个重要的概念。默认情况下，一个 Vue CLI 项目有三个模式：</p>
<ul>
<li>development 模式用于 vue-cli-service serve</li>
<li>test 模式用于 vue-cli-service test:unit</li>
<li>production 模式用于 vue-cli-service build 和 vue-cli-service test:e2e</li>
</ul>
<p>你可以通过传递 --mode 选项参数为命令行覆写默认的模式。</p>
<p>当运行 <code>vue-cli-service</code> 命令时，所有的环境变量都从对应的环境文件中载入。如果文件内部不包含 <code>NODE_ENV</code> 变量，它的值将取决于模式，例如，在 <code>production</code> 模式下被设置为 "production"，在 <code>test</code> 模式下被设置为 "test"，默认则是 "development"。</p>
<p><code>NODE_ENV</code> 将决定您的应用运行的模式，是开发，生产还是测试，因此也决定了创建哪种 webpack 配置。</p>
<p>例如通过将 <code>NODE_ENV</code> 设置为 "test"，Vue CLI 会创建一个优化过后的，并且旨在用于单元测试的 webpack 配置，它并不会处理图片以及一些对单元测试非必需的其他资源。</p>
<p>同理，<code>NODE_ENV=development</code> 创建一个 webpack 配置，该配置启用热更新，不会对资源进行 hash 也不会打出 vendor bundles，目的是为了在开发的时候能够快速重新构建。</p>
<p>当你运行 <code>vue-cli-service build</code> 命令时，无论你要部署到哪个环境，应该始终把 <code>NODE_ENV</code> 设置为 "production" 来获取可用于部署的应用程序。</p>
<h2 data-id="heading-2">示例配置</h2>
<p>我们现在有三个配置文件，分别如下</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#.env.development</span>
NODE_ENV=development
VUE_APP_AXIOS_BASEURL=http://xxxx
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#.env.preview 测试环境的配置</span>
NODE_ENV=production
VUE_APP_AXIOS_BASEURL=http://xxxx
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#.env.production</span>
NODE_ENV=production
VUE_APP_AXIOS_BASEURL=http://xxxx
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">在 axios 中使用</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;
<span class="hljs-keyword">const</span> conf = &#123;
  <span class="hljs-attr">baseURL</span>: process.env.VUE_APP_AXIOS_BASEURL,
&#125;;
<span class="hljs-keyword">return</span> axios.create(conf);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">package.json 配置</h2>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"vue-cli-service serve"</span>,
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"vue-cli-service build --mode preview"</span>,
    <span class="hljs-attr">"build:release"</span>: <span class="hljs-string">"vue-cli-service build"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">启动方式</h2>
<pre><code class="hljs language-bash copyable" lang="bash">npm run serve <span class="hljs-comment"># 默认 dev</span>
npm run build <span class="hljs-comment"># 测试环境</span>
npm run build:release <span class="hljs-comment"># 正式环境</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            