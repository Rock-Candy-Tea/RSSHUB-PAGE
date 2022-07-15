
---
title: '.NET 无商业，无授权开源框架 Furion v3.8.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d9665e9dfd3a314bbd8d4e6a57bbab8a076.png'
author: 开源中国
comments: false
date: Fri, 15 Jul 2022 08:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d9665e9dfd3a314bbd8d4e6a57bbab8a076.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-d9665e9dfd3a314bbd8d4e6a57bbab8a076.png" width="1920" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:left">先知 / Furion (<a href="https://gitee.com/dotnetchina/Furion/tree/experimental/">探索版</a>)</h1> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">一个应用程序框架，您可以将它集成到任何 .NET/C# 应用程序中。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">An application framework that you can integrate into any .NET/C# application.</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装 / Installation</h2> 
<ul> 
 <li><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion">Package Manager</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>Install-Package</span><span data-darkreader-inline-color style="--darkreader-inline-color:#bdb7af; color:#bbbbbb"> </span><span>Furion</span></span>
</pre> 
 </div> 
</div> 
<ul> 
 <li><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion">.NET CLI</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>dotnet</span><span data-darkreader-inline-color style="--darkreader-inline-color:#bdb7af; color:#bbbbbb"> </span><span>add</span><span data-darkreader-inline-color style="--darkreader-inline-color:#bdb7af; color:#bbbbbb"> </span><span>package</span><span data-darkreader-inline-color style="--darkreader-inline-color:#bdb7af; color:#bbbbbb"> </span><span>Furion</span></span>
</pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">例子 / Examples</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">我们在<a href="https://dotnetchina.gitee.io/furion">主页</a>上有不少例子，这是让您入门的第一个：</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">We have several examples<span> </span><a href="https://dotnetchina.gitee.io/furion">on the website</a>. Here is the first one to get you started:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>Serve</span><span>.</span><strong data-darkreader-inline-color style="--darkreader-inline-color:#ff6161; color:#990000">Run</strong><span>();</span></span>

<span><span>[</span><span>DynamicApiController</span><span>]</span></span>
<span><strong data-darkreader-inline-color style="--darkreader-inline-color:#e8e6e3; color:#000000">public</strong> <strong data-darkreader-inline-color style="--darkreader-inline-color:#e8e6e3; color:#000000">class</strong> <strong data-darkreader-inline-color style="--darkreader-inline-color:#8ba6c5; color:#445588">HelloService</strong></span>
<span><span>&#123;</span></span>
<span>    <strong data-darkreader-inline-color style="--darkreader-inline-color:#e8e6e3; color:#000000">public</strong> <strong data-darkreader-inline-color style="--darkreader-inline-color:#8ba6c5; color:#445588">string</strong> <strong data-darkreader-inline-color style="--darkreader-inline-color:#ff6161; color:#990000">Say</strong><span>()</span> <span>=></span> <span data-darkreader-inline-color style="--darkreader-inline-color:#ff5131; color:#dd2200">"Hello, Furion"</span><span>;</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">打开浏览器访问<span> </span><code>https://localhost:5001</code><span> </span>或<span> </span><code>http://localhost:5000</code>。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">Open browser access<span> </span><code>https://localhost:5001</code><span> </span>or<span> </span><code>http://localhost:5000</code>.</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档 / Documentation</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">您可以在<a href="https://dotnetchina.gitee.io/furion">主页</a>或<a href="https://gitee.com/link?target=https%3A%2F%2Ffurion.icu">备份主页</a>找到 Furion 文档。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">You can find the Furion documentation<span> </span><a href="https://dotnetchina.gitee.io/furion">on the website</a><span> </span>or<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Ffurion.icu">on the backup website</a>.</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">贡献 / Contributing</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">该存储库的主要目的是继续发展 Furion 核心，使其更快、更易于使用。 Furion 的开发在<span> </span><a href="https://gitee.com/dotnetchina/Furion">Gitee</a><span> </span>上公开进行，我们感谢社区贡献错误修复和改进。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">阅读<a href="https://dotnetchina.gitee.io/furion/docs/contribute">贡献指南</a>内容，了解如何参与改进 Furion。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">The main purpose of this repository is to continue evolving Furion core, making it faster and easier to use. Development of Furion happens in the open on<span> </span><a href="https://gitee.com/dotnetchina/Furion">Gitee</a>, and we are grateful to the community for contributing bugfixes and improvements.</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">Read<span> </span><a href="https://dotnetchina.gitee.io/furion/docs/contribute">contribution documents</a><span> </span>to learn how you can take part in improving Furion.</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">许可证 / License</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">Furion 采用<span> </span><a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">MulanPSL-2.0</a><span> </span>开源许可证。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">Furion uses the<span> </span><a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">MulanPSL-2.0</a><span> </span>open source license.</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>Copyright (c) 2020-2022 百小僧, Baiqian Co.,Ltd.</span>
<span>Furion is licensed under Mulan PSL v2.</span>
<span>You can use this software according to the terms andconditions of the Mulan PSL v2.</span>
<span>You may obtain a copy of Mulan PSL v2 at:</span>
<span>            https://gitee.com/dotnetchina/Furion/blob/master/LICENSE</span>
<span>THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUTWARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.</span>
<span>See the Mulan PSL v2 for more details.</span></pre> 
 </div> 
