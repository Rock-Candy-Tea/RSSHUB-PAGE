
---
title: '告别BeanUtils，Mapstruct从入门到精通、你想知道的前后端协作规范都在这了 _ 酱酱的下午茶第68期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3691'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 19:11:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=3691'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">今日主理人｜下午茶</h2>
<p>本期每日掘金由<a href="https://juejin.cn/user/1574156383557255" target="_blank" title="https://juejin.cn/user/1574156383557255"><strong>法医</strong></a>负责制作，欢迎大家关注👉👉<a href="https://juejin.cn/user/1574156383557255" target="_blank" title="https://juejin.cn/user/1574156383557255"><strong>法医</strong></a></p>
<p>PS：主理人目前正在招募中，有感兴趣的掘友们可以联系<a href="https://juejin.cn/user/3052665287739005" target="_blank" title="https://juejin.cn/user/3052665287739005"><strong>Captain</strong></a></p>
<p>酱酱们的下午茶新增优质作者介绍和码上掘金板块，专注于发掘站内优质创作者和优质内容，欢迎大家多提宝贵意见！</p>
<p><em>本文字数1500+，阅读时间大约需要 6 分钟。</em></p>
<blockquote>
<p>【掘金酱的下午茶】亮点：</p>
<ul>
<li>前端人必须掌握的抓包技能</li>
<li>肝不完这份HTTP八股文的你，再强大也是假的</li>
<li>深入剖析浏览器滚动条</li>
<li>你想知道的前后端协作规范都在这了</li>
<li>提升前端开发质量的十点经验沉淀</li>
<li>告别BeanUtils，Mapstruct从入门到精通</li>
<li>Flutter 3.3 之 SelectionArea 好不好用？用 “Bug” 带你全面了解它</li>
<li>……</li>
</ul>
<p><strong>筛选规则</strong>：文章发布时间在本期「掘金酱的下午茶」发布时间的1-3天内，且符合社区推荐标准，也会同步发布在掘金相关技术社群。</p>
</blockquote>
<h2 data-id="heading-1">每日干货｜下午茶</h2>
<p><strong>主理人们会对近期（1-3天）社区深度技术好文进行挖掘和筛选，优质的技术文章有机会出现在下方列表，排名不分先后。</strong></p>
























































































