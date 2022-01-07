
---
title: 'JMeter Grpc 插件 v1.2 发布，完爆 BloomRPC，支持自动化测试'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/yue-open/jmeter-grpc-request/raw/v1.2.0/dist/asset/jmeter-and-grpc.png'
author: 开源中国
comments: false
date: Fri, 07 Jan 2022 08:45:00 GMT
thumbnail: 'https://gitee.com/yue-open/jmeter-grpc-request/raw/v1.2.0/dist/asset/jmeter-and-grpc.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="Apache JMeter and gRPC logo" src="https://gitee.com/yue-open/jmeter-grpc-request/raw/v1.2.0/dist/asset/jmeter-and-grpc.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">这个JMeter采样器允许您向服务器发送一个gRPC请求</p> 
 <p style="margin-left:0; margin-right:0">它和HTTP请求一样简单</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.javadoc.io%2Fdoc%2Forg.apache.jmeter%2FApacheJMeter_core" target="_blank"><img alt="Javadocs" src="https://www.javadoc.io/badge/org.apache.jmeter/ApacheJMeter_core.svg" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2Ftagged%2Fjmeter" target="_blank"><img alt="Stack Overflow" src="https://img.shields.io/:stack%20overflow-jmeter-brightgreen.svg" referrerpolicy="no-referrer"></a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">他是一个功能强大的JMeter Grpc插件，可用于测试任何gRPC服务器，它不需要生成gRPC类或编译服务的protos二进制文件，只是一个非常简单的输入：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>gRPC服务的主机和端口</li> 
 <li>需要测试的RPC方法</li> 
 <li>proto文件路径</li> 
 <li>格式化的JSON请求数据</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">如何使用</h2> 
