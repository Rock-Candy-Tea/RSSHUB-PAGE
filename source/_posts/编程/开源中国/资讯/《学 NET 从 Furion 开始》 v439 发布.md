
---
title: '《学 .NET 从 Furion 开始》 v4.3.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3912ce51cbbea11da2dd1f271063b878f5a.png'
author: 开源中国
comments: false
date: Sat, 03 Sep 2022 10:17:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3912ce51cbbea11da2dd1f271063b878f5a.png'
---

<div>   
<div class="content">
                                                                                            <h2>项目信息</h2> 
<ul> 
 <li>开源地址：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>文档地址：<a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion/</a></li> 
 <li>开源协议：<a href="https://gitee.com/dotnetchina/Furion/blob/net6/LICENSE">MIT</a></li> 
</ul> 
<pre style="text-align:left"><span>MIT 许可证</span>

<span>版权 (c) 2020-2022 百小僧, Baiqian Co.,Ltd 和所有贡献者</span>

<span>特此免费授予任何获得本软件副本和相关文档文件（下称“软件”）的人不受限制地处置该软件的权利，包括不受限制地使用、复制、修改、合并、发布、分发、转授许可和/或出售该软件副本，以及再授权被配发了本软件的人如上的权利，须在下列条件下：</span>

<span>上述版权声明和本许可声明应包含在该软件的所有副本或实质成分中。</span>

<span>本软件是“如此”提供的，没有任何形式的明示或暗示的保证，包括但不限于对适销性、特定用途的适用性和不侵权的保证。在任何情况下，</span>
</pre> 
<h2>版本细节</h2> 
<p>本期主要对监听日志进行了改进和优化，解决了 11 个 Issue 功能建议。</p> 
<ul> 
 <li><code>v4.3.9</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5PIWD" target="_blank">https://gitee.com/dotnetchina/Furion/issues/I5PIWD</a></li> 
 <li><code>v4.3.8</code><span> </span>版本细节：<a href="https://gitee.com/dotnetchina/Furion/issues/I5PCXK" target="_blank">https://gitee.com/dotnetchina/Furion/issues/I5PCXK</a></li> 