<table><thead><tr><th>文章分类</th><th>作者</th><th>文章</th><th>简介</th></tr></thead><tbody><tr><td>前端</td><td>jecyu</td><td><a href="https://sourl.co/3PzmH4" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/3PzmH4" ref="nofollow noopener noreferrer"> 前端人必须掌握的抓包技能</a></td><td>学会抓包是软件开发人员必须掌握的调试技能，本文先介绍抓包的原理，再介绍抓包工具 whistle 的使用，whistle 非常强大，本文只是粗略的介绍，更多的使用技巧，大家可以查看官方文档<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwproxy.org%2Fwhistle%2Fwebui%2Fhttps.html" title="https://link.juejin.cn/?target=http%3A%2F%2Fwproxy.org%2Fwhistle%2Fwebui%2Fhttps.html" target="_blank">whistle 文档</a></td></tr><tr><td>前端</td><td>叫苏珊的_ikun</td><td><a href="https://sourl.co/YL8ZtZ" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/YL8ZtZ" ref="nofollow noopener noreferrer"> 肝不完这份HTTP八股文的你，再强大也是假的！</a></td><td>本文介绍了五层网络模型以及面试经常问的 输入URL后发生了什么？总结了GET和POST的区别</td></tr><tr><td>前端</td><td>乔珂力</td><td><a href="https://sourl.co/55La3F" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/55La3F" ref="nofollow noopener noreferrer">深入剖析浏览器滚动条</a></td><td>为什么要专门写一篇关于浏览器滚动条的文章呢？毕竟定制滚动条属于小众需求。事情源于一次产品上线之后，用户反馈滚动条也太丑了，设计让前端帮忙改一下</td></tr><tr><td>前端</td><td>政采云前端团队</td><td><a href="https://sourl.co/VYBnE3" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/VYBnE3" ref="nofollow noopener noreferrer">你想知道的前后端协作规范都在这了</a></td><td>如果你发现前端在处理大量的逻辑，那么就是协作规范存在问题啦！前端更多的是关注交互、渲染上的逻辑，应尽量避免复杂的业务逻辑处理。万事开头难！推一套规范是需要时间去沉淀的，前端和后端同学都应多些耐心，多些理解</td></tr><tr><td>前端</td><td>小杜杜</td><td><a href="https://juejin.cn/post/7139690286527021064#heading-10" target="_blank" title="https://juejin.cn/post/7139690286527021064#heading-10">提升前端开发质量的十点经验沉淀</a></td><td>分享一下平常开发经常出现问题，增加代码质量的十个小点</td></tr><tr><td>前端</td><td>八岁小孩学编程</td><td><a href="https://sourl.co/vvgV6q" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/vvgV6q" ref="nofollow noopener noreferrer"> 2k字轻松入门Pinia，猴子都可以看懂的教程</a></td><td>无论你是否之前接触过Vuex，我都更推荐你使用<code>Pinia</code>，他相比较于Vuex，有着更好的兼容性，在Vuex的基础上去掉了<code>Mutation</code>，让语法更加简练，更符合Vue3的<code>Composition api</code>，Vuex也不会再进行更新，现在已经处于维护状态了，而Pinia作为下一代的Vuex，又有什么理由不去学习和使用呢？</td></tr><tr><td>后端</td><td>阿里巴巴大淘宝技术</td><td><a href="https://sourl.co/BfsMqq" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/BfsMqq" ref="nofollow noopener noreferrer"> 告别BeanUtils，Mapstruct从入门到精通</a></td><td>通过本次调研，Mapstruct的高性能是毋庸置疑的，这也是我选择使用他的根本原因。在使用方式上和BeanUtils对比，Mapstruct需要创建mapper接口和自定义转换工具类，其实上手成本并不高，但是我们换取了高性能，这是非常值得的，所以强烈推荐大家使用Mapstruct，是时候和BeanUtils说再见了。</td></tr><tr><td>后端</td><td>云雨雪</td><td><a href="https://sourl.co/dNc9dS" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/dNc9dS" ref="nofollow noopener noreferrer">性能优化-如何爽玩多线程来开发</a></td><td>多线程大家肯定都不陌生，理论滚瓜烂熟，八股天花乱坠，但是大家有多少在代码中实践过呢？很多人在实际开发中可能就用用@Async，new Thread()。线程池也很少有人会自己去建，默认的随便用用。在工作中大家对于多线程开发，大多是用在异步，比如发消息，但是对于提效这块最重要的优势却很少有人涉及。因此本篇文章会结合我自己的工作场景带大家去发掘项目中的多线程场景，让你的代码快如闪电。</td></tr><tr><td>后端</td><td>王老狮</td><td><a href="https://sourl.co/mwbcmC" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/mwbcmC" ref="nofollow noopener noreferrer"> 数据数据中台体系化建设核心方法论</a></td><td>说到中台，最早是由阿里在2015年提出的"大前台，小中台"战略中延申出来的概念。灵感源于芬兰的一家游戏公司superCell，也就是接连做出部落冲突，皇室战争等爆款游戏的公司。该公司里一般5-7人就组织成一个独立开发团队，通过将公司开发过程中公共和通用的游戏素材和算法整合起来，并在过程中积累了非常科学的研发工具和框架体系，构建了一个强大的中台。这样就可以快速支持起一个小团队短时间内开发出一款新游戏。如果市场观察不好，也可以快速砍掉。减少试错成本。</td></tr><tr><td></td><td></td><td></td></tr><tr><td>后端</td><td>丘山子</td><td><a href="https://sourl.co/Wpsjpp" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/Wpsjpp" ref="nofollow noopener noreferrer">云青青兮欲雨——Go的数组与切片傻傻分不清楚？</a></td><td>我们在使用Go语言进行程序的编写时，不可避免会遇到切片和数组的抉择。其实我建议选切片，因为切片比数组更加好用，也更加安全。本文会比较切片与数组的异同，也会介绍切片的一些特性。</td></tr><tr><td>移动端</td><td>恋猫de小郭</td><td><a href="https://sourl.co/AiiMx9" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/AiiMx9" ref="nofollow noopener noreferrer">Flutter 3.3 之 SelectionArea 好不好用？用 “Bug” 带你全面了解它</a></td><td>SelectionArea的出现补全了 Flutter 的长久以来的短板之一，不过基于 SelectionArea 实现的复杂程度，目前 SelectionArea 还有不少的细节需要优化，但是万事开头难，本次 3.3 SelectionArea 的落地也算是一个不错的开始。</td></tr><tr><td>移动端</td><td>姚明振</td><td><a href="https://sourl.co/xrGQEC" target="_blank" rel="nofollow noopener noreferrer" title="https://sourl.co/xrGQEC" ref="nofollow noopener noreferrer"> iOS IconFont 最佳实践  干掉图片资源，优雅地使用 Icon</a></td><td>作为大前端开发者一定经常使用很多小图标，使用小图标不可避免的要导入图片资源，图片资源又要考虑倍率、尺寸和颜色，总之体验不佳。为了解决这个问题 Iconfont 应运而生，不过原生使用体验还是不够好，本文目的就是优化开发体验</td></tr></tbody></table>
<h2 data-id="heading-2">优秀作者推荐｜下午茶</h2>
<p>推荐作者来源于月榜上榜作者，欢迎大家关注榜单小助手，了解更多优质作者：<a href="https://juejin.cn/user/4433674252325966/posts" target="_blank" title="https://juejin.cn/user/4433674252325966/posts">juejin.cn/user/443367…</a></p>

























