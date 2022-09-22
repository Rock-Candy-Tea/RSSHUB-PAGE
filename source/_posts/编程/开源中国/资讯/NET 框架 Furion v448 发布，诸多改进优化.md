
---
title: '.NET 框架 Furion v4.4.8 发布，诸多改进优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8904f915c304648b79f967e251a4324ea1f.png'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 18:17:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8904f915c304648b79f967e251a4324ea1f.png'
---

<div>   
<div class="content">
                                                                                            <h2>前言</h2> 
<p>本期主要对日志性能、远程请求性能还有诸多模块性能进行改进。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目信息</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion" target="_blank">https://github.com/MonkSoul/Furion</a></li> 
 <li>文档：<a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion</a></li> 
</ul> 
<p><img height="1077" src="https://oscimg.oschina.net/oscnet/up-8904f915c304648b79f967e251a4324ea1f.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img src="https://foruda.gitee.com/images/1663755154660487900/2180053b_974299.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://foruda.gitee.com/images/1663832785364329117/f33bd15f_974299.png" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<ul> 
 <li><code>v4.4.8</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5SKUE">https://gitee.com/dotnetchina/Furion/issues/I5SKUE</a></li> 
 <li><code>v4.4.7</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5SEFE">https://gitee.com/dotnetchina/Furion/issues/I5SEFE</a></li> 
 <li><code>v4.4.6</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5RSFD">https://gitee.com/dotnetchina/Furion/issues/I5RSFD</a></li> 
 <li><code>v4.4.5</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5RHQX">https://gitee.com/dotnetchina/Furion/issues/I5RHQX</a></li> 
 <li><code>v4.4.4</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5R5TI">https://gitee.com/dotnetchina/Furion/issues/I5R5TI</a></li> 
 <li><code>v4.4.3</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5QVH3">https://gitee.com/dotnetchina/Furion/issues/I5QVH3</a></li> 
 <li><code>v4.4.2</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5QDHX">https://gitee.com/dotnetchina/Furion/issues/I5QDHX</a></li> 
 <li><code>v4.4.1</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5Q3SX">https://gitee.com/dotnetchina/Furion/issues/I5Q3SX</a></li> 
 <li><code>v4.4.0</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5PQHR">https://gitee.com/dotnetchina/Furion/issues/I5PQHR</a></li> 