<p><img src="https://static.oschina.net/uploads/space/2022/0107/090413_Rwc3_2720166.gif" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">插件安装</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">你需要将<span> </span><strong>jmeter-grpc-request</strong><span> </span>插件的<span> </span><code>jar</code><span> </span>包复制到JMeter的<span> </span><code>lib/ext</code><span> </span>目录下面，然后重启你的JMeter工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>jmeter-grpc-request</strong><span> </span>插件的<span> </span><code>jar</code><span> </span>包，可以从<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Freleases" target="_blank">Releases Page</a><span> </span>获得，也可以 在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjmeter-plugins.org%2F%3Fsearch%3Djmeter-grpc-request" target="_blank">JMeter Plugins Manager</a><span> </span>中找到</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">使用说明</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-indent:0px; text-transform:none; white-space:normal; widows:2; width:1233px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>序号</th> 
   <th>选项</th> 
   <th>描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Server Name or IP</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">gRPC服务器地址（域名或IP）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Port Number</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">gRPC服务器端口 (80/ 443)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">3</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SSL/TLS</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">开启SSL/TLS认证</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">4</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Proto Root Directory</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">proto文件的根路径</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">5</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Library Directory (Optional)</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">proto文件解析需要依赖的额外库的文件夹路径 (googleapis)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">6</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Full Method</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">用于请求测试的RPC方法</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Metadata</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><span style="background-color:#ffffff; color:#24292f">Metadata可以用于token身份验证等方式，支持以下两种方式传输（UTF-8）：</span><br> <span style="background-color:#ffffff; color:#24292f">1. 使用键值对（Key: Value）：</span><br> <span style="background-color:#ffffff; color:#24292f">  - key1: value1, key2: value2</span><br> <span style="background-color:#ffffff; color:#24292f">2.</span><span style="background-color:#ffffff; color:#24292f"> 使用 </span><span style="background-color:#ffffff; color:#24292f">Json String：</span><br> <span style="background-color:#ffffff; color:#24292f">   - &#123;"key1":"Value1", "key2":"value2"&#125;</span> <p> </p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">8</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Deadline</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">请求超时时间（单位：毫秒）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">9</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Send JSON Format With the Request</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">格式化的JSON请求数据</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">v1.2.0</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">概括</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">改变:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>添加选项以禁用 SSL/TLS 证书验证<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F45" target="_blank">#45</a></li> 
 <li>添加单元测试<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F47" target="_blank">#47</a></li> 
 <li>Metadata 支持JSON字符串与用户变量解析<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F79" target="_blank">#79</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F74" target="_blank">#74</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F84" target="_blank">#84</a></li> 
 <li>基于 proto 文件自动生成请求数据（请求数据mock）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F82" target="_blank">#82</a></li> 
 <li>Proto Root, Library, Metadata fields 支持用户变量<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F85" target="_blank">#85</a></li> 
 <li>规范 dependence，瘦身<code>jmeter-grpc-request.jar</code>插件<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F89" target="_blank">#89</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">修复:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>请求空值<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F61" target="_blank">#61</a></li> 
 <li>protoc 不支持解析大文件夹<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F89" target="_blank">#89</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">详细变化</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Shorten the exception message show in the report by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhuynhminhtan" target="_blank">@huynhminhtan</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F17" target="_blank">#17</a></li> 
 <li>Update readme by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhuynhminhtan" target="_blank">@huynhminhtan</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F25" target="_blank">#25</a></li> 
 <li>Update README by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhuynhminhtan" target="_blank">@huynhminhtan</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F39" target="_blank">#39</a></li> 
 <li>Add apache 2.0 license, same as jmeter-grpc-plugin by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdhartford" target="_blank">@dhartford</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F43" target="_blank">#43</a></li> 
 <li>Add option to disable SSL/TLS Cert verification by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdhartford" target="_blank">@dhartford</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F45" target="_blank">#45</a></li> 
 <li>Add Unit Test & Github Action Workflow by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fminhhoangvn" target="_blank">@minhhoangvn</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F47" target="_blank">#47</a></li> 
 <li>Update<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freadme.md%2F" target="_blank">README.md</a><span> </span>by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhuynhminhtan" target="_blank">@huynhminhtan</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F48" target="_blank">#48</a></li> 
 <li>Actions workflow by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhuynhminhtan" target="_blank">@huynhminhtan</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F52" target="_blank">#52</a></li> 
 <li>Support for NPN fallback and relative directories by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyanpaulo" target="_blank">@yanpaulo</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F50" target="_blank">#50</a></li> 
 <li>Include default field values. This addresses<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fissues%2F59" target="_blank">#59</a>by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fskarpushin" target="_blank">@skarpushin</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F61" target="_blank">#61</a></li> 
 <li>metadata value should decode. by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpengweiqhca" target="_blank">@pengweiqhca</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F74" target="_blank">#74</a></li> 
 <li>Metadata field allows Jmeter variables as parameter by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftotalys" target="_blank">@totalys</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F75" target="_blank">#75</a></li> 
 <li>adding label to metadata field by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftotalys" target="_blank">@totalys</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F76" target="_blank">#76</a></li> 
 <li>gRPCSampler Metadata can be Json String by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJayrajgondaliya" target="_blank">@Jayrajgondaliya</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F79" target="_blank">#79</a></li> 
 <li>Auto generate request data base on proto file(mock). by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyl-yue" target="_blank">@yl-yue</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F82" target="_blank">#82</a></li> 
 <li>Resolve page stutter caused by request mock by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyl-yue" target="_blank">@yl-yue</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F83" target="_blank">#83</a></li> 
 <li>Move Metadata update to when Sample is tested by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjacek-d" target="_blank">@jacek-d</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F84" target="_blank">#84</a></li> 
 <li>Let Proto root directory fully support '$&#123;&#125;' to refer to user variables by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyl-yue" target="_blank">@yl-yue</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F85" target="_blank">#85</a></li> 
 <li>Solve<code>CreateProcess Error = 206</code>, and slimming plug-in volume by<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyl-yue" target="_blank">@yl-yue</a>in<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F89" target="_blank">#89</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">新贡献者</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">特别感谢</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdhartford" target="_blank">@dhartford</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F43" target="_blank">#43</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fminhhoangvn" target="_blank">@minhhoangvn</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F47" target="_blank">#47</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyanpaulo" target="_blank">@yanpaulo</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F50" target="_blank">#50</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fskarpushin" target="_blank">@skarpushin</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F61" target="_blank">#61</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpengweiqhca" target="_blank">@pengweiqhca</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F74" target="_blank">#74</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftotalys" target="_blank">@totalys</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F75" target="_blank">#75</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJayrajgondaliya" target="_blank">@Jayrajgondaliya</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F79" target="_blank">#79</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyl-yue" target="_blank">@yl-yue</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F82" target="_blank">#82</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjacek-d" target="_blank">@jacek-d</a>做出了他们的第一个贡献<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F84" target="_blank">#84</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>完整更新日志</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fcompare%2Fv1.1.1...v1.2.0" target="_blank">v1.1.1...v1.2.0</a></p>
                                        </div>
                                      
</div>
            