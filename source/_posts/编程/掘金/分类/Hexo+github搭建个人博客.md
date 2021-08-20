
---
title: 'Hexo+github搭建个人博客'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=598'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 17:38:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=598'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>在我刚入行的时候，查看其他前辈的技术博客会很佩服，也想整个自己的博客，做做笔记，总结总结问题和解决方法等等，但是苦于对域名、博客什么的都不懂，不过现在好了，通过Hexo+Github,只需本地跑起来，然后将代码放到github上，就能拥有自己的博客，很简单，下边这是我的博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Freda011.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://reda011.github.io/" ref="nofollow noopener noreferrer">reda011.github.io/</a>，献丑了。</p>
<p>闲话少说，马上开搞</p>
<p>我的是win10 64位系统，接下来需要三个重要的东西：1、Node，2、Git，3、Github账户，三者缺一不可。</p>
<h2 data-id="heading-0">环境配置：</h2>
<ol>
<li>安装Node(必须)</li>
</ol>
<p>可去<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/" ref="nofollow noopener noreferrer">Node官网</a>下载最新版本node,一路下一步安装即可；</p>
<p>2.安装Git(必须)</p>
<p>可去<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://git-scm.com/" ref="nofollow noopener noreferrer">Git官网</a>下载，用以将本地代码推送到github上；</p>
<p>3.github账号(必须)</p>
<p>用以托管代码，没有账号的自行去<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/" ref="nofollow noopener noreferrer">github官网</a>申请；</p>
<p>4.安装Hexo</p>
<p>Node和Git安装好之后，就可以通过npm包管理工具安装Hexo：</p>
<pre><code class="copyable">$ npm install -g hexo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：国内使用npm有的时候会很慢，进而会导致很多奇怪的问题，可通过国内淘宝镜像代替</p>
<p>淘宝镜像使用方法：</p>
<pre><code class="copyable">$ npm install -g cnpm --registry=https://registry.npm.taobao.org
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述命令之后，即可使用cnpm代替后续的npm</p>
<p>5.初始化</p>
<pre><code class="copyable">$ hexo init Blog
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述命令会创建一个名为Blog的文件夹，博客初始化的所有内容都将存放在这个文件夹中</p>
<p>接下来切换到Blog目录下</p>
<pre><code class="copyable">$ cd Blog
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">$ npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行如下命令，生成静态页面</p>
<pre><code class="copyable">$ hexo generate(或者直接hexo g)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装hexo-server包</p>
<pre><code class="copyable">$ npm install hexo-server --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.本地启动</p>
<pre><code class="copyable">$ hexo server (hexo s)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器输入<a href="https://link.juejin.cn/?target=http%3A%2F%2Fbaixin.io%2F2015%2F08%2FHEXO%25E6%2590%25AD%25E5%25BB%25BA%25E4%25B8%25AA%25E4%25BA%25BA%25E5%258D%259A%25E5%25AE%25A2%2F%25E5%25B0%25B1%25E5%258F%25AF%25E4%25BB%25A5%25E7%259C%258B%25E5%2588%25B0%25E6%259C%2580%25E5%258E%259F%25E5%25A7%258B%25E7%259A%2584%25E6%2595%2588%25E6%259E%259C%25E4%25BA%2586" target="_blank" rel="nofollow noopener noreferrer" title="http://baixin.io/2015/08/HEXO%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/%E5%B0%B1%E5%8F%AF%E4%BB%A5%E7%9C%8B%E5%88%B0%E6%9C%80%E5%8E%9F%E5%A7%8B%E7%9A%84%E6%95%88%E6%9E%9C%E4%BA%86" ref="nofollow noopener noreferrer">http://localhost:4000</a>,就能看到本地hexo的helloworld页面</p>
<p>如上，本地已经能跑起来了。</p>
<h3 data-id="heading-1">配置Github</h3>
<p>1.创建一个repository</p>
<p>名字必须为：your_user_name.github.io,例如：reda.github.io</p>
<p>2.在本地Blog文件夹下的_config.yml中进行关联设置，将其deploy字段修改为如下：</p>
<pre><code class="copyable">deploy:
  type: git
  repository: https://github.com/reda/reda.github.io.git
  branch: master
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中repository字段设置成<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2F%257Byourname%257D%2F%257Byourname%257D.github.io.git" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/%7Byourname%7D/%7Byourname%7D.github.io.git" ref="nofollow noopener noreferrer">github.com/&#123;yourname&#125;/…</a></p>
<p>3.执行如下命令，进行Git部署</p>
<pre><code class="copyable">$ npm install hexo-deployer-git --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.最后，执行配置命令</p>
<pre><code class="copyable">$ hexo deploy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功之后，在浏览器输入<a href="https://link.juejin.cn/?target=http%3A%2F%2Freda.github.io%2F%25E5%25B0%25B1%25E8%2583%25BD%25E7%259C%258B%25E5%2588%25B0%25E8%2587%25AA%25E5%25B7%25B1%25E7%259A%2584%25E5%258D%259A%25E5%25AE%25A2%25E4%25BA%2586%25EF%25BC%258C%25E6%2598%25AF%25E4%25B8%258D%25E6%2598%25AF%25E5%25BE%2588%25E9%2585%25B7" target="_blank" rel="nofollow noopener noreferrer" title="http://reda.github.io/%E5%B0%B1%E8%83%BD%E7%9C%8B%E5%88%B0%E8%87%AA%E5%B7%B1%E7%9A%84%E5%8D%9A%E5%AE%A2%E4%BA%86%EF%BC%8C%E6%98%AF%E4%B8%8D%E6%98%AF%E5%BE%88%E9%85%B7" ref="nofollow noopener noreferrer">reda.github.io/就能看到自己的博客了，…</a></p>
<p>注意：有时hexo deploy时，会报错：</p>
<p>bash: /dev/tty: No such device or address </p>
<p>error: failed to execute prompt script (exit code 1) </p>
<p>fatal: could not read Username for 'GitHub · Where software is built': No error</p>
<p>...</p>
<p>此时可将上述repository字段设置成https://&#123;yourname&#125;:&#123;yourpassword&#125;@github.com/&#123;yourname&#125;/&#123;yourname&#125;.github.io.git</p>
<p>对了，如果你不喜欢Hexo默认的主题，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhexojs%2Fhexo%2Fwiki%2FThemes" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/hexojs/hexo/wiki/Themes" ref="nofollow noopener noreferrer">主题列表</a>还有很多主题供你选择，总有一款你中意。</p>
<h2 data-id="heading-2">更换主题</h2>
<p>按照各主题安装说明，直接clone到本地，然后将Blog文件夹下的_config.yml的theme字段修改为要替换的主题名称即可。</p>
<h2 data-id="heading-3">部署步骤</h2>
<p>每次部署基本可遵循以下三步：</p>
<pre><code class="copyable">$ hexo clean 
$ hexo generate 
$ hexo deploy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用命令：</p>
<pre><code class="copyable">$ hexo new "postName" #新建文章 
$ hexo new page "pageName" #新建页面 
$ hexo generate #生成静态页面至public目录 
$ hexo server #开启预览访问端口（默认端口4000，'ctrl + c'关闭server） 
$ hexo deploy #将.deploy目录部署到GitHub 
$ hexo help  #查看帮助 
$ hexo version  #查看Hexo的版本
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            