</ul> 
<hr> 
<ul> 
 <li> <p><strong>新特性</strong></p> 
  <ul> 
   <li>[新增] 新增友好异常可控制是否输出错误日志配置<span> </span><code>LogError: true</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PKJH">#I5PKJH</a></li> 
   <li>[新增]<span> </span><code>DateOnlyJsonConverter</code><span> </span>和<span> </span><code>DateOnlyOffsetJsonConverter</code><span> </span>序列化转换器<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/565">!565</a></li> 
   <li>[新增] 事件总线<span> </span><code>LogEnabled</code><span> </span>配置，可控制是否输出服务日志<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QLY5">#I5QLY5</a></li> 
   <li>[新增]<span> </span><strong>可实现任何多套规范化结果功能，支持特定控制器，特定方法</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QZ37">#I5QZ37</a></li> 
   <li>[新增]<span> </span><code>ILoggerFactory</code><span> </span>日志工厂动态批量添加文件日志拓展<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5R9PO">#I5R9PO</a></li> 
   <li>[新增]<span> </span><code>App.GetCommandLineConfiguration(args)</code><span> </span>解析命令行参数静态方法<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/803542c3e21496e92d2bf83aaa2d00831fcb09bc">803542c</a></li> 
   <li>[新增]<span> </span><code>Sql</code><span> </span>代理支持返回受影响行数<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5REJ9">#I5REJ9</a></li> 
   <li>[新增]<span> </span><strong>任意自定义日志文件名支持滚动日志删除功能</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5RFBQ">#I5RFBQ</a></li> 
   <li>[新增]<span> </span><code>.pcd</code><span> </span>图片类型<span> </span><code>MIME</code><span> </span>为<span> </span><code>image/x-photo-cd</code><span> </span>支持<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/5fafc8477a4d213d16db92cf030f409c758fab95">5fafc84</a></li> 
   <li>[新增] 默认日志输出当前线程<span> </span><code>Environment.CurrentManagedThreadId</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/b8fe2cdc49d1bd11e38ad37fa512acafc3d96417">b8fe2cd</a></li> 
   <li>[新增]<span> </span><code>app.UseInject(Action<UseInjectOptions>)</code><span> </span>重载方法，简化配置<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/0b645fede0ad81c4779a8b9b4b16d9c5d60c9662">0b645fe</a></li> 
  </ul> </li> 
 <li> <p><strong>突破性变化</strong></p> 
  <ul> 
   <li>[支持]<span> </span><strong><code>.NET 6.0.9</code><span> </span>和<span> </span><code>.NET 7.0 RC1</code></strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/be5b4098bae2153f8d49cf9797e454afde0d0aab">be5b40</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/1eee77bff0954336dcc5402a09a3195667bb80f2">1eee77b</a></li> 
   <li>[调整] 远程请求<span> </span><code>.SetBodyBytes</code><span> </span>为<span> </span><code>.SetFiles</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PMS5">#I5PMS5</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PIYI">#I5PIYI</a></li> 
   <li>[调整]<span> </span><code>FS.InitialContentTypeProvider()</code><span> </span>名称为<span> </span><code>FS.GetFileExtensionContentTypeProvider()</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/5fafc8477a4d213d16db92cf030f409c758fab95">5fafc84</a></li> 
   <li>[移除] 远程请求<span> </span><code>[BodyBytes]</code><span> </span>设计，采用<span> </span><code>HttpFile</code><span> </span>方式<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PMS5">#I5PMS5</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PIYI">#I5PIYI</a></li> 
   <li>[调整] 所有的<span> </span><code>AddInject</code><span> </span>和<span> </span><code>UseInject</code><span> </span>参数设计<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QCF0">#I5QCF0</a></li> 
   <li>[调整]<span> </span><strong>远程请求所有<span> </span><code>xxxAsStreamAsync</code><span> </span>返回值</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QVEB">#I5QVEB</a></li> 
  </ul> </li> 
 <li> <p><strong>问题修复</strong></p> 
  <ul> 
   <li>[修复] 远程请求代理模式非泛型参数导致数组溢出问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5Q3SN">#I5Q3SN</a></li> 
   <li>[修复]<span> </span><code>LoggingMonitor</code><span> </span>客户端<span> </span><code>IP</code><span> </span>记录错误<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QCU1">#I5QCU1</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/562">!562</a></li> 
   <li>[修复] 远程请求响应报文中包含<span> </span><code>charset=gbk</code><span> </span>进行序列化后乱码问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QVEB">#I5QVEB</a></li> 
   <li>[修复] 文件日志断电时丢失日志问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/db7d51bba569001bc363727a6683ab3f31c3fc1d">db7d51b</a></li> 
   <li>[修复] 动态<span> </span><code>WebAPI</code><span> </span>或控制台贴了<span> </span><code>[ApiDescriptionSettings(Tag = "")]</code><span> </span>标签之后导致注释丢失<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5REVF">#I5REVF</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5RE4J">#I5RE4J</a></li> 
   <li>[修复]<span> </span><strong>启用数据库日志但是没有配置配置文件出现空异常问题</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/33817bed9d47c85a57c0198c0819ad5cf1c41d0b">33817be</a></li> 
   <li>[修复]<span> </span><strong>控制台日志过滤无法过滤默认主机日志问题</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/33817bed9d47c85a57c0198c0819ad5cf1c41d0b">33817be</a></li> 
   <li>[修复]<span> </span><strong>脚手架错误的日志配置问题</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/33817bed9d47c85a57c0198c0819ad5cf1c41d0b">33817be</a></li> 
   <li>[修复]<span> </span><strong>高频压测情况下写日志并设置日志上下文导致并发更新出现<span> </span><code>System.AggregateException</code><span> </span>异常问题</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5RFBQ">#I5RFBQ</a></li> 
   <li>[修复]<span> </span><strong>日志文件名因<span> </span><code>Windows</code><span> </span>和<span> </span><code>Linux</code><span> </span>路径分隔符不一致导致日志文件创建失败问题，<code>Linux</code><span> </span>只支持<span> </span><code>/</code><span> </span>不支持<span> </span><code>\</code></strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5RFBQ">#I5RFBQ</a></li> 
   <li>[修复]<span> </span><code>Oops.Oh/Bah</code><span> </span>设置<span> </span><code>.WithData</code><span> </span>之后无效问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/580">!580</a></li> 
   <li>[修复] 基于<span> </span><code>Redis</code><span> </span>重写事件存储器序列化<span> </span><code>IEventSource</code><span> </span>实例异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/3e45020eca5948d18d5cb405a665aae44088fd20">3e45020</a></li> 
   <li>[修复] 使用<span> </span><code>Log</code><span> </span>静态类超高频率下写日志导致<span> </span><code>CPU</code><span> </span>激增问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5SDK5">#I5SDK5</a></li> 
   <li>[修复] 远程请求超高频率下发送请求导致<span> </span><code>CPU</code><span> </span>激增问题和异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5SJJR">#I5SJJR</a></li> 
  </ul> </li> 
 <li> <p><strong>其他更改</strong></p> 
  <ul> 
   <li>[调整]<span> </span><code>JWTEncryption</code><span> </span>静态类，支持无需注册<span> </span><code>services.AddJwt()</code><span> </span>使用<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PPKE">#I5PPKE</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5POLZ">#I5POLZ</a></li> 
   <li>[调整] 事件总线默认日志类名为<span> </span><code>System.Logging.EventBusService</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5QLY5">#I5QLY5</a></li> 
  </ul> </li> 
 <li> <p><strong>文档</strong></p> 
  <ul> 
   <li>[新增]<span> </span><code>.NET6</code><span> </span>升级<span> </span><code>.NET7</code><span> </span>文档</li> 
   <li>[新增]<span> </span><code>ASP.NET 7</code><span> </span>集成文档</li> 
   <li>[更新] 友好异常文档、日志记录文档、远程请求文档、依赖注入文档、即时通讯文档、事件总线文档、Worker Service 文档、单元测试文档、入门指南文档、数据库新增文档</li> 
  </ul> </li> 
</ul>
                                        </div>
                                      
</div>
            