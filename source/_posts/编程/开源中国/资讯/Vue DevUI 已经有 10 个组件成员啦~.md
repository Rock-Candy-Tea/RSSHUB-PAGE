
---
title: 'Vue DevUI 已经有 10 个组件成员啦~'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-577e42727457e09ef8859f96932f04c7421.png'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 12:35:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-577e42727457e09ef8859f96932f04c7421.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-577e42727457e09ef8859f96932f04c7421.png" referrerpolicy="no-referrer"></p> 
<p>3个月之前，我们在社区发了一篇文章，正式发起了 Vue DevUI 项目。<a href="https://my.oschina.net/u/4863191/blog/5037886">让我们一起建设 Vue DevUI 项目吧！</a></p> 
<p>很快就有不少热爱开源的小伙伴参与进来，于是我们迅速成立了<code>Vue DevUI 核心成员小组</code>，一起讨论出了Vue DevUI组件库的技术栈：</p> 
<ul> 
 <li>Vite</li> 
 <li>Vue3</li> 
 <li>TypeScript</li> 
 <li>JSX</li> 
</ul> 
<p>到目前为止该小组已发展到46名成员，Vue DevUI 组件库也新增了10个组件成员，并在npm发布了<code>v0.1.0</code>版本：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvue-devui%2Fv%2F0.1.0" target="_blank">vue-devui@0.1.0</a></p> 
<p>⚠️注意：该版本还不完善，不可用于生产环境。</p> 
<p>特别感谢以下小伙伴的贡献：</p> 
<ul> 
 <li><a href="https://gitee.com/brenner8023">brenner8023</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflxy1028" target="_blank">flxy1028</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkagol" target="_blank">kagol</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fto0simple" target="_blank">to0simple</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FZcating" target="_blank">Zcating</a></li> 
</ul> 
<p>接下来同步下Vue DevUI目前的进展情况，欢迎感兴趣的小伙伴参与到 Vue DevUI 项目的建设中来！👏🎉</p> 
<p>通过参与 Vue DevUI 项目，你可以：</p> 
<ul> 
 <li>学习最新的 Vite+Vue3+TSX 技术</li> 
 <li>学习如何设计和开发组件</li> 
 <li>参与到开源社区中来</li> 
 <li>结识一群热爱学习、热爱开源的朋友</li> 
</ul> 
<h1>新增组件</h1> 
<p>通用组件：</p> 
<ol> 
 <li>Button按钮组件</li> 
 <li>Panel面板组件</li> 
</ol> 
<p>导航组件：</p> 
<ol> 
 <li>Tabs选项卡组件</li> 
</ol> 
<p>反馈组件：</p> 
<ol> 
 <li>Alert警告组件</li> 
</ol> 
<p>数据录入组件：</p> 
<ol> 
 <li>CheckBox复选框组件</li> 
 <li>Radio单选框组件</li> 
 <li>Switch开关组件</li> 
 <li>TagsInput标签输入组件</li> 
 <li>TextInput文本框组件</li> 
</ol> 
<p>数据展示组件：</p> 
<ol> 
 <li>Avatar头像组件</li> 
</ol> 
<p>以下是网站的效果图：</p> 
<p><img alt="demo.png" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923d2294f20648a8b115759cdb8e4bab~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
<p><img alt="api.png" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46fbb52d6e9a43058095f7a22101c10a~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
<p>详细的 Release Notes 信息可以参考：</p> 
<p><a href="https://gitee.com/devui/vue-devui/releases/v0.2.0">https://gitee.com/devui/vue-devui/releases/v0.2.0</a></p> 
<h1>优化和规范</h1> 
<p>目前 Vue DevUI 组件库项目已增加以下规范：</p> 
<ol> 
 <li>Jest 单元测试</li> 
 <li>ESLint 代码规范</li> 
 <li>StyleLint 样式规范</li> 
 <li>ls-lint 文件夹/文件命名规范</li> 
 <li>CommitLint 代码提交规范</li> 
</ol> 
<h1>快速开始</h1> 
<p>快速开始三部曲：</p> 
<ul> 
 <li>安装</li> 
 <li>引入</li> 
 <li>使用</li> 
</ul> 
<h2>安装 vue-devui</h2> 
<pre><code>npm i vue-devui
# npm i vue-devui --registry=https://registry.npm.taobao.org/
</code></pre> 
<h2>引入 vue-devui</h2> 
<p>main.ts</p> 
<pre><code>import &#123; createApp &#125; from 'vue'
import App from './App.vue'

// 引入 Vue DevUI 组件库
import DevUI from 'vue-devui'
import 'vue-devui/style.css'

// 使用vue-devui
createApp(App).use(DevUI).mount('#app')
</code></pre> 
<h2>使用 Button 组件</h2> 
<p>App.vue</p> 
<pre><code><d-button>确定</d-button>
</code></pre> 
<p>效果图：</p> 
<p><img alt="devui button.png" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e456f1ea79344618a7dbae677a36061e~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
<p>以下是该项目的源码：</p> 
<p><a href="https://gitee.com/devui/vue-devui">https://gitee.com/devui/vue-devui</a></p> 
<p>参与贡献可以加小助手微信：devui-official，拉你进Vue DevUI核心成员小组～😋😋</p> 
<p>欢迎关注我们<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2F" target="_blank">DevUI</a>组件库，点亮我们的小星星🌟：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui" target="_blank">https://github.com/devcloudfe/ng-devui</a></p> 
<p>也欢迎使用DevUI新发布的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fhome" target="_blank">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p> 
<h1>预告</h1> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui" target="_blank">DevUI</a> 将于本月10日发布 DevUI 12 版本，除了升级 Angular 12 之外，更有超多有趣的新特性，尽情期待！</p> 
</blockquote> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui-admin" target="_blank">DevUI Admin</a> 2.0 版本也将在本月17号重磅发布，提供了一项神奇的黑科技，让我们拭目以待吧！</p> 
</blockquote>
                                        </div>
                                      
</div>
            