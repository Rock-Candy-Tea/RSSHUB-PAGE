
---
title: 'framework-plugin 轻量级安卓组件化架构插件'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=5342'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 19:46:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=5342'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">framework-plugin 组件化架构插件</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsongjianzaina%2Fframework-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/songjianzaina/framework-plugin" ref="nofollow noopener noreferrer">Github</a></p>
<h2 data-id="heading-1">优势</h2>
<ul>
<li>轻量级组件框架</li>
<li>即插即用</li>
<li>使用json文件动态配置, 减少同步时间</li>
</ul>
<h2 data-id="heading-2">使用</h2>
<ol>
<li>在项目的 <code>build.gradle</code> 中添加：</li>
</ol>
<pre><code class="copyable">buildscript &#123;
  repositories &#123;
   ...
maven &#123; url 'https://dl.bintray.com/songjianzaina/insoan' &#125;
   &#125;
  dependencies &#123;
     classpath 'com.insworks.plugin:framework-plugin:1.0.5'
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在宿主module中使用插件</li>
</ol>
<pre><code class="copyable">apply plugin: 'framework-plugin'
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>同步工程,等待文件夹自动生成</li>
</ol>
<h2 data-id="heading-3">配置</h2>
<p>你可以在build.gradle中配置插件的几个属性，如果不设置，所有的属性都使用默认值</p>
<pre><code class="copyable">frame&#123;
    subDirName "androidModule"//子模块目录 App默认androidModule Lib默认androidLib
    jsonName "androidModule"//子模块json文件名 默认同上

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">更新历史</h2>








































<table><thead><tr><th>版本号</th><th>功能点</th><th>链接</th></tr></thead><tbody><tr><td>1.0.0</td><td>初步实现架构文件自动生成</td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbintray.com%2Fsongjianzaina%2Finsoan%2Fframework-plugin%2F1.0.0%2Flink" target="_blank" rel="nofollow noopener noreferrer" title="https://bintray.com/songjianzaina/insoan/framework-plugin/1.0.0/link" ref="nofollow noopener noreferrer"> [外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-U2eorsaW-1598265667292)(https://api.bintray.com/packages/songjianzaina/insoan/framework-plugin/images/download.svg?version=1.0.0)] </a></td></tr><tr><td>1.0.1</td><td>增加全局文件夹以及全局libs</td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbintray.com%2Fsongjianzaina%2Finsoan%2Fframework-plugin%2F1.0.1%2Flink" target="_blank" rel="nofollow noopener noreferrer" title="https://bintray.com/songjianzaina/insoan/framework-plugin/1.0.1/link" ref="nofollow noopener noreferrer"> [外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-9Hm0qoay-1598265667294)(https://api.bintray.com/packages/songjianzaina/insoan/framework-plugin/images/download.svg?version=1.0.1)] </a></td></tr><tr><td>1.0.2</td><td>增加子模块目录名和配置文件名自定义配置</td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbintray.com%2Fsongjianzaina%2Finsoan%2Fframework-plugin%2F1.0.2%2Flink" target="_blank" rel="nofollow noopener noreferrer" title="https://bintray.com/songjianzaina/insoan/framework-plugin/1.0.2/link" ref="nofollow noopener noreferrer"> [外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-vIgu4B0t-1598265667295)(https://api.bintray.com/packages/songjianzaina/insoan/framework-plugin/images/download.svg?version=1.0.2)] </a></td></tr><tr><td>1.0.3</td><td>优化清单文件合并</td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbintray.com%2Fsongjianzaina%2Finsoan%2Fframework-plugin%2F1.0.3%2Flink" target="_blank" rel="nofollow noopener noreferrer" title="https://bintray.com/songjianzaina/insoan/framework-plugin/1.0.3/link" ref="nofollow noopener noreferrer"> [外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-tvinJuiM-1598265667296)(https://api.bintray.com/packages/songjianzaina/insoan/framework-plugin/images/download.svg?version=1.0.3)] </a></td></tr><tr><td>1.0.4</td><td>增加Activity自动注册清单文件 (还未完善)</td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbintray.com%2Fsongjianzaina%2Finsoan%2Fframework-plugin%2F1.0.4%2Flink" target="_blank" rel="nofollow noopener noreferrer" title="https://bintray.com/songjianzaina/insoan/framework-plugin/1.0.4/link" ref="nofollow noopener noreferrer"> [外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-we3hApma-1598265667297)(https://api.bintray.com/packages/songjianzaina/insoan/framework-plugin/images/download.svg?version=1.0.4)] </a></td></tr><tr><td>1.0.5</td><td>1.升级gradle依赖至4.0.0  <br> 2.新增values目录下attr和styles文件的自动生成 <br> 3.解决子模块libs目录so库无法引用的问题 <br> 4.优化插件加载方式 提升构建速度 <br> 5.移除多余log</td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbintray.com%2Fsongjianzaina%2Finsoan%2Fframework-plugin%2F1.0.5%2Flink" target="_blank" rel="nofollow noopener noreferrer" title="https://bintray.com/songjianzaina/insoan/framework-plugin/1.0.5/link" ref="nofollow noopener noreferrer"> [外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-bK2xtjUJ-1598265667298)(https://api.bintray.com/packages/songjianzaina/insoan/framework-plugin/images/download.svg?version=1.0.5)] </a></td></tr></tbody></table></div>  
</div>
            