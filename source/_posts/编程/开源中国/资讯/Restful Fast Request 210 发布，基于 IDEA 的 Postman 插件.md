
---
title: 'Restful Fast Request 2.1.0 发布，基于 IDEA 的 Postman 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
author: 开源中国
comments: false
date: Tue, 21 Dec 2021 08:56:00 GMT
thumbnail: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0px; margin-right:0px; text-align:left">简介</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com" target="_blank"><img alt height="80" src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg" width="80" referrerpolicy="no-referrer"></a><a href="https://gitee.com/kings/fast-request" target="_blank"><img alt height="80" src="https://resources.jetbrains.com/storage/products/company/brand/logos/IntelliJ_IDEA_icon.svg" width="80" referrerpolicy="no-referrer"> <img alt src="https://gitee.com/kings/fast-request/widgets/widget_3.svg" referrerpolicy="no-referrer"></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-fast-request" target="_blank">Restful Fast Request</a><span> </span>是一个强大的 restful api 工具包插件(Http Client)，可以根据已有的方法帮助您快速生成 url和 params。Restful Fast Request = API 调试工具+API 管理工具，它有一个漂亮的界面来完成请求、检查服务器响应、存储你的 api 请求和导出 api 请求，同时基于 idea 原生，调试代码更加快速、方便、简捷。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持 Spring 体系 (Spring MVC / Spring Boot)</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持JAX-RS</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left"><strong>对标及优势</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对比与 HTTP Client，Restful Fast Request不仅拥有 HTTP Client 内置的功能，还提供了友好易懂直观的界面，让使用者调试 API 的时候能够更加方便、简捷，同时各种类型参数也提供了不同的定制方式，更加灵活。</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left"><strong>宗旨</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#2c3e50">插件的宗旨是为</span><span style="color:#16a085"><span style="background-color:#ffffff"><strong>简化开发、提高效率</strong></span></span><span style="background-color:#ffffff; color:#2c3e50">而生，</span>我们的愿景是<span style="color:#c0392b"><strong>成为 IDEA 最好的搭档</strong></span>，就像魂斗罗中的 1P、2P，<span style="color:#c0392b"><strong>基友</strong></span>搭配，效率翻倍。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Restful Fast Request 2.1.0正式发布,具体更新内容如下：</h3> 
<ul> 
 <li>修复POST形式的API中@RequestBody、@RequestParam混合使用参数解析导致请求400异常</li> 
 <li>对嵌套类的解析支持</li> 
 <li>增加支持对控制器类级别@RequestMapping(path="/xxx")path的解析</li> 
 <li>Api tree针对带@RequestMapping类的扫描支持</li> 
 <li>格式化按钮暂时去除</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1.修复POST形式的API中@RequestBody、@RequestParam混合使用参数解析导致请求400异常</strong></p> 
<pre><span style="color:#bbb529">虽然不建议用用post去查询，但还是支持了

@ApiOperation</span>(<span style="color:#6a8759">"query user page"</span>)
<span style="color:#bbb529">@PostMapping</span>(<span style="color:#6a8759">"/page"</span>)
<span style="color:#cc7832">public </span>Result<CustomPage<WechatUserDto>> <span style="color:#ffc66d">findUserPage
</span>(
    <span style="color:#bbb529">@RequestBody </span>WechatUserQueryDto user<span style="color:#cc7832">,
</span><span style="color:#cc7832">    </span><span style="color:#bbb529">@RequestParam </span>Integer pageNo<span style="color:#cc7832">,
</span><span style="color:#cc7832"> </span><span style="color:#bbb529">@RequestParam </span>Integer pageSize<span style="color:#cc7832">,
</span><span style="color:#cc7832">   </span><span style="color:#bbb529">@RequestParam</span>(required = <span style="color:#cc7832">false</span>) String nickname) &#123;
&#125;</pre> 
<p><strong>2.对嵌套类的解析支持</strong></p> 
<p><span style="color:#27ae60"><strong>* 避免类嵌套循环引用，引起无限递归解析</strong></span></p> 
<p> </p> 
<p><strong>3.Api tree针对带@RequestMapping类的扫描支持</strong></p> 
<p>springboot系列，api的RequestMapping包装在一个interface中，经常会以<strong>jar</strong>包的形式出现，2.1.0增加了这种类型的扫描支持</p> 
<pre><span style="color:#bbb529">@FeignClient</span>(value = BusinessDataClient.<em>Client</em>)
<span style="color:#bbb529">@RequestMapping</span>(<span style="color:#6a8759">"/cardService"</span>)
<span style="color:#5a8199">public interface </span>CardService &#123;
<em>
</em><em>    </em><span style="color:#bbb529">@GetMapping</span>(<span style="color:#6a8759">"/list"</span>)
    List<CardDto> <span style="color:#5a8199">void </span><span style="color:#ffaa6d">list</span>()<span style="color:#cc7832">;
