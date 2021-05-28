
---
title: 'Flutter 零成本搭建个人小博客'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/592fd27b47514af6b4031e3bc0f72d84~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 19:56:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/592fd27b47514af6b4031e3bc0f72d84~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">成果 <a href="http://guuguo.top/" target="_blank" rel="nofollow noopener noreferrer">个人博客</a></h1>
<blockquote>
<p>一直会喊我郭师傅的同学进了百度。为她感到高兴的同时心里也有一丝苦涩。</p>
<p>一样的职业，我还在小公司徘徊挣扎，人家已经脱离了苦海。</p>
<p>基础薄弱！静不下心！技术浅尝辄止！五年多的经验却还如新手一般只会搬砖！！！</p>
<p>既然<strong>写博客</strong>能沉淀自己的知识体系，成为面试的加分项。</p>
<p>那还不快去做！！</p>
</blockquote>
<h1 data-id="heading-1">给自己搭一个零成本的博客网页，加油郭师傅！！</h1>
<p>亲手打造 <strong>谷果之家</strong></p>
<h1 data-id="heading-2">一 · 怎么下手？</h1>
<p>身为开发者，我们都知道，搭建博客，至少需要一个服务器来存储博客网页，一个域名对外访问。在这个友好又和善的世界里，有没有慈善家给我们免费提供这种玩意呢？</p>
<p>我就找到了下面这几个备选方案</p>
<ul>
<li>
<p><a href="https://pages.github.com/" target="_blank" rel="nofollow noopener noreferrer">github page</a> (移动用户需要翻墙，处于半墙状态，所以放弃了)</p>
</li>
<li>
<p>Coding page (最后的选择)</p>
</li>
<li>
<p>gitee page</p>
</li>
<li>
<p><a href="https://www.leancloud.cn/" target="_blank" rel="nofollow noopener noreferrer">leancloud</a> 免费开发版</p>
</li>
<li>
<p>阿里云oss</p>
</li>
</ul>
<p>试试用上面的东西来搞一下。</p>
<h1 data-id="heading-3">二. 尝试可行性</h1>
<ol>
<li>
<p>github 新建仓库，开启github pages <a href="https://zhuanlan.zhihu.com/p/38480155" target="_blank" rel="nofollow noopener noreferrer">参考这个博客</a></p>
</li>
<li>
<p>flutter构建简单的app demo</p>
</li>
<li>
<p>编译出web产物push到github</p>
</li>
</ol>
<p>热泪盈眶，经过一番操作后，成功在在网页上打开了我的<a href="http://guuguo.top/guuguo-home" target="_blank" rel="nofollow noopener noreferrer">demo网页</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/592fd27b47514af6b4031e3bc0f72d84~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过搞东西难免踩坑，在此记录下我遇到的几个小坑</p>
<ul>
<li>Flutter web 页面展示的时候中文先显示口口，一会儿后再正确展示</li>
</ul>
<blockquote>
<p>原因是flutter 编译的时候 渲染模式我 canvaskit时有的bug</p>
</blockquote>
<p>在编译的时候指定渲染模式为html就可以了<code>flutter build web --web-renderer html</code></p>
<ul>
<li>编译产物push到github 之后，打开网址展示的是一片空白？？？</li>
</ul>
<blockquote>
<p>stack overflow 大神给出了<a href="https://stackoverflow.com/questions/64415471/flutter-web-on-github-pages-not-showing-content" target="_blank" rel="nofollow noopener noreferrer">答案</a>，在flutter web html入口处删掉 <code><base href="/"></code>。 再次push，一切变为正常。</p>
</blockquote>
<ul>
<li>
<p>阿里云解析解析域名不可用，最后还是使用新网解析</p>
</li>
<li>
<p>Github pages 的页面有些网络无法访问，需要翻墙且服务满，最后切换到了coding的网站托管</p>
</li>
</ul>
<h1 data-id="heading-4">三.规划所需功能</h1>
<p>我只是一个普通的懒惰开发，功能当然是能简单就简单啦~</p>
<p>所以一期功能就这么几个==</p>
<h3 data-id="heading-5">ui</h3>
<ul>
<li>
<p>文章列表页</p>
</li>
<li>
<p>文章详情页</p>
</li>
<li>
<p>文章上传页</p>
</li>
</ul>
<h3 data-id="heading-6">数据</h3>
<ul>
<li>
<p>用户</p>
</li>
<li>
<p>角色-> 游客，普通用户，管理员</p>
</li>
<li>
<p>文章列表</p>
</li>
</ul>
<h3 data-id="heading-7">功能</h3>
<ul>
<li>
<p>文章删除</p>
</li>
<li>
<p>角色登录</p>
</li>
</ul>
<h1 data-id="heading-8">四.结果</h1>
<p>第一期开发完毕，规划好的几个功能都做好了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4ad707eae304b0d86f9b3d241e0a7ba~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e76782044f2487fbd582a88d39938fd~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a41928bde747019dde969f17e885d2~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            