
---
title: '实现一个简易的 npm install'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27b8f37a45514091aea07429eac5cea3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 20:45:44 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27b8f37a45514091aea07429eac5cea3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>现在写代码我们一般不会全部自己实现，更多是基于第三方的包来进行开发，这体现在目录上就是 src 和 node_modules 目录。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27b8f37a45514091aea07429eac5cea3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>src 和 node_modules（第三方包） 的比例不同项目不一样。</p>
<p>运行时查找第三方包的方式也不一样：</p>
<ul>
<li>在 node 环境里面，运行时就支持 node_modules 的查找。所以只需要部署 src 部分，然后安装相关的依赖。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d77658819404bdb9deb7dddac36d719~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在浏览器环境里面不支持 node_modules，需要把它们打包成浏览器支持的形式。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b5a9146da3f47c0874777e7a6ceb318~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>跨端环境下，它是上面哪一种呢？</p>
<p>都不是，不同跨端引擎的实现会有不同，跨端引擎会实现 require，可以运行时查找模块（内置的和第三方的），但是不是 node 的查找方式，是自己的一套。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b13337003dcd4b08a8cd578dd1b7ef76~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>和 node 环境下的模块查找类似，但是目录结构不一样，所以需要自己实现 xxx install。</p>
<h2 data-id="heading-0">思路分析</h2>
<p>npm 是有自己的 registry server 来支持 release 的包的下载，下载时是从 registry server 上下载。我们自己实现的话没必要实现这一套，直接用 git clone 从 gitlab 上下载源码即可。</p>
<h3 data-id="heading-1">依赖分析</h3>
<p>要实现下载就要先确定哪些要下载，确定依赖的方式和打包工具不同：</p>
<ul>
<li>打包工具通过 AST 分析文件内容确定依赖关系，进行打包</li>
<li>依赖安装工具通过用户声明的依赖文件 (package.json / bundle.json)来确定依赖关系，进行安装</li>
</ul>
<p>这里我们把包的描述文件叫做 bundle.json，其中声明依赖的包：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"name"</span>: <span class="hljs-string">"xxx"</span>,
    <span class="hljs-string">"dependencies"</span>: &#123;
        <span class="hljs-string">"yyyy"</span>: <span class="hljs-string">"aaaa/bbbb#release/1111"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通过分析项目根目录的 bundle.json 作为入口，下载每一个依赖，分析 bundle.json，然后继续下载每一个依赖项，递归这个过程。这就是依赖分析的过程。</strong></p>
