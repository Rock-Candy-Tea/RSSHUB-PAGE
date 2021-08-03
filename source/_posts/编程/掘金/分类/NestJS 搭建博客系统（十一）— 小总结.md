
---
title: 'NestJS 搭建博客系统（十一）— 小总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4692'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 23:17:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=4692'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">NestJS 搭建博客系统（十一）— 小总结</h1>
<p>本系列前 10 章搭建了一个简单的博客系统服务，主要功能包括：</p>
<ul>
<li>发布文章</li>
<li>关联标签</li>
<li>上传文件</li>
<li>登陆鉴权</li>
<li>Swagger 文档</li>
</ul>
<p>等功能</p>
<p>后续预告将从单用户系统扩展为多用户系统，同时也将开发留言模块，权限模块，用户管理模块等功能，感谢阅读，感谢！</p>
<h2 data-id="heading-1">系列</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=01.%25E6%2590%25AD%25E5%25BB%25BA%25E6%25A1%2586%25E6%259E%25B6.md" target="_blank" title="01.%E6%90%AD%E5%BB%BA%E6%A1%86%E6%9E%B6.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（一）— 搭建框架</a></li>
<li><a href="https://link.juejin.cn/?target=02.%25E7%25BC%2596%25E5%2586%2599%25E9%259D%2599%25E6%2580%2581%25E6%2596%2587%25E7%25AB%25A0CURD.md" target="_blank" title="02.%E7%BC%96%E5%86%99%E9%9D%99%E6%80%81%E6%96%87%E7%AB%A0CURD.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（二）— 编写静态文章CURD</a></li>
<li><a href="https://link.juejin.cn/?target=03.%25E4%25BD%25BF%25E7%2594%25A8TypeORM%2BMysql%25E5%25AE%259E%25E7%258E%25B0%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2581%25E4%25B9%2585%25E5%258C%2596.md" target="_blank" title="03.%E4%BD%BF%E7%94%A8TypeORM+Mysql%E5%AE%9E%E7%8E%B0%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（三）— 使用TypeORM+Mysql实现数据持久化</a></li>
<li><a href="https://link.juejin.cn/?target=04.%25E4%25BD%25BF%25E7%2594%25A8%25E6%258B%25A6%25E6%2588%25AA%25E5%2599%25A8%25E3%2580%2581%25E5%25BC%2582%25E5%25B8%25B8%25E8%25BF%2587%25E6%25BB%25A4%25E5%2599%25A8%25E5%25AE%259E%25E7%258E%25B0%25E7%25BB%259F%25E4%25B8%2580%25E8%25BF%2594%25E5%259B%259E%25E6%25A0%25BC%25E5%25BC%258F.md" target="_blank" title="04.%E4%BD%BF%E7%94%A8%E6%8B%A6%E6%88%AA%E5%99%A8%E3%80%81%E5%BC%82%E5%B8%B8%E8%BF%87%E6%BB%A4%E5%99%A8%E5%AE%9E%E7%8E%B0%E7%BB%9F%E4%B8%80%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（四）— 使用拦截器、异常过滤器实现统一返回格式</a></li>
<li><a href="https://link.juejin.cn/?target=05.%25E4%25BD%25BF%25E7%2594%25A8class-validator%2B%25E7%25B1%25BB%25E9%25AA%258C%25E8%25AF%2581%25E5%2599%25A8%25E5%25AE%259E%25E7%258E%25B0%25E8%25A1%25A8%25E5%258D%2595%25E9%25AA%258C%25E8%25AF%2581.md" target="_blank" title="05.%E4%BD%BF%E7%94%A8class-validator+%E7%B1%BB%E9%AA%8C%E8%AF%81%E5%99%A8%E5%AE%9E%E7%8E%B0%E8%A1%A8%E5%8D%95%E9%AA%8C%E8%AF%81.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（五）— 使用class-validator+类验证器实现表单验证</a></li>
<li><a href="https://link.juejin.cn/?target=06.%25E4%25BD%25BF%25E7%2594%25A8Swagger%25E7%2594%259F%25E6%2588%2590%25E6%2596%2587%25E6%25A1%25A3.md" target="_blank" title="06.%E4%BD%BF%E7%94%A8Swagger%E7%94%9F%E6%88%90%E6%96%87%E6%A1%A3.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（六）— 使用Swagger生成文档</a></li>
<li><a href="https://link.juejin.cn/?target=07.%25E4%25BD%25BF%25E7%2594%25A8JWT%25E5%25AE%259E%25E7%258E%25B0%25E6%25B3%25A8%25E5%2586%258C%25E7%2599%25BB%25E5%25BD%2595.md" target="_blank" title="07.%E4%BD%BF%E7%94%A8JWT%E5%AE%9E%E7%8E%B0%E6%B3%A8%E5%86%8C%E7%99%BB%E5%BD%95.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（七）— 使用JWT实现注册登录</a></li>
<li><a href="https://link.juejin.cn/?target=08.%25E9%25A1%25B9%25E7%259B%25AE%25E4%25BC%2598%25E5%258C%2596.md" target="_blank" title="08.%E9%A1%B9%E7%9B%AE%E4%BC%98%E5%8C%96.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（八）— 项目优化</a></li>
<li><a href="https://link.juejin.cn/?target=09.%25E6%25A0%2587%25E7%25AD%25BE%25E6%25A8%25A1%25E5%259D%2597.md" target="_blank" title="09.%E6%A0%87%E7%AD%BE%E6%A8%A1%E5%9D%97.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（九）— 标签模块</a></li>
<li><a href="https://link.juejin.cn/?target=10.%25E5%259B%25BE%25E5%25BA%258A%25E6%25A8%25A1%25E5%259D%2597.md" target="_blank" title="10.%E5%9B%BE%E5%BA%8A%E6%A8%A1%E5%9D%97.md" ref="nofollow noopener noreferrer">NestJS 搭建博客系统（十）— 图床模块</a></li>
</ul></div>  
</div>
            