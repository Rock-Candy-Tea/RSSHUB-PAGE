
---
title: 'MyBatis 分页插件 PageHelper 5.3.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9459'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 09:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9459'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">5.3.2 </h3> 
<ul> 
 <li>使用文档更新，所有参数都包含在内，首页默认文档改为中文。</li> 
 <li>Add support for kingbase. by<span> </span><strong>HanHuimin001</strong></li> 
 <li>增加<span> </span><code>debug</code><span> </span>参数，默认<span> </span><code>false</code>，为<code>true</code>时开启<code>debug</code>模式，开始<span> </span><code>debug</code><span> </span>模式后将记录调用堆栈 by<span> </span><strong>huyingqian</strong></li> 
 <li>Add 支持count的sql支持hint语法 by<span> </span><strong>zhanliquan</strong></li> 
 <li>增加<span> </span><code>PageProperties</code><span> </span>接口，框架内部实例化的扩展类如果实现了这个接口，可以通过这个接口的方法获取分页插件配置。</li> 
 <li>增加<span> </span><code>CountMsIdGen</code><span> </span>接口，可以通过<span> </span><code>countMsIdGen</code><span> </span>配置自定义实现类，该类用于生成查询对应COUNT查询的msId。默认实现还是使用<code>countSuffix</code><span> </span>，通过扩展可以实现如<span> </span><code>selectByExample</code><span> </span>映射到对应的<span> </span><code>selectCountByExample</code><span> </span>方法。</li> 
 <li>增加<span> </span><code>keepOrderBy</code><span> </span>和<span> </span><code>keepSubSelectOrderBy</code><span> </span>配置。</li> 
 <li>增加<span> </span><code>sqlParser</code><span> </span>配置，增加<span> </span><code>JSqlParser</code><span> </span>接口，解决 jsqlparser 和 jdk 兼容性导致无法额外配置的问题。</li> 
 <li>测试使用 logback 日志框架，去掉log4j。</li> 
 <li>解决<span> </span><code>dialectKey</code><span> </span>为空导致NPE，fixed #656</li> 
</ul> 
<p><strong>Starter 发布 1.4.5</strong></p> 
<pre><code class="language-xml"><dependency>
  <groupId>com.github.pagehelper</groupId>
  <artifactId>pagehelper-spring-boot-starter</artifactId>
  <version>1.4.5</version>
</dependency></code></pre> 
<p>使用文档已经更新到最新版本，包含所有参数配置说明。</p> 
<p>gitee: <a href="https://gitee.com/free/Mybatis_PageHelper/blob/master/wikis/zh/HowToUse.md">https://gitee.com/free/Mybatis_PageHelper/blob/master/wikis/zh/HowToUse.md</a></p> 
<p>github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpagehelper%2FMybatis-PageHelper%2Fblob%2Fmaster%2Fwikis%2Fzh%2FHowToUse.md" target="_blank">https://github.com/pagehelper/Mybatis-PageHelper/blob/master/wikis/zh/HowToUse.md</a></p>
                                        </div>
                                      
</div>
            