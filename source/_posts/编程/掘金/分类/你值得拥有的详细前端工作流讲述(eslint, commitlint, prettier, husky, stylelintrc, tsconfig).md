
---
title: '你值得拥有的详细前端工作流讲述(eslint, commitlint, prettier, husky, stylelintrc, tsconfig...)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04d9586df21c445da02b3957b48428c5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 20:02:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04d9586df21c445da02b3957b48428c5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04d9586df21c445da02b3957b48428c5~tplv-k3u1fbpfcp-watermark.image" alt="part-00001-1105" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">前言</h2>
<p>前端工程流配置是前端工程师想要独当一面必须掌握的一项技能，这一篇详细讲述如果一个项目从0开始搭建，会涉及到哪些规范，如何使用，配置，以及遇到的问题。总结不易，觉得有帮助可以点赞，收藏。为了方便下面内容的讲解，我用create-react-app创建一个项目json-react-template。</p>
<blockquote>
<p>这里需注意一点，create-react-app创建项目时候，已经帮你git init。自己写脚手架的时候也可以添加这个功能</p>
</blockquote>
<h2 data-id="heading-1">eslint</h2>
<p>说到工作流不得不提eslint，它是用来检查js/ts代码规范的一个插件。能够帮助我们写出更优雅的代码，但是很多人在使用eslint时候，往往会遇到一些问题，最大的问题就是eslint不生效，下面我们具体来操作一下。</p>
<h3 data-id="heading-2">引入eslint</h3>
<p>在这里我们需要做三件事</p>
<p>1：编辑器（我的是vs code）需要安装eslint插件</p>
<p>2：安装eslint包</p>
<p>3：引入.eslintrc文件</p>
<p>前两步比较简单，正常操作，下面主要说说.eslintrc。很多情况下我们不可能记住这么多规则，基本上到这里都是从网上复制一份过来。但是有时候就算是从网上copy可能也需要花费一些时间，主要是网上文章太多，选择的时候容易对我们造成干扰。这里我说一个我自己觉得比较优雅的方式，在我们的github上面，有一个git gists。这个是github提供给我们的一个功能，能够让我们保留一些代码片段，所以我们就可以事先找到一份.eslintrc配置放到上面，方便后面查找（这样今后就可以直接去gist复制了，方向明确）。写到这里，我已经把之前保存的.eslintrc复制到项目里了。
<img width="928" alt="截屏2021-08-02 下午7 22 06" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bf345397f994486bb25a6f1afa4ea7e~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">eslint不生效</h3>
<p>有了上面的配置，现在我们来说说eslint不生效情况，遇到这种情况我们该怎么办呢？一般三步走。</p>
<p>1：检查vs code是否安装了eslint插件</p>
<p>2：检查.eslintrc规则是否正确或者相关插件是否安装</p>
<p>3：重启下编辑器</p>
<p>步骤1和步骤3很简单一笔带过，下面我们来说一下步骤2。基本上很多eslint失效的情况都是步骤2造成的。因为我们是复制过来的规则，会导致有的插件没有安装或者由于eslint版本原因导致规则写法改变（网上找的规则是eslint低版本的，但是你现在的项目是高版本）。拿我刚刚的项目举例，现在我的vs code检查已经失效了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82d3fd7ed8df4dd68627d3e065e0a44c~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-02 下午6 55 22" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那如何检查上面所说的第二步是否有问题呢？很简单，执行一下eslint 让他去检查任意一个文件，这样就会暴露出问题。我主要以局部安装来说明，执行以下命令。</p>
<blockquote>
<p>./node_modules/eslint/bin/eslint.js ./src/App.js</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e997f45865c48a9ad3a9ca6540a8b93~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-02 下午7 23 14" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到报错说没有找到‘airbnb-base’。查阅了一下其实对应的插件是eslint-config-airbnb-base，所以这里的问题就是没有安装相关插件。我自己先安装完，继续执行上面的命令，又报错如下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e91bd4cc62c470cb9bd5c5835f67546~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-02 下午7 25 05" loading="lazy" referrerpolicy="no-referrer"></p>
<p>继续报错显示allowAfterThis这条命令不合法，说明这个eslint规则，在高版本里写法已经改变了，我先直接把这个规则注释掉，重新执行了一下命令。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f1b885fbfbc4ce8be08bc59be7af28e~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-02 下午7 27 17" loading="lazy" referrerpolicy="no-referrer">
发现eslint已经生效了，vs code开始显示错误，最后我们只要按照对应规则去更改即可。</p>
<h2 data-id="heading-4">.eslintignore</h2>
<p>现在再来说说.eslintignore，这个文件我觉得一定是要的。因为在打包的时候可以减少打包速度，具体可以看看我之前写的这篇<a href="https://juejin.cn/post/6888848660591968264" target="_blank" title="https://juejin.cn/post/6888848660591968264">前端优化详解以及需要关注的几个问题</a>。写.eslintignore需要注意一点,也是很多人写完不生效的原因。.eslintignore的路径前缀是/或者不写，但不要写./如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// .eslintignore</span>
./src/__test__<span class="hljs-comment">/*.js  // 错误写法
// 正确写法
/src/__test__/*.js 或者src/__test__/*.js
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">.stylelintrc/.stylelintignore</h2>
<p>这两个我们就一笔带过，和eslint几乎是一样的，如果stylelint失效，请参考eslint方法解决问题。</p>
<h2 data-id="heading-6">tslint</h2>
<p>tslint是用来检查ts语法规范的插件，但是由于tslint官方声明已经不在维护了，并且推荐用eslint来检查ts/tsx文件，所以今后使用eslint即可。那怎么做呢？很简单，只需要安装一些能检查ts的插件即可。更改一下<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fyizhengfeng-jj%2Ff039e5512f99178e829c6501a0877940" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/yizhengfeng-jj/f039e5512f99178e829c6501a0877940" ref="nofollow noopener noreferrer">.eslintrc配置(检查ts的版本)</a>
复制规则之后，如果失效，直接按照上面eslint的做法在来一遍即可。</p>
<h2 data-id="heading-7">tsconfig.json</h2>
<p>这次来说说tsconfig.json,它的配置有很多，具体可以看看官网<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.tslang.cn%2Fdocs%2Fhandbook%2Ftsconfig-json.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.tslang.cn/docs/handbook/tsconfig-json.html" ref="nofollow noopener noreferrer">www.tslang.cn/docs/handbo…</a>
接下来选几个项目中用到的属性进行说明，加深一下印象。</p>
<ul>
<li>module</li>
</ul>
<p>说明：这个字段表示ts编译后，模块是以哪种模块系统存在的，主要有以下几个'commonjs' | 'amd' | 'system' | 'umd' | 'es6' | 'es2015' | 'esnext'，我们用commonjs/es6举例，源码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> test = <span class="hljs-function">(<span class="hljs-params">value: number</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// commonjs编译如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-string">"__esModule"</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span> &#125;);
<span class="hljs-built_in">exports</span>.test = <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> test = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value);
&#125;;
<span class="hljs-built_in">exports</span>.test = test;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// es6编译如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> test = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>target</li>
</ul>
<p>说明：这个字段表示把ts编译成什么样的目标代码es5还是es6亦或是esnext。这个字段大家应该经常用到就不演示了。</p>
<ul>
<li>lib</li>
</ul>
<p>说明：这个字段表示需要引入什么库，默认不写lib字段是引入dom库，引入dom库是什么意思？用直白的话说就是可以用document这些全局的dom变量，如果你写了lib但是没有依赖dom，使用document的时候就会报错，如下。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02f02d59d70e4b2694d2e310954990b4~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-04 下午7 14 29" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>allowJs/checkJs</li>
</ul>
<p>说明：allowJs这个字段意思是否允许在ts文件里面引入js文件，checkJs表示是否检查js错误。</p>
<ul>
<li>jsx</li>
</ul>
<p>这个主要表示将.jsx文件编译成什么形式，有三种形式'preserve', 'react-native', or 'react'。在react的项目里面直接设置成react就行。</p>
<ul>
<li>noImplicitAny</li>
</ul>
<p>说明：这个表示当一个变量是隐式any类型的时候是否抛错，注意这里是隐式，不是你设置成any的。话说不清楚，直接看图。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/108fff9175bf4565862f66c2f4839738~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-04 下午7 45 10" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>moduleResolution</li>
</ul>
<p>说明：这个表示ts会以哪种规则去引入文件，有两种模式'node' | 'classic'，一般选择node模式，具体规则看这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_45534118%2Farticle%2Fdetails%2F104301916" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_45534118/article/details/104301916" ref="nofollow noopener noreferrer">链接</a>。</p>
<ul>
<li>include/exclude</li>
</ul>
<p>这两个字段很有用，一个是限制ts作用的范围，一个是排除特殊文件，比如我们想要编译src下面所有ts/tsx文件，但是又不想编译测试文件怎么办，可以如下配置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
<span class="hljs-string">"include"</span>: [
        <span class="hljs-string">"src/**/*.ts"</span>,
        <span class="hljs-string">"src/**/*.tsx"</span>
    ],
    <span class="hljs-string">"exclude"</span>: [
        <span class="hljs-string">"src/**/*.test.tsx"</span>
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>sourceMap</li>
</ul>
<p>生成相应的.map文件用于调试</p>
<ul>
<li>rootDir</li>
</ul>
<p>编译之后文件存放的目录</p>
<ul>
<li>declaration</li>
</ul>
<p>自动生成相应的 '.d.ts' 文件</p>
<p>还有很多字段不一一列举了，提供一个我们经常用到的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fyizhengfeng-jj%2F09270ba01da51463920d4ea5a3ea8d0a" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/yizhengfeng-jj/09270ba01da51463920d4ea5a3ea8d0a" ref="nofollow noopener noreferrer">tsconfig配置</a>，有详细的注释哦！</p>
<h3 data-id="heading-8">问题</h3>
<p>通过create-react-app创建的项目，就算使用上面的tsconfig配置，还是会出现一个'./logo.svg'找不到的问题。这个主要是ts无法识别这样的模块，所以就需要我们自己去定义module了，格式如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">declare <span class="hljs-built_in">module</span> <span class="hljs-string">'*.svg'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是这些代码是要写到.d.ts文件里面。那如何让.d.ts生效呢？大致如下，我们可以在tsconfig.json同级目录下建立types文件夹，在该文件夹下建一个名为index.d.ts的文件写入上面代码即可，.d.ts也是一个ts文件，所以也需要编译才行，此时可以使用include字段，如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"include"</span>: [
        <span class="hljs-string">"src/**/*.ts"</span>,
        <span class="hljs-string">"src/**/*.tsx"</span>,
        <span class="hljs-string">"types"</span>
    ],
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">commitlint</h2>
<p>commitlint之前关注的比较少一点，但是随着工作年限的增长，越来越多的项目有commit提交规范，所以了解他是很有必要的。我觉得现在的commit提交信息可以分为两大类，一个是angular标准规范，这种规范适用于xx库和xx插件的开发，方便生成CHANGELOG.md。另一种就是自己写提交规范，适用于自己公司的项目。下面按照两种规范一一说明。</p>
<h3 data-id="heading-10">angular提交规范</h3>
<p>不管是标准还是非标准，提交了commit之后，都需要做相应的检查，对于angular规范来说有专门的配套插件帮你，它就是commitlint。我们可以跟着安装下。这里注意我们需要安装@commitlint/config-conventional和@commitlint/cli这两个插件，安装成功之后我们应该如何去使用呢？这个时候就需要用到husky,husky插件可以帮我们接管git hooks，从而在相应的阶段做出正确的处理。在package.json配置如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"husky"</span>: &#123;
     <span class="hljs-string">"hooks"</span>: &#123;
           <span class="hljs-string">"commint-msg"</span>: <span class="hljs-string">"commitlint -E HUSKY_GIT_PARAMS"</span>
     &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">疑惑</h4>
