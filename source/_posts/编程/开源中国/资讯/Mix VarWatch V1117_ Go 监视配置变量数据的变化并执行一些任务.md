
---
title: 'Mix VarWatch V1.1.17_ Go 监视配置变量数据的变化并执行一些任务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7966'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 10:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7966'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>OpenMix 出品：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenmix.org%2Fmix-go" target="_blank">https://openmix.org</a></p> 
</blockquote> 
<h2 style="text-align:start">Mix VarWatch</h2> 
<p style="text-align:start">监视配置结构体变量的数据变化并执行一些任务</p> 
<p style="text-align:start">Monitor the data changes of configuration structure variables and perform some tasks</p> 
<h2>源码地址</h2> 
<p>Star 一下不迷路，下次用的时候还能找到</p> 
<p>- https://github.com/mix-go/varwatch<br> - https://gitee.com/mix-go/varwatch</p> 
<h2 style="text-align:start">Installation</h2> 
<div style="text-align:start"> 
 <pre><code>go get github.com/mix-go/varwatch
</code></pre> 
</div> 
<h2 style="text-align:start">Usage</h2> 
<p style="text-align:start">当采用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspf13%2Fviper" target="_blank">spf13/viper</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjinzhu%2Fconfigor" target="_blank">jinzhu/configor</a> 这种绑定变量的配置库来动态更新配置信息</p> 
<blockquote> 
 <p>任何采用 &Config 指针绑定数据的配置库都可以</p> 
</blockquote> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">var</span> Config <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Logger</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Level</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"level"`</span>
&#125; <span style="color:var(--color-prettylights-syntax-string)">`json:"logger" varwatch:"logger"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Database</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">User</span>    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"user"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Pwd</span>     <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"pwd"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Db</span>      <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"db"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">MaxOpen</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`json:"max_open"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">MaxIdle</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`json:"max_idle"`</span>
&#125; <span style="color:var(--color-prettylights-syntax-string)">`json:"database" varwatch:"database"`</span>
&#125;

err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> viper.<span style="color:var(--color-prettylights-syntax-entity)">Unmarshal</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>Config)</pre> 
</div> 
<p style="text-align:start">以动态修改日志级别举例：当 <code>Config.Logger.Level</code> 发生变化时我们需要执行一些代码修改日志的级别</p> 
<ul> 
 <li>首先将 Logger 节点配置 <code>varwatch:"logger"</code> 标签信息</li> 
 <li>然后采用以下代码执行监听逻辑</li> 
</ul> 
<div style="text-align:start"> 
 <pre>w <span style="color:var(--color-prettylights-syntax-constant)">:=</span> varwatch.<span style="color:var(--color-prettylights-syntax-entity)">NewWatcher</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>Config, <span style="color:var(--color-prettylights-syntax-constant)">10</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>)
w.<span style="color:var(--color-prettylights-syntax-entity)">Watch</span>(<span style="color:var(--color-prettylights-syntax-string)">"logger"</span>, <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">// 获取变化后的值</span>
    lv <span style="color:var(--color-prettylights-syntax-constant)">:=</span> Config.<span style="color:var(--color-prettylights-syntax-constant)">Logger</span>.<span style="color:var(--color-prettylights-syntax-constant)">Level</span>
    <span style="color:var(--color-prettylights-syntax-comment)">// 修改 logrus 的日志级别</span>
    logrus.<span style="color:var(--color-prettylights-syntax-entity)">SetLevel</span>(logrus.<span style="color:var(--color-prettylights-syntax-entity)">Level</span>(<span style="color:var(--color-prettylights-syntax-entity)">uint32</span>(lv)))
&#125;)</pre> 
 <div>
  需要动态修改连接池信息，或者数据库账号密码都可以通过上面的范例实现。
 </div> 
</div> 
<h2 style="text-align:start">License</h2> 
<p style="text-align:start">Apache License Version 2.0, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2F" target="_blank">http://www.apache.org/licenses/</a></p>
                                        </div>
                                      
</div>
            