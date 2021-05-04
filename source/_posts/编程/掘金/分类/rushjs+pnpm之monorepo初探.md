
---
title: 'rushjs+pnpm之monorepo初探'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39104c3fd583498b85f3db2160f632c1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 01:13:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39104c3fd583498b85f3db2160f632c1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<blockquote>
<p>所在开发团队内部因为项目比较多，所以在项目上大家采用了monorepo这种项目，也就是把团队内的所有项目都统一放到一个代码仓库里面，公共的一些包和组件抽取成独立子项目或者子组件放在同个monorepo项目里面，这样方便复用组件，相关的好处网络上也有不少的文章说到，这里就不展开细说。关于monorepo的模块管理工具其实有不少，在此之前有lerna yarn等，笔者所在的团队之前是用yarn来管理monorepo的，最近做一些优化，改用rushjs+pnpm来管理，这篇blog作为笔者的一些初探学习。</p>
</blockquote>
<h3 data-id="heading-1">技术选型</h3>
<p><a href="https://rushjs.io/" target="_blank" rel="nofollow noopener noreferrer">rushjs</a><br>
<a href="https://github.com/pnpm/pnpm" target="_blank" rel="nofollow noopener noreferrer">pnpm</a><br>
<a href="https://zhuanlan.zhihu.com/p/77577415" target="_blank" rel="nofollow noopener noreferrer">monorepo</a><br>
<a href="https://tsdx.io/" target="_blank" rel="nofollow noopener noreferrer">tsdx</a></p>
<h3 data-id="heading-2">rushjs 走读</h3>
<blockquote>
<p>Rush makes life easier for JavaScript developers who build and publish many NPM packages at once. If you’re looking to consolidate all your projects into a single repo, you came to the right place! Rush is a fast, professional solution for managing this scenario.</p>
</blockquote>
<p>摘抄自官网的introduction，简单讲就是rush的出现方便js开发者一次构建和发布多个npm包，如果考虑所有的project都放到同一个代码仓库里面的话(monorepo)可以考虑使用rush，rush为此提供了快速有效的解决方案。<br>
rush的一些特点（来自官方文档）：</p>
<ul>
<li><strong>A single NPM install</strong>: rush 将你所有的项目的依赖安装到一个公共的文件夹，这个的作用不仅仅只是类似于项目根目录下的package.json，rush还通过符号链（symlinks）去重构每个项目的node_modules.这个逻辑支持 pnpm npm yarn这几种包管理器。</li>
<li><strong>Automatic local linking</strong>:  rush repo里面的每个项目都可以自动符号链到其他的项目，不需要发布包，也不需要任何npm link.</li>
<li><strong>Fast builds</strong>: rush会分析你的依赖图谱然后按照正确的顺序构建你的项目，如果两个项目之间是没有任何依赖的，rush会通过分开的进程来按照这些依赖，这种多进程的方式会比采用单线程的方式有明显的加速。</li>
<li><strong>Subset and incremental builds</strong>:  子集和增量构建，在一个非常大的代码仓库里面，如果只是想使用或者开发其中一两个项目，这时候我们可以指定构建单独的项目,rush rebuild --to 只对你的上游依赖关系进行干净的构建，当你做了一些更改之后 <code>rush rebuild --from <project></code>  只对受影响的下游项目进行干净的构建。</li>
<li><strong>Cycli dependencies</strong>: 循环依赖关系，如果一个项目间接依赖于自己的旧版本时，循环中的项目使用最后发布的版本，而其他项目仍然获得最新的。（这个笔者看的时候不是特别理解，大概的意思就是可以很好的管理多个不同版本之间的循环依赖吧）</li>
<li><strong>Bulk publishing</strong>: 当需要对代码仓库里面的多个包做release的时候，rush会检测出那些包发生了更改，自动修改所有合适的版本号，然后在每个目录下执行<code>npm publish</code></li>
<li><strong>Changelog tracking</strong>: 有变动的时候自动将变动信息聚合到一个CHANGELOG.md文件</li>
</ul>
<h3 data-id="heading-3">pnpm 相关</h3>
<p>笔者也是接触不久，这方面也是参考掘金上其他同学的文章<br>
<a href="https://juejin.cn/post/6932046455733485575" target="_blank">juejin.cn/post/693204…</a></p>
<h3 data-id="heading-4">环境</h3>
<ol>
<li>环境，笔者使用的MAC，使用window的同学可能有些不一样，本文还是以MAC这种开发环境来描述</li>
<li>安装nodejs(出于开发方便可能还要装一下nvm，方便切换不同的node版本，这里提一句，nvm的安装还是有不少网络限制的，可能要走不少弯路。。。)</li>
<li>安装<code>yarn</code> 非必须，个人的开发习惯是从<code>npm</code>转换到<code>yarn</code>的，所以自己本地是有安装yarn，有需要的可以自行安装</li>
</ol>
<h3 data-id="heading-5">初始化工作</h3>
<p>创建一个空的目录作为项目目录</p>
<pre><code class="copyable">mkdir eason-td-monorepo
cd eason-td-monorepo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装rush(使用yarn安装，或者使用npm也行)</p>
<pre><code class="copyable">yarn global add @microsoft/rush
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39104c3fd583498b85f3db2160f632c1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装pnpm</p>
<pre><code class="copyable">yarn global add pnpm
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb4544ab48a2481096b08dcf5bb7dac5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>rush初始化项目</p>
<pre><code class="copyable">rush init
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365658cdec1d46179f29295af3acc9b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用编辑器打开，我这里用的是vscode，打开后看一下rush.json, emmm,一片警告</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e471c834c5c46d99c05e44011e78967~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这时候不要慌，因为这是个json配置文件，json配置文件一般是不允许有comment的，vscode内置了一种类型叫<code>JSON with Comments</code>,专门来识别这种类型，在右下角这里切换一下类型，切换到<code>JSON with Comments</code>就不会显示警告报错了，这里不展开细讲</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1fe6379dea347199958057577e2cf17~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
按上面的一步处理完之后，可以看到这边还是有一些拼写提示，虽然不是很重要，这里还是处理一下，可忽略该步骤</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd88dccfeaf94bbcabbf59bebdb80155~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
vscode打开setting,搜索<code>cSpell.words</code>,添加进入这个<code>pnpm</code>,之后应该就不会有报错提醒</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/254154307ef8473fbf6edf0ea2f178c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd02562854d419c8c093bb9d7dbb5a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>rush.json里面可以指定运行的工具，这里是指<code>pnpm</code>,<code>npm</code>, <code>yarn</code>这几个，我们这里指定pnpm就可以，其他的也可以玩一下，这里就不展开细讲</p>
<p>rush.json里面有一大堆配置和comment，emmm，这里也不仔细去研究，先看关键的，可以看一下<code>projects</code>这个配置,因为我们要创建的是一个monorepo项目，所以到时候会有多个子项目在这个monorepo项目里面，所以到时候可以重点关注一下这个</p>
<p>再来看一下目录下的这个位置<code>common/config/rush</code>，下面有一个对应的<code>pnpmfile.js</code>文件，如果我们不是用pnpm的话，可以删除这个文件，当然啦，这里不要删除，我们用的就是pnpm</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2454a5cfbea34203b2d790bff3cbe97b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">创建子项目</h3>
<p>在项目的根目录项目创建一个<code>apps</code>的路径，用于放置我们的子项目，我们这里创建一个landing的子项目</p>
<pre><code class="copyable">mkdir apps
cd apps
yarn create react-app landing
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行完上面的命令后会回去install各种依赖，这个过程会有点长，然后我们回到上面说的那个<code>rush.json</code>里面的<code>projects</code>配置项，为我们新增的这个子项目增加一个项目名还有指定对应的目录，如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99f1e9f3054d40768c0d822769c43e53~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行完之后我们再运行一个命令，这时候只要是在项目目录下即可，可以不用在项目的根目录，rush自己会处理识别这个</p>
<pre><code class="copyable">rush update
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54c65cb71d504649bc0e6a1a2a5e19da~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c50e0a1c6f34cb68501862d48892f0a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>install完成之后，切换到<code>apps/landing</code>目录下运行这个子项目，可以用npm、yarn或者rushx运行项目，rushx是在我们全局安装rush之后会带的一个命令，这里我们推荐用rushx</p>
<pre><code class="copyable">cd apps/landing
rushx start
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35fef936f502469cb2f4637526214a2a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候会运行本地项目，然后在本地的浏览器打开该项目的页面，默认是3000端口，如果本地3000端口被占用的话会提示是否用其他端口，这时候输入yes即可</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6953f5a1ab6445528354ac7a4a28d599~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0cb8a7ae9b540d8bd61f8fd6d47b1a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里一步的话我们的一个子应用算是跑起来了，我们这个项目是monorepo项目，所以单独一个项目是不够的，还需要多其他的子项目来实验，这里我们继续创建项目（control + c 结束运行刚刚的项目）</p>
<h3 data-id="heading-7">创建第二个子项目</h3>
<p>回到项目根目录，创建一个libs目录，这个目录的作用类似于library，把一些共用的组件或者包之类的放在这个目录</p>
<pre><code class="copyable">cd ../../
mkdir libs
cd libs
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候我们需要借助一个工具叫<code>tsdx</code>来创建我们的子组件项目，创建一个components的子项目，tsdx会提供三个模板供选择，这里我们选react就可以</p>
<pre><code class="copyable">npx tsdx create components
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb8aa0d7d6684e81b728e1ccca336e3d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89e1757199054886a2c2e7749b89593e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>切换到创建出来的路径，运行一下子应用，运行没有报错，我们就control+c结束运行</p>
<pre><code class="copyable">cd components
rushx start
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc97a95c6a7a40f3a607b78319a9fdf0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新增多了一个project，这时候我们要在rush.json里面增加这个project的配置信息</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05a29d39d22d42358513e1e4887acb77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们给新创建的project命名为<code>@shared/components</code>，需要注意的是，在我们创建的<code>libs/components/package.json</code>里面有默认的<code>name</code>，这里我们要保持两边统一，这样才可以识别到具体对应的project</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cc812584e61490ca2762e6d063bd396~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
回到项目根目录更新一下，这时候会重新安装依赖</p>
<pre><code class="copyable">cd ../../
rush update --purge
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结束之后我们尝试一下在landing这个项目里面安装刚刚声明的“包”，因为这时候rush知道我们引用的是一个本地monorepo项目里面的包，所以不会尝试着通过网络去npm查找这个对应的包</p>
<pre><code class="copyable">cd apps/landing
rush add --package @shared/components
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/874a54e29bef4b7d9a7896981d4f3c85~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到提示，现在是link的的project成功，下一步推荐运行build或者rebuild</p>
<pre><code class="copyable">rush build
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90ddad6c68b04b739499f34b257f6c24~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在landing项目中引用@shared/components，我们改一下<code>apps/landing/src/App.js</code></p>
<pre><code class="copyable">import logo from './logo.svg';
import './App.css';
import &#123; Thing &#125; from '@shared/components';

function App() &#123;
  return (
    <div className="App">
      <Thing />
    </div>
  );
&#125;

export default App;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新运行起这个apps/landing这个应用</p>
<pre><code class="copyable">rushx start
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22d245ac173e4c2bad7d9d8a5b539161~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到这时候已经可以正常link引入本地的包了，到这一步基本上我们的monorepo项目就告一段落</p>
<h3 data-id="heading-8">结语</h3>
<blockquote>
<p>本次只是一个初探，关于rush和pnpm等工具还有很多不懂的地方，文中若有不妥之处，还望各位读者同学雅正。</p>
</blockquote></div>  
</div>
            