<p>这样依赖分析的过程中进行包的下载，依赖分析结束，包的下载也就结束了。这是一种可行的思路。</p>
<p>但是这种思路存在问题，比如：版本冲突怎么办？循环依赖怎么办？</p>
<h3 data-id="heading-2">解决版本冲突</h3>
<p>版本冲突是多个包依赖了同一个包，但是依赖的版本不同，这时候就要选择一个版本来安装，我们可以简单的把规则定为使用高版本的那个。</p>
<h3 data-id="heading-3">解决循环依赖</h3>
<p>包之间是可能有循环依赖的（这也是为什么叫做依赖图，而不是依赖树），这种问题的解决方式就是记录下处理过的包，如果同个版本的包被分析过，那么久不再进行分析，直接拿缓存。</p>
<p>这种思路是解决循环依赖问题的通用思路。</p>
<p>我们解决了版本冲突和循环依赖的问题，还有没有别的问题？</p>
<p>版本冲突时会下载版本最高的包，但是这时候之前的低版本的包已经下载过了，那么就多了没必要的下载，能不能把这部分冗余下载去掉。</p>
<h3 data-id="heading-4">依赖分析和下载分离</h3>
<p>多下载了一些低版本的包的原因是我们在依赖分析的过程中进行了下载，那么能不能依赖分析的时候只下载 bundle.json 来做分析，分析完确定了依赖图之后再去批量下载依赖？</p>
<p>从 gitlab 上只下载 bundle.json 这一个文件需要通过 ssh 协议来下载，略微复杂，我们可以用一种更简单的思路来实现：</p>
<pre><code class="copyable">git clone --depth=1 --branch=bb xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加上 --depth 以后 git clone 只会下载单个 commit，速度会很快，虽然比不上只下载 bundle.json，但是也是可用的（我试过下载全部 commit 要 20s 的时候，下载单个 commit 只要 1s）。</p>
<p>这样我们在依赖分析的时候只下载一个 commit 到临时目录，分析依赖、解决冲突，确定了依赖图之后，再去批量下载，这时候用 git clone 下载全部的 commit。最后要把临时目录删除。</p>
<p>这样，通过分离依赖分析和下载，我们去掉了没必要的一些低版本包的下载。下载速度会得到一些提升。</p>
<h3 data-id="heading-5">全局缓存</h3>
<p>当本地有多个项目的时候，每个项目都是独立下载自己的依赖包的，这样对于一些公用的包会存在重复下载，解决方式是全局缓存。</p>
<p>分析完依赖进行下载每一个依赖包的时候，首先查找全局有没有这个包，如果有的话，直接复制过来，拉取下最新代码。如果没有的话，先下载到全局，然后复制到本地目录。</p>
<p>通过多了一层全局缓存，我们实现了跨项目的依赖包复用。</p>
<h2 data-id="heading-6">代码实现</h2>
<p>为了思路更清晰，下面会写伪代码</p>
<h3 data-id="heading-7">依赖分析</h3>
<p>依赖分析会递归处理 bundle.json，分析依赖并下载到临时目录，记录分析出的依赖。会解决版本冲突、循环依赖问题。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> allDeps = &#123;&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">installDeps</span>(<span class="hljs-params">projectDir</span>) </span>&#123;
    <span class="hljs-keyword">const</span> bundleJsonPath = path.resolve(projectDir, <span class="hljs-string">'bundle.json'</span>);
    <span class="hljs-keyword">const</span> bundleInfo = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(bundleJsonPath));
    
    <span class="hljs-keyword">const</span> bundleDeps = bundleInfo.dependencies;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> depName <span class="hljs-keyword">in</span> bundleDeps) &#123;
        <span class="hljs-keyword">if</span>(allDeps[depName]) &#123;
            <span class="hljs-keyword">if</span> (allDeps[depName] 和 bundleDeps[depName] 分支和版本一样) &#123;
                <span class="hljs-keyword">continue</span>;<span class="hljs-comment">// 跳过安装</span>
            &#125;
            <span class="hljs-keyword">if</span> (allDeps[depName] 和 bundleDeps[depName] 分支和版本不一样)&#123;
                <span class="hljs-keyword">if</span> (bundleDeps[depName] 版本 < allDeps[depName] 版本 ) &#123;
                    <span class="hljs-keyword">continue</span>;
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-comment">// 记录下版本冲突</span>
                    allDeps[depName].conflit = <span class="hljs-literal">true</span>;
                &#125;
           
            &#125;
        &#125;
        childProcess.exec(<span class="hljs-string">`git clone --depth=1 <span class="hljs-subst">$&#123;临时目录/depName&#125;</span>`</span>);
        allDeps[depName] = &#123;
            <span class="hljs-attr">name</span>: depName
            <span class="hljs-attr">url</span>: xxx
            <span class="hljs-attr">branch</span>: xxx
            <span class="hljs-attr">version</span>: xxx
        &#125;
        installDeps(<span class="hljs-string">`<span class="hljs-subst">$&#123;临时目录/depName&#125;</span>`</span>);
    &#125;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">下载</h3>
<p>下载会基于上面分析出的 allDeps 批量下载依赖，首先下载到全局缓存目录，然后复制到本地。</p>
<pre><code class="copyable">function batchInstall(allDeps) &#123;
    allDeps.forEach(dep => &#123;
        const 全局目录 = path.resolve(os.homedir(), '.xxx');
        if (全局目录/dep.name 存在) &#123;
            // 复制到本地
            childProcess.exec(`cp 全局目录/dep.name 本地目录/dep.name`);
        &#125; else &#123;
            // 下载到全局
            childProcess.exec(`git clone --depth=1 $&#123;全局目录/dep.name&#125;`);
             // 复制到本地
            childProcess.exec(`cp 全局目录/dep.name 本地目录/dep.name`);
        &#125;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就完成了依赖的分析和下载，实现了全局缓存。</p>
<h2 data-id="heading-9">总结</h2>
<p>我们首先梳理了不同环境（浏览器、node、跨端引擎）对于第三方包的处理方式不同，浏览器需要打包，node 是运行时查找，跨端引擎也是运行时查找，但是用自己实现的一套机制。</p>
<p>然后明确了打包工具确定依赖的方式是 AST 分析，而依赖下载工具则是基于包描述文件 bundl.json(package.json) 来分析。然后我们实现了递归的依赖分析，解决了版本冲突、循环依赖问题。</p>
<p>为了减少没必要的下载，我们做了依赖分析和下载的分离，依赖分析阶段只下载单个 commit，后续批量下载的时候才全部下载。下载方式没有实现 registry 的那套，而是直接从 gitlab 来 git clone。</p>
<p>为了避免多个项目的公共依赖的重复下载，我们实现了全局缓存，先下载到全局目录，然后再复制到本地。</p>
<p>npm install、yarn install 的实现流程细节会更多一些，但是整体流程类似。希望这篇文章能帮你梳理清楚思路：不同环境是怎么处理第三方包的，xxx install 的依赖分析和下载的流程是什么样的。</p></div>  
</div>
            