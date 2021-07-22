
---
title: 'package-lock.json需要提交到git？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4979'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 02:50:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=4979'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">package.json 与 package-lock.json</h2>
<p>两者都是项目的配置文件，声明了项目依赖的npm包及包的版本。</p>
<h3 data-id="heading-1">package.json</h3>
<p>package.json 包含以下内容：</p>
<ul>
<li>项目名称</li>
<li>项目版本</li>
<li>作者</li>
<li>项目许可证</li>
<li>执行命令</li>
<li>执行依赖</li>
<li>开发依赖</li>
</ul>























<table><thead><tr><th>项目名称</th><th>项目版本</th><th>作者</th><th>项目许可证</th><th>执行命令</th><th>执行依赖</th><th>开发依赖</th></tr></thead><tbody><tr><td>name</td><td>version</td><td>author</td><td>license</td><td>scripts</td><td>dependencies</td><td>devDependencies</td></tr></tbody></table>
<p>这里并不是所有的内容，只是列举了一些常用的字段，详细可参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.npmjs.com%2Fcli%2Fv7%2Fconfiguring-npm%2Fpackage-json%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.npmjs.com/cli/v7/configuring-npm/package-json/" ref="nofollow noopener noreferrer">官方文档</a>。</p>
<h3 data-id="heading-2">package-lock.json</h3>
<p>package-lock.json 在执行 npm i 的时候生成，用来记录实际安装的 npm 包的来源和版本。可以锁定安装时的包的版本，需要上传到 git，确保大家使用的包版本一致，避免由于依赖包不一致带来的问题。</p>
<h3 data-id="heading-3">dependencies 与 devDependencies 的区别</h3>
<p>dependencies 声明执行期需要的依赖，比如 echarts、jquery、axios、vue、react。
devDependencies 声明开发时所需要的依赖，比如：gulp、webpack、jest。</p>
<h3 data-id="heading-4">tips</h3>
<ul>
<li>
<ol>
<li>npm i 安装依赖时使用不同的参数，依赖增加到的位置不同：













<table><thead><tr><th>dependencies</th><th>devDependencies</th></tr></thead><tbody><tr><td>npm i xx</td><td>npm i xx --save-dev</td></tr></tbody></table>
</li>
</ol>
</li>
<li>
<ol start="2">
<li>执行 npm i 时会安装哪些依赖？
执行 npm i 时会安装 dependencies 和 devDependencies 里面的所有依赖</li>
</ol>
</li>
<li>
<ol start="3">
<li>既然已经在 package.json 中声明了依赖，为什么还需要 package-lock.json？</li>
</ol>
<ul>
<li>package.json 里只是声明了部分包的版本，并不是所有包。</li>
<li>我们除了需要固定大的依赖包版本，还需要固定依赖的依赖。</li>
</ul>
</li>
<li>
<ol start="4">
<li>版本前的符号含义</li>
</ol>

























<table><thead><tr><th>符号</th><th>含义</th></tr></thead><tbody><tr><td>无</td><td>精确匹配版本</td></tr><tr><td>^1.0.0</td><td>1.0.0 <= version < 2.0.0</td></tr><tr><td>~1.0.0</td><td>1.0.0 <= version < 2.0.0</td></tr><tr><td>=1.0.0</td><td>1.0.0 <= version</td></tr></tbody></table>
</li>
<li>
<ol start="4">
<li>如何锁定包的版本</li>
</ol>
<ul>
<li>npm i --save-exact/-E    仅对package.json中的包生效</li>
<li>依赖中声明的版本号不加符号    仅对package.json中的包生效</li>
<li>npm-shrinkwrap           生成锁定的依赖树文件</li>
<li>使用 yarn 代替 npm        yarn自动生成yarn-lock文件</li>
</ul>
</li>
</ul>
<h2 data-id="heading-5">总结</h2>
<p>这一篇提到了yarn，后面我们来看一下 yarn 和 npm 的区别。
前端开发并不难，难的是不能坚持下去，面对困难别退缩，滴水可以穿石。关注小姐姐，一起学一学。</p></div>  
</div>
            