
---
title: 'Apache 存在 Log4j 远程代码执行漏洞，将给相关企业带来哪些影响？还有哪些信息值得关注？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=3968'
author: 知乎
comments: false
date: Fri, 10 Dec 2021 08:34:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=3968'
---

<div>   
Glavo的回答<br><br><p><a data-draft-node="block" data-draft-type="link-card" href="http://link.zhihu.com/?target=https%3A//github.com/Glavo/log4j-patch" data-image="https://pic2.zhimg.com/v2-3a600311d9053866f7de6afd7876c2f2_bh.jpg" data-image-width="1200" data-image-height="600" class=" wrap external" target="_blank" rel="nofollow noreferrer">GitHub - Glavo/log4j-patch</a></p><p data-pid="DGJer95r">糊了一个简单有效的 patch 出来，将它附加在类路径的最前面即可禁用 JNDI 查找，阻止这个漏洞。适用于 Log4j2 所有版本，对 Java 版本没有要求。</p><p data-pid="UbiWvhcS">原理就是提供了一个空的 <code>JndiLookup</code> 用来覆盖 Log4j2 中的类，Log4j2 处理了加载失败的情况，会直接禁用 JNDI 查找，以此解决了这个问题。</p><p data-pid="IVRL_a-i">这是一个非侵入式的修补器，可以用来修补第三方无法修改代码的程序，譬如 Minecraft。这里提供了一个 javaagent，只需要添加 <code>-javaagent:log4j-patch-agent-1.0.jar</code> 就可以自动替换。 </p><p data-pid="rDWlhduL">这个也已经发布到 Maven Central 上了，自己的项目的话，将它作为第一个依赖项添加也能解决这个问题。</p><div class="highlight"><pre><code class="language-kotlin"><span><span class="n">dependencies</span> <span class="p">&#123;</span>
    <span class="n">implementation</span><span class="p">(</span><span class="s">"org.glavo:log4j-patch:1.0"</span><span class="p">)</span>
<span class="p">&#125;</span>
</span></code></pre></div>  
</div>
            