<table><thead><tr><th>用户名</th><th>简介</th><th>个人主页链接</th></tr></thead><tbody><tr><td>摸鱼的春哥</td><td>我没秃！真没！（哭腔，破音）</td><td><a href="https://juejin.cn/user/1714893870865303" title="https://juejin.cn/user/1714893870865303" target="_blank">juejin.cn/user/171489…</a></td></tr><tr><td>TodoCoder</td><td>多年后台开发及架构经验，分享编程思想，解决方案，擅长Java,go,python,k8s,docker及开源安全治理等，微信公众号：TodoCoder, 欢迎大家关注, 有开发上的问题欢迎留言，可以一起探讨，感谢！</td><td><a href="https://juejin.cn/user/2472125987040093%22https://juejin.cn/user/2472125987040093%22" target="_blank" title="https://juejin.cn/user/2472125987040093%22https://juejin.cn/user/2472125987040093%22">juejin.cn/user/247212…</a></td></tr><tr><td>fundroid</td><td>公众号「AndroidPub」</td><td><a href="https://juejin.cn/user/3931509309842872%22https://juejin.cn/user/3931509309842872%22" target="_blank" title="https://juejin.cn/user/3931509309842872%22https://juejin.cn/user/3931509309842872%22">juejin.cn/user/393150…</a></td></tr></tbody></table>
<h2 data-id="heading-3">趣味码上掘金分享｜下午茶</h2>















<table><thead><tr><th>作者</th><th>代码介绍</th><th>简介</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/user/2840793779295133" target="_blank" title="https://juejin.cn/user/2840793779295133">小南</a></td><td>【HTML】【休闲益智】躲包包小游戏（ 找靓仔的捉迷藏小游戏</td><td><a href="https://juejin.cn/post/7140398559156764703" target="_blank" title="https://juejin.cn/post/7140398559156764703">juejin.cn/post/714039…</a></td></tr></tbody></table>
<p><span href="https://code.juejin.cn/pen/7140113542069354509" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140113542069354509" data-src="https://code.juejin.cn/pen/7140113542069354509" style="display: none" loading="lazy"></iframe></span></p>
<h2 data-id="heading-4">📖 投稿专区｜下午茶</h2>
<blockquote>
<p>大家可以在评论区推荐认为不错的文章，并附上链接和推荐理由，有机会登上下一期。文章创建日期必须在近1-3天内；可以推荐自己的文章、也可以推荐他人的文章。</p>
</blockquote></div>  
</div>
            