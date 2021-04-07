
---
title: 'sureness 1.0.2 发布，面向 restful api 的认证鉴权框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/tomsun28/sureness/raw/master/docs/_images/benchmark_cn.png'
author: 开源中国
comments: false
date: Wed, 07 Apr 2021 08:33:00 GMT
thumbnail: 'https://gitee.com/tomsun28/sureness/raw/master/docs/_images/benchmark_cn.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p><strong>新增特性</strong></p> 
   <ul> 
    <li>支持seesion认证鉴权 #86   </li> 
    <li>添加seesion使用样例 #87   </li> 
    <li>添加分布式缓存session使用样例 #88   </li> 
    <li>去除防sql注入中的 (--)字符串正则匹配，防止其误识别jwt的问题 #85  </li> 
   </ul> 
   <p><strong>BugFix    </strong></p> 
   <p>Fix the problem that authentication is still needed when the resource… #84     <br> fix api can be accessed by any role when accessRole not config #83 </p> 
   <p><strong>使用</strong></p> 
   <pre><code><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>com.usthe.sureness<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>sureness-core<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.0.2<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></code></pre> 
   <h2 style="text-align:left"><strong><span style="color:#333333">📫</span> sureness</strong></h2> 
   <p style="text-align:left"><span style="color:#333333">在主流的前后端分离架构中，如何通过有效快速的认证鉴权来保护后端提供的</span><code><span style="color:#333333">restful api</span></code><span style="color:#333333">变得尤为重要。对现存框架，不原生支持</span><code><span style="color:#333333">rest</span></code><span style="color:#333333">的</span><code><span style="color:#333333">apache shiro</span></code><span style="color:#333333">，</span> <span style="color:#333333">还是深度绑定</span><code><span style="color:#333333">spring</span></code><span style="color:#333333">，学习曲线陡峭的</span><code><span style="color:#333333">spring security</span></code><span style="color:#333333">，或多或少都不是我们的理想型。</span><br> <span style="color:#333333">于是乎</span><code><span style="color:#333333">sureness</span></code><span style="color:#333333">诞生了，我们希望能解决这些，提供一个面向</span><strong><span style="color:#333333">restful api</span></strong><span style="color:#333333">，<strong>无框架依赖</strong>，可以<strong>动态修改权限</strong>，<strong>多认证策略</strong>，<strong>更快速度</strong>，<strong>易用易扩展</strong>的认证鉴权框架。</span></p> 
   <h2 style="text-align:left"><strong><span style="color:#333333">🎡</span> <span style="color:green">介绍</span></strong></h2> 
   <p style="text-align:left"><code><span style="color:#333333">sureness</span></code> <span style="color:#333333">是我们在深度使用权限框架</span> <code><span style="color:#333333">apache shiro</span></code> <span style="color:#333333">之后</span><span style="color:#333333">,</span><span style="color:#333333">吸取其一些优点全新设计开发的一个认证鉴权框架</span><br> <span style="color:#333333">1. 面向</span> <code><span style="color:#333333">restful api</span></code> <span style="color:#333333">的认证鉴权</span><span style="color:#333333">,</span><span style="color:#333333">基于</span> <code><span style="color:#333333">rbac</span></code><span style="color:#333333"> (</span><span style="color:#333333">用户</span><span style="color:#333333">-</span><span style="color:#333333">角色</span><span style="color:#333333">-</span><span style="color:#333333">资源</span><span style="color:#333333">)</span><span style="color:#333333">主要关注于对</span> <code><span style="color:#333333">restful api</span></code> <span style="color:#333333">的安全保护</span><br> <span style="color:#333333">2. 无特定框架依赖</span><span style="color:#333333">(</span><span style="color:#333333">本质就是过滤器处拦截判断</span><span style="color:#333333">,</span><span style="color:#333333">已有</span><code><span style="color:#333333">springboot,quarkus,javalin,ktor</span></code><span style="color:#333333">等集成样例</span><span style="color:#333333">)</span><br> <span style="color:#333333">3. 支持动态修改权限配置</span><span style="color:#333333">(</span><span style="color:#333333">动态修改配置每个</span><code><span style="color:#333333">rest api</span></code><span style="color:#333333">谁有权访问</span><span style="color:#333333">)</span><br> <span style="color:#333333">4. 支持</span> <code><span style="color:#333333">websocket</span></code><span style="color:#333333"> ,</span><span style="color:#333333">主流</span><code><span style="color:#333333">http</span></code><span style="color:#333333">容器</span> <code><span style="color:#333333">servlet</span></code> <span style="color:#333333">和</span> <code><span style="color:#333333">jax-rs</span></code><br> <span style="color:#333333">5. 支持多种认证策略</span><span style="color:#333333">, </span><code><span style="color:#333333">jwt, basic auth, digest auth</span></code><span style="color:#333333"> ... </span><span style="color:#333333">可扩展自定义支持的认证方式</span><br> <span style="color:#333333">6. 基于改进的字典匹配树拥有的高性能</span><br> <span style="color:#333333">7. 良好的扩展接口</span><span style="color:#333333">, </span><span style="color:#333333">样例和文档</span></p> 
   <p style="text-align:left"><code><span style="color:#333333">sureness</span></code><span style="color:#333333">的低配置，易扩展，不耦合其他框架，希望能帮助开发者对自己的项目多场景快速安全的进行保护</span></p> 
   <p style="text-align:left"><strong><span style="color:#333333">🔍</span> <span style="color:#333333">框架对比</span></strong></p> 
   <table border="1" cellspacing="0" style="width:776px"> 
    <thead> 
     <tr> 
      <td style="border-color:#cccccc"> <p style="text-align:center"><strong><span style="color:#333333">~</span></strong></p> </td> 
      <td style="border-color:#cccccc"> <p style="text-align:center"><strong><span style="color:#333333">sureness</span></strong></p> </td> 
      <td style="border-color:#cccccc"> <p style="text-align:center"><strong><span style="color:#333333">shiro</span></strong></p> </td> 
      <td style="border-color:#cccccc"> <p style="text-align:center"><strong><span style="color:#333333">spring security</span></strong></p> </td> 
     </tr> 
    </thead> 
    <tbody> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">多框架支持</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">需改动支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">不支持</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">restful api</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">需改动支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">websocket</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">不支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">不支持</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">过滤链匹配</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">优化的字典匹配树</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">ant</span><span style="color:#333333">匹配</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">ant</span><span style="color:#333333">匹配</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">注解支持</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">servlet</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">jax-rs</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">不支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">不支持</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">权限动态修改</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">需改动支持</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">需改动支持</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">性能速度</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">较快</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">较慢</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">较慢</span></p> </td> 
     </tr> 
     <tr> 
      <td style="border-color:#cccccc"> <p><strong><span style="color:#333333">学习曲线</span></strong></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">简单</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">简单</span></p> </td> 
      <td style="border-color:#dddddd"> <p><span style="color:#333333">陡峭</span></p> </td> 
     </tr> 
    </tbody> 
   </table> 
   <p style="text-align:left"><strong><span style="color:#333333">📈</span> <span style="color:#333333">基准性能测试</span></strong></p> 
   <p style="text-align:left"><img alt src="https://gitee.com/tomsun28/sureness/raw/master/docs/_images/benchmark_cn.png" referrerpolicy="no-referrer"></p> 
   <p style="text-align:left"><strong><span style="color:#333333">基准测试显示</span></strong><strong><span style="color:#333333">sureness</span></strong><strong><span style="color:#333333">对比无权限框架应用损耗</span></strong><strong><span style="color:#333333">0.026ms</span></strong><strong><span style="color:#333333">性能，</span></strong><strong><span style="color:#333333">shiro</span></strong><strong><span style="color:#333333">损耗</span></strong><strong><span style="color:#333333">0.088ms,spring security</span></strong><strong><span style="color:#333333">损耗</span></strong><strong><span style="color:#333333">0.116ms</span></strong><strong><span style="color:#333333">，</span></strong><strong> </strong><strong><span style="color:#333333">相比之下</span></strong><strong><span style="color:#333333">sureness</span></strong><strong><span style="color:#333333">基本不消耗性能，且性能</span></strong><strong><span style="color:#333333">(</span></strong><strong><span style="color:#333333">参考</span></strong><strong><span style="color:#333333">TPS</span></strong><strong><span style="color:#333333">损耗</span></strong><strong><span style="color:#333333">)</span></strong><strong><span style="color:#333333">是</span></strong><strong><span style="color:#333333">shiro</span></strong><strong><span style="color:#333333">的</span></strong><strong><span style="color:#333333">3</span></strong><strong><span style="color:#333333">倍，</span></strong><strong><span style="color:#333333">spring security</span></strong><strong><span style="color:#333333">的</span></strong><strong><span style="color:#333333">4</span></strong><strong><span style="color:#333333">倍</span></strong><br> <strong><span style="color:#333333">性能差距会随着</span></strong><strong><span style="color:#333333">api</span></strong><strong><span style="color:#333333">匹配链的增加而进一步拉大</span></strong><br> <span style="color:#333333">详见</span><span style="color:#333333"><a href="https://gitee.com/tomsun28/sureness-shiro-spring-security">基准测试</a></span></p> 
   <p style="text-align:left"><strong><span style="color:#333333">✌</span> <span style="color:#333333">框架支持样例</span></strong></p> 
   <ul> 
    <li><span style="color:#333333">[√] sureness集成springboot样例(配置文件方案) <a href="https://gitee.com/tomsun28/sureness/tree/master/sample-bootstrap">sample-bootstrap</a></span></li> 
    <li><span style="color:#333333">[√] sureness集成springboot样例(数据库方案) <a href="https://gitee.com/tomsun28/sureness/tree/master/sample-tom">sample-tom</a></span></li> 
    <li><span style="color:#333333">[√] sureness集成quarkus样例 <a href="https://gitee.com/tomsun28/sureness/tree/master/samples/quarkus-sureness">sample-quarkus</a></span></li> 
    <li><span style="color:#333333">[√] sureness集成javalin样例 <a href="https://gitee.com/tomsun28/sureness/tree/master/samples/javalin-sureness">sample-javalin</a></span></li> 
    <li><span style="color:#333333">[√] sureness集成ktor样例 <a href="https://gitee.com/tomsun28/sureness/tree/master/samples/ktor-sureness">sample-ktor</a></span></li> 
    <li><span style="color:#333333">[√] sureness集成spring webflux样例 <a href="https://gitee.com/tomsun28/sureness/tree/master/samples/spring-webflux-sureness">sample-spring-webflux</a></span></li> 
    <li><span style="color:#333333">[√] </span><span style="background-color:#ffffff; color:#40485b">sureness使用session样例 </span><a href="https://gitee.com/tomsun28/sureness/blob/master/samples/sureness-session">sureness-session</a></li> 
    <li><span style="color:#333333">[√] </span> <span style="background-color:#ffffff; color:#40485b">sureness分布式缓存session样例 </span><a href="https://gitee.com/tomsun28/sureness/blob/master/samples/sureness-redis-session">sureness-redis-session</a></li> 
    <li><span style="color:#333333">[√] more samples todo</span></li> 
   </ul> 
   <p style="text-align:left"><strong><span style="color:#333333">项目仓库地址，欢迎使用，开源不易，觉得不错请大佬们</span><span style="color:#333333">star</span><span style="color:#333333">下给予鼓励，感谢。</span></strong></p> 
   <p style="text-align:left"><span style="color:#333333"><a href="https://gitee.com/tomsun28/sureness">GITEE仓库地址</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fsureness" target="_blank">GITHUB仓库地址</a></span></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            