</ul> 
<p><img height="977" src="https://oscimg.oschina.net/oscnet/up-3912ce51cbbea11da2dd1f271063b878f5a.png" width="1543" referrerpolicy="no-referrer"></p> 
<p><img height="969" src="https://oscimg.oschina.net/oscnet/up-c1b0e7cb716920adfc889039228564d7584.png" width="1497" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>AppSettings</code><span> </span>配置的<span> </span><code>ExcludeAssemblies</code><span> </span>属性，支持忽略指定程序集扫描<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/7b7747f38c84acfe7df3469599bebf417e5ad843">7b7747f</a></li> 
    <li>[新增]<span> </span><code>Oops.Oh</code><span> </span>和<span> </span><code>Oops.Bah</code><span> </span>支持设置额外数据<span> </span><code>.WithData(data)</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5O38E">#I5O38E</a></li> 
    <li>[新增] 定时任务<span> </span><code>Crontab.GetSleepMilliseconds(baseTime)</code><span> </span>获取下一个发生时间的时间差<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/d024fae670b7ce3fd4bfd26aee70ed318a4c0383">d024fae</a></li> 
    <li>[新增]<span> </span><strong>友好异常默认打印异常日志，避免生产环境漏掉重要异常信息<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/6e3a5bdd0fd22a7f9ae618b7495cd64081a7f2e8">6e3a5bd</a></strong></li> 
    <li>[新增] 日志静态类<span> </span><code>Log.CreateLoggerFactory()</code><span> </span>静态方法<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/75c672afc58b393313916c433cb9d92c779b9629">75c672a</a></li> 
    <li>[新增] 多语言<span> </span><code>SharedResource</code><span> </span>模式，避免硬编程<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/18e80c7d7c2c2450c6ad429601716f546552e987">18e80c7</a></li> 
    <li>[新增]<span> </span><strong>事件总线<span> </span><code>MessageCenter</code><span> </span>静态类，解决从<span> </span><code>Fur v1.x</code><span> </span>版本升级问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/a29fc7cf63a3ea41b1617a6ad98a701a243e24f8">a29fc7c</a></strong></li> 
    <li>[新增] 组件化<span> </span><code>IWebComponent</code><span> </span>模式，支持<span> </span><code>.NET5+</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/08a44c347a56c467527935a8caac8966585f5d1a">08a44c3</a></li> 
    <li>[新增] 远程请求设置自己的<span> </span><code>HttpClient</code><span> </span>功能<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PBR3">#I5PBR3</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/544">!545</a></li> 
    <li>[新增]<span> </span><code>LoggingMonitor</code><span> </span>支持添加更多自定义配置<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PEPA">#I5PEPA</a></li> 
    <li>[新增]<span> </span><code>LoggingMonitor</code><span> </span>可配置<span> </span><code>WithReturnValue</code><span> </span>和<span> </span><code>ReturnValueThreshold</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PFJ1">#I5PFJ1</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PFOW">#I5PFOW</a></li> 
    <li>[新增]<span> </span><code>LoggingMonitor</code><span> </span>可配置<span> </span><code>MethodsSettings</code><span> </span>更多信息<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PFJ1">#I5PFJ1</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PFOW">#I5PFOW</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul> 
    <li>[新增]<span> </span><strong><code>Furion</code><span> </span>程序集<span> </span><code>PublicKeyToken</code><span> </span>强签名</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/26b12c0fd64b153a71496eb62110567e05450f20">26b12c0</a></li> 
    <li>[调整]<span> </span><strong>事件总线<span> </span><code>IEventBusFactory</code><span> </span>事件工厂方法<span> </span><code>AddSubscriber -> Subscribe</code>，<code>RemoveSubscriber -> Unsubscribe</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/a29fc7cf63a3ea41b1617a6ad98a701a243e24f8">a29fc7c</a></strong></li> 
    <li>[调整]<span> </span><code>.AddInject()</code><span> </span>和<span> </span><code>.UseInject()</code><span> </span>配置选项名称，移除<span> </span><code>Configure</code><span> </span>后缀<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/b6953cd586936593e40ef626c3b8a1e770239e43">b6953cd</a></li> 
    <li>[调整]<span> </span><strong>远程请求<span> </span><code>请求拦截</code>、<code>响应拦截</code><span> </span>和<span> </span><code>异常拦截</code><span> </span>委托签名，新增<span> </span><code>HttpClient</code><span> </span>参数</strong><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5OWBO">#I5OWBO</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 生成包含<span> </span><code>中文</code><span> </span>的<span> </span><code>JWT Token</code><span> </span>解密后出现乱码问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5O397">#I5O397</a></li> 
    <li>[修复] `HttpRequestMessage`` 拓展中追加查询参数时的空引用异常<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PENW">#I5PENW</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/547">!547</a></li> 
    <li>[修复] 日志模块配置多个<span> </span><code>IDatabaseLoggingWriter</code><span> </span>只有一个生效<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PFQ2">#I5PFQ2</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PFJ1">#I5PFJ1</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul> 
    <li>[调整] 默认输出文件日志模板，使其更加美观<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/1518cf3be74524ed0d3f73360068a9a0ec6685d9">#1518cf3</a></li> 
    <li>[调整] 默认规范化结果验证处理也支持状态码设置<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/2eb939074a14d29fcd3e4726937c8a8430765f48">2eb9390</a></li> 
    <li>[更新]<span> </span><code>SqlSugarCore</code><span> </span>拓展包和脚手架至<span> </span><code>5.1.2.6</code><span> </span>版本<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PCXK">#I5PCXK</a></li> 
    <li>[更新]<span> </span><code>JSON Schema</code><span> </span>关于<span> </span><code>LoggingMonitor</code><span> </span>更多配置<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5PFJ1">#I5PFJ1</a></li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>RabbitMQ</code><span> </span>事件总线文档</li> 
    <li>[更新]<span> </span><code>AppSettings</code><span> </span>配置文档、事件总线文档、多数据库配置文档、日志文档、定时任务文档、<code>MessageCenter</code><span> </span>文档、远程请求文档、组件化文档、入门指南、多语言文档。</li> 
   </ul> </li> 
 </ul> 
</blockquote>
                                        </div>
                                      
</div>
            