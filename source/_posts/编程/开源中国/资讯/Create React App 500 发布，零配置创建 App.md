
---
title: 'Create React App 5.0.0 发布，零配置创建 App'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4386'
author: 开源中国
comments: false
date: Fri, 24 Dec 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4386'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Create React App 5.0.0 现已发布，这是一个主要版本。Create React App 是由 Facebook 推出的脚手架，基本可以零配置搭建基于 webpack 的 React 开发环境，并内置了热更新等功能。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">具体更新内容如下：</span></p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Highlights</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>webpack 5 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11201" target="_blank">#11201</a>)</li> 
 <li>Jest 27 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11338" target="_blank">#11338</a>)</li> 
 <li>ESLint 8 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11375" target="_blank">#11375</a>)</li> 
 <li>PostCSS 8 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11121" target="_blank">#11121</a>)</li> 
 <li>Fast Refresh 改进和 bug 修复 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11105" target="_blank">#11105</a>)</li> 
 <li>支持 Tailwind (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11717" target="_blank">#11717</a>)</li> 
 <li>改进的包管理器检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11322" target="_blank">#11322</a>)</li> 
 <li>解除了所有的依赖关系，以便与其他工具更好地兼容 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11474" target="_blank">#11474</a>)</li> 
 <li>Dropped support for Node 10 and 12</li> 
 <li>不再支持 Node 10 和 12</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#24292f"><strong>从 4.0.x 迁移到 5.0.0</strong></span></h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f">在任何尚未 ejected 的已创建项目中，运行：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start">npm install --save --save-exact react-scripts@5.0.0</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">或者</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">yarn add --exact react-scripts@5.0.0</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>NOTE：</strong>如果在升级后遇到错误，你可能需要删除 node_modules 文件夹并通过运行 npm install（或 yarn）重新安装你的依赖。</p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Breaking Change</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>reate-react-app</code> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11322" target="_blank">#11322</a> 使用 env var 检测 yarn 或 npm 作为包管理器</li> 
  </ul> </li> 
 <li><code>babel-preset-react-app</code>, <code>cra-template-typescript</code>, <code>cra-template</code>, <code>create-react-app</code>, <code>eslint-config-react-app</code>, <code>react-app-polyfill</code>, <code>react-dev-utils</code>, <code>react-error-overlay</code>,<code>react-scripts</code> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11201" target="_blank">#11201</a> Webpack 5 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fraix" target="_blank">@raix</a> )</li> 
  </ul> </li> 
 <li><code>eslint-config-react-app</code>, <code>react-error-overlay</code>,<code>react-scripts</code> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F10761" target="_blank">#10761</a> chore：迁移到 @babel/eslint-parser</li> 
  </ul> </li> 
 <li><code>react-scripts</code> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11188" target="_blank">#11188</a> 弃用 root level template.json keys</li> 
  </ul> </li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#24292f">错误修复</span></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>react-scripts</code> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F11413" target="_blank">#11413</a> fix(webpackDevServer)：禁用警告覆盖</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Fpull%2F10511" target="_blank">#10511</a> 修复样式表中的 ICSS 语法</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">完整内容可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app%2Freleases%2Ftag%2Fv5.0.0" target="_blank">https://github.com/facebook/create-react-app/releases/tag/v5.0.0</a></p>
                                        </div>
                                      
</div>
            