</div> 
<h2>框架特色 / Feature</h2> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#46a1de; color:#3498db"><strong>木兰宽松开源协议，无需商业授权</strong></span></li> 
 <li>基于 .NET5/6 平台，没有历史包袱</li> 
 <li>极少依赖，只依赖两个第三方包</li> 
 <li>极速上手，一个 Inject() 完成配置</li> 
 <li>代码无侵入性，100% 兼容原生写法</li> 
</ul> 
<h2>项目仓库 / Repository</h2> 
<ul> 
 <li>Gitee：      <a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>GitHub：   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
 <li>Nuget：    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">https://www.nuget.org/packages/Furion</a></li> 
 <li>国内文档：<a href="https://dotnetchina.gitee.io/furion">https://dotnetchina.gitee.io/furion</a></li> 
 <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.icu" target="_blank">https://furion.icu</a></li> 
</ul> 
<h2>本期更新 / Upgrade</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>新特性</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span>规范化结果<span> </span><code>ExceptionMetadata</code><span> </span>和<span> </span><code>ValidationMetadata</code><span> </span>都可以获取<span> </span><code>ErrorCode</code><span> </span>属性<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5GJ6D" target="_blank">#I5GJ6D</a></li> 
    <li>[新增]<span> </span>远程请求对<span> </span><code>Url</code><span> </span>是否编码设置，<code>[Get(WithEncodeUrl = false)]</code><span> </span>和<span> </span><code>WithEncodeUrl(false)</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5GOBC" target="_blank">#I5GOBC</a></li> 
    <li>[新增]<span> </span>更强大的<span> </span><code>JWTEncryption.SecurityReadJwtToken('token')</code><span> </span>读取解析<span> </span><code>Token</code><span> </span>静态方法<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/574eeb601294378e68c3d57ceaf6cb17f36636e3" target="_blank">574eeb6</a></li> 
   </ul> </li> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[新增]<span> </span>升级所有<span> </span><code>.NET</code><span> </span>依赖包至<span> </span><code>6.0.7</code><span> </span>版本</li> 
    <li>[重构]<span> </span><code>JWT</code><span> </span><code>Token</code><span> </span>刷新逻辑<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5GXML" target="_blank">#I5GXML</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/574eeb601294378e68c3d57ceaf6cb17f36636e3" target="_blank">574eeb6</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[修复]<span> </span><code>Rider</code><span> </span>开发工具对同名脚手架 (<code>EFCore</code><span> </span>和<span> </span><code>SqlSugar</code>) 只显示一个问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/518" target="_blank">!518</a></li> 
    <li>[修复]<span> </span><code>UnitOfWork</code><span> </span>工作单元在<span> </span><code>EFCore</code><span> </span>中失效问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5H0T3" target="_blank">#I5H0T3</a></li> 
    <li>[修复]<span> </span><code>JWT</code><span> </span>中<span> </span><code>Token</code><span> </span>如果存在数组类型的值时，刷新<span> </span><code>Token</code><span> </span>后丢失了历史值<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5GXML" target="_blank">#I5GXML</a></li> 
    <li>[修复]<span> </span>远程请求<span> </span><code>WithEncodeUrl</code><span> </span>无法在<span> </span><code>[HttpMethod]</code><span> </span>设置问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/574eeb601294378e68c3d57ceaf6cb17f36636e3" target="_blank">574eeb6</a></li> 
    <li>[修复]<span> </span><code>Serve.Run()</code><span> </span>模式下添加自定义配置导致<span> </span><code>EFCore</code><span> </span>无法获取自定义配置文件问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5GZ0F" target="_blank">#I5GZ0F</a></li> 
    <li>[修复]<span> </span><code>Oops.Bah</code><span> </span>进入全局异常拦截器问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5H47S" target="_blank">#I5H47S</a></li> 
    <li>[修复]<span> </span><code>AddDbPool/AddDb</code><span> </span>扩展未根据配置<span> </span><code>Key</code><span> </span>路径读取问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5H6S4" target="_blank">#I5H6S4</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/pulls/520" target="_blank">!520</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[调整]<span> </span>多语言默认处理逻辑，<strong>允许不配置任何语言</strong>，过去版本会报错<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5GRD9" target="_blank">#I5GRD9</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/5077c5dab9ee94733817f55ff8224b853d0001a3" target="_blank">5077c5d</a></li> 
    <li>[改进]<span> </span>规范化文档<span> </span><code>Swagger</code><span> </span>性能</li> 
    <li>[调整]<span> </span>调整<span> </span><code>MongoDB</code><span> </span>仓储<span> </span><code>TDocument</code><span> </span>泛型约束<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/3f49055b6b80ef7861f58b0c6feabf5c87a32010" target="_blank">3f49055</a></li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[更新]<span> </span>远程请求文档，日志记录文档</li> 
   </ul> </li> 
 </ul> 
</blockquote>
                                        </div>
                                      
</div>
            