<p>1：如果按照上面的写法，husky必须是低版本，我的是4.3.8。网上的文章很多都是这种写法，但是当我操作的时候，husky已经到了7.x版本，结果发现commtlint失效，所以如果你想要上面的配置生效，可以和我一样下载4.3.8，那如果非要高版本了？先等等，下面内容会说道。</p>
<p>2：看到上面配置你可能会蒙，-E是什么意思，其他字母行么？先不要慌，今后遇到这种，我们不要多想这肯定是插件自带的参数，所以只需要执行--help,就可以看到其内容，如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66d8502290054700b388a235f178e967~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-05 上午11 55 01" loading="lazy" referrerpolicy="no-referrer">
可以看到-E就是"check message in the file at path given by environment variable value",翻译出来就是“在给定的环境路径下，检查信息”，而后面HUSKY_GIT_PARAMS就可以告诉husky 是检查哪一个hooks路径。</p>
<p>3：我们一直说commintlint，但是为什么插件安装的是@commitlint/cli。我们在npm上翻一下就知道，其实@commitlint/cli就是commitlint的别名，安装@commitlint/cli就行，别纠结。</p>
<p>4：那为什么还要安装@commitlint/config-conventional，因为commintlint只是来检查规范的，但是具体用哪种规范你也要定义好。就像eslint是检查规范工具，但是我们也要继承airbnb这个规则了。我们就把@commitlint/config-conventional当作airbnb即可。</p>
<p>5：所以你把husky版本降低你还会遇到报错，因为你没有指定commitlint.config.js。他是为了告诉commitlint需要继承哪种规范，配置如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">extends</span>: [
        <span class="hljs-string">'@commitlint/config-conventional'</span>
    ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6：现在提交代码时候，就可以看到错误了，如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/648bf4adfbc042d6b2258fb28f4ebbb1~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-05 下午2 04 03" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">angular规范写法</h4>
