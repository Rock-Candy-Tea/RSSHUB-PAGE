
---
title: 'NPM 7 workspace模式安装依赖执行找不到sentry-cli'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1090'
author: 掘金
comments: false
date: Tue, 11 May 2021 04:47:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=1090'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>搜遍了谷歌还有相关Github Repo Issues都没有，<br>npm workspace的资料都不多，<br>有个别都是yarn workspace说什么安装依赖异常，<br>换成国内的淘宝源啊，来来去去都说什么源找不到，<br>
<br>一顿操作猛如虎，问题还是没有解决。<br>只能自己摸索了，我的解决姿势感觉应该是全网第一例！<br></p>
<h2 data-id="heading-1">系统环境</h2>
<ul>
<li>Mac OS</li>
<li>Node 14.16.1</li>
<li>NPM 7.12.1
<ul>
<li>@sentry/cli 1.64.2</li>
</ul>
</li>
</ul>
<h2 data-id="heading-2">问题列表</h2>
<h3 data-id="heading-3">sentry-cli ENOENT</h3>
<pre><code class="hljs language-bash copyable" lang="bash">ERROR <span class="hljs-keyword">in</span> Sentry CLI Plugin: spawn /workspace/project/node_modules/@sentry/cli/sentry-cli ENOENT
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">not installed by @sentry/cli </h3>
<pre><code class="hljs language-bash copyable" lang="bash">error: sentry-cli was not installed by @sentry/cli install script 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">挣扎的姿势</h2>
<h3 data-id="heading-6">.npmrc配置源</h3>
<pre><code class="hljs language-bash copyable" lang="bash">sentrycli_cdnurl=https://npm.taobao.org/mirrors/sentry-cli/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>治标不治本，因为在单体模式下（非workspace）下，<br>走淘宝源安装是可以顺利且挺快的。。。<br>npm 7 workspace下还是找不到。<br>node_modules只装了一个残缺版本的@sentry/cli，<br>里面缺失sentry-cli这个（根据系统类型的二进制执行文件）。。<br></p>
<h3 data-id="heading-7">在主项目强装</h3>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 就是清除缓存和强制安装,删除大法。。都试过。。</span>
<span class="hljs-comment"># 没啥用,</span>
npm cache clean --force
rm -rf node_modules yarn.lock package-lock.json
npm install @sentry/cli  --force --legacy-peer-deps

<span class="hljs-comment"># 为毛要--legacy-peer-deps</span>
<span class="hljs-comment"># 因为不是对等依赖的子包，常规的install会抛出如下异常</span>
<span class="hljs-comment"># ERESOLVE unable to resolve dependency tree</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">安装最新包</h3>
<p>解决了这个问题，</p>
<pre><code class="hljs language-bash copyable" lang="bash">error: sentry-cli was not installed by @sentry/cli install script 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">最终解决(过渡方案)</h3>
<p>我跑到node_modules/@sentry/cli区域，<br>发现他提供了安装脚本，顺势执行了一波。。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># exec</span>
<span class="hljs-comment"># 我发现里面的逻辑就是判定当前使用什么系统，下载对应的二进制</span>
node ./node_modules/@sentry/cli/scripts/install.js

<span class="hljs-comment"># 果然执行完毕。。sentry-cli回来了。。</span>

<span class="hljs-comment"># 验证</span>
./node_modules/.bin/sentry-cli --<span class="hljs-built_in">help</span>
<span class="hljs-comment"># 可以正常输出</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次手动执行去执行？NO,NO,NO。。。<br>生命宝贵，能自动化的还是自动化好<br>
<br>npm 提供了prepare的钩子，可以在install之后自动执行。<br>官方文档：<a href="https://docs.npmjs.com/cli/v7/using-npm/scripts" target="_blank" rel="nofollow noopener noreferrer">npm scripts -> Life Cycle Scripts</a><br></p>
<h4 data-id="heading-10">package.json</h4>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"prepare"</span>: <span class="hljs-string">"husky install; node check-sentry.js"</span>,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">check-sentry.js</h4>
<p>最直接就是往项目根目录写一个js逻辑判定文件。。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/*
* 1. 逻辑不复杂，就是执行部分shell去判定
* 2. 二进制执行凉凉进入catch逻辑
* 3. 走一遍安装逻辑（有缓存会直接命中，输出use cache ....)
* 4. 最后就是输出版本号了。。
*/</span> 
<span class="hljs-keyword">const</span> &#123; execSync &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);
<span class="hljs-keyword">try</span> &#123;
  execSync(<span class="hljs-string">'./node_modules/.bin/sentry-cli -V'</span>);
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
  execSync(<span class="hljs-string">'node ./node_modules/@sentry/cli/scripts/install.js'</span>);
  execSync(<span class="hljs-string">'./node_modules/.bin/sentry-cli -V'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完结撒花，可以正常打包调用sentry上传sourcemap这些</p>
<h2 data-id="heading-12">总结</h2>
<p>有不对之处请留言，会及时修正，谢谢阅读！</p></div>  
</div>
            