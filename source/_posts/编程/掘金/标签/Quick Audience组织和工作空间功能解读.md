
---
title: 'Quick Audience组织和工作空间功能解读'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88bc69c4137749749878a8f09a829fd3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 22:12:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88bc69c4137749749878a8f09a829fd3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​近期，Quick Audience完成了权限系统全面升级，可以<strong>解决集团企业不同品牌、不同运营组织，不同消费者运营的诉求，精细化保障企业数据访问安全，提升管控的灵活度。</strong><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88bc69c4137749749878a8f09a829fd3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>Quick Audience整个系统分为组织管理和工作空间两层。一个组织可以包含多个工作空间，而每个工作空间的数据是隔离的。</p>
<p>组织层面，组织管理员拥有系统最高权限，可操作管理所有空间的数据和功能。空间层面，分为管理员、开发者、分析师、及自定义角色，权限作用范围均限定在本空间内。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c425a5e3fa67455c955e1246c2793b68~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>实际应用中，若集团存在多个品牌，多品牌之间需要进行数据隔离，建议直接将Quick Audience系统中的“组织“对应“集团”，各“工作空间”对应集团下属的各个“品牌”。由集团管理人员在系统的组织层面进行表权限管控和下放，实现不同的工作空间可见不同的原始表数据，同时各空间也有一定的操作自主性，可以进行空间人员的运营管控。</p>
<p>在依据集团的数据进行分析的同时也可以绑定品牌自有数据源进行数据分析。</p>
<p>若无品牌数据隔离场景，则无需划分多个工作空间，仅在默认空间内操作即可。</p>
<p>下面将从数据管控和人员管控两方面进行详细介绍。</p>
<p>1、数据管控，仅组织管理员可操作，在管理中心/组织管理/数据授权中设置，实现流程如下：</p>
<p>首先完成数据源的创建<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b52ab506894418a819f0a8baa874716~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>点击数据的操作功能，进行权限设置通过表权限、行权限、列权限实现不同程度的数据管控。</p>
<ul>
<li>若某张数据表专属于某个工作空间，可通过表权限完成设置。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e23dc84024af4c78889d9bc6c5713575~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<ul>
<li>若一张会员表中，既有品牌A的会员数据也有品牌B的会员数据，可通过行级权限功能对指定字段进行行过滤。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1439b35f2cfe44859a7b235651e987ff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<ul>
<li>若会员表中部分标签列专属于某个工作空间，则可以通过列权限进行设置。行、列权限可以同时使用，实现数据精准管控。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63c3f94b48484e1f8c5bbce355cbfe23~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>2、人员管控，分为组织和工作空间两种场景。</p>
<ul>
<li>
<p>组织管理员可进行全局管控，在管理中心/组织管理/组织成员中设置，主要完成组织成员的增删和角色的修改操作。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/768dae9d22234725a0c0e0d37c651261~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
</li>
<li>
<p>空间管理员只可对本空间内的成员进行管控，在管理中心/工作空间/空间成员管理中设置，主要完成空间成员的增减、角色管理、用户组设置。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5506a07dff492b834bf3a0d0bc95b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000282909%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000282909/" ref="nofollow noopener noreferrer">​原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            