<p>上面一系列的配置，可以让你在提交代码时候，进行commit规范检查，这个时候我们就要按照正确的规范提交了。那怎么样才算一个正确的规范了，网上有很多文章，这里我不说的太复杂，说的太复杂的反而让人不了解，具体可以看看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fblob%2Fmaster%2FCONTRIBUTING.md%23commit" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit" ref="nofollow noopener noreferrer">官网链接</a>。大致规范如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><type>(<scope>): <subject>

<span class="hljs-comment">// 空一行</span>

<body>

<span class="hljs-comment">// 空一行</span>

<footer>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1：header部分最重要分为type,scope,subject</p>
<p>type：build|ci|docs|feat|fix|perf|refactor|test</p>
<p>scope：表示改动的文件范围，就是写一下改了哪里的模块即可。</p>
<p>subject：对这次改动的具体描述，如改了什么bug或者增加了什么需求。</p>
<blockquote>
<p>！！！注意：这里一定要注意"feat(package.json): 增加了commintlint功能"。冒号后面一定要有一个空格哇！</p>
</blockquote>
<p>2：body部分就是写一下更详细的描述，这个是可选的。</p>
<p>3：footer部分表示如果你的改动是破坏性的比如你写的是插件，大版本升级把api都改了。需要在这里进行详细描述包括迁移说明。</p>
<h4 data-id="heading-13">commitizen/cz-conventional-changelog</h4>
<p>有的人如果记不住angular书写规范，可以安装这两个插件，这两个插件就是在你提交代码时候自动帮你组织commit信息，不用你自己想，但是我觉得自己手写更快点。cz-conventional-changelog这个和airbnb一样，是和commitizen配套使用的。</p>
<p>1：他们两个也有一个config配置文件，只不过我们是写在package.json里面，如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"config"</span>: &#123;
    <span class="hljs-string">"commitizen"</span>: &#123;
      <span class="hljs-string">"path"</span>: <span class="hljs-string">"./node_modules/cz-conventional-changelog"</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2：第二个问题由于我们都是局部安装的，所以不能全局使用git cz。这个时候我们可以写一个script命令来解决，提交时候就不再是git commit而是npm run commit可能感觉粗糙了点。如下</p>
