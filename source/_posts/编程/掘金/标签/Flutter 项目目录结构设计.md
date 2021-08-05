
---
title: 'Flutter 项目目录结构设计'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72b6369e41934560be6411c914188ef8~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:34:01 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72b6369e41934560be6411c914188ef8~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在传统 web 项目中，开发者会对项目中的公共物料做抽离复用，代码片段如：组件、接口、CSS 样式、类型（TypeScript 项目），资源如图片、icon 等。对于公共页面，更倾向于采用公共组件的形式来维护，因为页面是 web 项目中的最高级也是最重的容器，使用公共组件可以减少页面的部署次数、降低调用成本。而对于轻中量级的 Flutter 项目来说，页面是基础容器，扁平化的页面管理方式会随着页面的增多愈加难以维护，因此建议基于项目实际的业务架构进行目录结构设计，提升项目代码的可读性。</p>
<p>以 Apple Music 为例，它是长这样的：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72b6369e41934560be6411c914188ef8~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt="1_c09MpZJpX8eRnaWhpy-v6Q.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们从界面设计中可以拆出如下业务模块：</p>



































<table><thead><tr><th align="center">页面入口</th><th align="center">页面内容</th><th align="center">涉及的页面或模块</th></tr></thead><tbody><tr><td align="center">探索页</td><td align="center">给用户推荐一些个性化的曲库</td><td align="center">专辑详情页、歌手详情页、播放页等</td></tr><tr><td align="center">排行榜</td><td align="center">不同维度统计下的热歌</td><td align="center">专辑详情页、歌手详情页、播放页等</td></tr><tr><td align="center">搜索页</td><td align="center">个性化曲库内搜索</td><td align="center">搜索结果页</td></tr><tr><td align="center">乐曲库</td><td align="center">分类乐曲库</td><td align="center">歌单详情页、会员页</td></tr><tr><td align="center">设置页</td><td align="center">用户设置页，如歌曲偏好等</td><td align="center">登录页、用户信息设置页、会员页</td></tr></tbody></table>
<p>四个页面入口相对独立，本身并没有很重的业务逻辑，更多的是展示公共模块的信息。以【探索页】为例，展示用户个性化的专辑、歌手是页面的核心逻辑，登录页是完成该流程的前置条件，专辑模块、歌手模块、播放器模块是实现逻辑的必需物料。再以【设置页】为例，设置页只是不同页面的集合入口和信息的集中展示（这些子页面也可能相互跳转）。</p>
<p>综上，我们可以设计如下业务结构图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5bc3d6145a1429eb0c0d15f969c6d0c~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对上图中的四个模块的概念给出如下定义：</p>






























<table><thead><tr><th align="center">模块</th><th align="center">模块定义</th><th align="center">文件夹缩写</th></tr></thead><tbody><tr><td align="center">基础模块</td><td align="center">基础物料，自身不具备任何逻辑</td><td align="center">base</td></tr><tr><td align="center">通用模块</td><td align="center">自身带有业务逻辑的可复用模块，且保证独立</td><td align="center">common</td></tr><tr><td align="center">通用页面</td><td align="center">可复用的页面，如登录页、搜索页。或通过【多链路】展示的页面</td><td align="center">public</td></tr><tr><td align="center">业务页面</td><td align="center">一级页面，用户不需要进行交互操作即可查看的页面</td><td align="center">业务名</td></tr></tbody></table>
<p>目录结构如下：</p>
<pre><code class="hljs language-js copyable" lang="js">| 一 images                       <span class="hljs-comment">// 图片资源</span>
| 一 assets                       <span class="hljs-comment">// 其他资源，如 icon/svg/音频文件</span>
| 一 test                         <span class="hljs-comment">// 测试目录</span>
| 一 lib                          <span class="hljs-comment">// 资源目录</span>
| 一一 config                     <span class="hljs-comment">// 环境变量等配置</span>
| 一一 router                     <span class="hljs-comment">// 路由管理</span>
| 一一 common                     <span class="hljs-comment">// 通用模块</span>
   └── network                   <span class="hljs-comment">// 网络库</span>
   └── api                       <span class="hljs-comment">// 接口集合</span>
   └── components                <span class="hljs-comment">// 组件库</span>
| 一一 public                     <span class="hljs-comment">// 通用页面</span>
   └── login                     <span class="hljs-comment">// 登录模块</span>
    └── login_page               <span class="hljs-comment">// 登录页</span>
     └── login.dart
| 一一 pages                      <span class="hljs-comment">// 业务页面</span>
   └── Explore
   └── Setting
   └── Trending
     └── trending.dart
     └── Trending_list.dart
     └── Trending_list_search.dart <span class="hljs-comment">// 同一业务下二级文件命名采用继承的方式，使用’_’连接</span>
   └── Libarary
   └── Search
| 一一 helper                     <span class="hljs-comment">// 工具文件夹集合</span>
   └── format.dart               <span class="hljs-comment">// 各类工具函数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目录解析：</p>
<ul>
<li>目录根据业务进行拆分为四个支线，开发者只需要关心当前支线下的业务逻辑；</li>
<li>在上述开发场景下，一旦涉及到公共页面修改，开发者需要进入<code>public</code>文件修改，提高修改的谨慎性；</li>
<li>什么是【多链路】？如果一个页面只有唯一路径可以打开，那么该页面需要放在<code>pages</code>对应业务页面下；如果某页面有大于或等于二条的路径来打开查看，即为多链路，此时需要将该页面移动到<code>public</code>文件夹内；</li>
</ul>
<p>综上，该目录可以较好地满足一个中型项目的初始化。</p></div>  
</div>
            