&#125;</span>
</pre> 
<p><img height="806" src="https://oscimg.oschina.net/oscnet/up-12e89d135bcb2083582f454acae54488b77.png" width="2180" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><strong>4.增加支持对控制器类级别@RequestMapping(path="/xxx")path的解析</strong></p> 
<p>支持以下2中方式的url解析</p> 
<pre><span style="color:#bbb529">@Api</span>(<span style="color:#6a8759">"</span><span style="color:#6a8759">用户管理</span><span style="color:#6a8759">api"</span>)
<span style="color:#bbb529">@RestController
</span><span style="color:#bbb529">@RequestMapping</span>(<span style="color:#6a8759">"/userApi"</span>) 或者 <span style="color:#bbb529">@RequestMapping</span>(value=<span style="color:#6a8759">"/userApi"</span>)
<span style="color:#cc7832">public class </span>UserApiController &#123;&#125;</pre> 
<pre><span style="color:#bbb529">@Api</span>(<span style="color:#6a8759">"</span><span style="color:#6a8759">用户管理</span><span style="color:#6a8759">api"</span>)
<span style="color:#bbb529">@RestController
</span><span style="color:#bbb529">@RequestMapping</span>(path=<span style="color:#6a8759">"/userApi"</span>)
<span style="color:#cc7832">public class </span>UserApiController &#123;&#125;

</pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">投票支持</span></strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#c0392b"><strong>《2021优秀开源软件投票》第二轮投票已经开启，本次投票会决出最受欢迎TOP30。</strong></span>Fast Request本是个人为了方便调试API所开发，后面觉得好用便开源，目前是单人开发，开源不易，如果各位develop觉得好用，<strong><span style="color:#c0392b">请各位开发者为Fast Request投上宝贵的一票，谢谢！👇🏻👇🏻</span></strong><strong><span style="color:#c0392b">👇🏻</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#c0392b">投票地址</span></strong>：<strong><a href="https://www.oschina.net/project/top_cn_2021/?id=589">https://www.oschina.net/project/top_cn_2021/?id=589</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>点击链接即可到达投票界面</strong></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">文档</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://kings.gitee.io/fast-request/">https://kings.gitee.io/fast-request/</a></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">关于开源</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">欢迎各路好汉一起来参与完善 Restful Fast Request，我们期待你的 PR！</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>贡献代码：代码地址<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkings1990%2Ffast-request" target="_blank">Github</a><span> </span>|<span><span> </span></span><a href="https://gitee.com/kings/fast-request">Gitee</a>，欢迎提交 Issue 或者 Pull Requests</li> 
 <li>使用企业登记：<a href="https://gitee.com/kings/fast-request/issues/I4NDBQ">https://gitee.com/kings/fast-request/issues/I4NDBQ</a></li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">下载及安装</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.网页端 :<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-fast-request" target="_blank">https://plugins.jetbrains.com/plugin/16988-fast-request</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.IDEA插件市场:打开setting->plugins->Marketplace  搜索 Fast Request</p>
                                        </div>
                                      
</div>
            