<pre><code class="hljs language-javasciript copyable" lang="javasciript"> "scripts": &#123;
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "commit": "git-cz"
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里一个符合angular标准的提交规范就配置好了。</p>
<h3 data-id="heading-14">自己的commmit标准</h3>
<p>但如果我们就不想用angular规范该怎么办呢？有人会说可以设置自己的commintlint.config.js。可以是可以不过总觉得在他的限制范围内，我想自己获取到提交信息，然后根据提交的信息，用正则或者其他规则判断，从而给出对应的规范可以么？肯定是可以的。假如现在我们做了一个产品叫xx商城，项目名为json-shopping。这个项目中的bug和需求都有一个编号，所以我们想要的提交规范就是"[json-shopping-123]: 修复了xxbug"。不满足这种规范统一报错。那么我们该怎么做呢？我们参考一下<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2Fdev%2Fpackage.json%23L46" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/dev/package.json#L46" ref="nofollow noopener noreferrer">vue的做法</a>具体如下。</p>
<p>1：将commit-msg配置成自己的脚本</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"hooks"</span>: &#123;
      <span class="hljs-string">"commit-msg"</span>: <span class="hljs-string">"node scripts/verify-commit-msg.js"</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2：建立scripts文件夹，编写verify-commit-msg.js脚本如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>);
