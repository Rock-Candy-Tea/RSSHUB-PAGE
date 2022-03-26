
---
title: 'BeeCP-3.3.3， 一款小型 JDBC 连接池'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5db2a795beba7ff63b722ffc276d5614d3e.png'
author: 开源中国
comments: false
date: Sat, 26 Mar 2022 20:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5db2a795beba7ff63b722ffc276d5614d3e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong> 一：产品简介</strong></p> 
<p>BeeCP是一款小型JDBC连接池组件，它具有性能高，代码轻，稳定好的特点。</p> 
<p><strong>二：修改内容</strong></p> 
<p><strong>1：</strong>优化pom.xml文件，减少外部依赖包（日志包和JTA包需要自行下载）</p> 
<p><img height="525" src="https://oscimg.oschina.net/oscnet/up-5db2a795beba7ff63b722ffc276d5614d3e.png" width="407" referrerpolicy="no-referrer"></p> 
<p><strong>2：</strong>连接工厂类配置支持四种类型</p> 
<p><img height="226" src="https://oscimg.oschina.net/oscnet/up-38c015804a88ca61cfa9b4569522606af97.png" width="511" referrerpolicy="no-referrer"></p> 
<p><strong>3：</strong>重构XAConnection的支持部分，并提供一个本地XAConnection的实现（<strong>建议先试用，不要用于生产</strong>）</p> 
<p><strong>4：</strong>增加对JTA的支持（<strong>建议先试用，不要用于生产</strong>）</p> 
<p><strong>5：</strong>优化配置注入，支持大写属性（比如：URL）</p> 
<p><strong>三：代码质量</strong></p> 
<p><img alt="图片" src="https://user-images.githubusercontent.com/32663325/160237145-87b794bf-d64c-4246-8f26-68a93862f69d.png" referrerpolicy="no-referrer"></p> 
<p><strong>四：软件包下载</strong><span style="color:#333333"><strong>(Java7或更高版本)</strong></span></p> 
<pre><span><</span><span><span><span>dependency</span></span></span><span>></span>
   <span><</span><span><span><span>groupId</span></span></span><span>></span>com.github.chris2018998<span></</span><span><span><span>groupId</span></span></span><span>></span>
   <span><</span><span><span><span>artifactId</span></span></span><span>></span>beecp<span></</span><span><span><span>artifactId</span></span></span><span>></span>
   <span><</span><span><span><span>version</span></span></span><span>></span>3.3.3<span></</span><span><span><span>version</span></span></span><span>></span>
<span></</span><span><span><span>dependency</span></span></span><span>></span></pre> 
<p><strong>五：项目地址</strong></p> 
<ul> 
 <li>国内地址： <a href="https://gitee.com/Chris2018998/BeeCP">https://gitee.com/Chris2018998/BeeCP</a></li> 
 <li>国外地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FChris2018998%2FBeeCP" target="_blank">https://github.com/Chris2018998/BeeCP</a></li> 
</ul>
                                        </div>
                                      
</div>
            