
---
title: 'Restful Fast Request 2.1.2 发布，基于 IDEA 的 Postman 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 07:52:00 GMT
thumbnail: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:left">简介</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com" target="_blank"><img alt height="80" src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg" width="80" referrerpolicy="no-referrer"></a><a href="https://gitee.com/kings/fast-request" target="_blank"><img alt height="80" src="https://resources.jetbrains.com/storage/products/company/brand/logos/IntelliJ_IDEA_icon.svg" width="80" referrerpolicy="no-referrer"> <img alt src="https://gitee.com/kings/fast-request/widgets/widget_3.svg" referrerpolicy="no-referrer"></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-restful-fast-request" target="_blank">Restful Fast Request</a><span> </span>是一个强大的 restful api 工具包插件(Http Client)，可以根据已有的方法帮助您快速生成 url和 params。Restful Fast Request = API 调试工具+API 管理工具，它有一个漂亮的界面来完成请求、检查服务器响应、存储你的 api 请求和导出 api 请求，同时基于 idea 原生，调试代码更加快速、方便、简捷。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持 Spring 体系 (Spring MVC / Spring Boot)</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持JAX-RS</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>对标及优势</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对比与 HTTP Client，Restful Fast Request不仅拥有 HTTP Client 内置的功能，还提供了友好易懂直观的界面，让使用者调试 API 的时候能够更加方便、简捷，同时各种类型参数也提供了不同的定制方式，更加灵活。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>宗旨</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#2c3e50">插件的宗旨是为</span><span style="color:#16a085"><span style="background-color:#ffffff"><strong>简化开发、提高效率</strong></span></span><span style="background-color:#ffffff; color:#2c3e50">而生，</span>我们的愿景是<span style="color:#c0392b"><strong>成为 IDEA 最好的搭档</strong></span>，就像魂斗罗中的 1P、2P，<span style="color:#c0392b"><strong>基友</strong></span>搭配，效率翻倍。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Restful Fast Request 2.1.2正式发布,具体更新内容如下：</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>添加对导出api到Postman的支持</li> 
 <li>首次打开idea懒加载API Navigate树</li> 
 <li>SearchEveryWhere module标识</li> 
 <li>Url解析优化</li> 
 <li>API navigate tree展示优化</li> 
 <li>API保存分组优化</li> 
 <li>全局请求头支持</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><strong>1.添加对导出api到Postman的支持</strong></span><code> </code></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-13b611818167e7e94c4f95042b159310892.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2.<span style="background-color:#e6f6e6; color:#003100">SearchEveryWhere module标识</span></strong></p> 
<p><img height="1406" src="https://oscimg.oschina.net/oscnet/up-be89714b7d113fbe3830f1747efee43fc7a.png" width="2936" referrerpolicy="no-referrer"></p> 
<p><strong>3.Url解析优化</strong></p> 
<pre><span style="color:#808080">
</span><span style="color:#808080">支持以下example的解析
</span><span style="color:#808080">不再需要单独配置url replace config
</span>
<span style="color:#808080">场景1:url是类常量引用
</span><span style="color:#808080">@RequestMapping(Url1.URL_TEST)
</span><span style="color:#808080">@RestController
</span><span style="color:#808080">public class UrlTestController &#123;
</span><span style="color:#808080">    private static final String URL= "xxx";
</span>
<span style="color:#808080">    @GetMapping(value = URL)
</span><span style="color:#808080">    public Integer testUrl()&#123;
</span><span style="color:#808080">        return 1;
</span><span style="color:#808080">    &#125;
</span><span style="color:#808080">&#125;
</span>
<span style="color:#808080">场景2:value是一个数组
</span><span style="color:#808080">@RequestMapping(
</span><span style="color:#808080">    value = &#123;"/v1/save"&#125;,
</span><span style="color:#808080">    method = &#123;RequestMethod.POST&#125;
</span><span style="color:#808080">)</span>
</pre> 
<p><strong>4.API保存分组优化</strong></p> 
<pre><span style="color:#808080">保存api的时候,api将会保存到对应的请求指定到控制器名所在的分组(更加直观)</span></pre> 
<p><img height="1632" src="https://oscimg.oschina.net/oscnet/up-55075d1c977370580d64aee85641c939e8c.png" width="2872" referrerpolicy="no-referrer"></p> 
<p><strong>5.全局请求头支持</strong></p> 
<p><img height="1488" src="https://oscimg.oschina.net/oscnet/up-2556d0836a85950664624ac8cd1b435485c.png" width="2036" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.sheng90.wang%2Ffast-request" target="_blank">https://plugins.sheng90.wang/fast-request</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">关于开源</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">欢迎各路好汉一起来参与完善 Restful Fast Request，我们期待你的 PR！</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>贡献代码：代码地址<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Ffast-request" target="_blank">Github</a><span> </span>|<span><span> </span></span><a href="https://gitee.com/dromara/fast-request">Gitee</a>，欢迎提交 Issue 或者 Pull Requests</li> 
 <li>使用企业登记：<a href="https://gitee.com/kings/fast-request/issues/I4NDBQ">https://gitee.com/kings/fast-request/issues/I4NDBQ</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">下载及安装</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.网页端 :<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-fast-request" target="_blank">https://plugins.jetbrains.com/plugin/16988-fast-request</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.IDEA插件市场:打开setting->plugins->Marketplace  搜索 Fast Request</p> 
<p> </p>
                                        </div>
                                      
</div>
            