<span class="hljs-keyword">const</span> msgPath = process.env.HUSKY_GIT_PARAMS || <span class="hljs-string">'.git/COMMIT_EDITMSG'</span>;  <span class="hljs-comment">// 注意因为用的是husky所以这里是HUSKY_GIT_PARAMS</span>
<span class="hljs-keyword">const</span> msg = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>).readFileSync(msgPath, <span class="hljs-string">'utf-8'</span>).trim();
<span class="hljs-keyword">const</span> commitRE = <span class="hljs-regexp">/^\[json-shopping-\d+\]\:\s.&#123;1,50&#125;/</span>;

<span class="hljs-keyword">if</span> (!commitRE.test(msg)) &#123;
  <span class="hljs-built_in">console</span>.log();
  <span class="hljs-built_in">console</span>.error(
    chalk.red(<span class="hljs-string">`  提交信息不满足项目要求，具体如下\n`</span>) +
    chalk.red(<span class="hljs-string">`  [json-shopping-xxx]: 修复xxxbug\n`</span>) + 
    chalk.red(<span class="hljs-string">`  或者\n`</span>) + 
    chalk.red(<span class="hljs-string">`  [json-shopping-xxx]: 完成xxx需求\n`</span>)
  )
  process.exit(<span class="hljs-number">1</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>展示结果如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d737176369c47d99645f300b76d50b3~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-05 下午4 34 41" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">husky</h2>
<p>写到这里本来不想折腾了，husky4.x版本其实已经够用。但是无奈版本升级改动太大，本着写文章是为了让自己加深印象的原则，我们继续来说husky高版本。husky的作用就不说了，配合hooks可以帮我们做许多事情。常见的hooks有pre-commit，commint-msg，pre-push。如果想知道更多hooks作用可以查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2Fbook%2Fzh%2Fv2%2F%25E8%2587%25AA%25E5%25AE%259A%25E4%25B9%2589-Git-Git-%25E9%2592%25A9%25E5%25AD%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://git-scm.com/book/zh/v2/%E8%87%AA%E5%AE%9A%E4%B9%89-Git-Git-%E9%92%A9%E5%AD%90" ref="nofollow noopener noreferrer">这篇文章</a>。好了话不多说，我先把husky升级一下。emmmmmmmm...升级完果然commitlint失效了。</p>
<h3 data-id="heading-16">生成.husky</h3>
<p>高版本的husky是需要你使用.husky下面的hooks脚本，不会在自己调用.git hooks脚本，生成.husky脚本很简单。执行命令husky install即可。但是由于husky是局部安装的，所以一般都是写一个script命令，然后执行npm run prepare如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"react-scripts start"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"react-scripts build"</span>,
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"react-scripts test"</span>,
    <span class="hljs-string">"eject"</span>: <span class="hljs-string">"react-scripts eject"</span>,
    <span class="hljs-string">"prepare"</span>: <span class="hljs-string">"husky install"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们先按照husky官网生成一个hooks脚本，执行命令"npx husky add .husky/pre-commit "npm test""。截图看一下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f643a4eb25e94e22a21c53833eff6e55~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-05 下午5 16 13" loading="lazy" referrerpolicy="no-referrer">
我们发现生成了pre-commit文件，并且开头是". "<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>d</mi><mi>i</mi><mi>r</mi><mi>n</mi><mi>a</mi><mi>m</mi><mi>e</mi><mi mathvariant="normal">"</mi></mrow><annotation encoding="application/x-tex">(dirname "</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathnormal">d</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">n</span><span class="mord mathnormal">a</span><span class="mord mathnormal">m</span><span class="mord mathnormal">e</span><span class="mord">"</span></span></span></span></span>0")/_/husky.sh""。说明我们定义hooks脚本时候，需要在开头带上这句话，至于_文件夹下面的这个husky.sh文件是做什么的，具体看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_21567385%2Farticle%2Fdetails%2F116429214" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_21567385/article/details/116429214" ref="nofollow noopener noreferrer">这篇文章</a>。</p>
<h3 data-id="heading-17">实现commitlint</h3>
<p>现在我们知道了高版本的husky是需要自己在.husky文件夹下写一个脚本才会生效，那么按照上面的例子，我写了如下commit-msg脚本。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.sh"</span>

commitlint -E HUSKY_GIT_PARAMS
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1：但是git commit之后发现没有生效，原因是这个脚本是不可执行的，执行如下操作chmod ug+x .husky/*,给脚本添加执行权限。</p>
<p>2：继续git commit还是有问题，因为commitlint不是全局的并且已经没有HUSKY_GIT_PARAMS这个写法了，需要替换成$1。所以最终改成如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.

npx commitlint -e $1
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>3：如果想换成自己的commit规范，写法如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.sh"</span>

node ./scripts/verify-commit-msg.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">lint-stage</h2>
<p>在前端工程里面，我觉得检查有4个方面</p>
<p>1：vs code编辑器检查</p>
<p>2：webpack编译检查</p>
<p>3：git commit提交检查</p>
<p>4：CI/CD部署检查</p>
<p>只有做了这四个方面的检查，我觉得才是比较全的，今天我们介绍的是vs code和git commit。但是git commit之后，正常情况下如果这么设置"pre-commit: eslint src/*.js",检查的是全部文件，有点浪费性能。所以出现了lint-staged，他只会检查我们提交的文件，大大提高了性能，那该如何去做呢？如下</p>
<h3 data-id="heading-19">配置husky(7版本)</h3>
<p>.husky/pre-commit</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.sh"</span>

npx lint-staged
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">配置.lintstagedrc</h3>
<pre><code class="copyable">&#123;
  "*.js": [
      "eslint --fix"
  ],
  "*.(css|less)": [
      "stylelint --fix"
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然前提都是要先安装插件lint-staged。</p>
<h2 data-id="heading-21">jest.config.js</h2>
<p>一个完整的项目jest是必不可少的，配置jest也是典型几步，我们按照项目是react框架来举例。</p>
<p>1：安装jest enzyme @testing-library/react-hooks(测试hooks)插件</p>
<p>2：配置jest.config.js如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">roots</span>: [<span class="hljs-string">'<rootDir>/src'</span>],
    <span class="hljs-attr">setupFiles</span>: [],
    <span class="hljs-attr">clearMocks</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">collectCoverage</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">transform</span>: &#123;
        <span class="hljs-string">'^.+\\.tsx?$'</span>: <span class="hljs-string">'ts-jest'</span>
    &#125;,
    <span class="hljs-comment">// 1：解决Jest: a transform must export a `process` or `processAsync` function.</span>
    <span class="hljs-attr">moduleNameMapper</span>: &#123;
        <span class="hljs-string">'^.+\\.(css|less)$'</span>: <span class="hljs-string">'./jest/style.transform.js'</span>
    &#125;,
    <span class="hljs-attr">transformIgnorePatterns</span>: [<span class="hljs-string">'\\\\node_modules\\\\'</span>],
    <span class="hljs-attr">globals</span>: &#123;
        <span class="hljs-string">'ts-jest'</span>: &#123;
            <span class="hljs-attr">tsConfig</span>: <span class="hljs-string">'./tsconfig.json'</span>
        &#125;
    &#125;,
    <span class="hljs-attr">testRegex</span>: <span class="hljs-string">'(/__tests__/.*|(\\.|/)(test|spec))\\.tsx?$'</span>,
    <span class="hljs-attr">moduleFileExtensions</span>: [<span class="hljs-string">'ts'</span>, <span class="hljs-string">'tsx'</span>, <span class="hljs-string">'js'</span>, <span class="hljs-string">'jsx'</span>, <span class="hljs-string">'json'</span>, <span class="hljs-string">'node'</span>]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3：按照以上配置可能会出现一个"a transform must export a <code>process</code> or <code>processAsync</code> function."报错，解决方法如下。创建一个jest文件夹，在该文件夹下面创建style.transform.js，内容如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.export = &#123;
    <span class="hljs-function"><span class="hljs-title">process</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跑测试用例的时候可以直接写script命令然后执行，但是这里推荐一下我们的做法，我们的项目是在提交之前跑测试用例，那么该怎么做呢？用husky高版本举例。在.husky文件夹下面创建pre-push脚本并添加执行权限，内容如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.sh"</span>

npm run test
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在编写script命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"jest"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">prettier</h2>
<p>这个配置，主要是用来格式化代码，这里有一个疑问，现在已经有eslint帮我们规范格式了，为什么还要用prettier了，我觉得可能是因为有的格式问题没法自动fix，而且就算自动fix那也只能在git commit的时候。对于强迫症来说，从百度搜索复制一份代码过来，看着很多警告不及时处理有点受不了。如果添加了prettier就可以在保存的时候自动格式化。那么如何去做呢？如下</p>
<p>1：安装vs code插件prettier</p>
<p>2：安装prettier依赖包</p>
<p>3：配置.prettierrc</p>
<pre><code class="hljs language-javscript copyable" lang="javscript">&#123;
    "trailingComma": "es5",
    "tabWidth": 4,
    "semi": true,
    "singleQuote": true,
    "bracketSpacing": false,
    "arrowParens": "avoid"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4：在vs code中的setting里面设置，保存之后自动格式化
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5810955027394a4692d75b230b32de8c~tplv-k3u1fbpfcp-watermark.image" alt="c63ac7249a2102117fb6bc4ecc390147" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">conventional-changelog</h2>
<p>这是最后一个配置了，主要和angular规范一起使用生成CHANGELOG.md。首先安装conventional-changelog-cli依赖包，然后添加一个script命令即可
如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"changelog"</span>: <span class="hljs-string">"conventional-changelog-cli -p angular -i CHANGELOG.md -s -r 0"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">最后</h2>
<p>为什么要写这一篇文章，一是为了巩固自己的知识，让自己有能力做一个从0搭建一个完整的项目。虽然这只是第一步规范，但是却很重要，第二个原因是我可以储备一个react模版，这样下次再遇到react项目，就可以直接去我的github克隆下来，快速使用。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyizhengfeng-jj%2Fjson-react-template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yizhengfeng-jj/json-react-template" ref="nofollow noopener noreferrer">模版</a>已经上传，大家可以fork,在实际的项目使用中发现问题，并且提出意见，最后用一个效果图结束这篇文章。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/751726abeaa642b0a7cc340cc6b321e1~tplv-k3u1fbpfcp-watermark.image" alt="gifski2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-25">参考文章</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_45534118%2Farticle%2Fdetails%2F104301916" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_45534118/article/details/104301916" ref="nofollow noopener noreferrer">tsconfig常用配置解析</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_21567385%2Farticle%2Fdetails%2F116429214" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_21567385/article/details/116429214" ref="nofollow noopener noreferrer">husky6版本+commitlint使用与脚本全面分析（husky v4升级v6变化巨大）</a></p></div>  
</div>
            